# Meeting Notes - 2026-07-01

## 1. 회의 개요

| 항목 | 내용 |
|---|---|
| 일자 | 2026-07-01 |
| 목적 | 2차 멘토링 대비 진행상황 정리 및 남은 작업 확인 |
| 프로젝트 | Ansible 기반 클라우드 인프라 자동화 및 운영 최적화 시스템 구축 |
| 팀 | Team Dandelion |

---

## 2. 회의 목적

본 회의는 2차 멘토링을 앞두고 각 담당자의 최신 작업 진행상황을 공유하고, 멘토링 시 설명할 완료 범위와 진행 중 범위를 정리하기 위해 진행하였다.

주요 확인 대상은 다음과 같다.

~~~text
- DB 이중화 및 Failover 검증 상태
- Cloud Infrastructure 보안그룹 및 장애대응 문서 상태
- Docker Swarm / Restic Ansible Playbook 적용 상태
- Prometheus / Alertmanager 기반 장애 알림 구현 상태
- 멘토링 대비 자료 및 검증 시나리오 작성 상태
~~~

---

## 3. 담당자별 진행상황

### 3.1 이진욱 - DB / Service

| 항목 | 상태 |
|---|---|
| DB 이중화 구성 | 완료 |
| Primary - Replica 연동 | 완료 |
| Primary 장애 시 Replica 전환 | 진행 중 |
| Failover 자동화 또는 전환 검증 | 진행 중 |

MariaDB 기반 DB 이중화 작업을 진행하였으며, Primary - Replica 간 연동 작업을 완료하였다.

현재는 Primary DB 장애 발생 시 Replica DB로 자동 전환하거나 서비스가 Replica로 연결될 수 있도록 Failover 처리 검증을 진행 중이다.

멘토링 설명 기준:

~~~text
DB는 MariaDB Primary - Replica 구조로 연동을 완료했습니다.
현재는 Primary 장애 발생 시 Replica로 전환되는 Failover 흐름을 검증하고 있습니다.
최종 발표에서는 DB 이중화를 핵심 구현 또는 확장 검증 항목으로 구분하여 설명할 예정입니다.
~~~

---

### 3.2 백서빈 - Cloud Infrastructure

| 항목 | 상태 |
|---|---|
| 장애대응 절차서 | 완료 |
| 보안그룹 수정 | 완료 |
| 인프라 접근 정책 정리 | 완료 |

OpenStack 기반 인프라 구성과 관련하여 장애대응 절차서 작성을 완료하였다.

또한 서비스 구성과 모니터링, DB, Proxy 접근 흐름에 맞춰 보안그룹 정책을 수정하였다.

멘토링 설명 기준:

~~~text
Cloud Infrastructure 파트에서는 장애대응 절차서를 작성했고,
서비스 접근과 운영 검증에 필요한 보안그룹 정책을 수정했습니다.
이를 통해 서비스 구성뿐 아니라 장애 발생 시 대응 절차까지 문서화했습니다.
~~~

---

### 3.3 조민석 - Ansible Automation

| 항목 | 상태 |
|---|---|
| Docker Swarm Playbook 작성 | 완료 |
| Docker Swarm Playbook 적용 | 완료 |
| Restic Playbook 작성 | 완료 |
| Restic Playbook 적용 | 완료 |

Web 서비스 구조 변경에 대응하여 Docker Swarm 기반 Playbook을 작성하고 적용하였다.

또한 Restic 기반 백업 자동화를 위한 Playbook을 작성하고 적용하였다.

이로써 Web 서비스 배포 자동화와 Backup 자동화 범위가 Ansible Playbook 기준으로 강화되었다.

멘토링 설명 기준:

~~~text
Ansible 파트에서는 Docker Swarm Playbook과 Restic Playbook을 작성하고 적용했습니다.
이를 통해 Web 서비스 구성 자동화와 백업 자동화 범위를 Playbook 기준으로 설명할 수 있게 되었습니다.
~~~

---

### 3.4 박재우 - Monitoring / Alerting

| 항목 | 상태 |
|---|---|
| Prometheus - Alertmanager 연동 | 완료 |
| Container 장애 감지 | 완료 |
| DB 장애 감지 | 완료 |
| WordPress 장애 감지 | 완료 |
| Python 기반 알림 수신 처리 | 완료 |
| Alert Daemon 구현 | 완료 |
| Prometheus - Grafana 연동 | 진행 예정 |

Prometheus와 Alertmanager 연동 작업을 완료하였다.

Container, DB, WordPress 장애 발생 시 Python 기반 수신 처리 로직을 통해 알림을 받아 Alert Daemon으로 처리하는 구조를 구현하였다.

Prometheus와 Grafana 연동 작업은 이후 진행 예정이다.

멘토링 설명 기준:

~~~text
Monitoring 파트에서는 Prometheus와 Alertmanager를 연동했고,
Container, DB, WordPress 장애를 Python 기반 알림 처리 로직으로 받아 Alert Daemon으로 구현했습니다.
Grafana 연동은 다음 단계로 진행할 예정입니다.
~~~

---

### 3.5 정주헌 - PM / Validation / Documentation

| 항목 | 상태 |
|---|---|
| 멘토링 대비 자료 준비 | 진행 중 |
| GitHub 문서 기준 정리 | 진행 중 |
| 검증 시나리오 작성 | 진행 중 |
| 최신 진행상황 문서화 | 진행 중 |
| 멘토링 질문 정리 | 진행 중 |

2차 멘토링을 대비하여 GitHub 문서 구조를 정리하고, 최신 아키텍처 기준과 자동화 범위, 멘토링 질문을 정리하고 있다.

또한 Backup / Recovery 및 운영 검증 시나리오를 작성하고 있으며, 각 담당자의 최신 진행상황을 회의록과 작업일지에 반영하고 있다.

멘토링 설명 기준:

~~~text
PM / Validation 파트에서는 멘토링 대비 자료와 검증 시나리오를 작성 중입니다.
현재 완료된 구현 범위와 진행 중인 보완 범위를 문서로 분리하여 멘토링 시 설명할 수 있도록 정리하고 있습니다.
~~~

---

## 4. 주요 결정사항

| 번호 | 결정사항 |
|---:|---|
| 1 | DB는 Primary - Replica 연동 완료로 정리하고, Failover 자동화는 진행 중으로 표기한다. |
| 2 | Docker Swarm Playbook과 Restic Playbook은 작성 및 적용 완료로 정리한다. |
| 3 | Prometheus - Alertmanager 연동 및 장애 알림 Daemon 구현은 완료로 정리한다. |
| 4 | Prometheus - Grafana 연동은 진행 예정으로 분리한다. |
| 5 | 멘토링 시 완료 범위와 진행 중 범위를 명확히 구분하여 설명한다. |

---

## 5. 현재 완료 범위 요약

~~~text
- DB Primary - Replica 연동 완료
- 장애대응 절차서 작성 완료
- 보안그룹 수정 완료
- Docker Swarm Playbook 작성 및 적용 완료
- Restic Playbook 작성 및 적용 완료
- Prometheus - Alertmanager 연동 완료
- Container / DB / WordPress 장애 알림 처리 구현 완료
~~~

---

## 6. 진행 중 / 예정 범위 요약

~~~text
- Primary 장애 시 Replica 전환 자동화 또는 Failover 검증 진행 중
- Prometheus - Grafana 연동 진행 예정
- 멘토링 대비 자료 준비 진행 중
- 검증 시나리오 작성 진행 중
- 최신 문서 정리 진행 중
~~~

---

## 7. 멘토링 핵심 설명 문장

~~~text
현재 프로젝트는 OpenStack 기반 인프라 위에 Web, DB, Proxy, Monitoring, Backup / Recovery 구조를 구성하고,
Control Node에서 Ansible을 통해 서비스 구성과 운영 검증을 자동화하는 방향으로 진행 중입니다.

최근에는 DB Primary - Replica 연동, Docker Swarm Playbook 적용, Restic Playbook 적용,
Prometheus - Alertmanager 기반 장애 알림 구현까지 진행되었습니다.

남은 작업은 DB Failover 검증, Grafana 연동, Provisioning 자동화 검증, 복구 시나리오 문서화입니다.
~~~

---

## 8. 후속 작업

| 담당 | 후속 작업 |
|---|---|
| 이진욱 | Primary 장애 시 Replica 전환 검증 |
| 백서빈 | 장애대응 절차서 및 보안그룹 변경 내용 증빙 정리 |
| 조민석 | Docker Swarm / Restic Playbook 실행 결과 캡처 정리 |
| 박재우 | Prometheus - Grafana 연동 및 Dashboard 구성 |
| 정주헌 | 멘토링 자료 정리, 검증 시나리오 작성, 진행상황 문서화 |
