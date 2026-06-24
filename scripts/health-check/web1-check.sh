#!/bin/bash

### TODO : 도커 컨테이너로 조건 변경 && 백업본 교체 조건 확인 및 교체
result_web1=false

ping -c 3 web1
ping_result_web1=$?

#curl -s -o /dev/null -w "%{http_code}" http://web1
#curl_result_web1=$?

#ssh  -o ConnectTimeout=2 -i /home/ubuntu/.ssh/dandelion.pem ubuntu@web1 'docker container ls -a | grep web1 | grep healthy'
#ssh_result_web1=$?

if [ $ping_result_web1 -eq 0 ] #&& [ $curl_result_web1 -eq 0 ] && [ $ssh_result_web1 -eq 0 ]
then
  result_web1=true
  echo 'success web1'
else
  ssh  -o ConnectTimeout=2 -i /home/ubuntu/.ssh/dandelion.pem  ubuntu@web1 'docker container restart web1'
# ssh -o ConnectTimeout=2  -i /home/ubuntu/.ssh/dandelion.pem \
# ubuntu@backup 'cat $(ls -td /tmp/backup/* | head -n 1)/backup-web1.tar.gz' \
# ssh ubunutu@web1 "tar -xzf - -C /var/www/html/"

fi

export result_web1=$result_web1c