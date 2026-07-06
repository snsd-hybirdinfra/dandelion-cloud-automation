# Meeting Notes - 2026-07-06

## 1. 회의 개요

| 항목 | 내용 |
|---|---|
| 일자 | 2026-07-06 |
| 구분 | 4주차 진행상황 정리 |
| 프로젝트 | Ansible 기반 클라우드 인프라 자동화 및 운영 최적화 시스템 구축 |
| 팀 | Team Dandelion |
| 목적 | Monitoring, Recovery, Provisioning, Alert 진행상황 정리 |

---

## 2. 담당자별 진행상황

### 2.1 백서빈 - Monitoring / Alert Visualization

| 항목 | 상태 |
|---|---|
| Prometheus - Alertmanager 연동 | 완료 |
| Dashboard Alert 상태 출력 | 진행 중 |

Prometheus와 Alertmanager 연동을 완료하였다.

현재는 Dashboard에서 Alert 상태를 확인할 수 있도록 출력 구성을 진행 중이다.

---

### 2.2 조민석 - Recovery Automation

| 항목 | 상태 |
|---|---|
| Monitoring 제외 복구 Playbook 작성 | 완료 |
| Monitoring 제외 복구 Playbook 검증 | 완료 |

Monitoring 영역을 제외한 주요 서비스 복구 Playbook 작성과 검증을 완료하였다.

해당 범위는 Web, DB, Proxy, Backup / Recovery 등 주요 서비스 복구 자동화 범위를 기준으로 한다.

---

### 2.3 이진욱 - OpenStack Provisioning Automation

| 항목 | 상태 |
|---|---|
| Ansible 기반 인스턴스 생성 Playbook 작성 | 완료 |
| 보안그룹 생성 Playbook | 예정 |
| 서브넷 생성 Playbook | 예정 |
| Flavor 생성 Playbook | 예정 |
| Image 생성 Playbook | 예정 |

Ansible 기반 OpenStack 인스턴스 생성 Playbook을 작성하였다.

다음 작업으로 보안그룹, 서브넷, Flavor, Image 생성 Playbook을 작성할 예정이다.

---

### 2.4 박재우 - Alertmanager / Mail Alert

| 항목 | 상태 |
|---|---|
| Alertmanager 설정 수정 | 진행 |
| Mail Alert 테스트 점검 | 진행 |

Alertmanager 설정을 수정한 뒤 Mail Alert 테스트를 점검하고 있다.

해당 작업은 장애 발생 시 알림 전달 흐름을 검증하기 위한 작업이다.

---

## 3. 2026-07-06 기준 완료 / 진행 / 예정 항목

### 완료

~~~text
- Prometheus - Alertmanager 연동 완료
- Monitoring 제외 복구 Playbook 작성 완료
- Monitoring 제외 복구 Playbook 검증 완료
- Ansible 기반 인스턴스 생성 Playbook 작성 완료
~~~

### 진행

~~~text
- Dashboard Alert 상태 출력 진행 중
- Alertmanager 설정 수정 및 Mail Alert 테스트 점검 진행 중
~~~

### 예정

~~~text
- 보안그룹 생성 Playbook 작성 예정
- 서브넷 생성 Playbook 작성 예정
- Flavor 생성 Playbook 작성 예정
- Image 생성 Playbook 작성 예정
~~~

---

## 4. 발표 설명 기준

~~~text
Prometheus와 Alertmanager 연동은 완료되었고,
현재 Dashboard에서 Alert 상태를 출력하는 작업을 진행 중입니다.

Monitoring을 제외한 복구 Playbook 작성과 검증은 완료되었습니다.

OpenStack 인스턴스 생성 Playbook을 작성했으며,
다음 단계로 보안그룹, 서브넷, Flavor, Image 생성 Playbook을 작성할 예정입니다.

Alertmanager 설정 수정 후 Mail Alert 테스트를 점검하고 있습니다.
~~~
