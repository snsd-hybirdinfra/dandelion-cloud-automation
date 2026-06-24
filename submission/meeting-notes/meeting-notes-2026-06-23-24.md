<!-- STATUS: COMPLETE -->

# Team Dandelion 회의록

## 2026-06-23~2026-06-24 통합 회의록

## 1. 회의 정보

| 구분 | 내용 |
|---|---|
| 회의 일자 | 2026-06-23 ~ 2026-06-24 |
| 회의 구분 | Phase 1 서비스 구성 진행 및 DB / Web / Proxy / Monitoring 검증 준비 |
| 회의 장소 | ZEP 팀 회의실 / Discord |
| 작성자 | 정주헌 |
| 참석자 | 백서빈, 이진욱, 조민석, 박재우 |
| 비고 | 작성자는 2026-06-23 회의에 직접 참석하지 못했으며, 2026-06-24에 팀원별 공유 내용을 기준으로 진행 상황을 취합하였다. |

---

## 2. 회의 목적

- 2026-06-23 진행 내용과 2026-06-24 추가 진행 내용을 통합 정리
- DB Node 작업 완료 상태 확인
- Web2 설정 및 HAProxy Round Robin 동작 상태 확인
- Proxy Node 기반 Reverse Proxy 구성 완료 여부 확인
- 운영 스크립트 작성 및 수정 진행 상황 확인
- Prometheus 및 검증 체크리스트 후속 작업 범위 정리
- Phase 1 서비스 구성 완료 항목과 후속 검증 항목 분리

---

## 3. 진행 배경

2026-06-23에는 작성자가 회의에 직접 참석하지 못했으므로, 해당 일자의 세부 진행 내용은 팀원 공유 자료와 작업 결과를 기준으로 사후 확인하였다.

2026-06-24에는 23일 진행 내용과 24일 추가 진행 내용을 통합하여 DB Node, Web Node, Proxy Node, HAProxy Round Robin, 운영 스크립트, Prometheus 검증 준비 상태를 정리하였다.

따라서 본 회의록은 23일과 24일을 개별 회의록으로 분리하지 않고, 2026-06-23~2026-06-24 통합 진행 기록으로 작성한다.

---

## 4. 주요 진행 내용

### 4.1 이진욱 - DB Node / Proxy Node / HAProxy Reverse Proxy 구성

이진욱은 DB Node 작업, Proxy Node 구성, Reverse Proxy 구성, Web2 설정, HAProxy Round Robin 동작 검증을 진행하였다.

| 작업 항목 | 진행 내용 | 상태 |
|---|---|---|
| DB Node 작업 | DB Node 작업 완료 | 완료 |
| Proxy Node 작업 | Proxy Node 구성 작업 완료 | 완료 |
| Reverse Proxy 구성 | HAProxy 기반 Reverse Proxy 구성 완료 | 완료 |
| Web2 설정 | Web2 Node 서비스 설정 완료 | 완료 |
| HAProxy RR 검증 | Web1 / Web2 대상 Round Robin 방식 동작 이상 없음 확인 | 완료 |

DB Node 작업 완료 후 Proxy Node에서 HAProxy 기반 Reverse Proxy 구성을 진행하였다.

또한 Web2 설정을 완료하고, HAProxy가 Web1 / Web2로 요청을 Round Robin 방식으로 분산하는 것을 확인하였다.

이를 통해 기존 단일 Web Node 중심 구조에서 Web1 / Web2 기반 분산 구조로 확장되었으며, Phase 3 확장 목표였던 HAProxy Round Robin 기반 Web 이중화 구조가 정상적으로 동작함을 확인하였다.

---

### 4.2 박재우 - 운영 스크립트 및 Monitoring 검증 준비

박재우는 운영 및 검증 목적의 스크립트 작성과 수정 작업을 진행하였다.

| 작업 항목 | 진행 내용 | 상태 |
|---|---|---|
| 스크립트 작성 | 운영 점검 및 검증 목적의 스크립트 작성 | 진행 |
| 스크립트 수정 | 기존 스크립트 보완 및 수정 | 진행 |
| 검증 체크리스트 | 추후 검증 체크리스트 작성 예정 | 예정 |
| Prometheus 양식 | Prometheus 관련 양식 작성 및 적용 예정 | 예정 |

운영 스크립트는 서비스 상태 확인, 백업 결과 확인, 모니터링 상태 확인과 연계될 수 있도록 수정 중이다.

추후에는 검증 체크리스트를 작성하여 Web, DB, Proxy, HAProxy Round Robin, Backup, Prometheus 상태를 체계적으로 점검할 예정이다.

---

### 4.3 조민석 - Ansible 자동화 코드 작성 진행

조민석은 기존 common.yml 이후 Docker, Database, WordPress, Proxy, Backup 관련 Ansible 자동화 파일 작성을 진행하였다.

| 작업 항목 | 진행 내용 | 상태 |
|---|---|---|
| docker.yml | Web Node 대상 Docker 설치 자동화 작성 | 작성 |
| database.yml | DB Node 대상 MariaDB 및 WordPress DB 구성 자동화 작성 | 작성 |
| wordpress.yml | Web Node 대상 Custom WordPress 배포 자동화 작성 | 작성 |
| proxy.yml | Proxy Node 대상 HAProxy 구성 자동화 작성 | 작성 |
| backup.yml | DB 및 WordPress 파일 백업 자동화 작성 | 작성 |
| 실제 실행 | 서비스 구성 상태와 충돌 방지를 위해 실행 전 검증 필요 | 보류 |
| 전체 검증 | 문법 검사, 대상 확인, 실제 실행, 멱등성 검증 필요 | 예정 |

현재 Ansible 자동화 코드는 핵심 Playbook 작성 중심으로 진행되었으며, 실제 서비스 적용 및 전체 검증은 후속 작업으로 분리한다.

특히 proxy.yml과 backup.yml은 HAProxy 구성 및 백업 자동화 구조를 정의했으나, 실제 노드 적용과 백업 생성 검증은 아직 후속 작업으로 남아 있다.

---

### 4.4 정주헌 - PM / Architecture / Documentation 정리

정주헌은 2026-06-23 불참으로 인해 24일 기준으로 팀원별 진행 내용을 사후 취합하였다.

| 작업 항목 | 진행 내용 | 상태 |
|---|---|---|
| 진행 내용 취합 | 23일 및 24일 팀원별 작업 내용 취합 | 완료 |
| 날짜 기준 정리 | 23~24일 통합 진행 기록으로 정리 | 완료 |
| 완료 / 진행 / 예정 구분 | 실제 완료 항목과 후속 검증 항목 분리 | 완료 |
| 문서화 | 통합 회의록 및 작업일지 작성 | 완료 |
| 발표자료 반영 준비 | DB / Proxy / HAProxy RR 검증 결과 반영 예정 | 예정 |

이번 통합 기록에서는 23일 불참 사실을 명시하고, 24일 기준으로 확인 가능한 진행 내용을 중심으로 기록하였다.

---

## 5. 금일 결정 사항

| 번호 | 결정 내용 |
|---:|---|
| 1 | 2026-06-23과 2026-06-24 진행 내용은 통합 기록으로 작성한다. |
| 2 | 2026-06-23은 작성자 불참으로 인해 사후 공유 자료 기준으로 기록한다. |
| 3 | DB Node 작업 완료를 통합 진행 내용에 반영한다. |
| 4 | Proxy Node 작업 및 HAProxy Reverse Proxy 구성 완료를 반영한다. |
| 5 | Web2 설정 완료 및 HAProxy Round Robin 방식 정상 동작 확인을 반영한다. |
| 6 | 박재우의 스크립트 작성 및 수정은 진행 상태로 기록한다. |
| 7 | 검증 체크리스트와 Prometheus 양식은 추후 작성 예정으로 기록한다. |
| 8 | Ansible Playbook은 작성 상태와 실제 실행 검증 상태를 구분하여 기록한다. |
| 9 | 후속 작업은 HAProxy 증빙 캡처, Prometheus target 확인, cron 로그 확인, backup/restore 검증으로 진행한다. |

---

## 6. 이슈 및 대응

| 이슈 | 내용 | 대응 |
|---|---|---|
| 23일 작성자 불참 | 작성자가 23일 회의에 직접 참석하지 못함 | 24일 기준 팀원 공유 자료를 취합하여 통합 기록으로 작성 |
| Ansible 실제 실행 미완료 | 일부 Playbook은 작성되었으나 실제 실행 및 검증이 남아 있음 | 문법 검사, 대상 확인, 순차 실행, 멱등성 검증 진행 예정 |
| HAProxy 증빙 필요 | RR 동작은 확인되었으나 제출용 캡처 정리가 필요함 | Web1/Web2 응답 및 HAProxy 상태 캡처 정리 예정 |
| 스크립트 검증 필요 | 스크립트 작성 및 수정은 진행 중이나 실행 로그 확인 필요 | cron 실행 로그 및 스크립트 결과 확인 예정 |
| Prometheus 양식 필요 | Prometheus 설치 이후 점검 양식 정리가 필요함 | target 상태, 수집 항목, 대시보드 확인 양식 작성 예정 |

---

## 7. 다음 작업 계획

| 담당자 | 다음 작업 |
|---|---|
| 이진욱 | HAProxy Round Robin 검증 결과 캡처, Web1/Web2 응답 확인 자료 정리 |
| 박재우 | 검증 체크리스트 작성, Prometheus 양식 작성, 스크립트 실행 결과 확인 |
| 조민석 | Ansible Playbook 문법 검사, 대상 확인, 실제 실행 및 멱등성 검증 |
| 정주헌 | 23~24일 통합 회의록 / 작업일지 정리, 발표자료에 DB/Proxy/HAProxy 검증 결과 반영 |
| 백서빈 | 인스턴스 및 네트워크 구성 상태 캡처 보완 |

---

## 8. 회의 결과 요약

2026-06-23~2026-06-24 통합 진행 결과, DB Node 작업과 Proxy Node 기반 HAProxy Reverse Proxy 구성이 완료되었다.

이진욱은 DB Node 작업을 완료하고, Proxy Node에서 HAProxy 기반 Reverse Proxy 구성을 완료하였다. 또한 Web2 설정을 마무리하고 HAProxy가 Web1 / Web2로 요청을 Round Robin 방식으로 분산하는 것을 확인하였다.

박재우는 운영 스크립트 작성 및 수정 작업을 진행하였으며, 추후 검증 체크리스트와 Prometheus 관련 양식을 작성할 예정이다.

조민석은 Docker, Database, WordPress, Proxy, Backup 관련 Ansible 자동화 파일 작성을 진행하였으며, 실제 실행 및 전체 검증은 후속 작업으로 분리하였다.

본 통합 기록은 23일 작성자 불참 사실을 반영하여 24일 기준으로 팀원별 공유 내용을 취합한 문서이며, 후속 작업에서는 HAProxy 증빙 캡처, Prometheus target 확인, cron 실행 로그 확인, backup/restore 검증을 진행할 예정이다.
