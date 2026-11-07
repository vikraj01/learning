#!/usr/bin/env bash
# Download a backup from the storage account and put it back into the notes volume.
# Run on the VM, inside ~/notes:   ./restore.sh <storage-account-name> <backup-file-name>
# The current notes are replaced by the ones in the backup.
set -euo pipefail

ACCOUNT="${1:?usage: ./restore.sh <storage-account-name> <backup-file-name>}"
FILE="${2:?usage: ./restore.sh <storage-account-name> <backup-file-name>}"
VOLUME=notes_data
DIR=/mnt/data/backups

echo "1. Download $FILE"
az storage blob download --auth-mode login \
  --account-name "$ACCOUNT" --container-name backups \
  --name "$FILE" --file "$DIR/$FILE" --output none

echo "2. Stop the app and throw the old volume away"
docker compose down
docker volume rm "$VOLUME"

echo "3. Let Compose make a new, empty volume (and the containers), without starting them"
docker compose up --no-start

echo "4. Unpack the backup into the new volume"
docker run --rm -v "$VOLUME":/data -v "$DIR":/backup alpine \
  tar xzf "/backup/$FILE" -C /data

echo "5. Start the app"
docker compose up -d

echo "Done. Open the web page: the notes from the backup are back."
