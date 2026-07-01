<!-- STATUS: CURRENT -->

# Implementation Roadmap

## 1. 문서 목적

본 문서는 Team Dandelion 프로젝트의 구현 로드맵을 정리한다.

멘토링 및 최종 발표 기준으로 다음 내용을 명확히 구분한다.

```text
완료된 작업
진행 중인 작업
남은 기간 내 필수 보완 작업
확장 가능 작업
최종 제출 전 정리 작업
```

---

## 2. 프로젝트 최종 목표

```text
Control Node에서 Ansible Playbook을 실행하여
OpenStack 인스턴스 생성부터 서비스 구성, 모니터링, 백업 및 복구 검증까지 자동화한다.
```

---

## 3. 현재 구현 위치

현재 프로젝트는 다음 단계까지 진행되었다.

| 단계 | 내용 | 상태 |
|---|---|---|
| 1 | OpenStack 기반 인스턴스 구성 | 완료 |
| 2 | 인스턴스 구조 수정 및 시간대 설정 | 완료 |
| 3 | 생성된 인스턴스 대상 Ansible 구성 자동화 | 진행 / 일부 완료 |
| 4 | Docker Swarm 기반 Web 구성 | 완료 |
| 5 | HAProxy 구성 | 완료 |
| 6 | MariaDB 구성 및 Replica 검증 | 진행 |
| 7 | Monitoring Stack 설치 | 완료 |
| 8 | Grafana / Alertmanager 세부 설정 | 진행 |
| 9 | Restic 기반 Web / DB / Proxy 백업 | 완료 |
| 10 | 복구 테스트 및 복구 시나리오 5종 구성 | 테스트 실시 / 문서화 진행 |
| 11 | OpenStack Provisioning 자동화 | 보완 필요 |
| 12 | site.yml 통합 실행 및 최종 검증 | 예정 |

---

## 4. Phase 기준 로드맵

### 4.1 Phase 1 - 기본 인프라 및 서비스 구성

| 작업 | 상태 |
|---|---|
| OpenStack 인스턴스 구성 | 완료 |
| 네트워크 / 보안그룹 구성 | 완료 |
| SSH 접속 확인 | 완료 |
| Control Node 구성 | 완료 |
| 기본 Inventory 구성 | 완료 |
| Web / DB / Proxy 기본 구성 | 완료 |

### 4.2 Phase 2 - 운영 구성 확장

| 작업 | 상태 |
|---|---|
| Docker Swarm 기반 Web 구성 | 완료 |
| HAProxy 구성 | 완료 |
| MariaDB Replica 검증 | 진행 |
| Prometheus 설치 | 완료 |
| Exporter 설치 | 완료 |
| Grafana 설치 | 완료 |
| Alertmanager 설치 | 완료 |
| Restic 백업 구성 | 완료 |
| 복구 테스트 | 완료 |
| 복구 시나리오 문서화 | 진행 |

### 4.3 Phase 3 - 자동화 통합 및 검증

| 작업 | 상태 |
|---|---|
| 구조 변경 대응 Playbook 수정 | 진행 |
| Monitoring 세부 설정 | 진행 |
| Backup Playbook 검증 | 진행 |
| OpenStack Provisioning Playbook | 보완 필요 |
| wait-ssh.yml | 예정 |
| validate.yml | 예정 |
| site.yml 통합 실행 | 예정 |
| 멱등성 검증 | 예정 |
| 최종 문서 정리 | 진행 |

---

## 5. 남은 기간 작업 우선순위

| 우선순위 | 작업 | 이유 |
|---:|---|---|
| 1 | 최신 아키텍처 문서 정리 | 멘토링 기준점 확보 |
| 2 | 자동화 범위 문서 정리 | 주제 적합성 방어 |
| 3 | Provisioning Playbook 최소 구현 | “인스턴스 생성부터 자동화” 목표 증명 |
| 4 | 구조 변경 대응 Playbook 검증 | 실제 구현과 자동화 코드 일치 필요 |
| 5 | Grafana / Alertmanager 설정 완료 | 운영 최적화 증빙 |
| 6 | Restic 복구 시나리오 문서화 | 백업/복구 검증 완성 |
| 7 | Monitoring 백업 항목 추가 | 백업 범위 완성 |
| 8 | 최종 발표자료 최신화 | 발표 기준 통일 |
| 9 | 제출 패키지 정리 | 산출물 누락 방지 |
| 10 | GitHub README 정리 | 외부 검토 기준점 |

---

## 6. 필수 완료 범위

최종 제출 전 반드시 완료해야 하는 범위는 다음과 같다.

```text
1. 최신 아키텍처 문서
2. 자동화 범위 문서
3. Ansible 실행 구조 문서
4. Provisioning Playbook 최소 구현 또는 설계 문서
5. Docker Swarm / HAProxy 구성 증빙
6. Monitoring Stack 설치 및 target 확인 증빙
7. Restic 백업 및 복구 테스트 증빙
8. 복구 시나리오 5종 문서
9. 최종 발표자료
10. 회의록 / 작업일지
```

---

## 7. 최소 구현 기준

남은 기간을 고려할 때 Provisioning 자동화는 최소 범위로 구현한다.

```text
Security Group 생성
→ Instance 생성
→ Backup Volume 생성
→ Volume Attach
→ 생성 IP 확인
→ SSH Wait
→ Ansible Ping
```

이 범위까지 구현하면 다음 설명이 가능하다.

```text
Control Node에서 Ansible을 실행하여 OpenStack 리소스를 생성하고,
생성된 노드를 대상으로 서비스 구성과 운영 검증 자동화를 연결했습니다.
```

---

## 8. 확장 가능 범위

시간이 남을 경우 다음 작업을 확장한다.

| 확장 항목 | 설명 |
|---|---|
| Dynamic Inventory | OpenStack 인스턴스 정보를 자동 Inventory로 활용 |
| Full site.yml | provision부터 validate까지 통합 실행 |
| DB Replica 자동화 | MariaDB Replica 구성 자동화 고도화 |
| Grafana Provisioning | Dashboard / Data Source 코드화 |
| Alert Rule 자동화 | Prometheus Rule / Alertmanager 설정 자동화 |
| Monitoring 백업 | Grafana / Prometheus / Alertmanager 설정 백업 |
| 멱등성 검증 | Playbook 2회 실행 결과 비교 |

---

## 9. 리스크 및 대응

| 리스크 | 영향 | 대응 |
|---|---|---|
| Provisioning 자동화 실패 | 최종 목표 설명 약화 | 최소 구현 범위로 축소, 설계 문서로 방어 |
| 구조 변경으로 Playbook 불일치 | Ansible 기반성 약화 | 변경 구조 기준 Playbook 수정 |
| Monitoring 설정 미완료 | 운영 최적화 증빙 약화 | Target UP / 대표 Dashboard / Alert Rule 중심으로 정리 |
| DB Replica 검증 지연 | DB 이중화 완성도 약화 | 핵심 구현이 아닌 확장 검증 항목으로 분리 |
| 문서 간 기준 충돌 | 멘토링 혼선 | current-status.md 기준으로 통일 |
| 캡처 부족 | 발표 설득력 약화 | 검증 항목별 최소 캡처 목록 관리 |

---

## 10. 멘토링 설명 기준

```text
현재 프로젝트는 서비스 구성, 모니터링, 백업 및 복구 검증 자동화까지 상당 부분 구현했습니다.

최종 목표인 인스턴스 생성부터 자동화를 완성하기 위해 Provisioning Playbook을 최소 범위로 보완할 예정입니다.

남은 기간에는 기능을 무리하게 확장하기보다,
Provisioning 최소 구현, Playbook 검증, 복구 시나리오 문서화, 발표 증빙 정리에 집중하겠습니다.
```

---

## 11. 결론

본 프로젝트의 남은 구현 방향은 다음과 같다.

```text
기능 확장보다 자동화 흐름 완성
새 기술 추가보다 검증 증빙 강화
문서 분산보다 최신 기준 통일
수동 구축 설명보다 Ansible 실행 구조 강조
```

최종적으로 다음 흐름을 발표 기준으로 완성한다.

```text
OpenStack Provisioning
→ Ansible Configuration
→ Service Deployment
→ Monitoring
→ Backup
→ Recovery Validation
→ Operation Optimization
```
