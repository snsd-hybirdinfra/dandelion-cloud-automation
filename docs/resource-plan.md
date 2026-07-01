<!-- STATUS: CURRENT -->

# Resource Plan

## 1. 문서 목적

본 문서는 Team Dandelion 프로젝트의 최신 노드 스펙과 리소스 계획을 정리한다.

구성 변경에 따라 Web, DB, Proxy, Monitoring, Backup / Recovery 영역의 역할이 조정되었으므로, 본 문서를 최신 기준으로 사용한다.

---

## 2. 최신 노드 구성

| Node | vCPU | RAM | Disk | 역할 |
|---|---:|---:|---:|---|
| Control Node | 2 Core | 2 GB | 20 GB | Ansible 실행 및 중앙 관리 |
| Proxy Node | 1 Core | 1 GB | 15 GB | HAProxy 기반 Proxy 구성 |
| Web Node | 1 Core | 2 GB | 20 GB | Docker Swarm 기반 Web Service |
| DB Node | 2 Core | 4 GB | 20 GB | MariaDB 및 Replica 검증 |
| Backup / Recovery Node | 1 Core | 2 GB | 20 GB + 80 GB Cinder | Restic 백업 및 복구 검증 |
| Monitoring Node | 1 Core | 2 GB | 15 GB | Prometheus, Exporter, Grafana, Alertmanager |

---

## 3. 총 리소스 산정

| 항목 | 합계 |
|---|---:|
| vCPU | 8 Core |
| RAM | 13 GB |
| VM Root Disk | 110 GB |
| Cinder Volume | 80 GB |
| Total Disk | 190 GB |

---

## 4. 노드별 상세 역할

### 4.1 Control Node

Control Node는 전체 자동화의 실행 지점이다.

| 항목 | 내용 |
|---|---|
| 주요 역할 | Ansible 실행, Inventory 관리, Playbook 실행 |
| 주요 구성 | Ansible, SSH Key, ansible.cfg, inventory |
| 자동화 범위 | Provisioning, Common Setup, Service Deployment, Monitoring, Backup, Validation |

---

### 4.2 Proxy Node

Proxy Node는 외부 요청을 Web 서비스 영역으로 전달하는 역할을 수행한다.

| 항목 | 내용 |
|---|---|
| 주요 역할 | Proxy / HAProxy 구성 |
| 주요 구성 | HAProxy |
| 검증 항목 | HTTP 응답, Web 서비스 전달 확인 |

---

### 4.3 Web Node

Web Node는 Docker Swarm 기반 Web 서비스를 실행한다.

| 항목 | 내용 |
|---|---|
| 주요 역할 | Web Service 실행 |
| 주요 구성 | Docker, Docker Swarm, WordPress |
| 검증 항목 | Container 상태, Swarm Service 상태, HTTP 응답 |

---

### 4.4 DB Node

DB Node는 MariaDB를 구성하고, Replica 기반 이중화 검증을 진행한다.

| 항목 | 내용 |
|---|---|
| 주요 역할 | Database Service |
| 주요 구성 | MariaDB, Replica 검증 |
| 검증 항목 | MariaDB 상태, DB 접속, Replica 상태 |

---

### 4.5 Backup / Recovery Node

Backup / Recovery Node는 Restic 기반 백업과 복구 검증을 담당한다.

| 항목 | 내용 |
|---|---|
| 주요 역할 | 백업 저장 및 복구 검증 |
| 주요 구성 | Restic, Backup Scripts, Restore Test |
| 추가 디스크 | 80 GB Cinder Volume |
| 검증 항목 | Snapshot 생성, Restore Test, 복구 시나리오 |

---

### 4.6 Monitoring Node

Monitoring Node는 운영 상태 수집과 시각화, 알림 구성을 담당한다.

| 항목 | 내용 |
|---|---|
| 주요 역할 | Monitoring / Alerting |
| 주요 구성 | Prometheus, node_exporter, cAdvisor, mysqld_exporter, blackbox_exporter, Grafana, Alertmanager |
| 검증 항목 | Prometheus target, Grafana Dashboard, Alertmanager 설정 |

---

## 5. 구성 변경 반영 사항

| 변경 항목 | 기존 방향 | 최신 방향 |
|---|---|---|
| Web 구성 | Web1 / Web2 개별 구성 | 단일 Web Node 위 Docker Swarm 기반 구성 |
| Proxy 역할 | Reverse Proxy + Load Balancer 중심 | HAProxy 기반 Proxy 구성 |
| DB 구성 | 단일 DB Node | MariaDB Replica 검증 진행 |
| Monitoring | Prometheus 중심 | Prometheus + Exporter + Grafana + Alertmanager |
| Backup | backup.sh 중심 | Restic 기반 백업 및 복구 검증 |
| 시간 기준 | 기본 서버 시간 | 한국표준시 기준 설정 |

---

## 6. 리소스 산정 근거

| 노드 | 산정 근거 |
|---|---|
| Control Node | Ansible 실행 및 중앙 관리 용도이므로 2 Core / 2 GB 구성 |
| Proxy Node | HAProxy 기반 요청 전달 역할로 1 Core / 1 GB 구성 |
| Web Node | Docker Swarm 및 WordPress 실행을 고려하여 1 Core / 2 GB 구성 |
| DB Node | MariaDB 실행 및 Replica 검증을 고려하여 2 Core / 4 GB 구성 |
| Backup / Recovery Node | Restic 백업 저장과 복구 테스트를 위해 Cinder Volume 추가 |
| Monitoring Node | Prometheus, Grafana, Exporter 구성을 고려하여 1 Core / 2 GB 구성 |

---

## 7. 멘토링 확인 사항

멘토링 시 다음 사항을 확인한다.

```text
1. 현재 리소스 규모가 Docker Swarm, Monitoring Stack, Restic 백업 검증에 충분한지
2. DB Replica 검증을 위한 DB Node 리소스가 적정한지
3. Monitoring Node 1 Core / 2 GB 구성이 Prometheus + Grafana + Alertmanager에 충분한지
4. Backup / Recovery Node의 80 GB Cinder Volume이 제출용 검증에 적절한지
5. 최종 목표인 OpenStack Provisioning 자동화까지 고려할 때 노드 구성이 과하지 않은지
```
