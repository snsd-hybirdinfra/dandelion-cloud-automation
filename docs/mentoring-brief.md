<!-- STATUS: CURRENT -->

# Mentoring Brief

## 1. 멘토링 목적

본 문서는 멘토링 대비를 위해 프로젝트의 최신 상태, 구조 변경 사항, 자동화 범위, 남은 이슈, 질문 사항을 정리한다.

---

## 2. 프로젝트 주제

```text
Ansible 기반 클라우드 인프라 자동화 및 운영 최적화 시스템 구축
```

---

## 3. 프로젝트 한 줄 요약

OpenStack 기반 클라우드 인프라 위에 Web, DB, Proxy, Monitoring, Backup / Recovery 구성 요소를 배치하고, Control Node에서 Ansible Playbook과 운영 스크립트를 통해 인스턴스 생성부터 서비스 구성, 모니터링, 백업 및 복구 검증까지 자동화하는 것을 목표로 하는 프로젝트이다.

---

## 4. 현재 구현 요약

| 영역 | 현재 상태 |
|---|---|
| Infrastructure | OpenStack 인스턴스 구성 및 구조 수정 완료 |
| Time Sync | 한국표준시 기준 시간 설정 완료 |
| Web | 단일 Web Node 위 Docker Swarm 기반 구성 완료 |
| Proxy | HAProxy 구성 완료 |
| DB | MariaDB Replica 기반 이중화 검증 진행 중 |
| Monitoring | Prometheus, Exporter, Grafana, Alertmanager 설치 완료 |
| Monitoring Config | Grafana / Alertmanager 세부 설정 진행 중 |
| Backup | Restic 기반 Web / DB / Proxy 백업 진행 |
| Recovery | 복구 테스트 실시 |
| Recovery Scenario | 복구 시나리오 5종 구성 및 문서 작성 중 |
| Ansible | 구조 변경 대응 Playbook 수정 및 검증 진행 중 |
| Provisioning | OpenStack 인스턴스 생성 자동화 보완 필요 |

---

## 5. 최신 구조

```text
Admin
→ Control Node
→ Ansible Playbook
→ OpenStack / Managed Nodes
→ Web / DB / Proxy / Monitoring / Backup 구성
```

서비스 흐름은 다음과 같이 정리한다.

```text
User
→ Proxy / HAProxy
→ Docker Swarm 기반 Web Service
→ MariaDB DB
```

운영 흐름은 다음과 같다.

```text
Monitoring
→ Prometheus / Exporter / Grafana / Alertmanager

Backup / Recovery
→ Restic
→ Web / DB / Proxy 백업
→ 복구 테스트
→ 복구 시나리오 문서화
```

---

## 6. 최근 구조 변경 사항

| 변경 전 | 변경 후 |
|---|---|
| Web1 / Web2 개별 구성 | 단일 Web Node 위 Docker Swarm 기반 구성 |
| Proxy Node 중심 Load Balancing | HAProxy 구성 및 Web 서비스 구조에 맞춘 Proxy 흐름 |
| 단일 DB Node | MariaDB Replica 이중화 검증 진행 |
| Prometheus 설치 예정 | Prometheus / Exporter / Grafana / Alertmanager 설치 완료 |
| backup.sh 중심 | Restic 기반 백업 및 복구 테스트 |
| 수동 검증 중심 | 복구 시나리오 5종 기반 검증 문서화 |

---

## 7. 현재 완료 항목

- OpenStack 기반 인스턴스 구성
- 인스턴스 구조 수정
- 한국표준시 설정
- Docker Swarm 기반 Web 구성
- HAProxy 구성
- Prometheus 설치
- node_exporter 설치
- cAdvisor 설치
- mysqld_exporter 설치
- blackbox_exporter 설치
- Grafana 설치
- Alertmanager 설치
- Restic 설치
- Web / DB / Proxy Node 백업
- 복구 테스트
- 복구 시나리오 5종 구성

---

## 8. 현재 진행 중 항목

- OpenStack Provisioning Playbook 보완
- 구조 변경 대응 Ansible Playbook 수정 및 검증
- DB Replica 이중화 검증
- Grafana Dashboard 설정
- Alertmanager 알림 설정
- Monitoring 파트 백업 항목 추가
- 복구 시나리오 문서 작성
- 최신 구조 기준 문서 정리
- 발표자료 반영

---

## 9. 멘토링 때 확인받을 질문

### 9.1 자동화 범위 질문

```text
현재는 생성된 인스턴스 기반의 구성 자동화와 운영 자동화를 먼저 구현했고,
최종 목표는 OpenStack 인스턴스 생성부터 Ansible로 자동화하는 것입니다.

남은 기간에 provision.yml을 최소 범위로 구현해도 주제 적합성이 충분한지 확인받고 싶습니다.
```

### 9.2 Docker Swarm 구성 질문

```text
Web Node를 단일 노드 기반 Docker Swarm 구조로 재구성했습니다.

학원 프로젝트 범위에서 단일 노드 Swarm을 서비스 배포 구조로 설명해도 적절한지,
또는 단순 Docker Compose 구조로 설명하는 편이 더 안전한지 확인받고 싶습니다.
```

### 9.3 DB Replica 질문

```text
DB Node를 MariaDB Replica 기반 이중화 방향으로 확장 중입니다.

최종 발표에서 Replica를 핵심 구현으로 가져갈지,
아니면 확장 구현 및 검증 항목으로 분리하는 편이 나은지 확인받고 싶습니다.
```

### 9.4 Monitoring 질문

```text
Prometheus, node_exporter, cAdvisor, mysqld_exporter, blackbox_exporter, Grafana, Alertmanager를 설치했습니다.

최종 제출 기준에서 Exporter별 대시보드와 알림 정책까지 모두 구성해야 하는지,
또는 target up / 기본 메트릭 / 대표 대시보드 정도로 정리해도 충분한지 확인받고 싶습니다.
```

### 9.5 Backup / Recovery 질문

```text
Restic 기반으로 Web / DB / Proxy Node 백업과 복구 테스트를 실시했습니다.
복구 시나리오는 5종으로 구성하고 문서화 중입니다.

최종 평가 기준에서 실제 복구 캡처와 restore 절차 문서 중 어느 쪽을 더 중점적으로 준비해야 하는지 확인받고 싶습니다.
```

---

## 10. 멘토링 설명 문장

멘토링 시작 시 다음 흐름으로 설명한다.

```text
현재 프로젝트는 OpenStack 위에 Web, DB, Proxy, Monitoring, Backup / Recovery 구성 요소를 배치하고,
Control Node에서 Ansible로 전체 구성과 운영 검증을 자동화하는 방향으로 진행하고 있습니다.

현재까지는 생성된 인스턴스 기반의 서비스 구성, 모니터링, 백업 및 복구 검증을 구현했습니다.

최종 목표는 인스턴스 생성부터 서비스 구성까지 Ansible Playbook으로 연결하는 것이며,
이를 위해 OpenStack Provisioning Playbook을 추가 보완 범위로 정리했습니다.

멘토링에서는 현재 구현 범위가 주제에 적합한지, 그리고 남은 기간 동안 Provisioning 자동화와 운영 검증 중 어느 쪽에 더 집중해야 하는지 확인받고 싶습니다.
```

---

## 11. 남은 작업 우선순위

| 우선순위 | 작업 |
|---:|---|
| 1 | 최신 아키텍처 문서 정리 |
| 2 | 자동화 범위 문서 정리 |
| 3 | OpenStack Provisioning Playbook 최소 구현 |
| 4 | Ansible Playbook 실행 검증 |
| 5 | Grafana / Alertmanager 설정 완료 |
| 6 | Restic 복구 시나리오 문서화 |
| 7 | Monitoring 파트 백업 항목 추가 |
| 8 | 발표자료 최신 구조 반영 |
| 9 | 최종 증빙 캡처 정리 |
| 10 | GitHub README 정리 |

---

## 12. 멘토링 결론 요청

멘토링에서 최종적으로 확인받을 사항은 다음과 같다.

```text
1. 현재 구조가 프로젝트 주제에 적합한지
2. OpenStack 인스턴스 생성 자동화가 필수인지, 최소 구현으로 충분한지
3. Docker Swarm / DB Replica / Monitoring Stack 범위가 과하지 않은지
4. 남은 기간 동안 기능 구현과 문서화 중 어디에 더 집중해야 하는지
5. 최종 발표에서 강조해야 할 핵심 평가 포인트가 무엇인지
```
