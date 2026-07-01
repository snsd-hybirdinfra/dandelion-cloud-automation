<!-- STATUS: COMPLETE -->

# Team Dandelion 회의록

## 2026-06-30 회의록

## 1. 회의 정보

| 구분 | 내용 |
|---|---|
| 회의 일자 | 2026-06-30 |
| 회의 구분 | 구조 변경 반영, Monitoring 구성 완료, Backup / Recovery 검증 진행 |
| 회의 장소 | ZEP 팀 회의실 / Discord |
| 작성자 | 정주헌 |
| 참석자 | 정주헌, 백서빈, 이진욱, 조민석, 박재우 |

---

## 2. 회의 목적

- 29일 구조 변경 결정 이후 실제 반영 진행 상황 확인
- Web Node Docker Swarm 재구성 및 HAProxy 구성 완료 내용 공유
- 인스턴스 구조 수정 및 한국표준시 설정 반영 내용 확인
- 구조 변경에 따른 Ansible Playbook 수정 진행 상황 확인
- Prometheus, Exporter, Grafana, Alertmanager 설치 완료 상태 확인
- Restic 기반 Web / DB / Proxy Node 백업 및 복구 테스트 결과 공유
- 백업 스크립트, 모니터링 연계 작업, 복구 시나리오 문서화 진행 상태 정리

---

## 3. 주요 진행 내용

### 3.1 이진욱 - Web Node Docker Swarm 재구성 및 HAProxy 구성

이진욱은 Web Node 구성을 단일 노드 기반 Docker Swarm 구조로 재구성하고 HAProxy 구성을 완료하였다.

| 작업 항목 | 진행 내용 | 상태 |
|---|---|---|
| Web Node 구조 변경 | 단일 Web Node 위 Docker Swarm Cluster 구조로 재구성 | 완료 |
| Docker Swarm 구성 | Web 서비스 실행 구조를 Swarm 기반으로 수정 | 완료 |
| HAProxy 구성 | 변경된 Web 서비스 구조에 맞춰 HAProxy 구성 | 완료 |

기존 Web Node 구성은 개별 컨테이너 또는 Web1 / Web2 중심 구조였으나, 금일 작업을 통해 단일 Web Node 위에서 Docker Swarm 기반으로 서비스 구성을 재정리하였다.

HAProxy 구성도 변경된 Web 서비스 구조에 맞춰 완료하였다.

---

### 3.2 백서빈 - 인스턴스 구조 수정 및 한국표준시 설정

백서빈은 변경된 구성 방향에 맞춰 인스턴스 구조를 수정하고, 서버 시간을 한국표준시 기준으로 설정하였다.

| 작업 항목 | 진행 내용 | 상태 |
|---|---|---|
| 인스턴스 구조 수정 | 변경된 아키텍처 기준으로 인스턴스 구조 수정 | 완료 |
| 시간 설정 | 서버 시간대를 한국표준시 기준으로 수정 | 완료 |

한국표준시 설정은 로그 분석, 백업 파일 생성 시간, cron 실행 시간, 모니터링 이벤트 시각 확인의 일관성을 확보하기 위한 작업이다.

---

### 3.3 조민석 - 구조 변경 대응 Playbook 수정

조민석은 변경된 구조에 대응하여 기존 Ansible Playbook을 수정하였다.

| 작업 항목 | 진행 내용 | 상태 |
|---|---|---|
| 구조 변경 확인 | Docker Swarm, HAProxy, 인스턴스 구조 변경 내용 확인 | 완료 |
| Playbook 수정 | 변경된 구성에 맞춰 Ansible Playbook 수정 | 진행 |
| 자동화 정합성 보완 | 실제 구성과 Playbook 기준 일치 작업 | 진행 |

기존 Playbook은 이전 Web / Proxy / DB 구조를 기준으로 작성되었으므로, 변경된 Docker Swarm 및 HAProxy 구성에 맞춰 수정이 필요하다.

금일 작업에서는 구조 변경 사항을 반영하여 Playbook 수정 작업을 진행하였다.

---

### 3.4 박재우 - Monitoring Stack 설치 완료 및 설정 진행

박재우는 Prometheus와 주요 Exporter 설치를 완료하였고, Grafana 및 Alertmanager 설치까지 완료하였다.

| 작업 항목 | 진행 내용 | 상태 |
|---|---|---|
| Prometheus 설치 | 메트릭 수집 서버 설치 | 완료 |
| node_exporter 설치 | OS 메트릭 수집 Exporter 설치 | 완료 |
| cAdvisor 설치 | 컨테이너 메트릭 수집 Exporter 설치 | 완료 |
| mysqld_exporter 설치 | MariaDB 메트릭 수집 Exporter 설치 | 완료 |
| blackbox_exporter 설치 | HTTP / Endpoint 상태 점검 Exporter 설치 | 완료 |
| Grafana 설치 | 시각화 대시보드 도구 설치 | 완료 |
| Alertmanager 설치 | 알림 관리 도구 설치 | 완료 |
| Grafana 설정 | Dashboard 및 Data Source 설정 진행 | 진행 |
| Alertmanager 설정 | 알림 정책 및 연계 설정 진행 | 진행 |

금일 기준 Monitoring Stack의 핵심 구성 요소 설치는 완료되었으며, Grafana와 Alertmanager의 세부 설정은 진행 중이다.

---

### 3.5 정주헌 - Restic Backup / Recovery Test / 복구 시나리오 문서화

정주헌은 Restic을 설치하고 Web, DB, Proxy Node 대상 백업을 진행하였다.

또한 복구 테스트를 실시하고, 백업 스크립트와 복구 시나리오 문서화를 진행하였다.

| 작업 항목 | 진행 내용 | 상태 |
|---|---|---|
| Restic 설치 | Backup / Recovery 검증을 위한 Restic 설치 | 완료 |
| Web Node 백업 | Web Node 대상 백업 수행 | 완료 |
| DB Node 백업 | DB Node 대상 백업 수행 | 완료 |
| Proxy Node 백업 | Proxy Node 대상 백업 수행 | 완료 |
| 복구 테스트 | 백업 데이터를 이용한 복구 테스트 실시 | 완료 |
| 백업 스크립트 작성 | 백업 자동화 스크립트 작성 | 완료 |
| 모니터링 파트 제외 백업 스크립트 | Monitoring 파트 완료 전까지 제외 범위로 작성 | 완료 |
| Monitoring 파트 백업 추가 | Monitoring 작업 완료 후 추가 예정 | 예정 |
| 복구 시나리오 5종 구성 | 복구 검증 시나리오 5종 구성 | 완료 |
| 복구 시나리오 문서화 | 구성한 복구 시나리오 문서 작성 | 진행 |

현재 백업 스크립트는 Monitoring 파트를 제외한 범위까지 작성 완료되었으며, Monitoring 파트 작업이 완료되면 해당 영역의 백업 항목을 추가할 예정이다.

복구 시나리오는 5종으로 구성하였고, 현재 해당 내용을 문서로 작성 중이다.

---

## 4. 금일 결정 사항

| 번호 | 결정 내용 |
|---:|---|
| 1 | Web Node는 단일 노드 기반 Docker Swarm 구조로 재구성한 내용을 반영한다. |
| 2 | HAProxy 구성 완료 내용을 금일 작업으로 기록한다. |
| 3 | 인스턴스 구조 수정 및 한국표준시 설정 완료 내용을 기록한다. |
| 4 | 구조 변경에 따라 Ansible Playbook을 수정한다. |
| 5 | Prometheus, node_exporter, cAdvisor, mysqld_exporter, blackbox_exporter 설치 완료를 기록한다. |
| 6 | Grafana 및 Alertmanager 설치 완료를 기록한다. |
| 7 | Grafana와 Alertmanager 세부 설정은 진행 중으로 기록한다. |
| 8 | Restic 기반 Web / DB / Proxy Node 백업 및 복구 테스트 실시 결과를 기록한다. |
| 9 | 백업 스크립트는 Monitoring 파트 제외 범위까지 작성 완료한 것으로 기록한다. |
| 10 | Monitoring 파트 작업 완료 후 백업 스크립트에 Monitoring 백업 항목을 추가한다. |
| 11 | 복구 시나리오 5종 구성 완료 및 문서 작성 진행 상태를 기록한다. |

---

## 5. 이슈 및 대응

| 이슈 | 내용 | 대응 |
|---|---|---|
| 구조 변경 반영 필요 | Docker Swarm, HAProxy, 인스턴스 구조 변경으로 기존 문서와 Playbook 수정 필요 | architecture.md, resource-plan.md, Ansible Playbook 수정 |
| Monitoring 설정 미완료 | Grafana 및 Alertmanager 설치는 완료되었으나 세부 설정 진행 중 | Dashboard, Data Source, Alert Rule, Notification 설정 완료 예정 |
| Monitoring 백업 미반영 | Monitoring 파트 작업이 완료되지 않아 백업 스크립트에 아직 미반영 | Monitoring 구성 완료 후 백업 항목 추가 |
| 복구 문서화 진행 중 | 복구 시나리오 5종은 구성했으나 문서 작성 진행 중 | restore.md 또는 recovery-scenarios.md에 반영 |
| 시간 기준 불일치 가능성 | 서버 시간대가 다르면 로그, 백업, cron 시간 해석에 혼선 발생 | 한국표준시 기준으로 시간 설정 완료 |

---

## 6. 다음 작업 계획

| 담당자 | 다음 작업 |
|---|---|
| 이진욱 | Docker Swarm 및 HAProxy 구성 결과 캡처 정리, 서비스 상태 확인 자료 정리 |
| 백서빈 | 인스턴스 구조 변경 자료 및 KST 설정 캡처 정리 |
| 조민석 | 구조 변경 대응 Playbook 수정 완료, Playbook 실행 및 검증 |
| 박재우 | Grafana 및 Alertmanager 설정 완료, Dashboard / Alert Rule 검증 |
| 정주헌 | 복구 시나리오 문서 작성 완료, Monitoring 파트 백업 항목 추가 준비, 백업/복구 증빙 정리 |

---

## 7. 회의 결과 요약

2026년 6월 30일 회의에서는 29일 결정된 구조 변경 사항에 대한 실제 반영 진행 상황을 확인하였다.

이진욱은 Web Node를 단일 노드 기반 Docker Swarm Cluster 구조로 재구성하고 HAProxy 구성을 완료하였다.

백서빈은 변경된 아키텍처에 맞춰 인스턴스 구조를 수정하고, 서버 시간을 한국표준시 기준으로 수정하였다.

조민석은 구조 변경에 대응하여 Ansible Playbook 수정 작업을 진행하였다.

박재우는 Prometheus, node_exporter, cAdvisor, mysqld_exporter, blackbox_exporter 설치를 완료하였고, Grafana 및 Alertmanager 설치까지 완료하였다. 현재 Grafana와 Alertmanager 세부 설정을 진행 중이다.

정주헌은 Restic 설치 후 Web, DB, Proxy Node 백업을 진행하고 복구 테스트를 실시하였다. 또한 백업 스크립트를 작성하였으며, Monitoring 파트는 작업 완료 후 백업 항목에 추가할 예정이다.

복구 시나리오는 5종으로 구성하였고, 현재 해당 내용을 문서로 작성 중이다.
