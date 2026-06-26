Dandelion 인프라 백업 및 헬스체크 작업 정리



# 1. Cron 및 시스템 환경 설정
- backup 서버 Cron 등록

주기적인 데이터 백업을 수행하기 위해 backup 서버의 crontab에 스크립트를 등록했습니다.



Bash

crontab -e (작업 스케줄에 맞게 주기 설정 필요, 예: 매일 새벽 2시)

* 1 1 * * * /bin/bash /home/ubuntu/dandelion/backup.sh

- monitoring 서버 Cron 등록

전체 인프라의 상태를 주기적으로 감시하고 기록하기 위해 monitoring 서버의 crontab에 등록했습니다.



Bash

crontab -e (예: 매분 또는 5분마다 실행)

* * * * * * /bin/bash /home/ubuntu/dandelion/health-check.sh

# 2. 서버별 /etc/hosts 파일 수정

스크립트 내에서 IP 주소 대신 직관적인 호스트 네임(web1, web2, db, proxy, backup, control)을 사용할 수 있도록 각 서버의 /etc/hosts 파일에 도메인 지정을 완료했습니다.



# 3. 작업별 쉘 스크립트 분리 관리

유지보수와 디버깅을 용이하게 하기 위해 단일 스크립트로 동작하던 구조를 역할별로 세분화하여 분리했습니다.


백업 프로세스 (backup.sh 기반)
- db-backup.sh: MySQL 데이터베이스 덤프 백업 수행
- web-backup.sh: web1, web2 서버의 WordPress 업로드 파일 및 소스 아카이빙

헬스체크 프로세스 (health-check.sh 기반)
- proxy-check.sh: HAProxy 상태 점검 및 장애 시 재시작
- web1-check.sh / web2-check.sh: Docker 컨테이너 상태 점검 및 재시작
- db-check.sh: MySQL 서비스 활성화 상태 점검 및 원복
- backup-check.sh / control-check.sh: 스토리지 및 메모리 자원 상태 점검



# 4. 헬스체크 딜레이 제한 설정

장애 상황에서 스크립트가 무한정 대기하는 것을 방지하기 위해 SSH 접속 시 타임아웃 옵션을 2초로 엄격하게 제한했습니다.



옵션 반영: -o ConnectTimeout=2



장애 복구 및 복귀 메커니즘 (Failback)

# 5. 복구를 위한 임시 작업

각 점검 스크립트[db-check.sh, web1-check.sh, web2-check.sh] 에서 장애를 감지하면 자동으로 서비스를 재시작하거나 백업본을 통해 원복을 시도하는 복구 로직을 구현했습니다.



# 6. DB 장애 원복 시 최근 덤프로 덮어쓰기

db-check.sh 실행 중 mysqld 서비스가 다운되었거나 응답이 없을 경우, backup 서버에 저장된 가장 최신의 SQL 덤프 파일(backup.sql)을 가져와 자동으로 데이터베이스를 복구한 뒤 서비스를 재시작합니다.



Bash

## db-check.sh 내 복구 핵심 로직

ssh -o ConnectTimeout=2 ubuntu@backup 'cat $(ls -td /tmp/backup/* | head -n 1)/backup.sql' | mysql -h db -u wp_monitor -ptest123 wordpress_db

ssh -o ConnectTimeout=2 ubuntu@db 'sudo systemctl restart mysqld'

 원활한 복구를 위한 사전 작업 완료: 데이터베이스 원복 및 모니터링 쿼리 수행을 위해 각 노드에 mysql-client 패키지 설치를 완료했습니다.



# 7. Web 장애 원복 시 최근 덤프로 덮어쓰기 (주석 해제 및 검증 필요)

web1, web2 컨테이너 장애 시 우선 컨테이너 재시작(docker container restart)을 시도합니다. 만약 컨테이너 내부 소스 오염이 의심될 경우를 대비해, 백업 서버의 최근 압축본(backup-webX.tar.gz)을 스트리밍으로 쏘아 보내 컨테이너 내부에 덮어쓰는 로직이 준비되어 있습니다. (현재 안전을 위해 주석 처리됨)



# 8. 도커 컨테이너 수정

웹 서버들의 환경이 독립적인 Docker 컨테이너(dandelion-wp) 형태로 표준화됨에 따라, 헬스체크와 백업 모두 호스트 OS가 아닌 docker exec 및 docker container ls 명령어를 기반으로 동작하도록 전면 수정했습니다.


# 9. crontab 작업 결과 경로 수정

스크립트 파일 분리 이후 실행한 작업의 결과가 잘 저장되지 않는 문제가 있어 작업의 결과를 저장할 수 있도록 수정했습니다.

# phase1에서 있었던 문제점과 조치
1. db 계정의 권한이 ssh를 요청하는 서버에서만 가능해 backup 및 monitoring 노드에 mysql-client 설치 후 ssh 명령어에서 mysql 및 mysqldump 명령어로 수정
2. 실행 결과를 저장하기 위한 변수를 export해도 가져오지 못해 work_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"로 실행 경로를 잡아줌
3. http 요청의 결과가 정상적인지 판별해 결과를 판단해야 하는데, 이 과정에서 [curl -f http://web1 => curl -s -o /dev/null -w "%{http_code}" http://web2 => curl -fsS http://web1 로 변경]
4. 쉘 스크립트 실행 중 중단되는 문제가 있어서 | exit 1을 제거
5. docker container healthy 조건 변경


# 향후 수행 과제 (TODO)

[!IMPORTANT]

인프라 고도화 및 보안 강화를 위해 다음 작업들이 순차적으로 진행되어야 합니다.


## TODO 1. 복구 시나리오 작성 및 검증

현재 장애 감지 시 무조건적인 재시작 및 DB 덮어쓰기가 일어날 수 있으므로, 단순 일시적인 네트워크 지연인지 실제 서비스 다운인지 판별하는 정밀 인터벌 로직이 필요합니다.



실제 운영 환경과 유사한 스테이징 환경에서 DB/Web 원복 시나리오 시뮬레이션 테스트가 필요합니다.



## TODO 2. 백업 및 컨트롤 노드 메트릭 정의 및 복구 작업

backup-check.sh와 control-check.sh는 현재 단순 상태 조회(df, free) 및 결과 기록만 하고 있습니다.



조치 필요: 디스크 사용량이 90%를 초과하거나 메모리 가용량이 임계치 이하로 떨어질 경우 알림을 보내거나 오래된 백업을 퍼지(Purge)하는 구체적인 복구 액션이 정의되어야 합니다. (스크립트 내 Cinder 볼륨 전환 조건 확인 필요)



## TODO 3. 메트릭 수집 서버별 설정 및 그라파나(Grafana) 연동

텍스트 파일(/tmp/monitoring/...)에만 기록되는 로그 방식에서 벗어나 시각적인 모니터링 체계를 구축해야 합니다.



계획: 각 서버에 Prometheus Exporter(Node Exporter, Cadvisor 등)를 설치하고, 수집 서버에서 데이터를 당겨와 그라파나 대시보드로 시각화 및 Alerting 룰을 세팅합니다.



## TODO 4. DB 비밀번호 안전 조치 (보안 강화)

현재 문제점: db-check.sh 및 db-backup.sh 내에 MySQL 패스워드(ptest123)가 하드코딩되어 있거나 명령어 파이프라인에 노출되어 보안에 취약합니다.



조치 예정: 패스워드를 환경 변수로 관리하거나, 각 서버의 ~/.my.cnf 파일에 인증 정보를 안전하게 은닉(chmod 600)하여 패스워드 없이 mysql, mysqldump 명령어가 수행되도록 변경해야 합니다.