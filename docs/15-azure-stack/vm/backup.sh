#!/usr/bin/env bash
# Back up the notes database volume and upload it to the storage account.
# Run on the VM, inside ~/notes:   ./backup.sh <storage-account-name>
set -euo pipefail

ACCOUNT="${1:?usage: ./backup.sh <storage-account-name>}"
VOLUME=notes_data
DIR=/mnt/data/backups
FILE="notes-data-$(date +%Y-%m-%d-%H%M).tar.gz"

echo "1. Stop the database, so no file changes while we copy it"
docker compose stop db

echo "2. Pack the volume into $DIR/$FILE"
docker run --rm -v "$VOLUME":/data:ro -v "$DIR":/backup alpine \
  tar czf "/backup/$FILE" -C /data .

echo "3. Start the database again"
docker compose start db

echo "4. Upload it to $ACCOUNT, container 'backups'"
az storage blob upload --auth-mode login \
  --account-name "$ACCOUNT" --container-name backups \
  --name "$FILE" --file "$DIR/$FILE" --output none

echo "Done: $FILE"
