<!-- STATUS: CURRENT -->

# Mentoring Checklist

## 1. 문서 목적

본 문서는 멘토링 전 최종 점검표이다.

멘토링 전에는 모든 기능을 완성하는 것보다,
현재 상태를 정확히 설명하고 남은 작업을 명확히 제시하는 것이 중요하다.

---

## 2. GitHub 첫 화면 점검

| 점검 항목 | 기준 | 상태 |
|---|---|---|
| README 최신화 | 최신 구조 기준으로 작성 | 확인 필요 |
| 오래된 Docker Compose 설명 제거 | 최신 Web 구조와 충돌 없어야 함 | 확인 필요 |
| Web1 / Web2 / Round Robin 제거 | 과거 구조는 README에서 제거 | 확인 필요 |
| Docker Swarm Out of Scope 제거 | 최신 구조와 충돌 없어야 함 | 확인 필요 |
| 최신 문서 링크 | current-status, architecture, automation-scope 포함 | 확인 필요 |
| 멘토링 문서 링크 | mentoring-brief, mentoring-questions 포함 | 확인 필요 |

---

## 3. Ansible 점검

| 점검 항목 | 명령 / 기준 | 상태 |
|---|---|---|
| requirements.yml 존재 | community.general, openstack.cloud 포함 | 확인 필요 |
| site.yml 템플릿 제거 | nginx / web-test 제거 | 확인 필요 |
| provision.yml 존재 | OpenStack 최소 생성 골격 | 확인 필요 |
| wait-ssh.yml 존재 | SSH 대기 및 ping 확인 | 확인 필요 |
| validate.yml 존재 | Web / Proxy / DB / Monitoring / Backup 검증 | 확인 필요 |
| syntax-check | Ansible 문법 검사 | 확인 필요 |

권장 명령:

```bash
cd ~/dandelion-cloud-automation/ansible

ansible-galaxy collection install -r requirements.yml

ansible-playbook provision.yml --syntax-check
ansible-playbook -i inventory.ini wait-ssh.yml --syntax-check
ansible-playbook -i inventory.ini site.yml --syntax-check
ansible-playbook -i inventory.ini validate.yml --syntax-check
```

---

## 4. 최신 문서 점검

| 문서 | 점검 기준 | 상태 |
|---|---|---|
| docs/current-status.md | 완료 / 진행 / 예정 구분 | 확인 필요 |
| docs/architecture.md | 최신 노드 구조 반영 | 확인 필요 |
| docs/automation-scope.md | Provisioning / Configuration / Operation 구분 | 확인 필요 |
| docs/ansible-execution-design.md | site.yml 목표 구조 설명 | 확인 필요 |
| docs/provisioning-playbook-design.md | OpenStack 생성 자동화 설계 | 확인 필요 |
| docs/backup-recovery-plan.md | Restic / 복구 시나리오 5종 | 확인 필요 |
| docs/monitoring-plan.md | Prometheus / Grafana / Alertmanager | 확인 필요 |
| docs/mentoring-questions.md | 질문 정리 | 확인 필요 |
| docs/mentoring-explanation-script.md | 설명 스크립트 | 확인 필요 |

---

## 5. 구현 증빙 점검

| 영역 | 최소 증빙 |
|---|---|
| OpenStack | 인스턴스 목록, 보안그룹, 볼륨 |
| Ansible | ping, syntax-check, playbook 실행 결과 |
| Web | Docker / Swarm 상태, Web 응답 |
| Proxy | HAProxy 상태, Proxy 경유 응답 |
| DB | MariaDB 상태, DB 접속, Replica 검증 |
| Monitoring | Prometheus Target, Grafana, Alertmanager |
| Backup | Restic snapshots |
| Recovery | 복구 테스트 전/후 결과 |
| Documentation | README, Architecture, Runbook, Recovery Plan |

---

## 6. 멘토링에서 피해야 할 표현

| 피해야 할 표현 | 대체 표현 |
|---|---|
| 다 끝났습니다 | 현재 완료 범위와 보완 범위를 분리했습니다 |
| 인스턴스 생성도 완전 자동화입니다 | Provisioning 최소 구현 골격을 작성했고 실행 검증 중입니다 |
| DB 이중화 완료입니다 | MariaDB Replica 검증 진행 중입니다 |
| Alert까지 다 됩니다 | Alertmanager 설치 후 세부 설정 진행 중입니다 |
| 전체 site.yml 한 번에 됩니다 | 최종 목표는 통합 실행이며 현재는 baseline과 개별 Playbook 검증 중입니다 |

---

## 7. 멘토링 핵심 답변

```text
현재 프로젝트는 생성된 OpenStack 인스턴스를 대상으로
서비스 구성, 모니터링, 백업 및 복구 검증 자동화를 우선 구현했습니다.

최종 목표는 Control Node에서 Ansible Playbook을 실행하여
OpenStack 인스턴스 생성부터 서비스 구성까지 연결하는 것입니다.

이를 위해 provision.yml, wait-ssh.yml, validate.yml을 추가했고,
남은 기간에는 Provisioning 최소 구현 검증과 운영 증빙 정리에 집중할 예정입니다.
```

---

## 8. 멘토링 전 최종 명령

```powershell
$repo = "C:\Users\swfco\OneDrive\바탕 화면\github\dandelion-cloud-automation"
cd $repo

git status

Select-String -Path "$repo\README.md" -Pattern "Docker Compose|Web1|Web2|Round Robin|HAProxy RR|Docker Swarm.*Out of Scope|Nginx|A급|B급|C급"

Select-String -Path "$repo\ansible\site.yml" -Pattern "nginx|web-test|STATUS: TEMPLATE|TEMP"

Select-String -Path "$repo\README.md","$repo\docs\current-status.md","$repo\docs\architecture.md" -Pattern "Control Node|Ansible|OpenStack|Provisioning|Docker Swarm|HAProxy|MariaDB|Prometheus|Grafana|Alertmanager|Restic"
```

위 오래된 표현 검색에서 결과가 없어야 한다.

---

## 9. 결론

멘토링 전 최종 기준은 다음과 같다.

```text
README는 최신 구조 기준
docs는 current 문서 기준
ansible은 site.yml / provision.yml / wait-ssh.yml / validate.yml 기준
과거 회의록과 작업일지는 작성 당시 기록으로 보존
멘토링 질문은 mentoring-questions.md 기준
설명 흐름은 mentoring-explanation-script.md 기준
```
