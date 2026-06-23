#!/bin/bash

date=$(date +%Y-%m-%d)

mkdir -p "/tmp/monitoring/$date"

### TODO : 컴퓨팅 자원과 저장 공간 확인 및 조치

source ./web1-check.sh
source ./web2-check.sh
source ./db-check.sh
source ./proxy-check.sh
source ./backup-check.sh
source ./control-check.sh


echo -e "
==== $(date +%Y-%m-%d_%H:%M:%S) check results ====
result_web1=$result_web1
result_web2=$result_web2
result_db=$result_db
result_proxy=$result_proxy
result_backup=$result_backup
result_control=$result_control
" >> /tmp/monitoring/$date/check_results.txt