<!-- STATUS: COMPLETE -->
# Troubleshooting Guide

## 1. 목적

이 문서는 Team Dandelion 프로젝트에서 OpenStack 기반 인프라, Ansible 자동화, Docker Compose 기반 WordPress/MariaDB 서비스, Backup/Restore 검증, Monitoring 확장 구성 중 발생할 수 있는 주요 오류와 해결 방법을 정리한다.

문제 발생 시 단순히 명령어를 반복 실행하지 않고, 아래 순서로 원인을 좁혀간다.

~~~text
Network
→ SSH
→ Sudo
→ Python
→ Ansible Inventory
→ Playbook Syntax
→ Docker
→ Docker Compose
→ WordPress
→ MariaDB
→ Backup / Restore
→ Service Validation
~~~

---

## 2. SSH 접속 실패

### 증상

~~~text
UNREACHABLE
Permission denied
Connection timed out
No route to host
~~~

### 확인 항목

| 원인 | 확인 방법 | 해결 |
|---|---|---|
| IP 주소 오류 | inventory.ini 또는 OpenStack server list 확인 | 실제 서버 IP로 수정 |
| 보안그룹 22번 미허용 | OpenStack Security Group 확인 | TCP 22 허용 |
| SSH Key 경로 오류 | ansible_ssh_private_key_file 확인 | 올바른 Key 경로 입력 |
| 사용자 계정 오류 | ansible_user 확인 | ubuntu 계정 기준으로 수정 |
| 서버 미부팅 | OpenStack Console 확인 | 인스턴스 상태 확인 |
| 포트포워딩 오류 | 공유기 포트포워딩 확인 | 외부 포트와 내부 IP 매핑 수정 |

### 확인 명령어

~~~bash
ssh -i ~/.ssh/ansible_key ubuntu@SERVER_IP
openstack server list
openstack security group rule list
~~~

---

## 3. Ansible Ping 실패

### 증상

~~~text
ansible all -m ping
FAILED
UNREACHABLE
~~~

### 확인 순서

~~~text
1. inventory.ini IP 확인
2. ansible_user 확인
3. SSH Key 경로 확인
4. Managed Node SSH 접속 확인
5. Python3 설치 확인
6. sudo 권한 확인
~~~

### 확인 명령어

~~~bash
ansible all -m ping
ansible all -m ping -vvv
ssh -i ~/.ssh/ansible_key ubuntu@SERVER_IP
~~~

-vvv 옵션을 붙이면 상세 로그를 확인할 수 있다.

---

## 4. sudo 권한 오류

### 증상

~~~text
Missing sudo password
sudo: a password is required
BECOME password
~~~

### 확인 명령어

~~~bash
sudo -v
whoami
groups
~~~

### 해결 방법

Managed Node에서 sudo 권한을 확인한다.

~~~bash
sudo visudo
~~~

Ubuntu 기본 계정 기준:

~~~text
ubuntu ALL=(ALL) NOPASSWD:ALL
~~~

실습용 user1 계정 기준:

~~~text
user1 ALL=(ALL) NOPASSWD:ALL
~~~

---

## 5. Python 오류

### 증상

~~~text
/usr/bin/python3 not found
MODULE FAILURE
Failed to find required executable python
~~~

### 확인 명령어

~~~bash
python3 --version
which python3
~~~

### 해결 방법

~~~bash
sudo apt update
sudo apt install -y python3
~~~

inventory.ini에는 아래 값을 넣는다.

~~~ini
[all:vars]
ansible_python_interpreter=/usr/bin/python3
~~~

---

## 6. Playbook 문법 오류

### 증상

~~~text
Syntax Error while loading YAML
mapping values are not allowed
could not find expected ':'
~~~

### 원인

대부분 YAML 들여쓰기 문제다.

### 확인 명령어

~~~bash
cd ansible
ansible-playbook --syntax-check site.yml
~~~

### 기준

YAML은 탭을 쓰지 않고 스페이스 2칸 기준으로 작성한다.

---

## 7. apt lock 오류

### 증상

~~~text
Could not get lock /var/lib/dpkg/lock-frontend
Unable to acquire the dpkg frontend lock
~~~

### 원인

다른 apt 프로세스가 실행 중이다.

### 확인 명령어

~~~bash
ps aux | grep apt
~~~

### 해결 방법

잠시 기다린 후 다시 실행한다.

필요 시 아래 명령어로 상태를 복구한다.

~~~bash
sudo dpkg --configure -a
sudo apt update
~~~

---

## 8. Docker 설치 실패

### 증상

~~~text
docker: command not found
Failed to start docker.service
Unit docker.service not found
~~~

### 확인 명령어

~~~bash
docker --version
systemctl status docker
~~~

### 해결 방법

~~~bash
sudo apt update
sudo apt install -y docker.io
sudo systemctl enable docker
sudo systemctl start docker
~~~

---

## 9. Docker 권한 오류

### 증상

~~~text
permission denied while trying to connect to the Docker daemon socket
~~~

### 해결 방법

현재 사용자를 docker 그룹에 추가한다.

~~~bash
sudo usermod -aG docker $USER
newgrp docker
~~~

또는 실습 중에는 sudo로 실행한다.

~~~bash
sudo docker ps
~~~

---

## 10. Docker Compose 실행 실패

### 증상

~~~text
docker compose up -d 실패
yaml: line error
services must be a mapping
port is already allocated
~~~

### 원인

| 원인 | 설명 |
|---|---|
| YAML 문법 오류 | docker-compose.yml 들여쓰기 또는 구조 오류 |
| 포트 충돌 | 80, 443, 3000, 9090 등 기존 사용 중 |
| 이미지 Pull 실패 | Docker Hub 접근 실패 |
| Volume 권한 문제 | Docker Volume 또는 bind mount 권한 문제 |
| 환경변수 오류 | WordPress와 MariaDB 접속 정보 불일치 |

### 확인 명령어

~~~bash
cd docker/compose
docker compose config
docker compose ps
docker compose logs
docker ps -a
sudo ss -tulnp
~~~

### 해결 방법

Compose 문법을 먼저 확인한다.

~~~bash
cd docker/compose
docker compose config
~~~

컨테이너 상태를 확인한다.

~~~bash
docker compose ps
docker compose logs --tail 100
~~~

서비스를 재시작한다.

~~~bash
docker compose restart
~~~

구성이 꼬였을 경우 컨테이너만 내렸다가 다시 실행한다.

~~~bash
docker compose down
docker compose up -d
~~~

주의할 점은 DB 원본 볼륨을 임의로 삭제하지 않는 것이다.

삭제 금지 대상:

~~~text
db_data
wordpress_data
~~~

---

## 11. Custom WordPress Image Build 실패

### 증상

~~~text
docker build failed
failed to solve
COPY custom.ini failed
pull access denied
no space left on device
~~~

### 원인

| 원인 | 설명 |
|---|---|
| Dockerfile 오류 | FROM, COPY 경로 오류 |
| custom.ini 누락 | Dockerfile에서 참조하는 파일이 없음 |
| Docker Hub 접근 실패 | 외부 네트워크 또는 DNS 문제 |
| 디스크 부족 | 이미지 빌드 공간 부족 |

### 확인 명령어

~~~bash
ls -lh docker/wordpress
cat docker/wordpress/Dockerfile
docker build -t dandelion-wordpress ./docker/wordpress
docker images
docker system df
df -h
~~~

### 해결 방법

- Dockerfile의 base image가 `wordpress:php8.2-apache`인지 확인한다.
- `docker/wordpress/custom.ini` 파일이 존재하는지 확인한다.
- Docker Hub 접근 가능 여부를 확인한다.
- 디스크 부족 시 불필요한 이미지와 컨테이너를 정리한다.

~~~bash
docker image prune
docker container prune
docker system df
~~~

---

## 12. WordPress / MariaDB 컨테이너 실행 실패

### 증상

~~~text
WordPress container exited
MariaDB container exited
Error establishing a database connection
Bind for 0.0.0.0:80 failed: port is already allocated
~~~

### 원인

| 원인 | 설명 |
|---|---|
| 80번 포트 충돌 | 다른 프로세스가 80번 포트를 사용 중 |
| WordPress 환경변수 오류 | DB 접속 정보 불일치 |
| MariaDB 컨테이너 오류 | DB 초기화 실패 또는 볼륨 문제 |
| Docker Volume 문제 | 기존 볼륨 데이터와 설정 충돌 |
| Compose Network 문제 | WordPress가 DB 컨테이너를 찾지 못함 |

### 확인 명령어

~~~bash
cd docker/compose
docker compose ps
docker compose logs --tail 100
docker logs dandelion-wordpress --tail 100
docker logs dandelion-mariadb --tail 100
sudo ss -tulnp | grep :80
~~~

### 해결 방법

서비스를 재시작한다.

~~~bash
cd docker/compose
docker compose restart
~~~

DB 컨테이너만 재시작한다.

~~~bash
docker restart dandelion-mariadb
docker restart dandelion-wordpress
~~~

구성이 꼬였을 경우 컨테이너만 재생성한다.

~~~bash
cd docker/compose
docker compose down
docker compose up -d
~~~

---

## 13. HTTP 접속 실패

### 증상

~~~text
curl: Failed to connect
Connection refused
Connection timed out
HTTP 500
HTTP 502
HTTP 503
~~~

### 확인 항목

| 원인 | 확인 명령어 | 해결 |
|---|---|---|
| 컨테이너 미실행 | docker compose ps | WordPress / MariaDB 컨테이너 재시작 |
| 80번 포트 미오픈 | ss -tulnp | 포트 확인 |
| 보안그룹 80번 미허용 | OpenStack Security Group | TCP 80 허용 |
| 포트포워딩 오류 | 공유기 설정 확인 | 외부 포트와 내부 IP 매핑 수정 |
| DB 연결 실패 | docker logs dandelion-mariadb | DB 컨테이너 및 환경변수 확인 |

### 확인 명령어

~~~bash
curl -I http://localhost
curl -I http://SERVER_IP
docker compose ps
docker logs dandelion-wordpress --tail 100
docker logs dandelion-mariadb --tail 100
~~~

정상 기준:

~~~text
HTTP/1.1 200 OK
또는
HTTP/1.1 302 Found
~~~

---

## 14. Backup 실패

### 증상

~~~text
DB dump failed
No space left on device
Permission denied
Backup file not created
SCP transfer failed
~~~

### 확인 명령어

~~~bash
df -h
docker ps
docker logs dandelion-mariadb --tail 50
ls -lh /backup
bash scripts/backup.sh
echo $?
~~~

### 주요 원인과 해결

| 원인 | 해결 |
|---|---|
| MariaDB 컨테이너 미실행 | docker restart dandelion-mariadb |
| DB 인증 정보 오류 | backup.sh의 DB 계정 / 비밀번호 확인 |
| 디스크 부족 | 오래된 백업 삭제 또는 Cinder Volume 확장 |
| 백업 디렉터리 권한 문제 | /backup 디렉터리 권한 확인 |
| Backup Node 전송 실패 | SSH / SCP 접속 확인 |

### 백업 확인 기준

~~~bash
ls -lh /backup
file /backup/*.sql
file /backup/*.tar.gz
~~~

정상 기준:

~~~text
MariaDB dump 파일 생성
WordPress files archive 생성
백업 파일 크기가 0이 아님
~~~

---

## 15. Restore 실패

### 증상

~~~text
DB restore failed
gzip: stdin: not in gzip format
Cannot open: No such file or directory
WordPress page not recovered
Error establishing a database connection
~~~

### 확인 명령어

~~~bash
ls -lh /backup
file /backup/*.sql
file /backup/*.tar.gz
docker compose ps
docker volume ls
~~~

### 주요 원인과 해결

| 원인 | 해결 |
|---|---|
| 백업 파일 손상 | file 명령어로 백업 파일 형식 확인 |
| DB dump 파일 누락 | backup.sh 재실행 |
| WordPress files archive 누락 | WordPress 파일 백업 경로 확인 |
| MariaDB 컨테이너 미실행 | DB 컨테이너 재시작 |
| 복구 순서 오류 | DB 복구 후 WordPress files 복구 순서 확인 |

### 복구 검증 기준

~~~bash
curl -I http://localhost
docker compose ps
docker logs dandelion-wordpress --tail 50
docker logs dandelion-mariadb --tail 50
~~~

정상 기준:

~~~text
WordPress HTTP 응답 정상
MariaDB 컨테이너 running 상태
복구 후 WordPress 페이지 접근 가능
~~~

---

## 16. 리소스 부족 시 트러블슈팅

### 개요

운영 중 Web Node의 CPU, Memory, Disk, Network 리소스가 부족해질 경우 WordPress 접속 지연, MariaDB 응답 지연, 컨테이너 재시작, 백업 실패 등의 문제가 발생할 수 있다.

### 발생 가능한 리소스 부족 시나리오

| 시나리오 | 증상 | 주요 원인 |
|---|---|---|
| CPU 사용률 과다 | WordPress 접속 지연, 응답 속도 저하 | 트래픽 증가, PHP 처리량 증가 |
| Memory 부족 | 컨테이너 재시작, MariaDB 연결 실패 | WordPress/PHP 메모리 증가, DB 메모리 부족 |
| Disk 사용량 부족 | 백업 실패, DB 쓰기 실패 | DB 데이터 증가, 백업 파일 누적 |
| MariaDB 응답 지연 | WordPress DB connection error | DB 부하, 메모리 부족, 디스크 I/O 지연 |
| Backup 실패 | backup.sh 실행 실패 | 디스크 부족, 권한 문제, DB dump 실패 |
| Reverse Proxy 장애 | HTTPS 502/503 발생 | Backend 장애, HAProxy 설정 오류 |

### 기본 확인 명령어

~~~bash
uptime
free -h
df -h
top
docker ps
docker ps -a
docker stats
docker system df
curl -I http://localhost
docker logs dandelion-wordpress --tail 50
docker logs dandelion-mariadb --tail 50
~~~

### CPU 부족 대응

~~~bash
top
docker stats
ps aux --sort=-%cpu | head
~~~

임시 조치:

~~~bash
docker restart dandelion-wordpress
cd docker/compose
docker compose restart
~~~

개선 방향:

| 개선 방안 | 설명 |
|---|---|
| flavor 상향 | OpenStack 인스턴스 CPU 사양 증가 |
| 컨테이너 리소스 제한 | Docker Compose에서 CPU 제한 설정 |
| 모니터링 도입 | cAdvisor / Prometheus / Grafana로 CPU 사용률 추적 |

### Memory 부족 대응

~~~bash
free -h
docker stats
docker ps -a
dmesg | grep -i oom
journalctl -xe | grep -i oom
~~~

임시 조치:

~~~bash
docker container prune
docker image prune
cd docker/compose
docker compose restart
~~~

개선 방향:

| 개선 방안 | 설명 |
|---|---|
| flavor 상향 | Web Node 메모리 증설 |
| MariaDB 설정 조정 | DB 메모리 사용량 제한 |
| WordPress PHP 설정 조정 | custom.ini에서 memory_limit 조정 |
| Swap 구성 검토 | 실습 환경에서 임시 대응 가능 |

### Disk 부족 대응

~~~bash
df -h
du -sh /var/lib/docker
docker system df
docker volume ls
~~~

임시 조치:

~~~bash
docker system prune
docker image prune
docker container prune
find /backup -type f -mtime +7 -name "*.tar.gz" -delete
find /backup -type f -mtime +7 -name "*.sql" -delete
~~~

주의 사항:

~~~text
db_data
wordpress_data
~~~

위 Docker Volume은 원본 데이터이므로 삭제하면 안 된다.

---

## 17. HAProxy Reverse Proxy 장애

### 증상

~~~text
HTTPS 접속 실패
HTTP 502
HTTP 503
SSL certificate error
~~~

### 주요 원인

| 원인 | 설명 |
|---|---|
| Backend IP 오류 | haproxy.cfg의 Web Node IP가 잘못됨 |
| Web Node 장애 | WordPress HTTP 80 응답 실패 |
| 인증서 오류 | pem 파일 경로 또는 권한 문제 |
| 보안그룹 오류 | 80/443 포트 미허용 |

### 확인 명령어

~~~bash
docker ps
docker logs dandelion-haproxy --tail 100
curl -I http://WEB_NODE_IP
curl -k -I https://PROXY_NODE_IP
~~~

### 조치 방법

~~~bash
docker restart dandelion-haproxy
docker logs dandelion-haproxy --tail 100
~~~

---

## 18. Prometheus 메트릭 수집 실패

### 증상

~~~text
Prometheus target DOWN
metrics endpoint connection refused
~~~

### 주요 원인

| 원인 | 조치 |
|---|---|
| target IP 오류 | prometheus.yml의 target IP 수정 |
| exporter 미실행 | node_exporter 또는 cAdvisor 컨테이너 확인 |
| 보안그룹 차단 | 9100, 8080 포트 접근 허용 |
| Prometheus 설정 오류 | prometheus.yml 문법 확인 후 재시작 |

### 확인 명령어

~~~bash
curl http://WEB_NODE_IP:9100/metrics
curl http://WEB_NODE_IP:8080/metrics
docker logs dandelion-prometheus --tail 100
~~~

---

## 19. Grafana 접속 실패

### 증상

~~~text
Grafana dashboard connection failed
Connection refused
~~~

### 확인 명령어

~~~bash
docker ps
docker logs dandelion-grafana --tail 100
curl -I http://MONITORING_NODE_IP:3000
ss -tulnp
~~~

### 조치 방법

~~~bash
docker restart dandelion-grafana
~~~

보안그룹과 포트포워딩에서 3000 포트를 확인한다.

---

## 20. OpenStack 인스턴스 장애

### 증상

~~~text
Instance ERROR
Instance SHUTOFF
Floating IP 접속 불가
No valid host
~~~

### 주요 원인

| 원인 | 설명 |
|---|---|
| 자원 부족 | compute node에 CPU/RAM/Disk 부족 |
| 이미지 오류 | Ubuntu image 문제 |
| 네트워크 오류 | subnet/router 연결 문제 |
| 보안그룹 오류 | SSH/HTTP/HTTPS 포트 미허용 |
| Floating IP 오류 | FIP 연결 누락 또는 잘못된 대상 연결 |

### 확인 명령어

~~~bash
openstack server list
openstack server show SERVER_NAME
openstack console log show SERVER_NAME
openstack floating ip list
openstack security group rule list
~~~

### 조치 방법

| 원인 | 조치 |
|---|---|
| ERROR 상태 | console log 확인 후 재생성 |
| 네트워크 미연결 | subnet/router 연결 확인 |
| Floating IP 오류 | FIP 재연결 |
| 보안그룹 오류 | SSH/HTTP/HTTPS 규칙 확인 |

---

## 21. OpenStack CLI 자동화 실패

### 증상

~~~text
openstack command not found
Missing value auth-url
The request you have made requires authentication
Resource already exists
No Network found
~~~

### 주요 원인

| 원인 | 설명 |
|---|---|
| 인증 정보 오류 | openrc 또는 clouds.yaml 설정 문제 |
| CLI 미설치 | python-openstackclient 미설치 |
| 리소스 이름 오류 | image, flavor, network 이름 불일치 |
| 중복 생성 오류 | 이미 같은 이름의 리소스 존재 |
| 권한 부족 | 프로젝트 또는 사용자 권한 부족 |

### 확인 명령어

~~~bash
openstack token issue
openstack image list
openstack flavor list
openstack network list
openstack server list
~~~

### 조치 방법

- OpenStack 인증 정보를 다시 로드한다.
- image, flavor, network 이름을 확인한다.
- 이미 생성된 리소스가 있는지 확인한다.
- 중복 생성 방지 로직을 추가한다.
- 실패 시 B+ Stretch Goal은 제외하고 A급/B급 결과 중심으로 발표한다.

---

## 22. 운영 중 발생 가능한 장애 시나리오 요약

| 시나리오 | 증상 | 주요 확인 |
|---|---|---|
| SSH 접속 실패 | 서버 접속 불가 | SSH Key, 보안그룹, 포트포워딩 |
| 포트포워딩 장애 | 외부 접속 불가 | 공유기 포트포워딩, 내부 IP, 보안그룹 |
| WordPress 접속 실패 | 웹페이지 접속 불가 | docker ps, curl, WordPress logs |
| MariaDB 연결 실패 | DB connection error | MariaDB logs, 환경변수, Docker network |
| Docker Compose 실패 | 서비스 실행 불가 | docker compose config, logs |
| Custom Image Build 실패 | 이미지 빌드 실패 | Dockerfile, custom.ini, Docker Hub 접근 |
| Backup 실패 | 백업 파일 미생성 | backup.sh, df -h, DB logs |
| Restore 실패 | 복구 실패 | 백업 파일, volume, 복구 순서 |
| HAProxy 장애 | HTTPS 502/503 | haproxy.cfg, backend IP, 인증서 |
| Prometheus 수집 실패 | Target DOWN | exporter, prometheus.yml, 포트 |
| Grafana 접속 실패 | 대시보드 접속 불가 | Grafana logs, 3000 포트 |
| Ansible Ping 실패 | 자동화 대상 접근 불가 | inventory, SSH, Python |
| Ansible Playbook 실패 | 자동 배포 실패 | task log, 권한, Docker 상태 |
| OpenStack 인스턴스 장애 | ACTIVE 아님, 접속 불가 | server list/show, console log |
| OpenStack CLI 자동화 실패 | 노드 자동 생성 실패 | openrc/clouds.yaml, image/flavor/network |

---

## 23. 최종 문제 해결 우선순위

문제 발생 시 아래 순서로 확인한다.

~~~text
1. 인스턴스가 ACTIVE 상태인가?
2. IP 주소와 포트포워딩 대상이 맞는가?
3. 보안그룹에서 22/80/443 포트가 열려 있는가?
4. SSH Key가 맞는가?
5. ansible_user가 맞는가?
6. sudo 권한이 있는가?
7. Python3가 설치되어 있는가?
8. inventory.ini 문법이 맞는가?
9. site.yml 문법이 맞는가?
10. Docker가 실행 중인가?
11. Docker Compose 문법이 정상인가?
12. WordPress 컨테이너가 실행 중인가?
13. MariaDB 컨테이너가 실행 중인가?
14. HTTP 접속이 가능한가?
15. Backup / Restore 검증이 가능한가?
16. HAProxy / Monitoring 확장 항목이 A급 결과를 방해하지 않는가?
~~~

---

## 24. 운영 중 장애 대응 원칙

| 단계 | 원칙 |
|---|---|
| 1단계 | 접속 경로를 확인한다 |
| 2단계 | 인스턴스 상태를 확인한다 |
| 3단계 | 보안그룹과 포트포워딩을 확인한다 |
| 4단계 | Docker Compose 상태를 확인한다 |
| 5단계 | WordPress와 MariaDB 로그를 확인한다 |
| 6단계 | Backup / Restore 가능 여부를 확인한다 |
| 7단계 | Monitoring Target 상태를 확인한다 |
| 8단계 | 조치 결과를 문서화한다 |

장애 대응은 원인 확인 없이 재시작하는 방식이 아니라, 탐지 → 원인 분석 → 조치 → 검증 → 문서화 순서로 수행한다.
