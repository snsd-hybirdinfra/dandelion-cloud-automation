#!/bin/bash

DATE=$(date +%Y%m%d_%H%M%S)
SOURCE_DIR="/var/www/html"
BACKUP_DIR="/backup"
BACKUP_FILE="web_backup_${DATE}.tar.gz"

mkdir -p ${BACKUP_DIR}
tar -czf ${BACKUP_DIR}/${BACKUP_FILE} ${SOURCE_DIR}

echo "Backup completed: ${BACKUP_DIR}/${BACKUP_FILE}"
