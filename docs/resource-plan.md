<!-- STATUS: COMPLETE -->

# Resource Plan

## 1. 목적

본 문서는 Team Dandelion 프로젝트의 OpenStack 인스턴스별 리소스 산정 기준을 정의한다.

프로젝트는 Control, HAProxy, Web, DB, Backup, Monitoring Node를 분리하여 구성하며, 각 노드는 역할에 따라 vCPU, Disk, RAM을 다르게 할당한다.

---

## 2. Node Resource Allocation

| Node | Role | vCPU | Disk | RAM |
|---|---|---:|---:|---:|
| control | Ansible Control Node | 2 Core | 20 GB | 2 GB |
| haproxy | HAProxy Reverse Proxy Node | 1 Core | 15 GB | 1 GB |
| web | Custom WordPress Web Node | 1 Core | 20 GB | 2 GB |
| db | MariaDB Service Node | 2 Core | 20 GB | 4 GB |
| backup | Backup / Validation Node | 1 Core | 20 GB + 80 GB Cinder | 2 GB |
| monitoring | Prometheus / Grafana Monitoring Node | 1 Core | 15 GB | 2 GB |

---

## 3. Total Resource Requirement

| Resource | Total |
|---|---:|
| vCPU | 8 Core |
| VM Disk | 110 GB |
| Cinder Volume | 80 GB |
| Total Disk | 190 GB |
| RAM | 13 GB |

---

## 4. Resource Design Rationale

## 4.1 Control Node

Control Node는 Ansible 실행, inventory 관리, playbook 실행, SSH 기반 원격 구성을 담당한다.

서비스 트래픽을 직접 처리하지 않기 때문에 고성능 리소스는 필요하지 않지만, Ansible 실행과 로그 확인을 위해 2 Core / 2 GB RAM을 할당한다.

---

## 4.2 HAProxy Node

HAProxy Node는 사용자 HTTP / HTTPS 요청을 Web Node로 전달하는 Reverse Proxy 역할을 수행한다.

Phase 1에서는 단일 Web Node 대상 HTTP Reverse Proxy를 담당하고, Phase 3에서는 Web Node 1 / Web Node 2 대상 Load Balancing으로 확장될 수 있다.

HAProxy 자체는 경량 서비스이므로 1 Core / 1 GB RAM 기준으로 구성한다.

---

## 4.3 Web Node

Web Node는 Custom WordPress Container를 실행하는 서비스 노드이다.

WordPress 컨테이너 실행, Apache/PHP 처리, DB Node와의 연결을 담당한다.

기본 실습 환경에서는 1 Core / 2 GB RAM 기준으로 구성하며, 부하 증가 또는 Phase 3 확장 시 Web Node를 추가하는 방식으로 확장한다.

---

## 4.4 DB Node

DB Node는 MariaDB를 컨테이너가 아닌 직접 설치 방식으로 운영한다.

WordPress 데이터 저장 및 MariaDB Service 운영을 담당하므로 다른 서비스 노드보다 높은 RAM을 배정한다.

MariaDB 안정성을 위해 2 Core / 4 GB RAM 기준으로 구성한다.

---

## 4.5 Backup / Validation Node

Backup / Validation Node는 health_check.sh, backup.sh, MariaDB dump, WordPress files archive, restore.md 기반 복구 검증을 담당한다.

기본 OS Disk는 20 GB로 구성하고, 백업 데이터 저장을 위해 80 GB Cinder Volume을 추가로 연결한다.

Cinder Volume은 DB 원본 저장소가 아니라 백업 저장소로 사용한다.

---

## 4.6 Monitoring Node

Monitoring Node는 Prometheus와 Grafana를 구성하여 인프라 및 서비스 상태를 시각화하는 역할을 담당한다.

Phase 2 운영 확장 범위에 해당하며, node_exporter 및 cAdvisor와 연계하여 메트릭 수집 구조를 구성할 수 있다.

기본 리소스는 1 Core / 15 GB Disk / 2 GB RAM 기준으로 구성한다.

---

## 5. Phase별 리소스 기준

| Phase | Resource 기준 |
|---|---|
| Phase 1 | Control / HAProxy / Web / DB / Backup Node 구성 |
| Phase 2 | Monitoring Node 및 Cinder Backup Volume 구성 |
| Phase 3 | Web Node 2 추가 가능 |
| Post-Phase | DB Node 이중화 / MariaDB Replication / Failover 검토 |

Phase 3에서 Web Node 2를 추가할 경우 최소 추가 리소스는 다음과 같다.

| Additional Node | vCPU | Disk | RAM |
|---|---:|---:|---:|
| web-2 | 1 Core | 20 GB | 2 GB |

Phase 3 확장 시 전체 예상 리소스는 다음과 같다.

| Resource | Total |
|---|---:|
| vCPU | 9 Core |
| VM Disk | 130 GB |
| Cinder Volume | 80 GB |
| Total Disk | 210 GB |
| RAM | 15 GB |

---

## 6. 최종 기준

본 프로젝트의 기본 구현 기준은 다음과 같다.

~~~text
control    = 2 Core / 20 GB / 2 GB
haproxy    = 1 Core / 15 GB / 1 GB
web        = 1 Core / 20 GB / 2 GB
db         = 2 Core / 20 GB / 4 GB
backup     = 1 Core / 20 GB + 80 GB Cinder / 2 GB
monitoring = 1 Core / 15 GB / 2 GB
~~~

기본 구성 총합은 다음과 같다.

~~~text
Total vCPU        = 8 Core
Total VM Disk     = 110 GB
Total Cinder Disk = 80 GB
Total Disk        = 190 GB
Total RAM         = 13 GB
~~~

