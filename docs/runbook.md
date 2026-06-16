<!-- STATUS: COMPLETE -->

# Project Runbook

## 1. 문서 목적

본 문서는 Team Dandelion 프로젝트의 실행 절차를 정의한다.

본 프로젝트는 OpenStack 기반 Ubuntu 인스턴스 위에서 Ansible을 활용하여 Proxy Node, Web Node, DB Node, Backup / Validation Node를 구성하고, Docker Compose 기반 WordPress와 DB Node MariaDB 서비스/HAProxy 서비스를 배포한 뒤 상태 점검, 백업, 복구 검증을 수행한다.

본 Runbook은 Phase 1 필수 구성 및 기본 검증을 기준으로 작성한다.

---

## 2. Phase 기반 실행 기준

본 프로젝트는 Phase 기반 구현 로드맵을 사용한다.

~~~text
Phase 1: 필수 구성 및 기본 검증 단계
Phase 2: 운영 확장 및 검증 고도화 단계
Phase 3: 도전 확장 단계
Out of Scope: 제외 범위
~~~

실행 우선순위는 다음과 같다.

| Phase | 실행 기준 |
|---|---|
| Phase 1 | OpenStack, SSH, Ansible, Docker, MariaDB, WordPress, HAProxy HTTP Reverse Proxy, Health Check, Backup, Restore |
| Phase 2 | HTTPS, Cinder Backup Volume, Monitoring, backup/restore playbook화, Ansible roles 구조 분리 |
| Phase 3 | Web Node 2대, HAProxy Load Balancing, 공통 DB 연결, 장애 대응 검증 |

Phase 1이 완료되지 않은 상태에서는 Phase 2와 Phase 3을 진행하지 않는다.

---

## 3. 전체 실행 흐름

~~~text
1. Repository 최신화
2. OpenStack 인스턴스 상태 확인
3. Node IP 정리
4. SSH 접속 확인
5. Ansible 설정 확인
6. Ansible ping 확인
7. Playbook syntax check
8. site.yml 실행
9. DB Node MariaDB 확인
10. Web Node WordPress 확인
11. Proxy Node HAProxy 확인
12. Proxy Node 경유 WordPress 접속 확인
13. Web Node → DB Node 연결 확인
14. health_check.sh 실행
15. backup.sh 실행
16. restore.md 기반 복구 절차 검증
17. 캡처 및 문서 정리
~~~

---

## 4. 사전 준비

## 4.1 Repository 최신화

작업 전 최신 상태를 받는다.

~~~bash
git pull --rebase origin main
git status
~~~

주의:

~~~text
git add . 사용 금지
수정한 파일만 git add
작업 전후 git status 확인
~~~

---

## 4.2 OpenStack 인스턴스 확인

~~~bash
openstack server list
~~~

필수 노드:

| Node | Role | Status |
|---|---|---|
| Control Node | Ansible 실행 | ACTIVE |
| Proxy Node | HAProxy HTTP Reverse Proxy | ACTIVE |
| Web Node | Custom WordPress | ACTIVE |
| DB Node | MariaDB | ACTIVE |
| Backup / Validation Node | Health Check / Backup / Restore | ACTIVE |

---

## 4.3 Node IP 정리

실행 전 아래 표를 채운다.

| Node | Private IP | Floating IP / Forwarding | 비고 |
|---|---|---|---|
| Control Node |  |  |  |
| Proxy Node |  |  |  |
| Web Node |  |  |  |
| DB Node |  |  |  |
| Backup / Validation Node |  |  |  |

---

## 5. SSH 접속 확인

Control Node에서 각 노드로 SSH 접속을 확인한다.

~~~bash
ssh ubuntu@PROXY_NODE_IP
ssh ubuntu@WEB_NODE_IP
ssh ubuntu@DB_NODE_IP
ssh ubuntu@BACKUP_NODE_IP
~~~

Key 파일을 사용하는 경우:

~~~bash
ssh -i ~/.ssh/dandelion-key.pem ubuntu@PROXY_NODE_IP
ssh -i ~/.ssh/dandelion-key.pem ubuntu@WEB_NODE_IP
ssh -i ~/.ssh/dandelion-key.pem ubuntu@DB_NODE_IP
ssh -i ~/.ssh/dandelion-key.pem ubuntu@BACKUP_NODE_IP
~~~

Key 권한 오류가 발생하면 다음을 실행한다.

~~~bash
chmod 400 ~/.ssh/dandelion-key.pem
~~~

성공 기준:

| 대상 | 성공 기준 |
|---|---|
| Proxy Node | SSH 접속 성공 |
| Web Node | SSH 접속 성공 |
| DB Node | SSH 접속 성공 |
| Backup / Validation Node | SSH 접속 성공 |

---

## 6. Ansible 실행 준비

## 6.1 Ansible 디렉터리 이동

~~~bash
cd ansible
~~~

---

## 6.2 Ansible 버전 확인

~~~bash
ansible --version
~~~

---

## 6.3 ansible.cfg 확인

~~~bash
cat ansible.cfg
~~~

확인 기준:

| 항목 | 기준 |
|---|---|
| inventory | inventory.ini 지정 |
| remote_user | ubuntu |
| private_key_file | 실제 Key 경로 |
| host_key_checking | False |

---

## 6.4 inventory.ini 확인

~~~bash
cat inventory.ini
ansible-inventory --list
~~~

필수 그룹:

~~~text
proxy
web
db
backup
managed
~~~

예시 구조:

~~~ini
[proxy]
proxy-node ansible_host=PROXY_NODE_IP

[web]
web-node ansible_host=WEB_NODE_IP

[db]
db-node ansible_host=DB_NODE_IP

[backup]
backup-node ansible_host=BACKUP_NODE_IP

[managed:children]
proxy
web
db
backup
~~~

---

## 7. Ansible 기본 검증

## 7.1 Ping 테스트

~~~bash
ansible all -m ping
~~~

성공 기준:

~~~text
proxy-node | SUCCESS
web-node | SUCCESS
db-node | SUCCESS
backup-node | SUCCESS
~~~

---

## 7.2 Playbook 문법 확인

~~~bash
ansible-playbook site.yml --syntax-check
~~~

성공 기준:

~~~text
playbook: site.yml
~~~

---

## 7.3 Dry-run 가능 시 확인

필요 시 check mode를 사용한다.

~~~bash
ansible-playbook site.yml --check
~~~

단, Docker Compose 실행이나 파일 생성 작업은 check mode에서 실제와 다르게 동작할 수 있다.

---

## 8. Phase 1 Playbook 실행

## 8.1 전체 실행

~~~bash
ansible-playbook site.yml
~~~

실패 시 verbose 옵션으로 확인한다.

~~~bash
ansible-playbook site.yml -vv
~~~

---

## 8.2 역할별 실행 확인

필요 시 그룹별로 확인한다.

~~~bash
ansible proxy -m ping
ansible web -m ping
ansible db -m ping
ansible backup -m ping
~~~

---

## 8.3 Playbook 성공 기준

| 대상 | 성공 기준 |
|---|---|
| Proxy Node | Docker 설치 및 HAProxy 컨테이너 실행 |
| Web Node | Docker 설치 및 WordPress 컨테이너 실행 |
| DB Node | Docker 설치 및 MariaDB 서비스 실행 |
| Backup Node | health_check.sh / backup.sh 실행 준비 |

---

## 9. DB Node 검증

DB Node에서 MariaDB 서비스를 확인한다.

~~~bash
docker ps
sudo ss -tulnp | grep ':3306'
docker logs mariadb --tail 50
~~~

Web Node에서 DB 연결을 확인한다.

~~~bash
nc -zv DB_NODE_PRIVATE_IP 3306
~~~

성공 기준:

| 항목 | 기준 |
|---|---|
| Container | mariadb service active |
| Port | 3306 listening |
| Access | Web Node에서 DB Node 3306 접근 가능 |
| Security | DB Node 3306 전체 공개 금지 |

---

## 10. Web Node 검증

Web Node에서 WordPress 컨테이너를 확인한다.

~~~bash
docker ps
sudo ss -tulnp | grep ':80'
curl -I http://localhost
curl -I http://WEB_NODE_PRIVATE_IP
docker logs dandelion-wordpress --tail 50
~~~

성공 기준:

| 항목 | 기준 |
|---|---|
| Container | dandelion-wordpress running |
| Port | 80 listening |
| DB Connection | DB Node MariaDB 연결 |
| HTTP | Web Node 내부 HTTP 응답 |

---

## 11. Proxy Node 검증

Proxy Node에서 HAProxy 컨테이너를 확인한다.

~~~bash
docker ps
sudo ss -tulnp | grep ':80'
docker logs dandelion-haproxy --tail 50
curl -I http://PROXY_NODE_IP
~~~

성공 기준:

| 항목 | 기준 |
|---|---|
| Container | dandelion-haproxy running |
| Port | 80 listening |
| Backend | Web Node 80 연결 |
| HTTP | Proxy Node 경유 WordPress 응답 |

---

## 12. 전체 서비스 접속 검증

사용자 접속 흐름:

~~~text
Client
→ Proxy Node:80
→ HAProxy
→ Web Node:80
→ WordPress
→ DB Node:3306
→ MariaDB
~~~

검증 명령어:

~~~bash
curl -I http://PROXY_NODE_IP
curl http://PROXY_NODE_IP
~~~

브라우저에서 확인:

~~~text
http://PROXY_NODE_IP
~~~

성공 기준:

| 항목 | 기준 |
|---|---|
| HTTP Status | 200, 301, 302 중 정상 응답 |
| Browser | WordPress 화면 표시 |
| Proxy | HAProxy 로그에 backend 요청 표시 |
| Web | WordPress 컨테이너 로그에 요청 표시 |

---

## 13. Health Check 실행

Backup / Validation Node 또는 Control Node에서 실행한다.

~~~bash
bash scripts/health_check.sh
~~~

확인 대상:

| 항목 | 기준 |
|---|---|
| Proxy | HTTP 응답 |
| Web | HTTP 응답 |
| DB | 3306 연결 |
| Docker | 컨테이너 running |
| Disk | df -h 확인 |
| Memory | free -h 확인 |
| Port | ss -tulnp 확인 |

결과 캡처:

~~~text
screenshots/validation/health-check-result.png
~~~

---

## 14. Backup 실행

Backup / Validation Node 또는 Control Node에서 실행한다.

~~~bash
bash scripts/backup.sh
~~~

백업 결과물:

| 대상 | 결과물 |
|---|---|
| DB Node MariaDB | wordpress_db.sql |
| Web Node WordPress files | wordpress_files.tar.gz |

백업 디렉터리 예시:

~~~text
backup/
└── YYYYMMDD_HHMMSS/
    ├── wordpress_db.sql
    └── wordpress_files.tar.gz
~~~

확인 명령어:

~~~bash
ls -lh backup/
find backup/ -type f -name "*.sql"
find backup/ -type f -name "*.tar.gz"
~~~

성공 기준:

| 항목 | 기준 |
|---|---|
| DB Dump | wordpress_db.sql 생성 |
| Files Archive | wordpress_files.tar.gz 생성 |
| File Size | 0 byte 아님 |
| Log | 백업 실패 없음 |

---

## 15. Restore 절차 검증

복구 절차는 `restore.md` 기준으로 검증한다.

확인 항목:

| 항목 | 기준 |
|---|---|
| DB Restore | mysqldump 기반 MariaDB dump import 절차 존재 |
| Files Restore | WordPress files archive 복원 절차 존재 |
| 주의사항 | 기존 데이터 덮어쓰기 위험 명시 |
| 검증 결과 | 복구 절차 검토 또는 테스트 결과 기록 |

복구 검증은 운영 데이터를 무리하게 덮어쓰는 방식보다, 재현 가능한 절차와 명령어를 문서화하는 것을 우선한다.

---

## 16. 장애 상황 기록

장애가 발생하면 아래 형식으로 기록한다.

~~~text
## Incident Title

### 발생 일시
YYYY-MM-DD HH:MM

### 담당자
이름 / 역할

### 발생 위치
OpenStack / SSH / Ansible / Proxy / Web / DB / Backup / Monitoring

### 증상
무엇이 실패했는지 작성

### 확인 명령어
실행한 명령어 작성

### 원인
확인된 원인 작성

### 조치
수행한 해결 방법 작성

### 결과
복구 여부 작성

### 캡처
관련 캡처 파일 경로 작성

### 재발 방지
다음 실행 전 확인할 항목 작성
~~~

---

## 17. Phase 2 실행 절차

Phase 2는 Phase 1 완료 후 진행한다.

## 17.1 HTTPS 적용

~~~text
Proxy Node
→ HAProxy HTTPS
→ self-signed certificate
→ HTTP 80 to HTTPS 443 Redirect
~~~

검증:

~~~bash
curl -k -I https://PROXY_NODE_IP
curl -I http://PROXY_NODE_IP
~~~

---

## 17.2 Cinder Backup Volume 적용

~~~text
Backup / Validation Node
→ Cinder Volume attach
→ /backup mount
→ backup.sh result 저장
~~~

검증:

~~~bash
openstack volume list
lsblk
df -h
ls -lh /backup
~~~

Cinder Volume은 DB 원본 데이터 저장소가 아니라 백업 저장소로만 사용한다.

---

## 17.3 Monitoring 적용

~~~text
node_exporter
cAdvisor
Prometheus
Grafana
~~~

검증:

~~~bash
curl http://TARGET_NODE_IP:9100/metrics
curl http://TARGET_NODE_IP:8080/metrics
curl http://PROMETHEUS_IP:9090
curl http://GRAFANA_IP:3000
~~~

---

## 18. Phase 3 실행 절차

Phase 3는 도전 확장 단계이다.

~~~text
Client
→ Proxy Node / HAProxy Load Balancer
→ Web Node 1
→ Web Node 2
→ DB Node
~~~

실행 기준:

| 순서 | 작업 |
|---:|---|
| 1 | Web Node 2 생성 |
| 2 | inventory.ini에 Web Node 2 추가 |
| 3 | Web Node 2 Ansible ping 확인 |
| 4 | Web Node 2 WordPress 배포 |
| 5 | HAProxy backend에 Web Node 1 / Web Node 2 등록 |
| 6 | roundrobin 응답 확인 |
| 7 | 두 Web Node가 공통 DB Node에 연결되는지 확인 |
| 8 | Web Node 1 중지 시 Web Node 2 응답 확인 |

검증 명령어 예시:

~~~bash
for i in {1..10}; do curl http://PROXY_NODE_IP/health.html; done
~~~

Phase 3에서는 WordPress files 자동 동기화, DB Replication, OpenStack LBaaS / Octavia를 제외한다.

---

## 19. 캡처 정리

필수 캡처 경로:

~~~text
screenshots/cloud-infra/
screenshots/ansible/
screenshots/server/
screenshots/proxy/
screenshots/web/
screenshots/db/
screenshots/validation/
screenshots/backup/
screenshots/restore/
screenshots/troubleshooting/
~~~

Phase 2 또는 Phase 3 진행 시 추가 경로:

~~~text
screenshots/monitoring/
screenshots/storage/
screenshots/phase3/
~~~

---

## 20. 최종 실행 완료 기준

| 번호 | 기준 |
|---:|---|
| 1 | OpenStack 인스턴스 ACTIVE |
| 2 | Control Node에서 모든 Managed Node SSH 접속 성공 |
| 3 | ansible all -m ping 성공 |
| 4 | ansible-playbook site.yml 실행 성공 |
| 5 | DB Node MariaDB 서비스 running |
| 6 | Web Node WordPress 컨테이너 running |
| 7 | Proxy Node HAProxy 컨테이너 running |
| 8 | Proxy Node 경유 WordPress HTTP 접속 성공 |
| 9 | Web Node → DB Node 3306 연결 성공 |
| 10 | health_check.sh 실행 성공 |
| 11 | backup.sh 실행 성공 |
| 12 | restore.md 기반 복구 절차 검증 완료 |
| 13 | 장애 상황 1개 이상 정리 |
| 14 | 필수 캡처 및 문서 정리 완료 |

---

## 21. 핵심 Runbook 메시지

~~~text
본 Runbook의 핵심은 Phase 1 필수 구성을 안정적으로 완성하는 것이다.

OpenStack 인프라와 SSH 접속을 먼저 확인하고,
Ansible로 Docker 및 역할별 서비스를 배포한 뒤,
Proxy Node 경유 WordPress 접속, DB 연결, Health Check, Backup, Restore 순서로 검증한다.

Phase 1 결과만으로도 최종 발표가 가능하도록 구성하고,
Phase 2와 Phase 3은 시간이 남을 경우에만 확장한다.
~~~

