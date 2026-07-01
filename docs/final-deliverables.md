<!-- STATUS: CURRENT -->

# Final Deliverables

## 1. 문서 목적

본 문서는 Team Dandelion 프로젝트의 최종 산출물을 정의한다.

최종 제출물은 단순 구현 결과가 아니라 다음 항목을 함께 증명해야 한다.

```text
구현 결과
자동화 범위
운영 검증
백업 / 복구
문서화
발표 가능성
```

---

## 2. 최종 산출물 분류

| 분류 | 산출물 |
|---|---|
| Repository | GitHub 저장소 |
| Documentation | README, Architecture, Automation Scope, Runbook |
| Ansible | Inventory, Playbooks, Provisioning Design |
| Infrastructure | OpenStack 인스턴스 구성 자료 |
| Service | Web / DB / Proxy 구성 자료 |
| Monitoring | Prometheus / Exporter / Grafana / Alertmanager 자료 |
| Backup / Recovery | Restic 백업, 복구 테스트, 복구 시나리오 |
| Validation | 검증 체크리스트, 결과 캡처 |
| Submission | 회의록, 작업일지, 결과보고서, 발표자료 |

---

## 3. 필수 문서 산출물

| 문서 | 목적 | 상태 |
|---|---|---|
| README.md | 저장소 메인 설명 | 최신 기준 반영 |
| docs/current-status.md | 최신 진행 상태 | 작성 |
| docs/architecture.md | 최신 아키텍처 | 작성 |
| docs/resource-plan.md | 노드 스펙 및 리소스 | 작성 |
| docs/automation-scope.md | 자동화 범위 정의 | 작성 |
| docs/ansible-execution-design.md | Ansible 실행 구조 | 작성 |
| docs/provisioning-playbook-design.md | OpenStack Provisioning 설계 | 작성 |
| docs/runbook.md | 실행 절차 | 작성 |
| docs/pre-run-checklist.md | 실행 전 점검 | 작성 |
| docs/validation-plan.md | 검증 계획 | 작성 |
| docs/backup-recovery-plan.md | 백업 / 복구 계획 | 작성 |
| docs/monitoring-plan.md | 모니터링 계획 | 작성 |
| docs/implementation-roadmap.md | 남은 작업 계획 | 작성 |
| docs/mentoring-brief.md | 멘토링 대비 요약 | 작성 |
| docs/document-cleanup-policy.md | 문서 정리 기준 | 작성 |

---

## 4. Ansible 산출물

| 산출물 | 설명 | 상태 |
|---|---|---|
| ansible.cfg | Ansible 실행 설정 | 필요 |
| inventory.ini | 관리 대상 노드 정의 | 필요 |
| site.yml | 통합 실행 Playbook | 필요 |
| provision.yml | OpenStack 인스턴스 생성 자동화 | 보완 필요 |
| wait-ssh.yml | SSH 접속 대기 | 예정 |
| common.yml | 공통 환경 설정 | 필요 |
| docker-swarm.yml | Docker Swarm 기반 Web 구성 | 필요 |
| database.yml | MariaDB / Replica 구성 | 필요 |
| proxy.yml | HAProxy 구성 | 필요 |
| monitoring.yml | Monitoring Stack 구성 | 필요 |
| backup.yml | Restic 백업 구성 | 필요 |
| validate.yml | 운영 검증 | 예정 |

---

## 5. 구현 증빙 산출물

| 영역 | 증빙 |
|---|---|
| Infrastructure | OpenStack 인스턴스 목록, IP, 보안그룹, 볼륨 캡처 |
| Timezone | KST 설정 확인 캡처 |
| Ansible | ansible ping, playbook syntax-check, playbook 실행 결과 |
| Web | Docker Swarm 상태, Web 응답 캡처 |
| Proxy | HAProxy 상태, Proxy 경유 응답 캡처 |
| DB | MariaDB 상태, DB 접속, Replica 검증 캡처 |
| Monitoring | Prometheus target, Grafana dashboard, Alertmanager 화면 |
| Backup | Restic snapshots, 백업 스크립트 실행 결과 |
| Recovery | 복구 테스트 전/후 결과, 복구 시나리오 문서 |
| GitHub | commit log, 문서 구조, README |

---

## 6. Backup / Recovery 산출물

| 산출물 | 설명 | 상태 |
|---|---|---|
| Restic 설치 증빙 | Restic version 출력 | 완료 필요 |
| Web 백업 결과 | Web Node 백업 snapshot | 완료 |
| DB 백업 결과 | DB dump 또는 snapshot | 완료 |
| Proxy 백업 결과 | HAProxy 설정 백업 | 완료 |
| Monitoring 백업 결과 | Prometheus / Grafana / Alertmanager 설정 백업 | 예정 |
| 복구 테스트 결과 | Restore Test 결과 | 완료 |
| 복구 시나리오 5종 | Web / DB / Proxy / Repository / Composite Recovery | 문서화 진행 |

---

## 7. Monitoring 산출물

| 산출물 | 설명 | 상태 |
|---|---|---|
| Prometheus 설치 증빙 | Prometheus UI / systemd 상태 | 완료 |
| node_exporter | Target UP | 완료 |
| cAdvisor | Target UP | 완료 |
| mysqld_exporter | Target UP | 완료 |
| blackbox_exporter | Target UP | 완료 |
| Grafana | Dashboard / Data Source | 설정 진행 |
| Alertmanager | Alert Rule / Receiver | 설정 진행 |

---

## 8. 제출 패키지 구성

최종 제출 패키지는 다음 구조를 기준으로 한다.

```text
submission/
├── meeting-notes/
├── work-logs/
├── screenshots/
├── final-report/
└── presentation/
```

권장 제출 항목:

```text
1. 최종 결과보고서 PDF
2. 최종 발표자료 PDF/PPT
3. GitHub 저장소 링크
4. 주요 캡처 자료
5. 회의록
6. 작업일지
7. 검증 결과 요약
8. 백업 / 복구 시나리오 문서
```

---

## 9. 최종 발표에서 보여줄 핵심 증빙

| 순서 | 증빙 | 목적 |
|---:|---|---|
| 1 | 전체 아키텍처 | 구조 이해 |
| 2 | Ansible 실행 구조 | 자동화 증명 |
| 3 | Provisioning 설계 또는 실행 | 인스턴스 생성 자동화 목표 증명 |
| 4 | Docker Swarm / HAProxy | 서비스 구성 증명 |
| 5 | Prometheus Target | 모니터링 증명 |
| 6 | Grafana Dashboard | 운영 시각화 증명 |
| 7 | Restic Snapshot | 백업 증명 |
| 8 | Restore Test | 복구 검증 증명 |
| 9 | 복구 시나리오 5종 | 운영 대응력 증명 |
| 10 | GitHub 문서 구조 | 프로젝트 관리 증명 |

---

## 10. 완료 기준

최종 산출물 완료 기준은 다음과 같다.

```text
1. README에서 최신 기준 문서로 이동 가능
2. architecture.md와 presentation-outline.md 내용 일치
3. automation-scope.md에서 완료 / 진행 / 예정 범위 구분
4. ansible-execution-design.md에서 site.yml 목표 구조 설명 가능
5. backup-recovery-plan.md에서 복구 시나리오 5종 설명 가능
6. monitoring-plan.md에서 Exporter별 역할 설명 가능
7. implementation-roadmap.md에서 남은 작업 방어 가능
8. 회의록 / 작업일지 누락 없음
9. 캡처 자료와 문서 내용 일치
10. 발표자가 질문에 대해 문서 기준으로 답변 가능
```

---

## 11. 결론

최종 산출물은 다음 메시지를 증명해야 한다.

```text
Team Dandelion은 OpenStack 기반 클라우드 인프라 위에서
Ansible을 통해 구성 자동화와 운영 자동화를 구현하고,
Prometheus / Grafana 기반 모니터링,
Restic 기반 백업 및 복구 검증,
복구 시나리오 기반 운영 대응 체계를 구축하였다.
```
