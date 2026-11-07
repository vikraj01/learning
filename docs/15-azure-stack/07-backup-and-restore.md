# 7. Back up and restore

The notes are on the data disk. If someone runs `docker compose down -v`, or the disk breaks, or the VM is destroyed, they're gone. A **backup** is a copy kept somewhere else, and a **restore** puts it back.

We copy the whole `notes_data` volume into one `.tar.gz` file (a packed folder, like a `.zip`) and upload it to the storage account. That's outside the VM, so it survives whatever happens to the VM.

[Diagram: inside the VM, from disk to backup](./inside-the-vm.excalidraw)

## How the VM gets in, with no password

Terraform gave the VM an **identity** (a name in Azure, like a user) and gave that identity one permission: *Storage Blob Data Contributor* on our storage account, which means "may read and write files there". The VM logs in as itself. No password or key is stored anywhere.

## 1. Install the Azure command line on the VM

SSH in, then:

```bash
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
az login --identity
```

`--identity` means "log in as this VM". It prints a block of JSON with `"type": "servicePrincipal"`: that's the VM.

Set the storage account name (from `terraform output storage_account` on your laptop):

```bash
ACCOUNT=stlearningk3x9qa
az storage blob list --auth-mode login --account-name $ACCOUNT --container-name backups -o table
```

An empty list is right: no backups yet. `--auth-mode login` means "use who I'm logged in as".

If it says `AuthorizationPermissionMismatch`, the permission is still spreading through Azure. Wait five minutes and try again.

## 2. Make a note to look for

Open the web page and save a note: **before the backup**.

## 3. Back up

```bash
cd ~/notes
./backup.sh $ACCOUNT
```

```text
1. Stop the database, so no file changes while we copy it
2. Pack the volume into /mnt/data/backups/notes-data-2026-11-07-1130.tar.gz
3. Start the database again
4. Upload it to stlearningk3x9qa, container 'backups'
Done: notes-data-2026-11-07-1130.tar.gz
```

What the script does, step by step (open `backup.sh` and follow along):

1. `docker compose stop db`: postgres writes to its files all the time. Copying while it writes can give a broken copy, so we stop it for a few seconds. web and api stay up.
2. A throwaway `alpine` container gets two things: the volume at `/data` (`:ro`, read only) and the backups folder at `/backup`. It runs `tar czf`, which packs `/data` into one file in `/backup`. That's how you copy a volume: you can't `cp` it directly, but any container can see it.
3. `docker compose start db`.
4. `az storage blob upload` sends the file to the `backups` container.

Check it's in the storage account:

```bash
az storage blob list --auth-mode login --account-name $ACCOUNT --container-name backups -o table
```

```text
Name                                Blob Type    Length    Last Modified
----------------------------------  -----------  --------  -------------------------
notes-data-2026-11-07-1130.tar.gz   BlockBlob    6815744   2026-11-07T11:30:12+00:00
```

## 4. Something goes wrong

Save one more note: **after the backup**. Then destroy the data on purpose:

```bash
docker compose down -v
docker compose up -d
```

`-v` threw the volume away. Reload the page: no notes at all. Postgres started with an empty volume.

## 5. Restore

```bash
./restore.sh $ACCOUNT notes-data-2026-11-07-1130.tar.gz
```

```text
1. Download notes-data-2026-11-07-1130.tar.gz
2. Stop the app and throw the old volume away
3. Let Compose make a new, empty volume (and the containers), without starting them
4. Unpack the backup into the new volume
5. Start the app
Done. Open the web page: the notes from the backup are back.
```

Reload the page:

- **before the backup**: back. ✓
- **after the backup**: gone. It was saved after the backup was made, so the backup never had it.

That's the rule of backups: you get back what was there *when the backup was made*. Back up often.

Why step 3 uses `docker compose up --no-start` and not `docker volume create`: Compose likes to make its own volumes. It creates `notes_data`, the networks and the containers, but starts nothing. Then the backup goes into the empty volume, and when postgres starts it finds its files already there.

## 6. A backup only counts if it restores

A backup you never restored is a hope, not a backup. You just did the real test: you destroyed the data and brought it back. Do it again whenever the scripts or the app change.

## 7. Finished for today

On your laptop:

```bash
cd docs/15-azure-stack/terraform
terraform destroy
```

Everything goes, the storage account and its backups too (they were only for practice). In real life the storage account lives in its own Terraform folder, so destroying the VM never touches the backups.

## Check yourself

1. Why does `backup.sh` stop `db` but not `web` and `api`?
2. You restored a backup from 11:30. A note was saved at 11:45. Where is it?
3. How does the VM log in to the storage account without a password?

That's the whole stack: Terraform made it, the disk holds the data, Docker keeps it there, and the backup keeps it safe somewhere else.
