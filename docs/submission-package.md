<!-- STATUS: CURRENT -->

# Submission Package

## 1. 문서 목적

본 문서는 최종 제출 패키지 구성 기준을 정의한다.

제출 패키지는 구현 결과뿐 아니라 프로젝트 진행 과정, 역할 분담, 검증 결과, 백업/복구 절차, 발표자료를 함께 포함해야 한다.

---

## 2. 제출 패키지 목표

```text
멘토와 평가자가 GitHub 저장소와 제출자료만 보고
프로젝트 목표, 구현 구조, 자동화 범위, 검증 결과를 이해할 수 있도록 구성한다.
```

---

## 3. 제출 패키지 권장 구조

```text
submission/
├── meeting-notes/
├── work-logs/
├── screenshots/
│   ├── infrastructure/
│   ├── ansible/
│   ├── web-proxy/
│   ├── database/
│   ├── monitoring/
│   └── backup-recovery/
├── final-report/
└── presentation/
```

---

## 4. 제출 문서 목록

| 문서 | 설명 | 위치 |
|---|---|---|
| 최종 결과보고서 | 프로젝트 전체 결과 정리 | submission/final-report/ |
| 발표자료 | 최종 발표 PPT/PDF | submission/presentation/ |
| 회의록 | 날짜별 회의 내용 | submission/meeting-notes/ |
| 작업일지 | 날짜별 작업 내용 | submission/work-logs/ |
| 검증 결과 요약 | 주요 검증 결과 | docs/validation-plan.md 또는 별도 요약 |
| 백업 / 복구 문서 | Restic 백업 및 복구 시나리오 | docs/backup-recovery-plan.md |
| 모니터링 문서 | Prometheus / Grafana / Alertmanager | docs/monitoring-plan.md |
| 자동화 범위 문서 | Ansible / OpenStack 자동화 범위 | docs/automation-scope.md |

---

## 5. 캡처 자료 분류

### 5.1 Infrastructure

```text
- OpenStack 인스턴스 목록
- 네트워크 / 보안그룹
- Floating IP
- Cinder Volume
- KST 시간 설정
```

### 5.2 Ansible

```text
- ansible --version
- ansible-inventory --list
- ansible all -m ping
- playbook syntax-check
- playbook 실행 결과
```

### 5.3 Web / Proxy

```text
- Docker Swarm 상태
- docker service ls
- Web 서비스 응답
- HAProxy 상태
- Proxy 경유 접속 결과
```

### 5.4 Database

```text
- MariaDB 상태
- DB 접속 결과
- WordPress DB 연동
- Replica 상태 확인
```

### 5.5 Monitoring

```text
- Prometheus Target
- node_exporter UP
- cAdvisor UP
- mysqld_exporter UP
- blackbox_exporter UP
- Grafana Dashboard
- Alertmanager 화면
```

### 5.6 Backup / Recovery

```text
- Restic version
- restic snapshots
- 백업 스크립트 실행 결과
- 복구 테스트 결과
- 복구 전 / 후 서비스 상태
- 복구 시나리오 5종 문서
```

---

## 6. 최종 결과보고서 구성

권장 결과보고서 목차는 다음과 같다.

```text
1. 프로젝트 개요
2. 주제 및 목표
3. 팀원 역할
4. 전체 아키텍처
5. 인프라 구성
6. Ansible 자동화 구조
7. Web / Proxy / DB 구성
8. Monitoring 구성
9. Backup / Recovery 구성
10. 검증 결과
11. 장애 대응 및 복구 시나리오
12. 이슈 및 해결
13. 한계 및 개선 방향
14. 결론
```

---

## 7. 발표자료 구성

발표자료는 다음 흐름을 기준으로 한다.

```text
문제 정의
→ 목표
→ 아키텍처
→ 자동화 범위
→ 구현 결과
→ 운영 검증
→ 백업 / 복구
→ 남은 보완점
→ 결론
```

---

## 8. 제출 전 점검표

| 점검 항목 | 기준 |
|---|---|
| README 최신화 | 최신 기준 문서 링크 포함 |
| Architecture 최신화 | 현재 구조와 일치 |
| Automation Scope | 완료 / 진행 / 예정 구분 |
| Runbook | 실행 절차 포함 |
| Validation Plan | 검증 항목 포함 |
| Backup / Recovery | 복구 시나리오 5종 포함 |
| Monitoring | Exporter / Grafana / Alertmanager 포함 |
| Meeting Notes | 주요 회의일 기록 |
| Work Logs | 주요 작업일 기록 |
| Screenshots | 영역별 캡처 정리 |
| Presentation | 최신 구조 반영 |

---

## 9. 멘토링 전 임시 제출 기준

멘토링 전에는 최종 완성본이 아니어도 다음 기준을 충족하면 된다.

```text
1. 최신 기준 문서가 존재한다.
2. 현재 완료 / 진행 / 예정 범위가 구분되어 있다.
3. 최종 목표가 명확하다.
4. Provisioning 자동화가 보완 범위로 분리되어 있다.
5. 백업 / 복구 / 모니터링 증빙 방향이 정리되어 있다.
6. 남은 기간 로드맵이 있다.
```

---

## 10. 결론

제출 패키지는 단순 파일 모음이 아니라 프로젝트 설명 구조여야 한다.

최종 제출자료는 다음 질문에 답할 수 있어야 한다.

```text
무엇을 만들었는가?
왜 만들었는가?
어떻게 자동화했는가?
어떻게 검증했는가?
장애가 나면 어떻게 복구하는가?
남은 한계와 개선 방향은 무엇인가?
```
