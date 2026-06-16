<!-- STATUS: COMPLETE -->

# Pre-Run Checklist

## 1. 문서 목적

본 문서는 Team Dandelion 프로젝트 실행 전 필수 점검 항목을 정의한다.

본 프로젝트는 Phase 기반 구현 로드맵을 사용한다.

~~~text
Phase 1: 필수 구성 및 기본 검증 단계
Phase 2: 운영 확장 및 검증 고도화 단계
Phase 3: 도전 확장 단계
Out of Scope: 제외 범위
~~~

본 체크리스트는 Phase 1 필수 구성 실행 전에 반드시 확인해야 하는 항목을 기준으로 작성한다.

---

## 2. Phase 1 실행 전 전체 점검 흐름

~~~text
OpenStack 리소스 확인
→ Ubuntu 인스턴스 확인
→ Control / Proxy / Web / DB / Backup Node 확인
→ 네트워크 / 라우터 / 서브넷 확인
→ 보안그룹 확인
→ SSH 접속 확인
→ Ansible inventory 확인
→ Ansible ping 확인
→ Docker 설치 준비
→ DB Node MariaDB 준비
→ Web Node WordPress 준비
→ Proxy Node HAProxy 준비
→ Health Check / Backup / Restore 준비
→ 캡처 및 문서 저장 경로 확인
~~~

---

## 3. OpenStack 사전 점검

| 체크 | 항목 | 확인 기준 |
|---|---|---|
| [ ] | OpenStack Dashboard 접속 | Horizon 접속 가능 |
| [ ] | 프로젝트 선택 | 올바른 프로젝트 선택 |
| [ ] | Ubuntu 이미지 확인 | Ubuntu 이미지 사용 가능 |
| [ ] | Flavor 확인 | 인스턴스 생성 가능한 Flavor 존재 |
| [ ] | Key Pair 확인 | SSH 접속용 Key Pair 존재 |
| [ ] | Network 확인 | Private Network 존재 |
| [ ] | Subnet 확인 | Private Subnet 존재 |
| [ ] | Router 확인 | External Network와 연결 가능 |
| [ ] | Security Group 확인 | SSH / HTTP / DB 포트 정책 구성 가능 |
| [ ] | Floating IP 또는 접속 경로 확인 | 외부 접속 방식 확보 |

확인 명령어 예시:

~~~bash
openstack image list
openstack flavor list
openstack keypair list
openstack network list
openstack subnet list
openstack router list
openstack security group list
~~~

---

## 4. 인스턴스 점검

Phase 1에서는 다음 노드가 필요하다.

| 체크 | Node | 역할 | 상태 기준 |
|---|---|---|---|
| [ ] | Control Node | Ansible 실행 | ACTIVE |
| [ ] | Proxy Node | HAProxy HTTP Reverse Proxy | ACTIVE |
| [ ] | Web Node | Custom WordPress | ACTIVE |
| [ ] | DB Node | MariaDB | ACTIVE |
| [ ] | Backup / Validation Node | Health Check / Backup / Restore | ACTIVE |

확인 명령어:

~~~bash
openstack server list
~~~

각 노드의 Private IP를 정리한다.

| Node | Private IP | Floating IP / Forwarding | 비고 |
|---|---|---|---|
| Control Node |  |  |  |
| Proxy Node |  |  |  |
| Web Node |  |  |  |
| DB Node |  |  |  |
| Backup / Validation Node |  |  |  |

---

## 5. 네트워크 점검

| 체크 | 항목 | 확인 기준 |
|---|---|---|
| [ ] | Control Node → Proxy Node 통신 | SSH 가능 |
| [ ] | Control Node → Web Node 통신 | SSH 가능 |
| [ ] | Control Node → DB Node 통신 | SSH 가능 |
| [ ] | Control Node → Backup Node 통신 | SSH 가능 |
| [ ] | Client → Proxy Node | HTTP 80 접근 가능 |
| [ ] | Proxy Node → Web Node | HTTP 80 접근 가능 |
| [ ] | Web Node → DB Node | TCP 3306 접근 가능 |
| [ ] | Backup Node → Web Node | HTTP 80 접근 가능 |
| [ ] | Backup Node → DB Node | TCP 3306 접근 가능 |

---

## 6. 보안그룹 점검

## 6.1 Phase 1 필수 포트

| 체크 | Source | Destination | Port | Purpose |
|---|---|---|---:|---|
| [ ] | Admin / Control Node | All Managed Nodes | 22 | SSH / Ansible |
| [ ] | Client / Allowed Range | Proxy Node | 80 | WordPress HTTP access |
| [ ] | Proxy Node | Web Node | 80 | HAProxy backend |
| [ ] | Web Node | DB Node | 3306 | WordPress DB connection |
| [ ] | Backup / Validation Node | Web Node | 80 | Health check / file backup |
| [ ] | Backup / Validation Node | DB Node | 3306 | MariaDB dump |
| [ ] | Backup / Validation Node | Proxy Node | 80 | Proxy health check |

DB Node의 3306 포트는 전체 공개하지 않는다.

---

## 6.2 Phase 2 추가 포트

Phase 2를 진행할 경우에만 추가한다.

| 체크 | Source | Destination | Port | Purpose |
|---|---|---|---:|---|
| [ ] | Client / Allowed Range | Proxy Node | 443 | HTTPS access |
| [ ] | Monitoring Node | Target Nodes | 9100 | node_exporter |
| [ ] | Monitoring Node | Target Nodes | 8080 | cAdvisor |
| [ ] | Admin / Allowed Range | Monitoring Node | 9090 | Prometheus |
| [ ] | Admin / Allowed Range | Monitoring Node | 3000 | Grafana |

---

## 7. SSH 접속 점검

Control Node에서 각 노드로 SSH 접속이 가능해야 한다.

~~~bash
ssh ubuntu@PROXY_NODE_IP
ssh ubuntu@WEB_NODE_IP
ssh ubuntu@DB_NODE_IP
ssh ubuntu@BACKUP_NODE_IP
~~~

| 체크 | 대상 | 성공 기준 |
|---|---|---|
| [ ] | Proxy Node | SSH 접속 성공 |
| [ ] | Web Node | SSH 접속 성공 |
| [ ] | DB Node | SSH 접속 성공 |
| [ ] | Backup / Validation Node | SSH 접속 성공 |

SSH 실패 시 확인한다.

~~~text
Key Pair
Security Group
Private IP
Floating IP 또는 포트포워딩
사용자명 ubuntu
권한 chmod 400
~~~

---

## 8. Ansible 실행 전 점검

Control Node에서 확인한다.

| 체크 | 항목 | 명령어 | 성공 기준 |
|---|---|---|---|
| [ ] | Ansible 설치 | ansible --version | 버전 출력 |
| [ ] | 설정 파일 | cat ansible.cfg | inventory 경로 확인 |
| [ ] | Inventory 파일 | cat inventory.ini | proxy / web / db / backup 그룹 확인 |
| [ ] | Inventory 파싱 | ansible-inventory --list | 노드 목록 출력 |
| [ ] | Ping 테스트 | ansible all -m ping | 모든 노드 SUCCESS |
| [ ] | Playbook 문법 | ansible-playbook site.yml --syntax-check | Syntax check 통과 |

실행 예시:

~~~bash
cd ansible
ansible --version
ansible-inventory --list
ansible all -m ping
ansible-playbook site.yml --syntax-check
~~~

---

## 9. Docker 실행 전 점검

Proxy Node, Web Node, DB Node에서 Docker가 정상 동작해야 한다.

| 체크 | 항목 | 명령어 | 성공 기준 |
|---|---|---|---|
| [ ] | Docker 설치 | docker --version | 버전 출력 |
| [ ] | Docker Compose | docker compose version | 버전 출력 |
| [ ] | Docker 서비스 | systemctl status docker | active |
| [ ] | Docker 권한 | docker ps | permission error 없음 |
| [ ] | Disk 여유 | df -h | 충분한 여유 공간 |
| [ ] | Memory 여유 | free -h | 최소 실행 가능 |

---

## 10. DB Node 실행 전 점검

DB Node는 MariaDB 서비스를 실행한다.

| 체크 | 항목 | 확인 기준 |
|---|---|---|
| [ ] | MariaDB service configuration 파일 준비 | DB Node MariaDB package configuration/docker-compose.yml 존재 |
| [ ] | MariaDB 이미지 기준 | mariadb-server package |
| [ ] | DB 이름 확인 | wordpress |
| [ ] | DB 사용자 확인 | wordpress |
| [ ] | DB 비밀번호 확인 | 공개 문서에 실제 비밀번호 노출 금지 |
| [ ] | 3306 포트 정책 | Web Node / Backup Node만 접근 가능 |
| [ ] | DB volume 기준 | Docker volume 또는 로컬 volume 사용 |

DB Node 실행 후 확인 명령어:

~~~bash
docker ps
sudo ss -tulnp | grep ':3306'
docker logs mariadb --tail 50
~~~

---

## 11. Web Node 실행 전 점검

Web Node는 Custom WordPress 컨테이너를 실행한다.

| 체크 | 항목 | 확인 기준 |
|---|---|---|
| [ ] | Dockerfile 준비 | docker/wordpress/Dockerfile 존재 |
| [ ] | Base Image | wordpress:php8.2-apache |
| [ ] | custom.ini 준비 | docker/wordpress/custom.ini 존재 |
| [ ] | Web compose 파일 준비 | docker/compose/web/docker-compose.yml 존재 |
| [ ] | DB Host 설정 | DB_NODE_PRIVATE_IP:3306 |
| [ ] | DB User 설정 | MariaDB 사용자와 일치 |
| [ ] | DB Password 설정 | MariaDB 비밀번호와 일치 |
| [ ] | 80 포트 사용 | WordPress HTTP 응답 가능 |

Web Node 실행 후 확인 명령어:

~~~bash
docker ps
sudo ss -tulnp | grep ':80'
curl -I http://localhost
~~~

---

## 12. Proxy Node 실행 전 점검

Proxy Node는 HAProxy HTTP Reverse Proxy를 실행한다.

| 체크 | 항목 | 확인 기준 |
|---|---|---|
| [ ] | HAProxy compose 파일 준비 | docker/proxy/docker-compose.yml 존재 |
| [ ] | haproxy.cfg 준비 | docker/proxy/haproxy.cfg 존재 |
| [ ] | Backend IP 설정 | Web Node Private IP 반영 |
| [ ] | Listen Port | 80 |
| [ ] | Backend Port | Web Node 80 |
| [ ] | 보안그룹 | Client / Allowed Range에서 80 접근 가능 |

Proxy Node 실행 후 확인 명령어:

~~~bash
docker ps
sudo ss -tulnp | grep ':80'
curl -I http://PROXY_NODE_IP
docker logs dandelion-haproxy --tail 50
~~~

---

## 13. Backup / Validation 실행 전 점검

Backup / Validation Node는 health_check.sh, backup.sh, restore.md 검증을 담당한다.

| 체크 | 항목 | 확인 기준 |
|---|---|---|
| [ ] | health_check.sh 준비 | scripts/health_check.sh 존재 |
| [ ] | backup.sh 준비 | scripts/backup.sh 존재 |
| [ ] | restore.md 준비 | restore.md 또는 docs/restore.md 존재 |
| [ ] | Proxy Node 접근 | HTTP 80 접근 가능 |
| [ ] | Web Node 접근 | HTTP 80 접근 가능 |
| [ ] | DB Node 접근 | TCP 3306 접근 가능 |
| [ ] | 백업 저장 경로 | backup/ 또는 /backup 경로 준비 |
| [ ] | 실행 권한 | chmod +x 적용 필요 여부 확인 |

실행 예시:

~~~bash
bash scripts/health_check.sh
bash scripts/backup.sh
~~~

---

## 14. Phase 1 실행 직전 최종 체크

| 체크 | 항목 |
|---|---|
| [ ] | 모든 노드 ACTIVE 상태 확인 |
| [ ] | 모든 노드 Private IP 정리 |
| [ ] | 보안그룹 포트 정책 정리 |
| [ ] | Control Node에서 SSH 접속 확인 |
| [ ] | ansible all -m ping 성공 |
| [ ] | site.yml syntax check 통과 |
| [ ] | DB Node MariaMariaDB service configuration 준비 |
| [ ] | Web Node WordPress compose 준비 |
| [ ] | Proxy Node HAProxy compose 준비 |
| [ ] | health_check.sh 준비 |
| [ ] | backup.sh 준비 |
| [ ] | restore.md 준비 |
| [ ] | 캡처 저장 폴더 준비 |
| [ ] | GitHub 최신 상태 확인 |
| [ ] | 팀원별 담당 캡처 기준 공유 |

---

## 15. Phase 2 실행 전 조건

Phase 2는 아래 조건을 만족한 뒤 진행한다.

| 체크 | 조건 |
|---|---|
| [ ] | Phase 1 필수 구성 완료 |
| [ ] | Proxy Node 경유 WordPress HTTP 접속 성공 |
| [ ] | Web Node → DB Node MariaDB 연결 확인 |
| [ ] | health_check.sh 실행 성공 |
| [ ] | backup.sh 실행 성공 |
| [ ] | restore.md 검증 완료 |
| [ ] | 필수 캡처 확보 |
| [ ] | Phase 1 기준 발표 가능 상태 확보 |

Phase 2 대상:

~~~text
HTTPS
Cinder Backup Volume
node_exporter
cAdvisor
Prometheus
Grafana
backup / restore playbook화
Ansible roles 구조 분리
~~~

---

## 16. Phase 3 실행 전 조건

Phase 3은 아래 조건을 만족한 뒤 진행한다.

| 체크 | 조건 |
|---|---|
| [ ] | Phase 1 완료 |
| [ ] | Phase 2 주요 항목 완료 또는 발표 가능한 수준 확보 |
| [ ] | Web Node 2 생성 가능한 리소스 확보 |
| [ ] | HAProxy backend 2개 등록 가능 |
| [ ] | 공통 DB Node 연결 구조 확인 |
| [ ] | 실패 시 Phase 1 / Phase 2 기준 발표 가능 |

Phase 3에서는 다음 항목을 제외한다.

~~~text
WordPress files 자동 동기화
DB Replication
DB Clustering
OpenStack LBaaS / Octavia
Auto Scaling
~~~

---

## 17. 캡처 폴더 확인

실행 전 아래 폴더를 준비한다.

~~~text
screenshots/
├── cloud-infra/
├── ansible/
├── server/
├── proxy/
├── web/
├── db/
├── validation/
├── backup/
├── restore/
├── troubleshooting/
├── monitoring/
└── phase3/
~~~

---

## 18. 실행 중단 기준

다음 문제가 발생하면 Phase 2 또는 Phase 3으로 확장하지 않고 Phase 1 안정화에 집중한다.

| 문제 | 조치 |
|---|---|
| 인스턴스 생성 실패 | 리소스 / flavor / quota 확인 |
| SSH 접속 불가 | Key / Security Group / IP 확인 |
| Ansible ping 실패 | inventory / SSH / user 확인 |
| Docker 설치 실패 | apt / network / disk 확인 |
| MariaDB 실행 실패 | compose / volume / env 확인 |
| WordPress DB 연결 실패 | DB IP / security group / env 확인 |
| HAProxy 접속 실패 | haproxy.cfg / backend IP 확인 |
| backup.sh 실패 | 권한 / 디스크 / DB 접속 확인 |
| restore 절차 미검증 | restore.md 보완 후 재확인 |

---

## 19. 핵심 실행 전 메시지

~~~text
Phase 1 실행 전에는 OpenStack 리소스, SSH, Ansible, Docker, Proxy/Web/DB/Backup 통신 구조를 먼저 확인한다.

Phase 1이 안정화되기 전에는 HTTPS, Cinder, Prometheus/Grafana, Web Node 2대 확장으로 넘어가지 않는다.

최종 발표는 Phase 1 필수 구성과 검증 결과만으로도 성립해야 한다.
~~~



