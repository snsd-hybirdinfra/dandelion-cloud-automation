<!-- STATUS: COMPLETE -->
# Project Runbook

## 1. 목적

이 문서는 Team Dandelion 프로젝트의 실행 절차를 정리한다.

본 프로젝트는 Ansible Control Node에서 Managed Node로 SSH 접속하여 서버 초기 설정, Docker 설치, Nginx 컨테이너 배포, 상태 점검, 백업 및 복구 검증을 수행한다.

---

## 2. 전체 실행 흐름

~~~text
1. GitHub Repository Clone
2. Cloud Server 준비
3. SSH Key 기반 접속 확인
4. Inventory IP 수정
5. Ansible Ping Test
6. Playbook Syntax Check
7. Playbook 실행
8. Docker / Nginx 확인
9. Health Check 실행
10. Backup / Restore 검증
~~~

---

## 3. Repository Clone

~~~bash
git clone https://github.com/snsd-hybirdinfra/dandelion-cloud-automation.git
cd dandelion-cloud-automation
~~~

---

## 4. Ansible 실행 전 확인

실행 전 아래 문서를 먼저 확인한다.

~~~text
docs/pre-run-checklist.md
docs/troubleshooting.md
~~~

필수 조건은 다음과 같다.

| 조건 | 설명 |
|---|---|
| 서버 준비 | Control Node, Web Node, Backup Node 준비 |
| SSH 접속 | Control Node에서 Managed Node로 SSH 접속 가능 |
| sudo 권한 | Managed Node에서 sudo 실행 가능 |
| Python3 | Managed Node에 Python3 설치 |
| Inventory | 실제 서버 IP로 inventory.ini 수정 |
| Security Group | 22, 80 포트 허용 |

---

## 5. Inventory 수정

파일 위치:

~~~text
ansible/inventory.ini
~~~

예시:

~~~ini
[web]
web-node ansible_host=10.21.1.11 ansible_user=ubuntu

[backup]
backup-node ansible_host=10.21.1.12 ansible_user=ubuntu

[all:vars]
ansible_ssh_private_key_file=~/.ssh/ansible_key
ansible_python_interpreter=/usr/bin/python3
~~~

주의사항:

- ansible_host는 실제 서버 IP로 수정한다.
- ansible_user는 실제 접속 계정으로 수정한다.
- SSH Key 경로가 실제 위치와 맞는지 확인한다.

---

## 6. Ansible Ping Test

~~~bash
cd ansible
ansible all -m ping
~~~

정상 결과:

~~~text
pong
~~~

Ping 테스트가 실패하면 아래 문서를 확인한다.

~~~text
docs/troubleshooting.md
~~~

---

## 7. Playbook Syntax Check

~~~bash
ansible-playbook --syntax-check site.yml
~~~

정상 결과:

~~~text
playbook: site.yml
~~~

---

## 8. Playbook 실행

~~~bash
ansible-playbook site.yml
~~~

Playbook에서 수행하는 작업:

| 작업 | 대상 |
|---|---|
| apt cache update | all |
| basic package install | all |
| docker.io install | all |
| docker service enable/start | all |
| nginx image pull | web |
| nginx container deploy | web |
| docker ps 확인 | web |

---

## 9. Docker / Nginx 확인

Web Node에서 확인:

~~~bash
docker ps
curl -I http://localhost
~~~

외부에서 확인:

~~~bash
curl -I http://web-node-ip
~~~

---

## 10. Health Check 실행

스크립트 위치:

~~~text
scripts/health_check.sh
~~~

실행:

~~~bash
chmod +x scripts/health_check.sh
./scripts/health_check.sh
~~~

확인 항목:

- Hostname
- Uptime
- Memory
- Disk
- IP Address
- Listening Ports
- Docker Status
- Running Containers
- HTTP Check

---

## 11. Backup 실행

스크립트 위치:

~~~text
scripts/backup.sh
~~~

테스트 파일 생성:

~~~bash
sudo mkdir -p /var/www/html
echo "Team Dandelion Backup Test" | sudo tee /var/www/html/index.html
~~~

백업 실행:

~~~bash
chmod +x scripts/backup.sh
sudo ./scripts/backup.sh
~~~

백업 확인:

~~~bash
ls -lh /backup
~~~

---

## 12. Restore 검증

장애 상황 생성:

~~~bash
sudo rm -f /var/www/html/index.html
ls -l /var/www/html
~~~

복구 실행:

~~~bash
sudo tar -xzf /backup/백업파일명.tar.gz -C /
~~~

복구 확인:

~~~bash
cat /var/www/html/index.html
curl http://localhost
~~~

---

## 13. 실행 결과 캡처 기준

| 항목 | 저장 위치 |
|---|---|
| Cloud Instance | screenshots/cloud-infra/ |
| Server / Docker | screenshots/server/ |
| Ansible 실행 결과 | screenshots/ansible/ |
| Health / Backup / Restore | screenshots/validation/ |

---

## 14. 최종 성공 기준

아래 조건을 만족하면 프로젝트 실행 성공으로 판단한다.

| 기준 | 결과 |
|---|---|
| Ansible Ping 성공 | pong |
| Playbook 실행 성공 | failed=0 |
| Docker 서비스 실행 | active |
| Nginx 컨테이너 실행 | docker ps 확인 |
| HTTP 응답 성공 | HTTP/1.1 200 OK |
| 백업 파일 생성 | /backup 디렉터리 확인 |
| 복구 성공 | index.html 복구 확인 |

---

## 15. 핵심 요약

~~~text
Ansible로 서버 초기 설정과 Docker 기반 Nginx 배포를 자동화하고,
Health Check, Backup, Restore 절차로 자동화 결과를 검증한다.
~~~


