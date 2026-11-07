# 4. Docker on the data disk

Docker keeps everything in one folder: images, containers, and **volumes** (the postgres data). By default that folder is `/var/lib/docker`, on the OS disk. The OS disk is small, and it's Linux's own. We want Docker's things on the data disk, in `/mnt/data`.

That folder has a name: Docker's **data root**. We change it in Docker's settings file, `/etc/docker/daemon.json`.

[Diagram: inside the VM, from disk to backup](./inside-the-vm.excalidraw)

## 1. Install Docker

On the VM:

```bash
curl -fsSL https://get.docker.com | sudo sh
sudo usermod -aG docker azureuser
exit
```

`usermod -aG docker` lets you run `docker` without `sudo`. It takes effect at your next login, so `exit` and SSH in again.

```bash
docker run --rm hello-world
```

```text
Hello from Docker!
```

## 2. Where does Docker keep things now?

```bash
docker info --format '{{.DockerRootDir}}'
docker info --format '{{.Driver}}'
```

```text
/var/lib/docker
overlayfs
```

The first line is the data root: on the OS disk, which is what we want to change.

The second line matters too. `overlayfs` means newer Docker hands **images** to a helper program called **containerd**, which keeps them in its own folder, `/var/lib/containerd`. So there are two folders to move:

| Folder | What's in it | Setting |
| --- | --- | --- |
| `/var/lib/docker` | containers, **volumes**, networks | `data-root` in `/etc/docker/daemon.json` |
| `/var/lib/containerd` | images | `root` in `/etc/containerd/config.toml` |

(If yours says `overlay2`, images are in `/var/lib/docker` too, and you can skip the containerd parts below.)

## 3. Stop Docker

Never move the folders while Docker is running: it writes into them all the time.

```bash
sudo systemctl stop docker.socket docker containerd
```

`docker.socket` would wake Docker up again as soon as someone runs a `docker` command, so it's stopped too.

## 4. Copy the folders to the data disk

```bash
sudo rsync -aHX /var/lib/docker/     /mnt/data/docker/
sudo rsync -aHX /var/lib/containerd/ /mnt/data/containerd/
```

`rsync -a` copies everything with its owners and permissions. `-H` and `-X` keep hard links and extra attributes, which Docker's files use. The `/` at the end of each path means "the contents of this folder".

## 5. Tell Docker and containerd

```bash
echo '{ "data-root": "/mnt/data/docker" }' | sudo tee /etc/docker/daemon.json
```

For containerd, add one line at the very top of its settings file:

```bash
sudo sed -i '1i root = "/mnt/data/containerd"' /etc/containerd/config.toml
head -3 /etc/containerd/config.toml
```

```text
root = "/mnt/data/containerd"
#   Copyright 2018-2022 Docker Inc.
...
```

## 6. Start and check

```bash
sudo systemctl start containerd docker
docker info --format '{{.DockerRootDir}}'
docker images
```

```text
/mnt/data/docker
REPOSITORY    TAG       IMAGE ID       CREATED       SIZE
hello-world   latest    ...
```

The data root moved, and `hello-world` is still there, because we copied it.

Prove that new things land on the data disk. Watch the "Used" column before and after:

```bash
df -h / /mnt/data
docker pull postgres:17-alpine
df -h / /mnt/data
```

`/mnt/data` grows, `/` doesn't.

## 7. Throw the old copies away

Once everything works:

```bash
sudo rm -rf /var/lib/docker /var/lib/containerd
```

That frees the space on the OS disk. Only run it after step 6 showed `/mnt/data/docker`.

## Why this order matters after a restart

At start, Linux mounts `/mnt/data` (fstab, page 3) and then starts Docker. If the disk ever failed to mount, `/mnt/data` would be an empty folder on the OS disk, and Docker would start there, empty. Your notes wouldn't be lost (they're still on the data disk), just not visible. `df -h /mnt/data` tells you which one you're looking at.

## Check yourself

1. Which file holds Docker's settings, and which line moves its data root?
2. Why do we stop Docker before copying?
3. After this page, where will the postgres volume of the notes app live?

Next: [Push the images](05-push-the-images.md).
