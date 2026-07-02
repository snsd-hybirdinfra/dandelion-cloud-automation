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
