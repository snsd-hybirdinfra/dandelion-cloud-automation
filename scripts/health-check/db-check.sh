#!/bin/bash

### TODO : cinder 볼륨으로 조건 변경 &&  백업본 교체 조건 확인 및 교체

result_db=false

ping -c 3 db
ping_result_db=$?

ssh  -o ConnectTimeout=2 -i /home/ubuntu/.ssh/dandelion.pem ubuntu@db 'sudo systemctl status mysqld | grep active'
ssh_result_db=$?

if [ $ping_result_db -eq 0 ] && [ $ssh_result_db -eq 0 ]
then
  result_db=true
  echo 'success db'
else
  ssh -o ConnectTimeout=2   -i /home/ubuntu/.ssh/dandelion.pem ubuntu@db 'sudo systemctl restart mysqld'
# ssh -o ConnectTimeout=2 -i /home/ubuntu/.ssh/dandelion.pem \
# ubuntu@backup 'cat $(ls -td /tmp/backup/* | head -n 1)/backup.sql'  | \
# ssh ubuntu@db "mysql -u사용자이름 -p'비밀번호' wordpress "
fi

export result_db=$result_db