# Meeting Notes - 2026-07-08

## 1. 회의 개요

| 항목 | 내용 |
|---|---|
| 일자 | 2026-07-08 |
| 구분 | 4주차 작업내용 정리 |
| 프로젝트 | Ansible 기반 클라우드 인프라 자동화 및 운영 최적화 시스템 구축 |
| 팀 | Team Dandelion |
| 목적 | 발표자료, 모니터링 자동화, OpenStack Playbook 문서화, 최종 제출 기준 정리 |

---

## 2. 담당자별 작업내용

### 2.1 백서빈 - Infrastructure Presentation

| 항목 | 상태 |
|---|---|
| 인프라 발표자료 정리 | 진행 중 |

#### 상세 내용

인프라 파트의 발표자료를 정리하고 있다.

OpenStack 기반 인프라 구성, 네트워크, 보안그룹, 인스턴스 구성 및 검증 내용을 발표자료에 반영하는 작업이다.

#### 발표 설명 기준

~~~text
인프라 파트는 OpenStack 기반 인프라 구성과 검증 결과를 발표자료로 정리하고 있습니다.
~~~

---

### 2.2 조민석 - Monitoring Automation / Restore Automation

| 항목 | 상태 |
|---|---|
| 모니터링 구성 Playbook 작성 | 완료 |
| 모니터링 Restore Playbook 작성 | 진행 중 |

#### 상세 내용

모니터링 구성 자동화를 위한 Ansible Playbook 작성을 완료하였다.

현재는 모니터링 구성 장애 또는 손상 상황에 대응하기 위한 Restore Playbook을 작성하고 있다.

#### 발표 설명 기준

~~~text
모니터링 구성 Playbook 작성을 완료했고,
현재 모니터링 Restore Playbook을 작성 중입니다.

이를 통해 모니터링 구성 자동화와 복구 자동화 범위를 확장하고 있습니다.
~~~

---

### 2.3 이진욱 - OpenStack Playbook Documentation

| 항목 | 상태 |
|---|---|
| OpenStack 노드 / 인스턴스 Playbook 문서화 | 진행 중 |

#### 상세 내용

OpenStack 노드 및 인스턴스 생성 Playbook에 대한 문서화를 진행하고 있다.

기존에 작성한 인스턴스, 보안그룹, 서브넷, Flavor, Image, Keypair 관련 Playbook의 실행 목적과 사용 흐름을 정리하는 작업이다.

#### 발표 설명 기준

~~~text
OpenStack 노드 및 인스턴스 생성 Playbook을 문서화하고 있습니다.

최종 제출 시 Ansible Playbook 기반 인프라 생성 자동화 산출물로 정리할 예정입니다.
~~~

---

### 2.4 박재우 - Monitoring Documentation

| 항목 | 상태 |
|---|---|
| 모니터링 설치 문서화 | 진행 중 |
| 모니터링 구성 문서화 | 진행 중 |

#### 상세 내용

Prometheus, Alertmanager, Grafana 등 모니터링 설치 및 구성 내용을 문서화하고 있다.

해당 문서는 최종 발표와 제출 산출물에서 모니터링 구성 근거 자료로 활용한다.

#### 발표 설명 기준

~~~text
모니터링 설치 및 구성 내용을 문서화하고 있습니다.

Prometheus, Alertmanager, Grafana 구성 흐름과 검증 결과를 최종 산출물에 반영할 예정입니다.
~~~

---

## 3. 최종 제출 기준

이번 프로젝트의 소스코드는 Ansible Playbook 중심으로 제출할 예정이다.

| 제출 영역 | 제출 기준 |
|---|---|
| 소스코드 | Ansible Playbook 중심 제출 |
| 인프라 자동화 | OpenStack 리소스 생성 Playbook |
| 서비스 구성 자동화 | 서비스 / DB / Proxy / Monitoring 구성 Playbook |
| 복구 자동화 | Restore / Recovery Playbook |
| 검증 | Playbook 실행 결과 및 캡처 기반 증빙 |

---

## 4. 2026-07-08 기준 완료 / 진행 항목

### 완료

~~~text
- 모니터링 구성 Playbook 작성 완료
~~~

### 진행

~~~text
- 인프라 발표자료 정리 중
- 모니터링 Restore Playbook 작성 중
- OpenStack 노드 / 인스턴스 Playbook 문서화 진행 중
- 모니터링 설치 및 구성 문서화 진행 중
~~~

### 제출 기준

~~~text
- 소스코드는 Ansible Playbook 중심으로 제출 예정
~~~

---

## 5. 후속 작업

| 담당 | 후속 작업 |
|---|---|
| 백서빈 | 인프라 발표자료 정리 완료 및 캡처 반영 |
| 조민석 | 모니터링 Restore Playbook 작성 완료 및 실행 검증 |
| 이진욱 | OpenStack 노드 / 인스턴스 Playbook 문서화 완료 |
| 박재우 | 모니터링 설치 및 구성 문서화 완료 |
| 정주헌 | 최종 제출 산출물 구조 정리 및 발표 흐름 반영 |

---

## 6. 회의 결론

~~~text
2026-07-08 기준으로 모니터링 구성 Playbook 작성이 완료되었고,
모니터링 Restore Playbook 작성, OpenStack Playbook 문서화,
모니터링 설치 및 구성 문서화, 인프라 발표자료 정리가 진행 중이다.

최종 소스코드는 Ansible Playbook 중심으로 제출할 예정이다.
~~~
