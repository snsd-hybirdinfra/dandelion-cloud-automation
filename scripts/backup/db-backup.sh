#!/bin/bash


### TODO : include cinder
ssh -i /home/ubuntu/.ssh/dandelion.pem ubuntu@db "mysqldump -u사용자이름 -p'비밀번호' wordpress" > "/tmp/backup/$date/backup.sql"
ping -c 3 db
db_backup_result=$?

export db_backup_result=$db_backup_result