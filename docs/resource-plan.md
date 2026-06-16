<!-- STATUS: COMPLETE -->

# Resource Plan

## 1. 목적

본 문서는 Team Dandelion 프로젝트의 OpenStack 인스턴스별 최소 리소스 산정 기준을 정의한다.

프로젝트는 Control, HAProxy, Web, DB, Backup Node를 분리하여 구성하며, 각 노드는 역할에 따라 vCPU, Disk, RAM을 다르게 할당한다.

---

## 2. Node Resource Allocation

| Node | Role | vCPU | Disk | RAM |
|---|---|---:|---:|---:|
| control | Ansible Control Node | 2 Core | 20 GB | 2 GB |
| haproxy | HAProxy Reverse Proxy Node | 1 Core | 15 GB | 1 GB |
| web | Custom WordPress Web Node | 2 Core | 20 GB | 2 GB |
| db | MariaDB Service Node | 2 Core | 20 GB | 4 GB |
| backup | Backup / Validation Node | 1 Core | 80 GB | 2 GB |

---

## 3. Total Resource Requirement

| Resource | Total |
|---|---:|
| vCPU | 8 Core |
| Disk | 155 GB |
| RAM | 11 GB |

---

## 4. Resource Design Rationale

## 4.1 Control Node

Control Node는 Ansible 실행, inventory 관리, playbook 실행, SSH 기반 원격 구성을 담당한다.

서비스 트래픽을 직접 처리하지 않기 때문에 고성능 리소스는 필요하지 않지만, Ansible 실행과 로그 확인을 위해 최소 2 Core / 2 GB RAM을 할당한다.

---

## 4.2 HAProxy Node

HAProxy Node는 사용자 HTTP 요청을 Web Node로 전달하는 Reverse Proxy 역할을 수행한다.

Phase 1에서는 단일 Web Node 대상 HTTP Reverse Proxy를 담당하고, Phase 3에서는 Web Node 1 / Web Node 2 대상 Load Balancing으로 확장될 수 있다.

HAProxy 자체는 경량 서비스이므로 1 Core / 1 GB RAM 기준으로 구성한다.

---

## 4.3 Web Node

Web Node는 Custom WordPress Container를 실행하는 서비스 노드이다.

WordPress 컨테이너 실행, Apache/PHP 처리, DB Node와의 연결을 담당하므로 2 Core / 2 GB RAM을 할당한다.

---

## 4.4 DB Node

DB Node는 MariaDB를 컨테이너가 아닌 직접 설치 방식으로 운영한다.

WordPress 데이터 저장 및 MariaDB Service 운영을 담당하므로 Web Node보다 높은 RAM을 배정한다.

MariaDB 안정성을 위해 2 Core / 4 GB RAM 기준으로 구성한다.

---

## 4.5 Backup / Validation Node

Backup / Validation Node는 health_check.sh, backup.sh, MariaDB dump, WordPress files archive, restore.md 기반 복구 검증을 담당한다.

백업 파일 보관이 필요하므로 다른 노드보다 큰 Disk를 할당한다.

기본 Disk는 80 GB로 설정하며, Phase 2에서 Cinder Volume을 별도 백업 저장소로 확장할 수 있다.

---

## 5. Phase별 리소스 확장 기준

| Phase | Resource 기준 |
|---|---|
| Phase 1 | Control / HAProxy / Web / DB / Backup Node 구성 |
| Phase 2 | Monitoring Node 또는 Cinder Backup Volume 추가 가능 |
| Phase 3 | Web Node 2 추가 가능 |

Phase 3에서 Web Node 2를 추가할 경우 최소 추가 리소스는 다음과 같다.

| Additional Node | vCPU | Disk | RAM |
|---|---:|---:|---:|
| web-2 | 2 Core | 20 GB | 2 GB |

Phase 3 확장 시 전체 예상 리소스는 다음과 같다.

| Resource | Total |
|---|---:|
| vCPU | 10 Core |
| Disk | 175 GB |
| RAM | 13 GB |

---

## 6. 최종 기준

본 프로젝트의 기본 구현 기준은 다음과 같다.

~~~text
control  = 2 Core / 20 GB / 2 GB
haproxy  = 1 Core / 15 GB / 1 GB
web      = 2 Core / 20 GB / 2 GB
db       = 2 Core / 20 GB / 4 GB
backup   = 1 Core / 80 GB / 2 GB
~~~

기본 구성 총합은 다음과 같다.

~~~text
Total vCPU = 8 Core
Total Disk = 155 GB
Total RAM  = 11 GB
~~~

