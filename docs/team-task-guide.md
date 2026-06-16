<!-- STATUS: COMPLETE -->

# Team Task Guide

## 1. 문서 목적

본 문서는 Team Dandelion 프로젝트의 팀원별 작업 기준과 산출물 기준을 정의한다.

본 프로젝트는 Phase 기반 구현 로드맵을 사용한다.

~~~text
Phase 1: 필수 구성 및 기본 검증 단계
Phase 2: 운영 확장 및 검증 고도화 단계
Phase 3: 도전 확장 단계
Out of Scope: 제외 범위
~~~

Phase 1에서는 Control Node, Proxy Node, Web Node, DB Node, Backup / Validation Node를 분리한 기본 운영 구조를 완성한다.

---

## 2. 전체 역할 분담

| 이름 | 역할 | 주요 담당 |
|---|---|---|
| 정주헌 | PM / Architecture | 전체 구조 설계, GitHub 관리, 문서 통합, 발표 흐름, 제출자료 관리 |
| 백서빈 | Cloud Infrastructure | OpenStack 인스턴스, 네트워크, 보안그룹, Floating IP 또는 포트포워딩 |
| 이진욱 | Server / Virtualization | Docker 설치, Custom WordPress, MariaDB, HAProxy 컨테이너 구성 지원 |
| 조민석 | Ansible Automation | ansible.cfg, inventory.ini, site.yml 작성 및 실행 |
| 박재우 | Monitoring / Backup / Validation | health_check.sh, backup.sh, restore.md, 검증 결과 정리 |

---

## 3. Phase 1 필수 구성 목표

Phase 1의 목표는 다음 구조를 반드시 완성하는 것이다.

~~~text
Client
→ Proxy Node
   └── HAProxy HTTP Reverse Proxy

→ Web Node
   └── Custom WordPress Container

→ DB Node
   └── MariaDB Service

→ Backup / Validation Node
   ├── health_check.sh
   ├── backup.sh
   ├── mysqldump 기반 mysqldump 기반 MariaDB dump
   ├── WordPress files archive
   └── restore.md 검증

Control Node
→ Ansible 실행
→ Proxy / Web / DB / Backup Node 관리
~~~

---

## 4. 공통 작업 규칙

## 4.1 Git 작업 규칙

작업 전 항상 최신 상태를 받는다.

~~~bash
git pull --rebase origin main
~~~

작업 후 상태를 확인한다.

~~~bash
git status
~~~

커밋 시에는 본인이 수정한 파일만 추가한다.

~~~bash
git add docs/example.md
git commit -m "Update example document"
git pull --rebase origin main
git push origin main
~~~

다음 명령은 사용하지 않는다.

~~~bash
git add .
~~~

---

## 4.2 파일명 규칙

| 구분 | 기준 |
|---|---|
| 문서 | 소문자와 하이픈 사용 |
| 캡처 | 기능과 결과가 드러나는 이름 사용 |
| 스크립트 | 역할이 드러나는 이름 사용 |
| 디렉터리 | 담당 영역별로 분리 |

예시:

~~~text
screenshots/cloud-infra/instance-list.png
screenshots/ansible/ansible-ping.png
screenshots/proxy/proxy-http-result.png
screenshots/web/wordpress-container.png
screenshots/db/mariadb-container.png
screenshots/backup/backup-files-list.png
~~~

---

## 5. 정주헌: PM / Architecture

## 5.1 담당 범위

| 구분 | 작업 |
|---|---|
| 구조 설계 | Phase 기반 구현 범위 정의 |
| 문서 통합 | README, architecture, roadmap, scope control 관리 |
| GitHub 관리 | Repository 구조, 상태 자동 갱신, 문서 검수 |
| 제출 관리 | Google Drive 제출자료 구조 관리 |
| 발표 흐름 | 인프라 → 자동화 → 서비스 → 검증 → 복구 흐름 정리 |

---

## 5.2 필수 산출물

~~~text
README.md
docs/architecture.md
docs/scope-control.md
docs/implementation-roadmap.md
docs/mentoring-brief.md
docs/mentoring-questions.md
docs/final-deliverables.md
docs/review-checklist.md
presentation/presentation-outline.md
~~~

---

## 5.3 확인 기준

| 확인 항목 | 기준 |
|---|---|
| Phase 용어 | Phase 1 / Phase 2 / Phase 3로 통일 |
| 금지 용어 | A급 / B급 / B+ / C급 잔존 여부 확인 |
| 서비스 기준 | WordPress / MariaDB / HAProxy 기준 유지 |
| 제외 항목 | Kubernetes, Docker Swarm, LBaaS 등 제외 유지 |
| 제출자료 | GitHub 문서와 Google Drive 산출물 연결 |

---

## 6. 백서빈: Cloud Infrastructure

## 6.1 담당 범위

| 구분 | 작업 |
|---|---|
| OpenStack | Ubuntu 이미지 기반 인스턴스 생성 |
| Node 구성 | Control / Proxy / Web / DB / Backup Node 구성 |
| Network | 네트워크, 라우터, 서브넷 구성 |
| Security Group | SSH, HTTP, DB 포트 정책 구성 |
| External Access | Floating IP 또는 포트포워딩 기반 접속 구성 |
| Evidence | 인프라 구성 캡처 정리 |

---

## 6.2 Phase 1 필수 작업

~~~text
1. Ubuntu 이미지 확인
2. Control Node 생성
3. Proxy Node 생성
4. Web Node 생성
5. DB Node 생성
6. Backup / Validation Node 생성
7. 네트워크 / 라우터 / 서브넷 구성
8. 보안그룹 구성
9. SSH 접속 확인
10. Proxy Node 외부 HTTP 접속 경로 확인
~~~

---

## 6.3 보안그룹 기준

| Source | Destination | Port | Purpose |
|---|---|---:|---|
| Admin / Control Node | All Managed Nodes | 22 | SSH / Ansible |
| Client / Allowed Range | Proxy Node | 80 | WordPress HTTP access |
| Proxy Node | Web Node | 80 | HAProxy backend |
| Web Node | DB Node | 3306 | WordPress DB connection |
| Backup / Validation Node | Web Node | 80 | Health check / file backup |
| Backup / Validation Node | DB Node | 3306 | mysqldump 기반 mysqldump 기반 MariaDB dump |

DB Node의 3306 포트는 전체 공개하지 않는다.

---

## 6.4 필수 캡처

~~~text
screenshots/cloud-infra/ubuntu-image-list.png
screenshots/cloud-infra/instance-list.png
screenshots/cloud-infra/control-node-active.png
screenshots/cloud-infra/proxy-node-active.png
screenshots/cloud-infra/web-node-active.png
screenshots/cloud-infra/db-node-active.png
screenshots/cloud-infra/backup-node-active.png
screenshots/cloud-infra/network-subnet-router.png
screenshots/cloud-infra/security-group-rules.png
screenshots/cloud-infra/floating-ip-or-port-forwarding.png
screenshots/cloud-infra/ssh-test.png
~~~

---

## 7. 이진욱: Server / Virtualization

## 7.1 담당 범위

| 구분 | 작업 |
|---|---|
| 공통 서버 | Ubuntu 기본 확인, Docker 설치 확인 |
| Proxy Node | HAProxy 컨테이너 실행 지원 |
| Web Node | Custom WordPress Image Build 및 컨테이너 실행 |
| DB Node | MariaDB 서비스 실행 |
| Compose | 역할별 Docker Compose 파일 구성 |
| Evidence | docker ps, 포트, 로그 캡처 정리 |

---

## 7.2 Phase 1 필수 작업

~~~text
1. Proxy / Web / DB Node OS 정보 확인
2. Docker 설치 확인
3. Docker Compose 사용 가능 여부 확인
4. DB Node에서 MariaDB 서비스 실행
5. Web Node에서 Custom WordPress 컨테이너 실행
6. Web Node WordPress가 DB Node MariaDB에 연결되는지 확인
7. Proxy Node에서 HAProxy HTTP Reverse Proxy 실행
8. Proxy Node 경유 WordPress HTTP 접속 확인
~~~

---

## 7.3 권장 Docker 구성

~~~text
docker/
├── wordpress/
│   ├── Dockerfile
│   ├── custom.ini
│   └── README.md
├── compose/
│   ├── web/
│   │   └── docker-compose.yml
│   └── db/
│       └── docker-compose.yml
└── proxy/
    ├── docker-compose.yml
    └── haproxy.cfg
~~~

---

## 7.4 필수 캡처

~~~text
screenshots/server/os-info.png
screenshots/server/docker-version.png
screenshots/server/docker-compose-version.png
screenshots/db/mariadb-container.png
screenshots/web/custom-wordpress-build.png
screenshots/web/wordpress-container.png
screenshots/proxy/haproxy-container.png
screenshots/proxy/proxy-http-result.png
screenshots/server/listening-ports.png
~~~

---

## 8. 조민석: Ansible Automation

## 8.1 담당 범위

| 구분 | 작업 |
|---|---|
| ansible.cfg | Ansible 기본 설정 |
| inventory.ini | Proxy / Web / DB / Backup Node 등록 |
| site.yml | Docker 설치 및 역할별 서비스 배포 |
| 검증 | ansible ping, syntax check, playbook 실행 |
| Evidence | Ansible 실행 결과 캡처 |

---

## 8.2 Phase 1 필수 작업

~~~text
1. ansible.cfg 작성
2. inventory.ini 작성
3. proxy / web / db / backup 그룹 구성
4. ansible all -m ping 실행
5. site.yml 작성
6. Docker 설치 자동화
7. DB Node MariaDB 설치 및 구성 자동화
8. Web Node WordPress 배포 자동화
9. Proxy Node HAProxy 배포 자동화
10. playbook 실행 결과 정리
~~~

---

## 8.3 inventory.ini 기준

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

[all:vars]
ansible_user=ubuntu
ansible_ssh_private_key_file=~/.ssh/dandelion-key.pem
~~~

---

## 8.4 필수 캡처

~~~text
screenshots/ansible/ansible-version.png
screenshots/ansible/inventory-list.png
screenshots/ansible/ansible-ping.png
screenshots/ansible/site-yml-syntax-check.png
screenshots/ansible/site-yml-run-result.png
screenshots/ansible/proxy-deploy-result.png
screenshots/ansible/wordpress-deploy-result.png
screenshots/ansible/mariadb-deploy-result.png
~~~

---

## 9. 박재우: Monitoring / Backup / Validation

## 9.1 담당 범위

| 구분 | 작업 |
|---|---|
| Health Check | Proxy / Web / DB 상태 점검 |
| Backup | mysqldump 기반 mysqldump 기반 MariaDB dump, WordPress files archive |
| Restore | restore.md 기반 복구 절차 검증 |
| Troubleshooting | 장애 상황 1개와 복구 절차 정리 |
| Phase 2 Monitoring | node_exporter, cAdvisor, Prometheus, Grafana |
| Evidence | 검증 결과 캡처 정리 |

---

## 9.2 Phase 1 필수 작업

~~~text
1. health_check.sh 실행
2. Proxy Node HTTP 응답 확인
3. Web Node HTTP 응답 확인
4. DB Node 3306 연결 확인
5. backup.sh 실행
6. DB Node mysqldump 기반 mysqldump 기반 MariaDB dump 생성
7. Web Node WordPress files archive 생성
8. restore.md 기반 복구 절차 검증
9. 장애 상황 1개와 복구 절차 정리
~~~

---

## 9.3 health_check.sh 확인 대상

| 구분 | 확인 대상 |
|---|---|
| Proxy | Proxy Node HTTP 응답 |
| Web | Web Node HTTP 응답 |
| DB | DB Node 3306 연결 |
| Docker | HAProxy / WordPress / MariaDB 서비스 상태 |
| Resource | CPU / Memory / Disk |
| Port | 서비스 포트 listening 상태 |

---

## 9.4 backup.sh 결과물

| Backup Target | Output |
|---|---|
| DB Node MariaDB | wordpress_db.sql |
| Web Node WordPress files | wordpress_files.tar.gz |

---

## 9.5 필수 캡처

~~~text
screenshots/validation/health-check-result.png
screenshots/backup/backup-command-result.png
screenshots/backup/db-dump-created.png
screenshots/backup/wordpress-files-archive.png
screenshots/restore/restore-document.png
screenshots/troubleshooting/incident-and-recovery.png
~~~

---

## 10. Phase 2 작업 기준

Phase 2는 Phase 1 완료 후 가능한 범위에서 진행한다.

| 항목 | 담당 후보 | 설명 |
|---|---|---|
| HTTPS self-signed | Server / Ansible | Proxy Node HAProxy HTTPS |
| Cinder Backup Volume | Cloud / Backup | Backup Node에 Cinder attach |
| node_exporter | Monitoring | OS Metrics |
| cAdvisor | Monitoring | Container Metrics |
| Prometheus | Monitoring | Metrics 수집 |
| Grafana | Monitoring | Dashboard |
| backup playbook | Ansible / Backup | backup.sh playbook화 |
| roles 구조 | Ansible | site.yml 역할 분리 |
| 상세 검증 리포트 | PM / Validation | 검증 근거 고도화 |

---

## 11. Phase 3 작업 기준

Phase 3는 도전 확장 단계이다.

| 항목 | 담당 후보 | 설명 |
|---|---|---|
| Web Node 2 생성 | Cloud Infrastructure | 추가 Web Node 생성 |
| Web Node 2 WordPress 배포 | Server / Ansible | 기존 Web Node와 동일하게 배포 |
| HAProxy backend 2개 등록 | Server / Ansible | web1 / web2 backend 구성 |
| Round Robin 검증 | Validation | Web-1 / Web-2 응답 분산 |
| 공통 DB 검증 | Server / Validation | 두 Web Node가 동일 DB Node 연결 |
| 장애 테스트 | Validation | Web-1 중지 시 Web-2 응답 |

Phase 3에서는 WordPress files 자동 동기화, DB Replication, OpenStack LBaaS / Octavia를 제외한다.

---

## 12. 팀원별 제출 기준

각 팀원은 본인 담당 영역에 대해 다음 자료를 제출한다.

| 제출 항목 | 기준 |
|---|---|
| 작업 내용 | 본인이 수행한 작업 요약 |
| 명령어 | 핵심 실행 명령어 |
| 결과 캡처 | 성공 결과 캡처 |
| 문제 상황 | 발생한 오류 또는 이슈 |
| 해결 과정 | 해결 방법 또는 우회 방법 |
| 남은 이슈 | 최종 미해결 사항이 있으면 기록 |

---

## 13. 최종 검수 기준

| 검수 항목 | 기준 |
|---|---|
| Phase 용어 | Phase 1 / Phase 2 / Phase 3로 통일 |
| 금지 용어 | A급 / B급 / B+ / C급 사용 금지 |
| 서비스 기준 | WordPress / MariaDB / HAProxy 기준 유지 |
| 노드 기준 | Proxy / Web / DB / Backup Node 분리 유지 |
| 문서 기준 | 문서마다 목적, 범위, 검증 기준 포함 |
| 캡처 기준 | 파일명과 담당 영역이 명확해야 함 |
| 제외 기준 | Kubernetes, Docker Swarm, LBaaS, DB Replication 제외 유지 |

---

## 14. 핵심 팀 운영 메시지

~~~text
본 프로젝트는 팀원별 작업을 단순히 나누는 것이 아니라,
Proxy / Web / DB / Backup 계층을 분리한 클라우드 운영 구조를 함께 완성하는 프로젝트이다.

각 팀원은 본인 담당 영역의 구현 결과를 명령어, 캡처, 문서, 트러블슈팅 로그로 남겨야 한다.

Phase 1 필수 구성이 완료된 이후에만 Phase 2 운영 확장과 Phase 3 도전 확장을 진행한다.
~~~


