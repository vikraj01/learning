# 3. Mount the data disk

The VM has two disks now. Linux uses the first one. The second one is new and empty, like a USB stick fresh out of the box: before you can keep files on it, you prepare it and give it a place.

## How Linux sees files: one tree

On Windows each disk is a letter: `C:`, `D:`. Linux has **no letters**. There is one tree, and it starts at `/` (called **root**). Everything is somewhere under `/`:

```text
/                  ← root: the top of the tree (the OS disk)
├── bin            programs (ls, cp, ...)
├── etc            settings files (/etc/fstab, /etc/docker/daemon.json)
├── home
│   └── azureuser  your files
├── var
│   └── lib
│       └── docker Docker's files, by default
├── dev            every disk shows up here as a file: /dev/sda, /dev/sdb
└── mnt            an empty place to hang extra disks
    └── data       ← our data disk will hang here
```

To use another disk, you **mount** it: you hang it on a folder of the tree. That folder is the **mount point**. After `mount /dev/sdb1 /mnt/data`, anything written into `/mnt/data` goes onto the data disk. Everything else still goes onto the OS disk.

[Diagram: inside the VM, from disk to backup](./inside-the-vm.excalidraw)

Four steps for a new disk:

1. **Find** it.
2. **Partition** it: mark out the space (we use all of it, one partition).
3. **Format** it: write a **filesystem** onto it, the table of contents that keeps track of which file is where. We use `ext4`, the usual one on Linux.
4. **Mount** it, and write it in `/etc/fstab` so it's mounted again after every restart.

SSH into the VM first (page 2, step 5).

## 1. Find the disk

```bash
lsblk
```

```text
NAME    MAJ:MIN RM  SIZE RO TYPE MOUNTPOINTS
sda       8:0    0   30G  0 disk
├─sda1    8:1    0   29G  0 part /
├─sda14   8:14   0    4M  0 part
├─sda15   8:15   0  106M  0 part /boot/efi
└─sda16 259:0    0  913M  0 part /boot
sdb       8:16   0   32G  0 disk
```

- `sda`: the OS disk, 30 GB. Its partition `sda1` is mounted at `/`.
- `sdb`: our data disk, **32 GB**, no partitions, no mount point. That's the one.

The letter can differ (`sdb`, `sdc`). Always pick by size and "no partitions". Azure also keeps a fixed name for slot (LUN) 0, which you can check:

```bash
ls -l /dev/disk/azure/scsi1/
```

```text
lrwxrwxrwx 1 root root 12 Nov  7 10:02 lun0 -> ../../../sdb
```

Save it in a variable so the next commands use the right disk:

```bash
DISK=/dev/sdb
```

!!! danger "Pick the right disk"
    The next two commands wipe the disk you give them. `sda` is Linux itself. Check `lsblk` once more.

## 2. Partition

```bash
sudo parted $DISK --script mklabel gpt mkpart data ext4 0% 100%
lsblk $DISK
```

```text
NAME   MAJ:MIN RM SIZE RO TYPE MOUNTPOINTS
sdb      8:16   0  32G  0 disk
└─sdb1   8:17   0  32G  0 part
```

- `mklabel gpt`: a fresh partition table (GPT is the modern kind).
- `mkpart data ext4 0% 100%`: one partition named `data`, from the start to the end.

## 3. Format

```bash
sudo mkfs.ext4 -L data ${DISK}1
```

```text
Creating filesystem with 8388096 4k blocks and 2097152 inodes
...
Writing superblocks and filesystem accounting information: done
```

`-L data` gives it a label, so you recognise it later.

## 4. Mount

```bash
sudo mkdir -p /mnt/data
sudo mount ${DISK}1 /mnt/data
df -h /mnt/data
```

```text
Filesystem      Size  Used Avail Use% Mounted on
/dev/sdb1        32G   24K   30G   1% /mnt/data
```

It works now, but only until the next restart. A mount is forgotten when the computer starts again.

## 5. Mount it after every restart: /etc/fstab

`/etc/fstab` is the list of disks Linux mounts when it starts. Every line is: *which disk*, *where*, *filesystem*, *options*.

Disk letters can change between restarts (`sdb` today, `sdc` tomorrow). So we name the disk by its **UUID**, an ID written into the filesystem when we formatted it. It never changes.

```bash
sudo blkid ${DISK}1
```

```text
/dev/sdb1: LABEL="data" UUID="3f6c2b1e-8d4a-4b6e-9c1f-2a7d5e8b9c01" BLOCK_SIZE="4096" TYPE="ext4" PARTLABEL="data" PARTUUID="..."
```

Add the line (this takes the UUID straight from `blkid`):

```bash
UUID=$(sudo blkid -s UUID -o value ${DISK}1)
echo "UUID=$UUID  /mnt/data  ext4  defaults,nofail  0  2" | sudo tee -a /etc/fstab
```

- `defaults`: normal read and write.
- `nofail`: if the disk is missing, start anyway. Without it, a missing disk stops the VM from starting at all, and you can't SSH in to fix it.
- `0 2`: no old-style backup (`0`), and check this disk for errors at start, after `/` (`2`).

**Test the line before you restart.** Unmount, then let fstab mount it:

```bash
sudo umount /mnt/data
sudo mount -a
df -h /mnt/data
```

Same output as before means the line is right. If `mount -a` prints an error, fix `/etc/fstab` now (`sudo nano /etc/fstab`).

Now the real test:

```bash
sudo reboot
```

Wait a minute, SSH in again, and run `df -h /mnt/data`. It's back.

## 6. A folder for backups

`/mnt/data` belongs to root. Make a folder for page 7 that belongs to you:

```bash
sudo mkdir -p /mnt/data/backups
sudo chown azureuser: /mnt/data/backups
ls -l /mnt/data
```

```text
drwxr-xr-x 2 azureuser azureuser  4096 Nov  7 10:20 backups
drwx------ 2 root      root      16384 Nov  7 10:10 lost+found
```

`lost+found` is made by `mkfs.ext4`. Leave it alone.

## Check yourself

1. You write a file to `/home/azureuser/a.txt`. Which disk is it on? And `/mnt/data/b.txt`?
2. Why does fstab use the UUID and not `/dev/sdb1`?
3. What would happen at restart without `nofail`, if the data disk was missing?

Next: [Docker on the data disk](04-docker-on-the-data-disk.md).
