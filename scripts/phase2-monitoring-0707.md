# 현재까지 진행 사항

1. phase1(backup & monitoring)
	1. 백업 노드에 백업 스크립트, 모니터링 노드에 헬스체크 스크립트 작성(헬스체크에 백업본을 통한 복구 명령어)
	2. 스크립트 분리 및 cron 작업 등록
	3. 컨테이너 환경으로 명령어 수정

2. phase2(monitoring)
	1. web 노드에 node exporter, blackbox exporter,  cAdviosr 컨테이너, db노드에 mysql exporter node exporter, 모든 노드에 node exporter 설치 / monitoring 노드에 promethus와 grafana, alertmanager 설치
	2. fastapi로 alertmanager 알람을 받아서 복구 작업 정의(수동으로 확인이 필요하여 사용하지 않음)
	3. grafana와 promethus 및 alertmanager 연동
 
 # 오늘 작업한 내용
 monitoring 노드 backup-monitoring.sh

 ```
 #!/bin/bash

# grafana data
sudo tar -cvzf "grafana_data_$(date +%Y%m%d_%H%M%S).tar.gz" /var/lib/grafana/

# grafana config
sudo tar -cvzf "grafana_config_$(date +%Y%m%d_%H%M%S).tar.gz" /etc/grafana/

# promethus
sudo tar -cvzf "promethus_backup_$(date +%Y%m%d_%H%M%S).tar.gz" /home/ubuntu/dandeliondir/monitoring/prometheus-3.5.4.linux-amd64

# alertmanager
sudo tar -cvzf "alertmanager_backup_$(date +%Y%m%d_%H%M%S).tar.gz" /home/ubuntu/dandeliondir/monitoring/alertmanager-0.28.1.linux-amd64
```