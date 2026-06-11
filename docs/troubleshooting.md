# Troubleshooting Guide

## 1. 목적

이 문서는 Ansible 기반 클라우드 인프라 자동화 실습 중 발생할 수 있는 주요 오류와 해결 방법을 정리한다.

문제 발생 시 아래 순서로 확인한다.

~~~text
Network
→ SSH
→ Sudo
→ Python
→ Ansible Inventory
→ Playbook Syntax
→ Docker
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
| IP 주소 오류 | inventory.ini 확인 | 실제 서버 IP로 수정 |
| 보안그룹 22번 미허용 | Cloud Security Group 확인 | TCP 22 허용 |
| SSH Key 경로 오류 | ansible_ssh_private_key_file 확인 | 올바른 Key 경로 입력 |
| 사용자 계정 오류 | ansible_user 확인 | ubuntu 또는 user1로 수정 |
| 서버 미부팅 | 클라우드 콘솔 확인 | 인스턴스 상태 확인 |

### 확인 명령어

~~~bash
ssh -i ~/.ssh/ansible_key ubuntu@server-ip
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
ansible all -m ping -vvv
~~~

-vvv 옵션을 붙이면 상세 로그를 볼 수 있다.

---

## 4. sudo 권한 오류

### 증상

~~~text
Missing sudo password
sudo: a password is required
BECOME password
~~~

### 해결 방법

Managed Node에서 sudo 권한을 확인한다.

~~~bash
sudo -v
~~~

비밀번호 없이 sudo가 필요하면 아래 설정을 추가한다.

~~~bash
sudo visudo
~~~

Ubuntu 기본 계정 기준:

~~~text
ubuntu ALL=(ALL) NOPASSWD:ALL
~~~

user1 계정 기준:

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

### 해결 방법

Managed Node에서 Python3 설치 여부를 확인한다.

~~~bash
python3 --version
which python3
~~~

없으면 설치한다.

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

YAML은 탭을 쓰지 말고 스페이스 2칸 기준으로 작성한다.

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
sudo usermod -aG docker 
newgrp docker
~~~

또는 실습 중에는 sudo로 실행한다.

~~~bash
sudo docker ps
~~~

---

## 10. Nginx 컨테이너 실행 실패

### 증상

~~~text
Conflict. The container name "/web-test" is already in use
Bind for 0.0.0.0:80 failed: port is already allocated
~~~

### 해결 방법

기존 컨테이너를 삭제한다.

~~~bash
sudo docker rm -f web-test
~~~

80번 포트를 사용하는 프로세스를 확인한다.

~~~bash
sudo ss -tulnp | grep :80
~~~

다시 실행한다.

~~~bash
sudo docker run -d --name web-test -p 80:80 nginx
~~~

---

## 11. HTTP 접속 실패

### 증상

~~~text
curl: Failed to connect
Connection refused
Connection timed out
~~~

### 확인 항목

| 원인 | 확인 명령어 | 해결 |
|---|---|---|
| 컨테이너 미실행 | docker ps | nginx 컨테이너 실행 |
| 80번 포트 미오픈 | ss -tulnp | 포트 확인 |
| 보안그룹 80번 미허용 | Cloud Console | TCP 80 허용 |
| 잘못된 IP 접속 | ip addr | 올바른 IP 사용 |

### 확인 명령어

~~~bash
curl -I http://localhost
curl -I http://server-ip
~~~

---

## 12. Backup 실패

### 증상

~~~text
tar: Cannot stat
No such file or directory
Permission denied
~~~

### 확인 항목

~~~bash
ls -ld /var/www/html
ls -ld /backup
~~~

### 해결 방법

~~~bash
sudo mkdir -p /var/www/html
sudo mkdir -p /backup
echo "Team Dandelion Backup Test" | sudo tee /var/www/html/index.html
sudo ./backup.sh
~~~

---

## 13. Restore 실패

### 증상

~~~text
Cannot open: No such file or directory
gzip: stdin: not in gzip format
~~~

### 확인 항목

~~~bash
ls -lh /backup
file /backup/backup-file.tar.gz
~~~

### 복구 명령어

~~~bash
sudo tar -xzf /backup/백업파일명.tar.gz -C /
~~~

복구 확인:

~~~bash
cat /var/www/html/index.html
~~~

---

## 14. 문제 해결 우선순위

문제 발생 시 아래 순서로 확인한다.

~~~text
1. 서버가 켜져 있는가?
2. IP 주소가 맞는가?
3. 보안그룹에서 22/80 포트가 열려 있는가?
4. SSH Key가 맞는가?
5. ansible_user가 맞는가?
6. sudo 권한이 있는가?
7. Python3가 있는가?
8. inventory.ini 문법이 맞는가?
9. site.yml 문법이 맞는가?
10. Docker가 실행 중인가?
11. Nginx 컨테이너가 실행 중인가?
12. HTTP 접속이 가능한가?
~~~

---

## 15. 최종 기준

Troubleshooting의 핵심은 에러 메시지를 기준으로 원인을 좁히는 것이다.

단순히 명령어를 다시 실행하지 말고, Network → SSH → Ansible → Docker → Service 순서로 확인한다.
