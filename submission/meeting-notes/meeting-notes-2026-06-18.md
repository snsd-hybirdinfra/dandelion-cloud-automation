<!-- STATUS: COMPLETE -->

# Team Dandelion 회의록

## 2026-06-18 회의록

## 1. 회의 정보

| 구분 | 내용 |
|---|---|
| 회의 일자 | 2026-06-18 |
| 회의 구분 | 리소스표 기반 인스턴스 생성 및 Control Node SSH 접속 검증 |
| 회의 장소 | ZEP 팀 회의실 / Discord |
| 작성자 | 정주헌 |
| 참석자 | 정주헌, 백서빈, 이진욱, 조민석, 박재우 |

---

## 2. 회의 목적

- 최신 OpenStack 인스턴스 리소스 기준 확정
- 확정된 리소스표 기준으로 인스턴스 생성 진행 내용 정리
- Backup Node의 OS Disk와 Cinder Volume 분리 기준 정리
- Monitoring Node 추가 방향 정리
- 포트포워딩 기반 Control Node SSH 접속 검증 결과 공유
- 관리자 접근 구조와 Control Node 중심 관리 구조 재확인
- 2026-06-18 기준 진행 내용 및 후속 작업 정리

---

## 3. 주요 논의 내용

### 3.1 최신 리소스 산정 기준 확정 및 인스턴스 생성

금일 논의를 통해 OpenStack 인스턴스별 최신 리소스 산정 기준을 확정하고, 해당 리소스표에 맞춰 인스턴스 생성을 진행하였다.

최신 리소스 기준은 다음과 같다.

| Node | vCPU | Disk | RAM |
|---|---:|---:|---:|
| control | 2 Core | 20 GB | 2 GB |
| haproxy | 1 Core | 15 GB | 1 GB |
| web | 1 Core | 20 GB | 2 GB |
| db | 2 Core | 20 GB | 4 GB |
| backup | 1 Core | 20 GB + 80 GB Cinder | 2 GB |
| monitoring | 1 Core | 15 GB | 2 GB |

기존 리소스 산정과 비교하여 HAProxy Node는 1 GB RAM 기준으로 유지하고, Web Node는 1 Core 기준으로 조정하였다.

Backup Node는 OS Disk와 Backup Volume을 분리하여, 기본 OS Disk 20 GB와 Cinder Volume 80 GB를 사용하는 구조로 정리하였다.

Monitoring Node는 Phase 2 운영 확장 범위로 추가한다.

---

### 3.2 전체 리소스 총합 재산정

최신 리소스 기준에 따라 전체 필요 리소스를 다시 산정하고, 해당 기준으로 OpenStack 인스턴스 생성을 진행하였다.

| Resource | Total |
|---|---:|
| vCPU | 8 Core |
| VM Disk | 110 GB |
| Cinder Volume | 80 GB |
| Total Disk | 190 GB |
| RAM | 13 GB |

VM Disk는 각 인스턴스의 Root Disk 합계이며, Cinder Volume은 Backup Node에 연결되는 별도 백업 저장소로 계산한다.

따라서 전체 저장공간 기준은 VM Disk 110 GB와 Cinder Volume 80 GB를 합산한 190 GB로 정리한다.

---

### 3.3 Backup Node 저장소 구조 정리

Backup Node는 기존 단일 Disk 기준이 아니라 OS Disk와 백업 저장소를 분리하는 구조로 정리하였다.

| 항목 | 기준 |
|---|---|
| OS Disk | 20 GB |
| Cinder Volume | 80 GB |
| Mount Path | /backup |
| 저장 대상 | MariaDB dump, WordPress files archive, restore 검증 자료 |
| 사용 목적 | Backup / Validation |
| 제외 기준 | DB 원본 저장소로 사용하지 않음 |

Cinder Volume은 DB Node의 원본 데이터 저장소가 아니라, Backup / Validation Node에서 백업 결과물을 보관하기 위한 저장소로 사용한다.

---

### 3.4 Monitoring Node 추가 방향 정리

Monitoring Node는 Phase 2 운영 확장 범위로 추가하기로 하였다.

| 항목 | 내용 |
|---|---|
| Node | monitoring |
| vCPU | 1 Core |
| Disk | 15 GB |
| RAM | 2 GB |
| 주요 역할 | Prometheus / Grafana |
| Phase 기준 | Phase 2 운영 확장 |

Monitoring Node는 Prometheus와 Grafana를 통해 서비스 및 인프라 상태를 시각화하는 역할을 담당한다.

node_exporter와 cAdvisor는 각 노드의 메트릭 수집을 위해 연계할 수 있다.

---

### 3.5 포트포워딩 기반 Control Node SSH 접속 검증

최신 리소스표 기준으로 생성한 인스턴스 중 Control Node에 대해 공유기 포트포워딩을 통한 외부 SSH 접속이 정상적으로 수행되는 것을 확인하였다.

해당 검증을 통해 Control Node가 프로젝트의 관리 진입점 역할을 수행할 수 있음을 확인하였다.

검증된 관리 접근 구조는 다음과 같다.

~~~text
Admin
→ Router Port Forwarding
→ Control Node SSH
→ Ansible / SSH
→ Proxy / Web / DB / Backup / Monitoring Node
~~~

관리자는 각 노드에 직접 접속하지 않고 Control Node에만 SSH로 접근한다.

이후 Control Node에서 Ansible과 SSH를 통해 전체 노드를 관리하는 구조로 진행한다.

---

### 3.6 현재 구현 범위와 향후 확장 방향 재확인

현재 구현 범위에서는 단일 DB Node 구조를 유지한다.

DB Node는 MariaDB를 직접 설치하고 systemd 서비스로 운영하는 방식으로 구성한다.

다만 멘토링 이후 논의된 내용을 반영하여, 추후 확장 방향에는 DB Node 이중화, MariaDB Replication, DB Failover 구조를 포함한다.

| 구분 | 현재 기준 | 향후 확장 방향 |
|---|---|---|
| DB 구조 | 단일 DB Node | DB Node 이중화 |
| DB 서비스 | MariaDB systemd Service | MariaDB Replication |
| 장애 대응 | Backup / Restore 중심 | Failover 구조 검토 |
| 프로젝트 반영 | Phase 1~3 | Post-Phase Extension |

---

## 4. 결정 사항

| 번호 | 결정 내용 |
|---:|---|
| 1 | 최신 리소스 산정 기준에 Monitoring Node를 포함한다. |
| 2 | HAProxy Node는 1 Core / 15 GB / 1 GB 기준으로 구성한다. |
| 3 | Web Node는 1 Core / 20 GB / 2 GB 기준으로 구성한다. |
| 4 | DB Node는 2 Core / 20 GB / 4 GB 기준으로 구성한다. |
| 5 | Backup Node는 1 Core / 20 GB OS Disk / 2 GB RAM 기준으로 구성한다. |
| 6 | Backup Node에는 80 GB Cinder Volume을 추가 연결한다. |
| 7 | Cinder Volume은 /backup 경로에 마운트하여 백업 저장소로 사용한다. |
| 8 | Cinder Volume은 DB 원본 저장소로 사용하지 않는다. |
| 9 | 기본 구성 총합은 vCPU 8 Core, VM Disk 110 GB, Cinder Volume 80 GB, Total Disk 190 GB, RAM 13 GB로 정리한다. |
| 10 | 최신 리소스표 기준으로 OpenStack 인스턴스 생성을 진행하였다. |
| 11 | 포트포워딩 기반 Control Node SSH 접속이 정상적으로 확인되었다. |
| 12 | 관리자는 Control Node에만 접속하고, Control Node에서 Ansible / SSH로 전체 노드를 관리한다. |
| 13 | DB Node 이중화는 현재 구현 범위가 아니라 Post-Phase 확장 방향으로 둔다. |

---

## 5. 다음 작업 계획

| 담당자 | 다음 작업 |
|---|---|
| 정주헌 | 회의록, 작업일지, resource-plan.md, 발표자료 리소스 표 최신화 |
| 백서빈 | 최신 리소스 기준에 맞춰 인스턴스 및 Cinder Volume 구성 확인 |
| 이진욱 | 노드별 기본 환경 구성 및 서비스 패키지 설치 진행 |
| 조민석 | Control Node에서 각 노드 SSH 접속 및 ansible ping 검증 준비 |
| 박재우 | Backup Node의 /backup 경로 및 Cinder Volume 기준으로 backup.sh 수정 준비 |

---

## 6. 회의 결과 요약

2026년 6월 18일 회의에서는 OpenStack 인스턴스별 최신 리소스 산정 기준을 확정하고, 해당 기준에 맞춰 인스턴스 생성을 진행하였다.

Control, HAProxy, Web, DB, Backup, Monitoring Node 기준으로 리소스를 다시 산정하고 인스턴스 생성을 진행하였으며, 기본 구성 총합은 vCPU 8 Core, VM Disk 110 GB, Cinder Volume 80 GB, Total Disk 190 GB, RAM 13 GB로 정리하였다.

Backup Node는 OS Disk 20 GB와 80 GB Cinder Volume을 분리하여 구성하기로 하였으며, Cinder Volume은 DB 원본 저장소가 아니라 MariaDB dump, WordPress files archive, restore 검증 자료를 저장하는 백업 저장소로 사용한다.

또한 공유기 포트포워딩을 통해 외부 환경에서 Control Node까지 SSH 접속되는 것을 확인하였다.

이를 통해 관리자는 Control Node에만 접속하고, Control Node에서 Ansible과 SSH를 통해 전체 노드를 관리하는 구조를 실제로 검증하였다.
