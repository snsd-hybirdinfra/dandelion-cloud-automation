#!/bin/bash

###=============================================================================================================================  web1 backup
ping -c 3 web1; ping -c 3 web2

ssh -i /home/ubuntu/.ssh/dandelion.pem ubuntu@web1 'docker exec dandelion-wp tar czf - /var/www/html' > /tmp/backup/$date/backup-web1.tar.gz
ssh -i /home/ubuntu/.ssh/dandelion.pem ubuntu@web2 'docker exec dandelion-wp tar czf - /var/www/html' > /tmp/backup/$date/backup-web2.tar.gz
web_backup_result=$?

export web_backup_result