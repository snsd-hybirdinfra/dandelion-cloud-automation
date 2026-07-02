# Meeting Notes - 2026-07-02

## 1. 회의 개요

| 항목 | 내용 |
|---|---|
| 일자 | 2026-07-02 |
| 구분 | 멘토링 실시 |
| 프로젝트 | Ansible 기반 클라우드 인프라 자동화 및 운영 최적화 시스템 구축 |
| 팀 | Team Dandelion |
| 목적 | 멘토링 결과 반영 및 3주차 / 4주차 작업 방향 정리 |

---

## 2. 멘토링 결과 요약

멘토링 결과, 남은 프로젝트 기간은 다음 방향으로 정리한다.

| 기간 | 작업 방향 |
|---|---|
| 3주차 | 구현 마무리 작업 |
| 4주차 | 가용성 테스트, 부하 테스트, 임계치 검증, DR 점검, 발표자료 준비 |

---

## 3. 3주차 작업 방향

3주차는 신규 기능 확장보다 현재 구현 중인 기능을 마무리하는 데 집중한다.

~~~text
- Ansible Playbook 정리 및 실행 검증
- Docker Swarm Playbook 적용 결과 정리
- Restic Playbook 적용 결과 정리
- DB Primary - Replica 구성 및 Failover 테스트 마무리
- Prometheus / Alertmanager / Python Alert Daemon 동작 검증
- Grafana 연동 준비 또는 진행
- 복구 시나리오 문서화
- GitHub 문서 기준 정리
~~~

---

## 4. 4주차 작업 방향

4주차는 구현 확장보다 운영 검증과 발표 준비에 집중한다.

~~~text
- 가용성 테스트
- 부하 테스트
- 장애 임계치 검증
- Prometheus Alert Rule 검증
- Alertmanager 알림 흐름 검증
- DB Failover 검증
- Restic 백업 / 복구 검증
- DR 점검
- 발표자료 준비
- 시연 흐름 정리
- 캡처 자료 정리
~~~

---

## 5. 담당자별 최신 진행상황

### 5.1 이진욱 - DB / Service

| 항목 | 상태 |
|---|---|
| DB Primary - Replica 연동 | 완료 |
| Failover 테스트 | 진행 중 |
| Primary 장애 시 Replica 전환 검증 | 진행 중 |

#### 멘토링 반영 내용

~~~text
DB 파트는 Primary - Replica 연동 완료 상태를 기준으로,
Primary 장애 발생 시 Replica로 전환되는 Failover 테스트를 계속 진행한다.

최종 발표에서는 DB 이중화 자체를 완료 범위로 설명하되,
자동 Failover는 테스트 결과에 따라 완료 또는 진행 중으로 구분한다.
~~~

---

## 6. 결정사항

| 번호 | 결정사항 |
|---:|---|
| 1 | 3주차는 구현 마무리 작업 중심으로 진행한다. |
| 2 | 4주차는 가용성 테스트, 부하 테스트, 임계치 검증, DR 점검, 발표자료 준비에 집중한다. |
| 3 | DB Failover 테스트는 이진욱 담당으로 계속 진행한다. |
| 4 | 신규 기능 추가보다 기존 구현의 검증 가능성과 발표 가능성을 우선한다. |

---

## 7. 후속 작업

| 담당 | 후속 작업 |
|---|---|
| 정주헌 | 멘토링 결과 문서화, 검증 시나리오 정리, 발표 흐름 정리 |
| 이진욱 | DB Failover 테스트 진행 및 결과 정리 |
| 백서빈 | 인프라 가용성 / 보안그룹 / DR 점검 자료 정리 |
| 조민석 | Docker Swarm / Restic Playbook 실행 결과 정리 |
| 박재우 | Prometheus / Alertmanager / Grafana 연동 및 임계치 검증 |

---

## 8. 멘토링 이후 핵심 방향

~~~text
남은 기간에는 기능을 더 벌리기보다,
현재 구현된 OpenStack, Ansible, Docker Swarm, MariaDB, Prometheus, Alertmanager, Restic 기반 구조를
검증 가능한 산출물로 정리한다.

3주차는 구현 마무리,
4주차는 가용성 테스트, 부하 테스트, 임계치 검증, DR 점검, 발표자료 준비에 집중한다.
~~~
