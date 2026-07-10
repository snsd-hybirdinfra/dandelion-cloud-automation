# Meeting Notes - 2026-07-07

## 1. 회의 개요

| 항목 | 내용 |
|---|---|
| 일자 | 2026-07-07 |
| 구분 | 4주차 작업내용 정리 |
| 프로젝트 | Ansible 기반 클라우드 인프라 자동화 및 운영 최적화 시스템 구축 |
| 팀 | Team Dandelion |
| 목적 | Monitoring, DB Automation, OpenStack Provisioning, Backup 수정 작업 정리 |

---

## 2. 담당자별 작업내용

### 2.1 백서빈 - Monitoring / Dashboard

| 항목 | 상태 |
|---|---|
| Dashboard Alert 상태 출력 | 완료 |

#### 상세 내용

Dashboard에서 Alert 상태를 출력하는 작업을 완료하였다.

이를 통해 Prometheus - Alertmanager 연동 이후 발생한 Alert 상태를 화면에서 확인할 수 있는 구성이 마련되었다.

#### 발표 설명 기준

~~~text
Prometheus - Alertmanager 연동 이후 Dashboard에서 Alert 상태를 출력하는 작업을 완료했습니다.
장애 발생 및 알림 상태를 시각적으로 확인할 수 있도록 구성했습니다.
~~~

---

### 2.2 조민석 - DB Automation

| 항목 | 상태 |
|---|---|
| DB 이중화 자동화 Playbook 작성 | 진행 / 작성 |

#### 상세 내용

DB 이중화 구성을 자동화하기 위한 Ansible Playbook을 작성하였다.

해당 Playbook은 DB Primary - Replica 구성 또는 DB 이중화 구성 자동화를 위한 작업으로 정리한다.

#### 발표 설명 기준

~~~text
DB 이중화 구성을 Ansible Playbook으로 자동화하는 작업을 진행했습니다.
기존 DB 이중화 및 Failover 검증 결과를 자동화 산출물로 확장했습니다.
~~~

---

### 2.3 이진욱 - OpenStack Provisioning Automation

| 항목 | 상태 |
|---|---|
| 보안그룹 생성 Playbook | 작성 |
| 서브넷 생성 Playbook | 작성 |
| Flavor 생성 Playbook | 작성 |
| Image 생성 Playbook | 작성 |
| Keypair 생성 Playbook | 작성 |

#### 상세 내용

OpenStack 인프라 생성 자동화를 위해 보안그룹, 서브넷, Flavor, Image, Keypair 생성 Playbook을 작성하였다.

이 작업은 기존 인스턴스 생성 Playbook과 연계되어 OpenStack Provisioning 자동화 범위를 확장하는 작업이다.

#### 발표 설명 기준

~~~text
OpenStack 인스턴스 생성 Playbook에 이어,
보안그룹, 서브넷, Flavor, Image, Keypair 생성 Playbook을 작성했습니다.

이를 통해 OpenStack Provisioning 자동화 범위를 인스턴스 생성뿐 아니라
인프라 리소스 생성 영역까지 확장했습니다.
~~~

---

### 2.4 박재우 - Alert / Backup

| 항목 | 상태 |
|---|---|
| Alertmanager / Prometheus Time Sync 점검 | 진행 |
| Backup Node의 Prometheus 백업 부분 수정 | 진행 / 수정 |

#### 상세 내용

Alertmanager와 Prometheus 간 Time Sync 관련 사항을 점검하였다.

또한 Backup Node에서 Prometheus 백업 부분을 수정하였다.

해당 작업은 모니터링 데이터 및 설정 백업의 안정성을 높이기 위한 작업이다.

#### 발표 설명 기준

~~~text
Alertmanager와 Prometheus의 Time Sync 관련 부분을 점검하고,
Backup Node에서 Prometheus 백업 부분을 수정했습니다.

이를 통해 모니터링 구성의 백업 안정성과 알림 연동 정확성을 개선했습니다.
~~~

---

## 3. 2026-07-07 기준 완료 / 진행 항목

### 완료 또는 작성 완료

~~~text
- Dashboard Alert 상태 출력 완료
- DB 이중화 자동화 Playbook 작성
- 보안그룹 생성 Playbook 작성
- 서브넷 생성 Playbook 작성
- Flavor 생성 Playbook 작성
- Image 생성 Playbook 작성
- Keypair 생성 Playbook 작성
~~~

### 진행 / 수정

~~~text
- Alertmanager / Prometheus Time Sync 점검
- Backup Node의 Prometheus 백업 부분 수정
~~~

---

## 4. 후속 작업

| 담당 | 후속 작업 |
|---|---|
| 백서빈 | Dashboard Alert 출력 화면 캡처 및 발표자료 반영 |
| 조민석 | DB 이중화 자동화 Playbook 실행 검증 및 결과 캡처 |
| 이진욱 | OpenStack Provisioning Playbook 실행 검증 및 결과 캡처 |
| 박재우 | Time Sync 점검 결과 정리, Prometheus 백업 수정 결과 검증 |
| 정주헌 | 7월 7일 작업내용 문서화 및 최종 발표 흐름 반영 |

---

## 5. 회의 결론

~~~text
2026-07-07 기준으로 Dashboard Alert 상태 출력이 완료되었고,
DB 이중화 자동화 Playbook과 OpenStack Provisioning 관련 Playbook 작성이 진행되었다.

또한 Alertmanager / Prometheus Time Sync 점검과 Backup Node의 Prometheus 백업 부분 수정이 진행되었다.

이후에는 각 Playbook 및 수정 항목의 실행 검증, 캡처 정리, 발표자료 반영이 필요하다.
~~~
