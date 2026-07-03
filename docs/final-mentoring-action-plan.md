<!-- STATUS: CURRENT -->

# Final Mentoring Action Plan

## 1. 문서 목적

본 문서는 2026-07-02 멘토링 결과를 반영하여 남은 프로젝트 작업 방향을 정리한다.

---

## 2. 멘토링 결과 핵심

~~~text
3주차:
구현 마무리 작업

4주차:
가용성 테스트, 부하 테스트, 임계치 검증, DR 점검, 발표자료 준비
~~~

---

## 3. 3주차 작업 범위

3주차는 현재 구현 중인 기능을 마무리하는 단계이다.

| 영역 | 작업 |
|---|---|
| Ansible | site.yml, provision.yml, wait-ssh.yml, validate.yml 정리 및 문법 검증 |
| Service | Docker Swarm Playbook 적용 결과 정리 |
| DB | Primary - Replica 연동 상태 정리, Failover 테스트 진행 |
| Monitoring | Prometheus / Alertmanager / Python Alert Daemon 검증 |
| Backup | Restic Playbook 적용 결과 정리 |
| Recovery | 복구 시나리오 작성 |
| Documentation | README, current-status, architecture, automation-scope 최신화 |

---

## 4. 4주차 작업 범위

4주차는 운영 검증과 발표 준비 단계이다.

| 영역 | 작업 |
|---|---|
| Availability | 서비스 가용성 테스트 |
| Load Test | Web / Proxy / DB 부하 테스트 |
| Threshold | CPU, Memory, HTTP 상태, DB 상태 임계치 검증 |
| Alert | Prometheus Alert Rule 및 Alertmanager 알림 검증 |
| DR | 백업 / 복구 / Failover / 설정파일 복구 점검 |
| Presentation | 발표자료, 시연 순서, 캡처 정리 |

---

## 5. DB Failover 진행상황

| 항목 | 상태 |
|---|---|
| Primary - Replica 연동 | 완료 |
| Failover 테스트 | 진행 중 |
| Primary 장애 시 Replica 전환 검증 | 진행 중 |

멘토링 기준 설명:

~~~text
DB는 Primary - Replica 연동을 완료했고,
현재 Primary 장애 발생 시 Replica 전환이 가능한지 Failover 테스트를 진행 중입니다.
~~~

---

## 6. 최종 발표 핵심 메시지

~~~text
본 프로젝트는 OpenStack 기반 인프라 위에 Web, DB, Proxy, Monitoring, Backup / Recovery 구조를 구성하고,
Control Node에서 Ansible을 통해 서비스 구성 자동화와 운영 검증을 수행하는 시스템이다.

남은 기간에는 신규 기능 확장보다,
가용성 테스트, 부하 테스트, 장애 임계치 검증, DR 점검, 발표자료 준비에 집중한다.
~~~

---

## 8. 2026-07-03 진행상황 및 다음 주 역할 조정

| 영역 | 내용 | 상태 |
|---|---|---|
| Recovery | Restore 자동화 구현 완료 | 완료 |
| Recovery | Restore 자동화 검증 | 예정 |
| DB | DB 이중화 Failover 테스트 완료 | 완료 |
| DB | DB 복구 점검 완료 | 완료 |
| Infra | 다음 주 모니터링 파트 보조 | 예정 |
| Service | 다음 주 자동화 파트 보조 | 예정 |

### 8.1 다음 주 운영 방향

~~~text
다음 주에는 인프라 담당자와 서비스 담당자를 각각 모니터링 파트와 자동화 파트 보조로 투입한다.

4주차 주요 목표는 가용성 테스트, 부하 테스트, 장애 임계치 검증, DR 점검, 발표자료 준비이다.
~~~

### 8.2 발표 반영 문장

~~~text
DB는 Primary - Replica 기반 이중화 구성 이후 Failover 테스트와 복구 점검을 완료했습니다.

Restore 자동화는 구현을 완료했으며,
다음 단계로 실제 복구 검증을 진행할 예정입니다.

4주차에는 인프라와 서비스 담당자를 모니터링 / 자동화 파트 보조로 투입하여
가용성 테스트, 부하 테스트, 임계치 검증, DR 점검, 발표자료 준비에 집중합니다.
~~~
