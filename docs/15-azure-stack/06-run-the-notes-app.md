# 6. Run the notes app on the VM

Everything is ready: a disk at `/mnt/data`, Docker keeping its things there, and the images on Docker Hub. Now the same three-part app from section 14 runs in Azure, and anyone can open it.

## What's different from section 14

- `image:` instead of `build:`. The VM pulls the images, it doesn't build them.
- `PORT` is set for web and api (the new code reads it).
- Web's door is VM port **80**, the normal web port, so the address needs no `:3000`. The network security group lets port 80 in from the internet (page 2).
- api and db still have no `ports:`. Nobody outside can reach them, not even you.

```yaml
  web:
    image: ${DOCKERHUB_USER}/notes-web:1.0
    environment:
      PORT: 3000
      API_URL: http://api:4000
    ports:
      - "80:3000"
```

The full file is `notes-app/compose.yaml`.

## 1. Copy two files to the VM

On your laptop, from `docs/15-azure-stack/`:

```bash
IP=$(terraform -chdir=terraform output -raw public_ip)
ssh -i ~/.ssh/azure_learning azureuser@$IP mkdir -p notes
scp -i ~/.ssh/azure_learning notes-app/compose.yaml notes-app/env.example vm/*.sh azureuser@$IP:notes/
```

`scp` is `cp` over SSH. The scripts are for page 7.

## 2. Make the .env

SSH in, then:

```bash
cd ~/notes
cp env.example .env
nano .env
```

```text
DOCKERHUB_USER=tanvikanwar23
DB_USER=notes
DB_PASSWORD=pick-a-long-one
DB_NAME=notes
```

`Ctrl+O`, `Enter` saves, `Ctrl+X` leaves. Check that Compose reads it:

```bash
docker compose config | grep image:
```

```text
    image: tanvikanwar23/notes-api:1.0
    image: postgres:17-alpine
    image: tanvikanwar23/notes-web:1.0
```

## 3. Start it

```bash
docker compose pull
docker compose up -d
docker compose ps
```

```text
NAME           IMAGE                          SERVICE   STATUS                    PORTS
notes-api-1    tanvikanwar23/notes-api:1.0    api       Up 10 seconds
notes-db-1     postgres:17-alpine             db        Up 16 seconds (healthy)   5432/tcp
notes-web-1    tanvikanwar23/notes-web:1.0    web       Up 9 seconds              0.0.0.0:80->3000/tcp
```

Only web has a `0.0.0.0:80->` door.

```bash
docker compose logs web api
```

```text
web-1  | web on port 3000, api at http://api:4000
api-1  | api on port 4000, database host: db
```

Those lines come from the new code: the ports came from the environment.

## 4. Open it from anywhere

On your laptop, open `http://<public IP>` (the `web_url` output from page 2). Or on your phone, off Wi-Fi: it's on the internet. Save two notes.

## 5. Where are the notes, really?

```bash
docker volume inspect notes_data --format '{{.Mountpoint}}'
```

```text
/mnt/data/docker/volumes/notes_data/_data
```

On the data disk, because of page 4. Look inside (it belongs to postgres, so `sudo`):

```bash
sudo ls /mnt/data/docker/volumes/notes_data/_data
```

```text
PG_VERSION  base  global  pg_hba.conf  pg_wal  postgresql.conf  ...
```

That's postgres's own files. Your notes are in there, in postgres's format.

## 6. Does it survive a restart?

```bash
sudo reboot
```

Wait a minute and reload the page. The notes are still there. Three things made that happen:

1. fstab mounted the data disk at `/mnt/data` (page 3).
2. Docker started with its data root on `/mnt/data` (page 4).
3. `restart: unless-stopped` started the three containers again.

## Check yourself

1. Why is there no `ports:` under `api` and `db`?
2. You run `docker compose down`. Are the notes gone? And with `down -v`?
3. Which three things bring the app back after `reboot`?

Next: [Back up and restore](07-backup-and-restore.md).
