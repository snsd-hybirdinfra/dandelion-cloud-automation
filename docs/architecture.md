<!-- STATUS: COMPLETE -->

# System Architecture

## 1. 문서 목적

본 문서는 Team Dandelion 프로젝트의 전체 시스템 아키텍처를 정의한다.

본 프로젝트는 OpenStack 기반 Ubuntu 인스턴스 위에서 Ansible을 활용하여 Proxy, Web, DB, Backup / Validation 계층을 분리하고, Docker Compose 기반 WordPress와 DB Node MariaDB 서비스 서비스 배포, HAProxy Reverse Proxy, 상태 점검, 백업 및 복구 검증을 수행하는 구조를 가진다.

본 문서는 Phase 1 필수 구성 구조를 기준으로 작성하며, Phase 2 운영 확장과 Phase 3 도전 확장 구조도 함께 설명한다.

---

## 2. Phase 기반 아키텍처 전략

본 프로젝트는 기존 A급 / B급 / B+ 표현 대신 Phase 기반 구현 전략을 사용한다.

~~~text
Phase 1: 필수 구성 및 기본 검증 단계
Phase 2: 운영 확장 및 검증 고도화 단계
Phase 3: 도전 확장 단계
Out of Scope: 제외 범위
~~~

Phase 1에서는 최종 발표와 시연을 위해 반드시 필요한 기본 운영 구조를 구성한다.

Phase 2에서는 Phase 1 위에 HTTPS, Cinder Backup Volume, Prometheus/Grafana, 자동화 개선을 추가한다.

Phase 3에서는 Web Node를 2대로 확장하고 HAProxy Load Balancing을 통해 확장성을 검증한다.

---

## 3. Phase 1 기본 아키텍처

## 3.1 전체 구조

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
   ├── mysqldump 기반 MariaDB dump
   ├── WordPress files archive
   └── restore.md 검증

Control Node
→ Ansible 실행
→ Proxy / Web / DB / Backup Node 관리
~~~

---

## 3.2 노드별 역할

| Node | Role | Main Components |
|---|---|---|
| Control Node | Ansible 실행 및 전체 자동화 제어 | ansible.cfg, inventory.ini, site.yml |
| Proxy Node | 외부 HTTP 접속 진입점 | HAProxy HTTP Reverse Proxy |
| Web Node | WordPress 서비스 실행 | Custom WordPress Container |
| DB Node | WordPress 데이터 저장 | MariaDB Service |
| Backup / Validation Node | 상태 점검, 백업, 복구 검증 | health_check.sh, backup.sh, restore.md |

---

## 3.3 계층별 책임

| Layer | Responsibility |
|---|---|
| Infrastructure Layer | OpenStack 인스턴스, 네트워크, 라우터, 서브넷, 보안그룹 구성 |
| Access Layer | Floating IP 또는 포트포워딩 기반 외부 접속 제공 |
| Automation Layer | Ansible 기반 서버 설정 및 서비스 배포 |
| Proxy Layer | HAProxy HTTP Reverse Proxy를 통한 Web Node 접속 중계 |
| Web Layer | Custom WordPress Container 실행 |
| Database Layer | MariaDB Service를 DB Node에서 분리 실행 |
| Validation Layer | 상태 점검, 백업, 복구 절차 검증 |
| Management Layer | GitHub, Google Drive, 문서, 캡처, 제출자료 관리 |

---

## 4. Phase 1 통신 흐름

## 4.1 사용자 접속 흐름

~~~text
User / Browser
→ Proxy Node:80
→ HAProxy
→ Web Node:80
→ WordPress Container
→ DB Node:3306
→ MariaDB Service
~~~

사용자는 Web Node에 직접 접근하지 않고 Proxy Node를 통해 WordPress에 접근한다.

Phase 1에서 HAProxy는 HTTP Reverse Proxy 역할까지만 수행한다.  
HTTPS와 HTTP to HTTPS Redirect는 Phase 2에서 처리한다.

---

## 4.2 Ansible 자동화 흐름

~~~text
Control Node
→ SSH
→ Proxy Node
→ Web Node
→ DB Node
→ Backup / Validation Node
~~~

Control Node는 Ansible을 실행하여 각 대상 노드에 Docker를 설치하고, 역할별 컨테이너를 배포한다.

| 대상 노드 | 자동화 대상 |
|---|---|
| Proxy Node | Docker 설치, HAProxy 컨테이너 배포 |
| Web Node | Docker 설치, Custom WordPress 컨테이너 배포 |
| DB Node | Docker 설치, MariaDB 서비스 배포 |
| Backup / Validation Node | health_check.sh, backup.sh, restore 절차 검증 지원 |

---

## 4.3 백업 및 복구 흐름

~~~text
Backup / Validation Node
→ DB Node mysqldump 기반 MariaDB dump
→ Web Node WordPress files archive
→ Backup files 저장
→ restore.md 기반 복구 절차 검증
~~~

백업 대상은 다음과 같다.

| Backup Target | Description |
|---|---|
| mysqldump 기반 MariaDB dump | DB Node의 WordPress database dump |
| WordPress files archive | Web Node의 WordPress files archive |
| Restore procedure | restore.md 기반 복구 절차 검증 |

Phase 1에서는 로컬 또는 지정 경로에 백업 결과를 저장한다.

Phase 2에서는 Cinder Volume을 Backup / Validation Node에 attach하여 `/backup` 경로로 마운트하고, 백업 결과를 Cinder Volume에 저장하는 방식으로 확장한다.

---

## 5. Phase 1 서비스 구성

## 5.1 Proxy Node

Proxy Node는 외부 접속을 받는 진입점이다.

| Item | Value |
|---|---|
| Service | HAProxy |
| Role | HTTP Reverse Proxy |
| Listen Port | 80 |
| Backend | Web Node:80 |
| Phase 1 Scope | HTTP Reverse Proxy only |
| Phase 2 Scope | HTTPS, Redirect |

Phase 1에서는 다음 흐름을 검증한다.

~~~text
Client
→ Proxy Node:80
→ HAProxy
→ Web Node:80
~~~

---

## 5.2 Web Node

Web Node는 WordPress 서비스를 실행한다.

| Item | Value |
|---|---|
| Service | Custom WordPress |
| Base Image | wordpress:php8.2-apache |
| Runtime | Docker / Docker Compose |
| External Access | Proxy Node 경유 |
| DB Connection | DB Node MariaDB |

Web Node는 DB를 직접 포함하지 않고 DB Node의 MariaDB에 연결한다.

---

## 5.3 DB Node

DB Node는 MariaDB를 단독으로 실행한다.

| Item | Value |
|---|---|
| Service | MariaDB |
| Image | mariadb:10.11 |
| Runtime | Docker / Docker Compose |
| Access Source | Web Node |
| Data Role | WordPress database |

DB Node는 Web Node와 분리하여 서비스 계층과 데이터 계층을 구분한다.

---

## 5.4 Backup / Validation Node

Backup / Validation Node는 상태 점검, 백업, 복구 검증을 담당한다.

| Item | Value |
|---|---|
| Health Check | health_check.sh |
| Backup | backup.sh |
| DB Backup | mysqldump 기반 MariaDB dump |
| File Backup | WordPress files archive |
| Restore | restore.md 기반 절차 검증 |

---

## 6. 네트워크 및 보안 구조

## 6.1 기본 포트 정책

| Source | Destination | Port | Purpose |
|---|---|---:|---|
| Admin / Control | All Managed Nodes | 22 | SSH / Ansible |
| Client | Proxy Node | 80 | WordPress HTTP access |
| Proxy Node | Web Node | 80 | HAProxy backend |
| Web Node | DB Node | 3306 | WordPress database connection |
| Backup / Validation Node | Web Node | 80 | Health check / file backup |
| Backup / Validation Node | DB Node | 3306 | mysqldump 기반 MariaDB dump |
| Admin / Control | Monitoring Node | 9090 / 3000 | Phase 2 monitoring access |

---

## 6.2 보안그룹 기준

| Security Group | Allowed Inbound |
|---|---|
| sg-control | SSH management access |
| sg-proxy | HTTP 80 from client or allowed range |
| sg-web | HTTP 80 from Proxy Node, SSH from Control Node |
| sg-db | MariaDB 3306 from Web Node and Backup / Validation Node, SSH from Control Node |
| sg-backup | SSH from Control Node, access to Web / DB for validation |
| sg-monitoring | Phase 2 only: Prometheus / Grafana access |

SSH 접속은 관리자 또는 허용된 대역에서만 접근하도록 제한한다.

DB Node의 3306 포트는 전체 공개하지 않고 Web Node와 Backup / Validation Node에서만 접근하도록 제한한다.

---

## 7. Phase 2 운영 확장 아키텍처

Phase 2는 Phase 1 기본 구조 위에 운영 보강 기능을 추가한다.

~~~text
Phase 1 기본 구조
+ HAProxy HTTPS
+ HTTP to HTTPS Redirect
+ Cinder Backup Volume
+ node_exporter
+ cAdvisor
+ Prometheus
+ Grafana
+ backup / restore playbook
+ Ansible roles
~~~

---

## 7.1 HTTPS 확장

~~~text
Client
→ HTTPS 443
→ Proxy Node / HAProxy
→ Web Node / WordPress
~~~

Phase 2에서는 self-signed 인증서를 사용하여 HTTPS 접속을 검증하고, HTTP 80에서 HTTPS 443으로 Redirect를 구성한다.

---

## 7.2 Cinder Backup Volume 확장

~~~text
Backup / Validation Node
→ Cinder Volume attach
→ /backup mount
→ mysqldump 기반 MariaDB dump 저장
→ WordPress files archive 저장
~~~

Cinder Volume은 DB 원본 데이터 저장소가 아니라 Backup / Validation Node의 백업 저장소로 사용한다.

DB Node의 MariaDB 원본 데이터를 Cinder Volume에 직접 올리는 방식은 Docker Volume 경로, 권한, 복구 복잡도 문제로 이번 범위에서 제외한다.

---

## 7.3 Monitoring 확장

~~~text
Web Node
→ node_exporter
→ cAdvisor

Monitoring Node
→ Prometheus
→ Grafana
~~~

Prometheus는 node_exporter와 cAdvisor의 메트릭을 수집하고, Grafana는 수집된 데이터를 시각화한다.

---

## 8. Phase 3 도전 확장 아키텍처

Phase 3는 Web Node를 2대로 확장하고 HAProxy Load Balancing을 검증하는 도전 확장 단계이다.

~~~text
Client
→ Proxy Node / HAProxy Load Balancer
→ Web Node 1 / WordPress
→ Web Node 2 / WordPress
→ DB Node / MariaDB
→ Backup / Validation Node
~~~

Phase 3의 검증 범위는 다음과 같다.

| Item | Validation |
|---|---|
| Web Node 2대 | Web-1 / Web-2 모두 WordPress 응답 |
| HAProxy LB | roundrobin 기반 응답 분산 |
| Common DB | 두 Web Node가 동일 DB Node에 연결 |
| Failure Test | Web Node 1 중지 시 Web Node 2 응답 |

---

## 9. Phase 3 제한 사항

WordPress는 DB뿐만 아니라 `wp-content/uploads`, plugins, themes 같은 파일도 로컬에 저장한다.

따라서 Web Node 2대 구성 시 WordPress files 동기화 문제가 발생할 수 있다.

이번 프로젝트에서는 아래 항목을 구현 범위에서 제외한다.

~~~text
WordPress files 자동 동기화
wp-content/uploads 공유
plugin/theme 동기화
NFS 기반 WordPress shared storage
Object Storage 연동
DB Replication
DB Clustering
OpenStack LBaaS / Octavia
Auto Scaling
~~~

Phase 3 시연은 HAProxy roundrobin, Web-1/Web-2 응답 분산, 공통 DB Node 연결 확인 수준으로 제한한다.

---

## 10. 검증 기준

| Validation Area | Method |
|---|---|
| SSH | Control Node에서 각 대상 노드 SSH 접속 |
| Ansible | ansible all -m ping |
| Docker | docker ps |
| Proxy | Proxy Node에서 HAProxy 컨테이너 running 확인 |
| Web | Web Node에서 WordPress 컨테이너 running 확인 |
| DB | DB Node에서 MariaDB 서비스 running 확인 |
| HTTP | Proxy Node 경유 WordPress HTTP 접속 |
| DB Connection | Web Node WordPress가 DB Node MariaDB 연결 |
| Port | ss -tulnp 또는 유사 명령으로 포트 확인 |
| Health Check | health_check.sh 실행 |
| Backup | backup.sh 실행 |
| Restore | restore.md 기반 복구 절차 검증 |

---

## 11. 핵심 아키텍처 메시지

~~~text
본 프로젝트는 OpenStack 기반 Ubuntu 인스턴스 위에서
Control Node, Proxy Node, Web Node, DB Node, Backup / Validation Node를 분리하고,
Ansible을 통해 Docker 기반 WordPress, MariaDB, HAProxy HTTP Reverse Proxy를 배포한다.

이후 상태 점검, 백업, 복구 절차 검증을 통해
단순 서비스 배포가 아닌 인프라 운영 자동화 흐름을 완성한다.
~~~

