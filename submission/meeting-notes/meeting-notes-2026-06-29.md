<!-- STATUS: COMPLETE -->

# Team Dandelion 회의록

## 2026-06-29 회의록

## 1. 회의 정보

| 구분 | 내용 |
|---|---|
| 회의 일자 | 2026-06-29 |
| 회의 구분 | Phase 확장 구성 변경 및 담당 역할 재조정 |
| 회의 장소 | ZEP 팀 회의실 / Discord |
| 작성자 | 정주헌 |
| 참석자 | 정주헌, 백서빈, 이진욱, 조민석, 박재우 |

---

## 2. 회의 목적

- 2026-06-29 기준 팀원별 진행 상황 공유
- DB Node Replica 기반 이중화 작업 진행 상태 확인
- 인프라 장애 대응 보고서 작성 진행 상태 확인
- Backup Playbook 및 후속 Ansible 작업 범위 확인
- Monitoring Exporter 설치 예정 범위 정리
- Monitoring / Validation / Backup / Recovery 담당 역할 재분배
- Web Node 구성 및 Proxy Node 역할 변경 방향 정리
- 세부 노드 스펙 변경 필요사항 확인

---

## 3. 주요 진행 내용

### 3.1 이진욱 - DB Node Replica 이중화 작업 진행

이진욱은 DB Node를 Replica 기반으로 이중화하는 작업을 진행 중이다.

| 작업 항목 | 진행 내용 | 상태 |
|---|---|---|
| DB Node 이중화 | 단일 DB Node 구조에서 Replica 기반 이중화 구조로 확장 작업 진행 | 진행 |
| DB Replica 구성 | MariaDB Replica 구조 검토 및 구성 작업 진행 | 진행 |
| DB 고가용성 방향 | 장애 발생 시 DB 연속성 확보를 위한 확장 방향 반영 | 진행 |

기존 구성에서는 단일 DB Node를 기준으로 MariaDB 서비스를 운영하였으나, 29일 기준으로 DB Node를 Replica 기반 이중화 구조로 확장하는 작업을 진행 중이다.

해당 작업은 DB 장애 대응력과 서비스 연속성을 높이기 위한 확장 작업으로 분류한다.

---

### 3.2 백서빈 - 인프라 작업 완료 및 장애 대응 보고서 작성

백서빈은 Phase 1, Phase 2 인프라 작업을 완료하고, 현재 인프라 작업 중 발생 가능한 장애 대응 보고서를 작성 중이다.

| 작업 항목 | 진행 내용 | 상태 |
|---|---|---|
| Phase 1 인프라 작업 | 기본 인프라 구성 완료 | 완료 |
| Phase 2 인프라 작업 | 운영 확장 관련 인프라 구성 완료 | 완료 |
| 장애 대응 보고서 | 인프라 작업 중 발생 가능한 장애 및 대응 절차 정리 | 진행 |

인프라 담당 영역은 구축 중심 작업에서 장애 대응 문서화 중심으로 전환되었다.

장애 대응 보고서에는 인스턴스, 네트워크, 보안그룹, 디스크, SSH 접속, Cinder Volume 등 인프라 계층에서 발생 가능한 문제와 대응 절차를 포함할 예정이다.

---

### 3.3 조민석 - Ansible 작업 완료 및 Backup Playbook 후속 작업 예정

조민석은 Backup Playbook 작업 완료 시 후속 작업을 진행할 예정이며, 그 외 Ansible 관련 작업은 완료 상태로 정리하였다.

| 작업 항목 | 진행 내용 | 상태 |
|---|---|---|
| Ansible 기본 작업 | 기존 Playbook 및 기본 자동화 작업 완료 | 완료 |
| 서비스 Playbook | 주요 서비스 구성 관련 Playbook 작업 완료 | 완료 |
| Backup Playbook 연계 | Backup Playbook 작업 완료 이후 후속 작업 예정 | 예정 |
| 추가 작업 | Backup Playbook 완료 시 실행 검증 및 보완 작업 예정 | 예정 |

현재 조민석의 주요 Ansible 작업은 대부분 완료되었으며, 남은 작업은 Backup Playbook 완료 이후 실행 검증 및 후속 보완 작업으로 정리한다.

---

### 3.4 박재우 - Monitoring Exporter 설치 예정

박재우는 Prometheus 기반 모니터링 구성을 위해 주요 Exporter 설치를 진행할 예정이다.

| 작업 항목 | 진행 내용 | 상태 |
|---|---|---|
| Prometheus | 모니터링 서버 구성 예정 | 예정 |
| node_exporter | 서버 OS 메트릭 수집용 Exporter 설치 예정 | 예정 |
| cAdvisor | 컨테이너 메트릭 수집용 Exporter 설치 예정 | 예정 |
| mysqld_exporter | MariaDB 메트릭 수집용 Exporter 설치 예정 | 예정 |
| blackbox_exporter | HTTP / Endpoint 상태 점검용 Exporter 설치 예정 | 예정 |

Monitoring 파트는 Prometheus를 중심으로 node_exporter, cAdvisor, mysqld_exporter, blackbox_exporter를 연계하여 서버, 컨테이너, DB, 서비스 엔드포인트 상태를 수집하는 방향으로 진행한다.

---

## 4. 담당 역할 재조정

기존 Monitoring / Backup / Validation 담당 범위를 세분화하여 다음과 같이 역할을 조정하였다.

| 영역 | 담당자 | 역할 |
|---|---|---|
| Monitoring | 박재우 | Prometheus 및 Exporter 구성, 메트릭 수집, 모니터링 화면 구성 |
| Validation | 정주헌 | 서비스 검증 시나리오 작성, 검증 체크리스트 작성, 결과 확인 |
| Backup | 정주헌 | 백업 구조 검증, 백업 결과 확인, 백업 증빙 정리 |
| Recovery | 정주헌 | 복구 절차 작성, 복구 검증, restore 문서화 |

역할 조정 결과, 박재우는 Monitoring 파트에 집중하고, 정주헌은 검증 및 백업/복구 파트를 담당한다.

이를 통해 Monitoring 구성과 검증/복구 문서화 작업을 분리하여 진행한다.

---

## 5. 구성 변경 사항

### 5.1 Web Node 구성 변경

기존 Web Node 구성은 단일 Web Node 또는 Web1 / Web2 기반 구성으로 검토되었으나, 29일 기준으로 Web Node 구성을 Docker Swarm Cluster 기반으로 수정하는 방향으로 변경하였다.

| 구분 | 기존 방향 | 변경 방향 |
|---|---|---|
| Web 구성 | 단일 Web Node 또는 Web1 / Web2 개별 구성 | Docker Swarm Cluster 기반 구성 |
| 서비스 배포 | 개별 Web Node 배포 | Swarm 기반 서비스 배포 |
| 확장 방향 | Web Node 추가 방식 | Cluster 기반 Web 서비스 운영 |

Docker Swarm Cluster 구성을 통해 Web 서비스 영역의 확장성과 장애 대응 구조를 강화하는 방향으로 정리한다.

---

### 5.2 Proxy Node 역할 변경

Proxy Node는 기존에 Reverse Proxy와 Load Balancer 역할을 함께 수행하는 방향으로 검토되었으나, 29일 기준으로 Load Balancer 역할을 제거하고 Reverse Proxy 역할만 수행하는 방향으로 변경하였다.

| 구분 | 기존 역할 | 변경 역할 |
|---|---|---|
| Proxy Node | Reverse Proxy + Load Balancer | Reverse Proxy 전담 |
| Load Balancer | Proxy Node에서 수행 | Web Node / Web Cluster 영역에서 수행 |
| 트래픽 흐름 | Proxy → Web1 / Web2 분산 | Proxy → Web Cluster 진입점 전달 |

변경 후 구조는 다음과 같이 정리한다.

~~~text
User
→ Proxy Node
→ Reverse Proxy
→ Web Cluster / Load Balancing 영역
→ WordPress Service
~~~

Proxy Node는 외부 요청을 받아 내부 Web 서비스 영역으로 전달하는 Reverse Proxy 역할에 집중한다.

Load Balancing 역할은 Web Node 또는 Docker Swarm Cluster 영역에서 수행하는 방향으로 변경한다.

---

### 5.3 세부 노드 스펙 변경

구성 변경에 따라 세부 노드 스펙 변경이 필요하다.

| 변경 항목 | 내용 | 상태 |
|---|---|---|
| Web Node 스펙 | Docker Swarm Cluster 구성에 맞춰 재검토 필요 | 진행 |
| DB Node 스펙 | Replica 기반 이중화 구성에 맞춰 재검토 필요 | 진행 |
| Proxy Node 스펙 | Reverse Proxy 전담 역할 기준으로 재검토 필요 | 진행 |
| Monitoring Node 스펙 | Exporter 및 Prometheus 구성 기준으로 재검토 필요 | 진행 |

세부 노드 스펙은 29일 기준으로 변경 필요성이 확인되었으며, 최종 스펙은 실제 구성 및 검증 결과에 따라 별도 문서에 반영한다.

---

## 6. 금일 결정 사항

| 번호 | 결정 내용 |
|---:|---|
| 1 | DB Node는 Replica 기반 이중화 작업을 진행한다. |
| 2 | 백서빈은 Phase 1, Phase 2 인프라 작업 완료 후 장애 대응 보고서를 작성한다. |
| 3 | 조민석은 Backup Playbook 작업 완료 시 후속 검증 및 보완 작업을 진행한다. |
| 4 | 박재우는 Prometheus, node_exporter, cAdvisor, mysqld_exporter, blackbox_exporter 설치를 진행할 예정이다. |
| 5 | Monitoring 파트는 박재우가 담당한다. |
| 6 | 검증 및 백업/복구 파트는 정주헌이 담당한다. |
| 7 | Web Node 구성은 Docker Swarm Cluster 기반으로 수정한다. |
| 8 | Proxy Node는 Load Balancer 역할을 제거하고 Reverse Proxy 역할만 수행한다. |
| 9 | Load Balancer 역할은 Web Node 또는 Web Cluster 영역에서 수행하는 방향으로 변경한다. |
| 10 | 구성 변경에 따라 세부 노드 스펙을 재정리한다. |

---

## 7. 이슈 및 대응

| 이슈 | 내용 | 대응 |
|---|---|---|
| 기존 구조와 변경 구조 차이 | 기존 Proxy 기반 HAProxy RR 구조와 Docker Swarm 기반 Web Cluster 구조가 다름 | architecture.md, resource-plan.md, 발표자료에 변경 구조 반영 |
| DB 이중화 범위 확대 | 단일 DB Node에서 Replica 기반 이중화로 범위 확장 | 진행 상태와 검증 결과를 별도로 기록 |
| Proxy 역할 변경 | Proxy Node의 Load Balancer 역할 제거 필요 | Reverse Proxy 전담 구조로 문서 수정 |
| Monitoring 범위 확대 | Exporter 종류가 증가함 | Prometheus target 및 Exporter별 역할 표 작성 |
| 검증 / 백업 / 복구 담당 변경 | 기존 Monitoring/Backup 담당 범위 재조정 필요 | 담당자별 역할표 수정 |

---

## 8. 다음 작업 계획

| 담당자 | 다음 작업 |
|---|---|
| 이진욱 | DB Replica 구성 진행, DB 이중화 구조 검증 자료 정리 |
| 백서빈 | 인프라 장애 대응 보고서 작성, 변경된 노드 스펙 정리 |
| 조민석 | Backup Playbook 완료 후 실행 검증 및 보완 작업 진행 |
| 박재우 | Prometheus 및 Exporter 설치, target 상태 확인 준비 |
| 정주헌 | 검증 체크리스트 작성, 백업/복구 절차 정리, 변경 아키텍처 문서 반영 |

---

## 9. 회의 결과 요약

2026년 6월 29일 회의에서는 기존 Phase 구성 이후 프로젝트 확장 방향과 담당 역할을 재조정하였다.

이진욱은 DB Node를 Replica 기반으로 이중화하는 작업을 진행 중이며, 백서빈은 Phase 1, Phase 2 인프라 작업을 완료하고 인프라 장애 대응 보고서를 작성 중이다.

조민석은 주요 Ansible 작업을 완료한 상태이며, Backup Playbook 작업 완료 후 후속 검증 및 보완 작업을 진행할 예정이다.

박재우는 Prometheus, node_exporter, cAdvisor, mysqld_exporter, blackbox_exporter 설치를 진행할 예정이다.

역할은 Monitoring 파트를 박재우가 담당하고, 검증 및 백업/복구 파트는 정주헌이 담당하는 방식으로 조정하였다.

또한 Web Node 구성을 Docker Swarm Cluster 기반으로 수정하고, Proxy Node는 Load Balancer 역할을 제거한 뒤 Reverse Proxy 역할만 수행하도록 변경하였다.

Load Balancer 역할은 Web Node 또는 Web Cluster 영역에서 수행하는 방향으로 조정하였으며, 이에 따라 세부 노드 스펙을 재정리할 예정이다.
