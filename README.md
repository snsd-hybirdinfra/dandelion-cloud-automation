<!-- STATUS: CURRENT -->

# Team Dandelion - Cloud Infrastructure Automation

## 1. 프로젝트 주제

```text
Ansible 기반 클라우드 인프라 자동화 및 운영 최적화 시스템 구축
```

---

## 2. 프로젝트 개요

본 프로젝트는 OpenStack 기반 클라우드 인프라 위에 Web, DB, Proxy, Monitoring, Backup / Recovery 구성 요소를 배치하고, Control Node에서 Ansible Playbook과 운영 스크립트를 실행하여 인프라 구성, 서비스 배포, 모니터링, 백업 및 복구 검증을 자동화하는 것을 목표로 한다.

최종 목표는 다음과 같다.

```text
Control Node에서 Ansible Playbook 실행
→ OpenStack 인스턴스 생성
→ 네트워크 / 보안그룹 / 볼륨 구성
→ Inventory 구성
→ 공통 환경 설정
→ 서비스 배포
→ 모니터링 구성
→ 백업 및 복구 검증
→ 운영 상태 검증
```

현재는 생성된 OpenStack 인스턴스를 기반으로 서비스 구성, 모니터링, 백업 및 복구 검증 자동화를 우선 구현하였으며, OpenStack Provisioning 자동화는 nsible/provision.yml 기준으로 최소 구현 범위를 관리하며, 실제 환경 값 반영 후 실행 검증한다.

---

## 3. 최신 기준 문서

멘토링 및 최종 발표 기준은 다음 문서를 우선 참조한다.

| 문서 | 목적 |
|---|---|
| [Current Status](docs/current-status.md) | 최신 프로젝트 진행 상태 |
| [Architecture](docs/architecture.md) | 최신 아키텍처 기준 |
| [Automation Scope](docs/automation-scope.md) | Ansible / OpenStack 자동화 범위 |
| [Ansible Execution Design](docs/ansible-execution-design.md) | Ansible 실행 구조와 site.yml 목표 |
| [Provisioning Playbook Design](docs/provisioning-playbook-design.md) | OpenStack 인스턴스 생성 자동화 설계 |
| [Implementation Roadmap](docs/implementation-roadmap.md) | 남은 구현 작업과 우선순위 |
| [Mentoring Brief](docs/mentoring-brief.md) | 멘토링 대비 요약 및 질문 |
| [Mentoring Questions](docs/mentoring-questions.md) | 멘토링 당일 확인 질문 |
| [Mentoring Explanation Script](docs/mentoring-explanation-script.md) | 멘토링 설명 스크립트 |
| [Mentoring Checklist](docs/mentoring-checklist.md) | 멘토링 전 최종 점검표 |
| [Runbook](docs/runbook.md) | 운영 실행 절차 |
| [Validation Plan](docs/validation-plan.md) | 검증 계획 |
| [Backup and Recovery Plan](docs/backup-recovery-plan.md) | 백업 및 복구 계획 |
| [Monitoring Plan](docs/monitoring-plan.md) | 모니터링 계획 |
| [Final Deliverables](docs/final-deliverables.md) | 최종 산출물 기준 |
| [Submission Package](docs/submission-package.md) | 제출 패키지 구성 기준 |
| [Document Cleanup Policy](docs/document-cleanup-policy.md) | 최신 문서와 과거 기록 구분 기준 |

---

## 4. 최신 아키텍처 요약

```text
Admin
→ Control Node
→ Ansible Playbook
→ OpenStack Managed Nodes
→ Web / DB / Proxy / Monitoring / Backup 구성
```

서비스 흐름은 다음과 같다.

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

## 5. 노드 구성

| 노드 | 역할 | 주요 구성 |
|---|---|---|
| Control Node | 중앙 관리 및 Ansible 실행 | Ansible, Inventory, Playbooks |
| Proxy Node | 외부 요청 전달 및 Proxy 처리 | HAProxy |
| Web Node | Web 서비스 실행 | Docker, Docker Swarm, WordPress |
| DB Node | 데이터베이스 서비스 | MariaDB, Replica 검증 |
| Monitoring Node | 운영 모니터링 | Prometheus, node_exporter, cAdvisor, mysqld_exporter, blackbox_exporter, Grafana, Alertmanager |
| Backup / Recovery Node | 백업 및 복구 검증 | Restic, Backup Scripts, Restore Test, Recovery Scenarios |

---

## 6. 자동화 범위

본 프로젝트의 자동화 범위는 다음과 같이 구분한다.

| 계층 | 설명 | 현재 상태 |
|---|---|---|
| Provisioning Automation | OpenStack 인스턴스, 네트워크, 보안그룹, 볼륨 생성 자동화 | 보완 필요 |
| Configuration Automation | 생성된 서버의 공통 설정 및 패키지 구성 | 진행 / 일부 완료 |
| Service Deployment Automation | Web, DB, Proxy 서비스 구성 | 진행 / 구조 변경 반영 중 |
| Monitoring Automation | Prometheus, Exporter, Grafana, Alertmanager 구성 | 설치 완료 / 설정 진행 |
| Backup Automation | Restic 기반 백업 구성 | Web / DB / Proxy 완료 |
| Recovery Validation | 복구 테스트 및 복구 시나리오 검증 | 테스트 실시 / 문서화 진행 |
| Operation Optimization | 운영 상태 검증 및 장애 대응 문서화 | 진행 중 |

---

## 7. 현재 완료 항목

| 분류 | 완료 내용 |
|---|---|
| Infrastructure | OpenStack 기반 인스턴스 구성 |
| Infrastructure | 인스턴스 구조 수정 |
| Infrastructure | 한국표준시 기준 시간 설정 |
| Web | 단일 Web Node 기반 Docker Swarm 재구성 |
| Proxy | HAProxy 구성 |
| Monitoring | Prometheus 설치 |
| Monitoring | node_exporter 설치 |
| Monitoring | cAdvisor 설치 |
| Monitoring | mysqld_exporter 설치 |
| Monitoring | blackbox_exporter 설치 |
| Monitoring | Grafana 설치 |
| Monitoring | Alertmanager 설치 |
| Backup | Restic 설치 |
| Backup | Web / DB / Proxy Node 백업 진행 |
| Recovery | 백업 데이터 기반 복구 테스트 실시 |
| Recovery | 복구 시나리오 5종 구성 |

---

## 8. 현재 진행 중 항목

| 분류 | 진행 내용 |
|---|---|
| Provisioning Automation | OpenStack 인스턴스 생성 자동화 Playbook 보완 |
| Ansible | 구조 변경 대응 Playbook 수정 및 검증 |
| Database | MariaDB Replica 이중화 검증 |
| Monitoring | Grafana 세부 설정 |
| Monitoring | Alertmanager 세부 설정 |
| Backup | Monitoring 파트 백업 항목 추가 |
| Recovery | 복구 시나리오 문서 작성 |
| Documentation | 최신 아키텍처 기준 문서 정리 |
| Presentation | 멘토링 및 최종 발표자료 반영 |

---

## 9. Ansible 실행 목표

최종 목표는 Control Node에서 다음 명령으로 전체 자동화 흐름을 실행하는 것이다.

```bash
ansible-playbook -i inventory.ini site.yml
```

권장 실행 구조는 다음과 같다.

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

현재는 생성된 인스턴스를 대상으로 구성 자동화와 운영 검증 자동화를 우선 구현하고 있으며, `provision.yml`을 통해 OpenStack 인스턴스 생성 자동화를 보완한다.

---

## 10. Backup / Recovery

백업 및 복구는 Restic을 기준으로 구성한다.

| 대상 | 내용 | 상태 |
|---|---|---|
| Web Node | Web 서비스 구성 및 파일 백업 | 완료 |
| DB Node | MariaDB 백업 | 완료 |
| Proxy Node | HAProxy 설정 백업 | 완료 |
| Monitoring Node | Prometheus / Grafana / Alertmanager 설정 백업 | 예정 |
| Recovery Test | 백업 데이터 기반 복구 테스트 | 실시 |
| Recovery Scenario | 복구 시나리오 5종 구성 | 완료 / 문서화 진행 |

---

## 11. Monitoring

Monitoring Stack은 다음 구성 요소를 기준으로 한다.

| 구성 요소 | 역할 | 상태 |
|---|---|---|
| Prometheus | 메트릭 수집 및 저장 | 설치 완료 |
| node_exporter | Host OS 메트릭 수집 | 설치 완료 |
| cAdvisor | Container 메트릭 수집 | 설치 완료 |
| mysqld_exporter | MariaDB 메트릭 수집 | 설치 완료 |
| blackbox_exporter | HTTP / Endpoint 상태 점검 | 설치 완료 |
| Grafana | Dashboard 시각화 | 설치 완료 / 설정 진행 |
| Alertmanager | 알림 관리 | 설치 완료 / 설정 진행 |

---

## 12. 디렉터리 구조

```text
dandelion-cloud-automation/
├── README.md
├── ansible/
│   ├── site.yml
│   ├── ansible.cfg
│   ├── inventory.ini
│   └── *.yml
├── docker/
├── docs/
├── presentation/
├── scripts/
│   ├── backup/
│   └── health-check/
├── screenshots/
├── submission/
│   ├── meeting-notes/
│   └── work-logs/
├── tools/
└── .github/workflows/
```

---

## 13. 평가 기준 대응

| 평가 항목 | 대응 방향 |
|---|---|
| 전문성 | OpenStack, Ansible, Docker Swarm, MariaDB, HAProxy, Prometheus, Grafana, Alertmanager, Restic 활용 |
| 차별성 | 구축 자동화뿐 아니라 모니터링, 백업, 복구 검증까지 운영 흐름으로 연결 |
| 완성도 | 서비스 구성, 모니터링 설치, 백업/복구 테스트, 복구 시나리오 문서화 |
| 프로젝트 관리 | GitHub 문서 구조, 회의록, 작업일지, 제출 패키지 관리 |
| 발표 및 시연 | Ansible 실행 구조, 서비스 응답, Prometheus Target, Restic Snapshot, Restore Test 중심 시연 |

---

## 14. 멘토링 설명 기준

멘토링 시 다음 문장을 기준으로 설명한다.

```text
현재 프로젝트는 OpenStack 기반 인프라 위에 Web, DB, Proxy, Monitoring, Backup / Recovery 구성 요소를 배치하고,
Control Node에서 Ansible을 통해 구성 자동화와 운영 검증 자동화를 수행하는 구조입니다.

현재까지는 생성된 인스턴스 기반으로 서비스 구성, 모니터링, 백업 및 복구 검증을 구현했습니다.

최종 목표는 OpenStack 인스턴스 생성부터 Ansible Playbook으로 연결하는 것이며,
이를 위해 Provisioning Playbook을 추가 보완 범위로 정리했습니다.
```

---

<<<<<<< HEAD
## 15. 구현 일정 기준

| 구분 | 목표 완료일 | 기준 |
|---|---|---|
| Phase 1 필수 구성 | 2026-06-26 | OpenStack, Ubuntu Instance, Control / Proxy / Web / DB / Backup Node, SSH, Ansible, Docker Compose, WordPress와 MariaDB, HAProxy HTTP Reverse Proxy, Health Check, Backup/Restore, 필수 캡처 완료 |
| Phase 2 운영 확장 | 2026-07-10 | HTTPS, Cinder Backup Volume, node_exporter, cAdvisor, Prometheus/Grafana, Playbook 개선 중 가능한 항목 |
| Phase 3 도전 확장 | 2026-07-10 이전 여유 시 | Web Node 2대, HAProxy Load Balancing, 공통 DB 연결 검증 |
| 최종 정리 | 2026-07-14 | 결과보고서, 시연 영상, 소스코드, 작업일지, 회의록, Google Drive 제출자료 정리 |

---

## 16. 프로젝트 핵심 메시지

~~~text
OpenStack 인프라 구성부터 Ansible 자동화, Proxy / Web / DB / Backup 계층 분리,
Docker Compose 기반 WordPress와 DB Node MariaDB 서비스 서비스 배포, HAProxy HTTP Reverse Proxy,
상태 점검, DB 및 파일 백업, 복구 절차 검증, GitHub 기반 산출물 관리까지
하나의 인프라 운영 자동화 흐름으로 연결한다.
~~~

<!-- AUTO_STATUS_START -->
## 자동 생성 프로젝트 상태

아래 상태는 팀원이 파일을 push할 때 자동으로 갱신된다.

## 2. 전체 진행률

| 완료 | 전체 | 진행률 |
|---:|---:|---:|
| 21 | 51 | 41% |

## 담당자별 진행 상태

| 영역 | 담당자 | 완료 | 전체 | 진행률 | 상태 |
|---|---|---:|---:|---:|---|
| PM / Architecture | 정주헌 | 11 | 12 | 92% | 🟡 진행 중 |
| Cloud Infrastructure | 백서빈 | 3 | 5 | 60% | 🟡 진행 중 |
| Server / Virtualization | 이진욱 | 1 | 5 | 20% | 🟡 진행 중 |
| Ansible Automation | 조민석 | 2 | 9 | 22% | 🟡 진행 중 |
| Monitoring / Backup / Validation | 박재우 | 0 | 9 | 0% | ❌ 미착수 |
| Submission Package | 정주헌 | 4 | 11 | 36% | 🟡 진행 중 |

상세 상태는 [Project Status](./docs/project-status.md) 문서에서 확인한다.

<!-- AUTO_STATUS_END -->




=======
## 15. 문서 기준
>>>>>>> 71122c9 (Add OpenStack provisioning and validation baseline playbooks)

과거 회의록, 작업일지, 날짜별 작업 문서에는 작성 당시 기준의 구조가 포함될 수 있다.

최신 기준은 다음 문서를 우선한다.

```text
docs/current-status.md
docs/architecture.md
docs/automation-scope.md
docs/ansible-execution-design.md
docs/provisioning-playbook-design.md
docs/mentoring-brief.md
```


