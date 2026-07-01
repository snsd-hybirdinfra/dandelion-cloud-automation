<!-- STATUS: CURRENT -->

# Presentation Outline

## 1. 발표 제목

```text
Ansible 기반 클라우드 인프라 자동화 및 운영 최적화 시스템 구축
```

---

## 2. 발표 핵심 메시지

본 프로젝트는 OpenStack 기반 클라우드 인프라 위에 Web, DB, Proxy, Monitoring, Backup / Recovery 구성 요소를 배치하고, Control Node에서 Ansible Playbook과 운영 스크립트를 실행하여 인프라 구성, 서비스 배포, 모니터링, 백업 및 복구 검증을 자동화하는 프로젝트이다.

최종 목표는 Control Node에서 Ansible Playbook을 실행하여 OpenStack 인스턴스 생성부터 서비스 구성, 모니터링, 백업 및 복구 검증까지 연결하는 것이다.

---

## 3. 발표 흐름

| 순서 | 슬라이드 | 핵심 내용 |
|---:|---|---|
| 1 | 프로젝트 개요 | 주제, 목표, 팀 역할 |
| 2 | 문제 정의 | 수동 인프라 구성과 운영 검증의 한계 |
| 3 | 최종 목표 | Control Node 기반 Ansible 통합 자동화 |
| 4 | 전체 아키텍처 | OpenStack, Control Node, Web, DB, Proxy, Monitoring, Backup |
| 5 | 자동화 범위 | Provisioning / Configuration / Operation 자동화 구분 |
| 6 | 인프라 구성 | 인스턴스 구조, 리소스, 시간대 설정 |
| 7 | Web / Proxy 구성 | Docker Swarm 기반 Web, HAProxy 구성 |
| 8 | DB 구성 | MariaDB 및 Replica 검증 방향 |
| 9 | Monitoring 구성 | Prometheus, Exporter, Grafana, Alertmanager |
| 10 | Backup / Recovery | Restic 백업, 복구 테스트, 복구 시나리오 5종 |
| 11 | Ansible Playbook 구조 | site.yml, provision.yml, common.yml, service playbooks |
| 12 | 검증 결과 | 서비스 응답, 모니터링 target, 백업 snapshot, 복구 테스트 |
| 13 | 이슈 및 해결 | 구조 변경, Playbook 수정, 시간대, 백업 범위 |
| 14 | 남은 작업 | Provisioning 자동화, 멱등성 검증, 문서화 |
| 15 | 결론 | 구축 자동화에서 운영 최적화까지 확장 |

---

## 4. 슬라이드별 상세 내용

### 4.1 프로젝트 개요

```text
Team Dandelion은 Ansible을 기반으로 OpenStack 클라우드 인프라 구성과 운영 자동화를 구현한다.
```

포함 내용:

- 프로젝트 주제
- 팀원 역할
- 전체 일정
- 최종 산출물

---

### 4.2 문제 정의

```text
수동 인프라 구성은 반복성이 낮고, 장애 발생 시 복구 절차가 사람에게 의존한다.
```

포함 내용:

- 인스턴스 생성 및 설정 반복 문제
- 서비스 구성 절차 불일치
- 모니터링 / 백업 / 복구 검증 누락 가능성
- 문서와 실제 환경 불일치 위험

---

### 4.3 최종 목표

```text
Control Node에서 Ansible Playbook을 실행하여
OpenStack 인스턴스 생성부터 서비스 구성, 모니터링, 백업 및 복구 검증까지 자동화한다.
```

포함 내용:

- Control Node 중심 구조
- Ansible 기반 자동화
- OpenStack Provisioning 자동화 목표
- Day-1 / Day-2 운영 자동화 구분

---

### 4.4 전체 아키텍처

```text
Admin
→ Control Node
→ Ansible
→ OpenStack Managed Nodes
→ Web / DB / Proxy / Monitoring / Backup
```

포함 내용:

- 노드 구성
- 서비스 흐름
- 운영 관리 흐름
- 최신 구조 기준

---

### 4.5 자동화 범위

```text
Provisioning Automation
→ Configuration Automation
→ Service Deployment Automation
→ Monitoring Automation
→ Backup Automation
→ Recovery Validation
```

포함 내용:

- 완료된 자동화 범위
- 진행 중인 자동화 범위
- 보완 예정인 Provisioning 자동화
- 멘토링 질문 포인트

---

### 4.6 인프라 구성

포함 내용:

- OpenStack 인스턴스 구성
- 노드별 스펙
- Cinder Volume
- Security Group
- 한국표준시 설정

---

### 4.7 Web / Proxy 구성

포함 내용:

- 단일 Web Node 위 Docker Swarm 구성
- WordPress 서비스
- HAProxy 구성
- Proxy 경유 서비스 접근

---

### 4.8 DB 구성

포함 내용:

- MariaDB 구성
- DB 접속 검증
- Replica 이중화 검증 진행
- DB 백업 대상

---

### 4.9 Monitoring 구성

포함 내용:

- Prometheus
- node_exporter
- cAdvisor
- mysqld_exporter
- blackbox_exporter
- Grafana
- Alertmanager
- target 상태 확인

---

### 4.10 Backup / Recovery 구성

포함 내용:

- Restic 설치
- Web Node 백업
- DB Node 백업
- Proxy Node 백업
- 복구 테스트
- 복구 시나리오 5종
- Monitoring 백업 추가 예정

---

### 4.11 Ansible Playbook 구조

최종 목표 Playbook 구조:

```text
site.yml
├── provision.yml
├── wait-ssh.yml
├── common.yml
├── docker-swarm.yml
├── database.yml
├── proxy.yml
├── monitoring.yml
├── backup.yml
└── validate.yml
```

포함 내용:

- 현재 완료된 Playbook
- 구조 변경 대응 수정 중인 Playbook
- provision.yml 보완 예정
- 전체 실행 흐름

---

### 4.12 검증 결과

포함 내용:

- Ansible ping
- Web 서비스 응답
- Proxy 경유 접속
- DB 상태
- Prometheus target
- Grafana Dashboard
- Restic snapshot
- 복구 테스트 결과

---

### 4.13 이슈 및 해결

| 이슈 | 대응 |
|---|---|
| 구조 변경 발생 | 최신 아키텍처 문서 기준으로 통일 |
| Web 구성 변경 | Docker Swarm 기반으로 재구성 |
| Monitoring 범위 확대 | Exporter / Grafana / Alertmanager 설치 |
| 백업 범위 변경 | Restic 기반 Web / DB / Proxy 백업 수행 |
| OpenStack Provisioning 미완성 | 최종 목표 보완 범위로 분리 |

---

### 4.14 남은 작업

| 우선순위 | 작업 |
|---:|---|
| 1 | OpenStack Provisioning Playbook 최소 구현 |
| 2 | 구조 변경 대응 Playbook 검증 |
| 3 | Grafana / Alertmanager 설정 완료 |
| 4 | DB Replica 검증 |
| 5 | Monitoring 파트 백업 추가 |
| 6 | 복구 시나리오 문서 작성 완료 |
| 7 | 최종 발표 캡처 정리 |

---

### 4.15 결론

```text
본 프로젝트는 단순 서버 구축이 아니라,
OpenStack 기반 인프라 위에서 Ansible을 활용해 구성 자동화, 서비스 배포, 모니터링, 백업 및 복구 검증까지 연결한 운영 최적화 프로젝트이다.
```

---

## 5. 발표 시 강조할 문장

```text
현재까지는 생성된 OpenStack 인스턴스 기반으로 서비스 구성, 모니터링, 백업 및 복구 검증 자동화를 구현했습니다.

최종 목표는 Control Node에서 Ansible Playbook을 실행하여 인스턴스 생성부터 서비스 구성까지 자동화하는 것입니다.

따라서 본 프로젝트는 Provisioning 자동화와 Operation 자동화를 연결하는 구조로 발전시키고 있습니다.
```

---

## 6. 멘토링 전 확인 항목

```text
1. 최신 architecture.md와 발표자료 내용이 일치하는가
2. automation-scope.md에서 완료 / 진행 / 예정 범위가 분리되어 있는가
3. current-status.md가 실제 구현 상태와 맞는가
4. resource-plan.md가 최신 노드 구성과 맞는가
5. OpenStack Provisioning 자동화가 보완 범위로 명확히 적혀 있는가
```
