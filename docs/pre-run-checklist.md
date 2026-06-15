<!-- STATUS: COMPLETE -->
# Pre-Run Checklist

## 1. 목적

이 문서는 Ansible Playbook 실행 전에 반드시 확인해야 할 사전 조건을 정리한다.

Ansible 자동화는 서버, 네트워크, SSH, sudo 권한, Python 환경이 준비되어 있어야 정상 실행된다.

---

## 2. 전체 사전 준비 흐름

~~~text
Cloud Server Ready
→ Network / Security Group Ready
→ SSH Access Ready
→ Sudo Permission Ready
→ Python Ready
→ Ansible Inventory Ready
→ Ansible Ping Test
→ Playbook Execution
~~~

---

## 3. Cloud Infrastructure Checklist

담당자: 백서빈

| 항목 | 확인 명령 / 기준 | 상태 |
|---|---|---|
| Control Node 생성 | 클라우드 콘솔 확인 | TBD |
| Web Node 생성 | 클라우드 콘솔 확인 | TBD |
| Backup Node 생성 | 클라우드 콘솔 확인 | TBD |
| Public IP 확인 | 클라우드 콘솔 또는 ip addr | TBD |
| Private IP 확인 | 클라우드 콘솔 또는 ip addr | TBD |
| Security Group 설정 | 22, 80 허용 확인 | TBD |
| SSH 접속 가능 | ssh user@server-ip | TBD |

---

## 4. Server Environment Checklist

담당자: 이진욱

| 항목 | 확인 명령 | 상태 |
|---|---|---|
| Hostname 확인 | hostname | TBD |
| OS 확인 | cat /etc/os-release | TBD |
| Kernel 확인 | uname -r | TBD |
| 사용자 확인 | whoami | TBD |
| IP 확인 | ip addr | TBD |
| 패키지 업데이트 | sudo apt update | TBD |
| 기본 패키지 설치 | sudo apt install -y curl wget git vim net-tools | TBD |
| Docker 설치 여부 | docker --version | TBD |
| Docker 서비스 상태 | systemctl status docker | TBD |

---

## 5. SSH / Sudo Checklist

담당자: 조민석

| 항목 | 확인 명령 | 상태 |
|---|---|---|
| SSH Key 생성 | ls -al ~/.ssh | TBD |
| 공개키 확인 | cat ~/.ssh/ansible_key.pub | TBD |
| Managed Node 접속 | ssh -i ~/.ssh/ansible_key ubuntu@server-ip | TBD |
| sudo 권한 확인 | sudo -v | TBD |
| Python 확인 | python3 --version | TBD |

---

## 6. Ansible Checklist

담당자: 조민석

| 항목 | 확인 명령 | 상태 |
|---|---|---|
| Ansible 설치 | ansible --version | TBD |
| Inventory 파일 확인 | cat ansible/inventory.ini | TBD |
| ansible.cfg 확인 | cat ansible/ansible.cfg | TBD |
| Playbook 문법 확인 | ansible-playbook --syntax-check ansible/site.yml | TBD |
| Ping 테스트 | ansible all -m ping | TBD |
| Playbook 실행 | ansible-playbook ansible/site.yml | TBD |

---

## 7. Validation Checklist

담당자: 박재우

| 항목 | 확인 명령 | 상태 |
|---|---|---|
| Docker 상태 확인 | systemctl is-active docker | TBD |
| 컨테이너 확인 | docker ps | TBD |
| HTTP 응답 확인 | curl -I http://localhost | TBD |
| 백업 스크립트 확인 | ls -l scripts/backup.sh | TBD |
| 백업 실행 | sudo ./backup.sh | TBD |
| 백업 파일 확인 | ls -lh /backup | TBD |
| 복구 테스트 | tar -xzf backup-file -C / | TBD |

---

## 8. 실행 전 필수 확인

Playbook 실행 전 아래 조건은 반드시 만족해야 한다.

| 필수 조건 | 담당 |
|---|---|
| 서버 3대 준비 완료 | 백서빈 |
| Control Node에서 Managed Node로 SSH 가능 | 조민석 |
| Managed Node에 sudo 가능 | 이진욱 / 조민석 |
| inventory.ini IP 정보 최신화 | 조민석 |
| 보안그룹 22번 포트 허용 | 백서빈 |
| Web Node 80번 포트 허용 | 백서빈 |
| site.yml 문법 오류 없음 | 조민석 |

---

## 9. 실행 순서

~~~bash
cd dandelion-cloud-automation/ansible

ansible --version

ansible all -m ping

ansible-playbook --syntax-check site.yml

ansible-playbook site.yml
~~~

---

## 10. 실패 시 확인 순서

Ansible 실행이 실패하면 아래 순서로 확인한다.

~~~text
1. IP 주소가 맞는지 확인
2. Security Group에서 22번 포트가 열려 있는지 확인
3. SSH Key 경로가 맞는지 확인
4. ansible_user 값이 맞는지 확인
5. Managed Node에서 sudo 권한이 있는지 확인
6. Python3가 설치되어 있는지 확인
7. inventory.ini 문법이 맞는지 확인
8. site.yml 들여쓰기가 맞는지 확인
~~~

---

## 11. 최종 기준

이 체크리스트의 목적은 단순 실행이 아니라, 자동화 실행 전 장애 원인을 줄이는 것이다.

즉, Ansible Playbook 실행 전에 서버, 네트워크, SSH, sudo, Python, Inventory 상태를 먼저 검증한다.



