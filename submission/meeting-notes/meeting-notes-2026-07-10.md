# Meeting Notes - 2026-07-10

## 1. 회의 개요

| 항목 | 내용 |
|---|---|
| 일자 | 2026-07-10 |
| 구분 | 4주차 최종 구현 및 발표자료 정리 |
| 프로젝트 | Ansible 기반 클라우드 인프라 자동화 및 운영 최적화 시스템 구축 |
| 팀 | Team Dandelion |
| 목적 | 인프라 발표자료, 통합 Playbook 검증, OpenStack 자원 설정, 모니터링 문서화 및 최종 PPT 정리 |

---

## 2. 담당자별 작업내용

### 2.1 백서빈 - Infrastructure Presentation

| 항목 | 상태 |
|---|---|
| 인프라 파트 PPT 작성 | 완료 |

#### 상세 내용

OpenStack 기반 인프라 구성 및 검증 결과를 정리한 인프라 파트 발표자료 작성을 완료하였다.

발표자료에는 인스턴스 구성, 네트워크, 서브넷, 보안그룹, 노드별 역할 및 인프라 검증 내용을 반영하였다.

#### 발표 설명 기준

~~~text
OpenStack 기반 인프라 구성과 검증 결과를 발표자료로 정리했습니다.

인스턴스, 네트워크, 보안그룹과 노드별 역할을 중심으로
인프라 구성 결과를 설명할 예정입니다.
~~~

---

### 2.2 조민석 - site.yml Integration Validation

| 항목 | 상태 |
|---|---|
| 생성 인스턴스 대상 site.yml 검증 | 진행 중 |

#### 상세 내용

OpenStack Playbook으로 생성된 인스턴스를 대상으로 통합 Playbook인 `site.yml`의 실행 검증을 진행하고 있다.

Inventory 연결, SSH 접근, 역할별 Playbook 호출, 서비스 설정 적용 및 실행 결과를 확인하는 작업이다.

#### 주요 검증 항목

~~~text
- 생성 인스턴스 SSH 접근 확인
- Ansible Ping 확인
- Inventory 대상 호스트 확인
- site.yml 구문 검사
- 역할별 Playbook 호출 확인
- PLAY RECAP 결과 확인
~~~

#### 발표 설명 기준

~~~text
OpenStack Playbook으로 생성한 인스턴스를 대상으로
통합 Playbook인 site.yml의 실행을 검증하고 있습니다.

Inventory 연결부터 역할별 Playbook 실행과 서비스 설정 적용 여부를
순차적으로 확인하고 있습니다.
~~~

---

### 2.3 이진욱 - Floating IP / Cinder Volume Playbook

| 항목 | 상태 |
|---|---|
| Floating IP 설정 Playbook 수정 | 진행 |
| Cinder Volume 생성 및 연결 Playbook 수정 | 진행 |
| Backup Node Volume 마운트 구성 | 진행 |

#### 상세 내용

OpenStack 인스턴스에 Floating IP를 할당할 수 있도록 Ansible Playbook을 수정하였다.

또한 Cinder Volume을 생성하고 Backup Node에 연결한 뒤,
운영체제에서 해당 볼륨을 마운트할 수 있도록 Playbook을 수정하였다.

#### 주요 수정 내용

~~~text
- Floating IP 생성 및 인스턴스 연결
- Cinder Volume 생성
- Cinder Volume과 Backup Node 연결
- 연결 장치 확인
- 파일시스템 생성
- 마운트 디렉터리 생성
- Backup Node Volume 마운트
- 재부팅 후 자동 마운트를 위한 설정 검토
~~~

#### 발표 설명 기준

~~~text
OpenStack 인스턴스에 Floating IP를 할당하고,
Cinder Volume을 Backup Node에 연결할 수 있도록
Ansible Playbook을 수정했습니다.

연결된 볼륨은 Backup Node에서 백업 저장공간으로
사용할 수 있도록 마운트 구성을 적용하고 있습니다.
~~~

---

### 2.4 박재우 - Monitoring Documentation

| 항목 | 상태 |
|---|---|
| 모니터링 설치 문서화 | 진행 중 |
| 모니터링 구성 문서화 | 진행 중 |
| 모니터링 검증 결과 정리 | 진행 중 |

#### 상세 내용

Prometheus, Alertmanager, Grafana 등 모니터링 구성에 대한 문서화를 진행하고 있다.

설치 절차, 설정 파일, Target 연결, Alert Rule, Mail Alert,
Dashboard 구성 및 백업·복구 검증 내용을 문서에 반영하는 작업이다.

#### 주요 문서화 항목

~~~text
- Prometheus 설치 및 설정
- Prometheus Target 연결
- Alert Rule 설정
- Alertmanager 연동
- Mail Alert 설정 및 수신 결과
- Grafana Dashboard 구성
- Monitoring 데이터 백업
- Monitoring 설정 복구
~~~

#### 발표 설명 기준

~~~text
Prometheus, Alertmanager, Grafana의 설치와 구성 내용을
문서화하고 있습니다.

Target 수집, 장애 알림, Dashboard 시각화와
백업·복구 검증 결과를 최종 산출물에 반영할 예정입니다.
~~~

---

### 2.5 정주헌 - PM / Presentation Integration

| 항목 | 상태 |
|---|---|
| 최종 PPT 초안 작성 | 완료 |
| 인프라 파트 내용 수정 | 진행 |
| 인프라 파트 디자인 보완 | 진행 |
| 발표자료 전체 흐름 정리 | 진행 |

#### 상세 내용

최종 결과보고서와 발표에 사용할 PPT 초안 작성을 완료하였다.

현재 인프라 파트의 내용과 디자인을 수정하고 있으며,
팀원별 역할과 구현 결과가 명확히 구분되도록 발표자료 전체 구조를 보완하고 있다.

#### 주요 작업 내용

~~~text
- 최종 PPT 18페이지 초안 작성
- 역할별 발표 구간 구성
- 인프라 파트 문구 수정
- 인프라 파트 디자인 보완
- 전체 시스템 아키텍처 구성
- 구현 결과 및 검증 증빙 배치 기준 정리
- 발표자료 문구 간소화
~~~

#### 발표 설명 기준

~~~text
최종 발표자료의 전체 초안을 작성했습니다.

현재 인프라 파트의 내용과 디자인을 보완하고 있으며,
각 팀원의 역할과 구현 결과가 명확하게 보이도록
발표 흐름을 정리하고 있습니다.
~~~

---

## 3. 주요 결정사항

| 구분 | 결정 내용 |
|---|---|
| 발표자료 | 18페이지 구성 유지 |
| 역할 구분 | 기존 담당 역할 기준으로 발표 구간 분리 |
| 인프라 증빙 | OpenStack 인스턴스, 네트워크, 보안그룹 결과 반영 |
| 자동화 증빙 | site.yml 실행 결과 및 PLAY RECAP 반영 |
| 스토리지 구성 | Cinder Volume을 Backup Node에 연결 및 마운트 |
| 모니터링 산출물 | 설치, 설정, 알림, 백업·복구 내용을 문서화 |
| 최종 검증 | 생성 인스턴스 대상 통합 Playbook 실행 결과 확인 |

---

## 4. 2026-07-10 기준 완료 항목

~~~text
- 백서빈: 인프라 파트 PPT 작성
- 정주헌: 최종 PPT 초안 작성
~~~

---

## 5. 2026-07-10 기준 진행 항목

~~~text
- 조민석: 생성 인스턴스 대상 site.yml 실행 검증
- 이진욱: Floating IP 설정 Playbook 수정
- 이진욱: Cinder Volume의 Backup Node 연결 및 마운트 Playbook 수정
- 박재우: 모니터링 설치 및 구성 문서화
- 정주헌: 인프라 파트 내용 수정 및 디자인 보완
~~~

---

## 6. 후속 작업

| 담당 | 후속 작업 |
|---|---|
| 백서빈 | 인프라 발표자료 최종 검토 및 필요한 증빙 캡처 전달 |
| 조민석 | site.yml 실행 검증 및 PLAY RECAP 결과 정리 |
| 이진욱 | Floating IP 및 Cinder Volume Playbook 실행 검증 |
| 박재우 | 모니터링 문서화 완료 및 검증 캡처 정리 |
| 정주헌 | 팀원별 자료 취합, PPT 수정 및 최종 발표 흐름 정리 |

---

## 7. 검증 기준

### site.yml 검증

~~~text
ansible-playbook --syntax-check site.yml
ansible-playbook site.yml
~~~

확인 기준:

~~~text
- unreachable=0
- failed=0
- 역할별 Playbook 정상 호출
- 대상 서비스 정상 실행
~~~

### Floating IP 검증

~~~text
openstack floating ip list
openstack server list
~~~

확인 기준:

~~~text
- Floating IP 생성 확인
- 대상 인스턴스 연결 확인
- 외부 또는 관리망 접근 확인
~~~

### Cinder Volume 검증

~~~text
openstack volume list
openstack server volume list <INSTANCE_NAME>
lsblk
df -h
mount
~~~

확인 기준:

~~~text
- Cinder Volume 생성 확인
- Backup Node 연결 확인
- 운영체제 장치 인식 확인
- 마운트 경로 확인
- 읽기 및 쓰기 확인
~~~

---

## 8. 회의 결론

~~~text
2026-07-10 기준으로 인프라 파트 발표자료와 최종 PPT 초안 작성이 완료되었다.

현재 생성 인스턴스를 대상으로 site.yml 통합 실행 검증을 진행하고 있으며,
Floating IP 설정과 Cinder Volume의 Backup Node 연결 및 마운트를 위한
Ansible Playbook을 수정하고 있다.

모니터링 파트는 설치, 설정, 알림, 백업 및 복구 내용을 중심으로
문서화를 진행하고 있으며, 최종 발표자료는 인프라 파트 수정과
전체 발표 흐름 보완 작업을 진행한다.
~~~
