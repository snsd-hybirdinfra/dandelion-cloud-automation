#!/bin/bash


### TODO : include cinder
mysqldump -u wp_backup -ptest123 -h db wordpress_db > /tmp/backup/$date/backup.sql
ping -c 3 db
db_backup_result=$?

if [ $db_backup_result -eq 0 ]
then
        echo 'success db'
        db_backup_result=true
else
        echo 'failed db'
        db_backup_result=false
fi

export db_backup_result=$db_backup_result