<!-- STATUS: COMPLETE -->

# Team Dandelion 회의록

## 2026-06-16 회의록

## 1. 회의 정보

| 구분 | 내용 |
|---|---|
| 회의 일자 | 2026-06-16 |
| 회의 구분 | Phase 기반 범위 재정리 및 최종 아키텍처 정렬 |
| 회의 장소 | ZEP 팀 회의실 / Discord |
| 작성자 | 정주헌 |
| 참석자 | 정주헌, 백서빈, 이진욱, 조민석, 박재우 |

---

## 2. 회의 목적

- 기존 등급 기반 구현 범위를 Phase 기반 로드맵으로 재정리
- Phase 1 / Phase 2 / Phase 3 / Out of Scope 기준 확정
- Proxy / Web / DB / Backup Node 분리 구조 확정
- MariaDB 구성 방식을 컨테이너 방식에서 직접 설치 방식으로 수정
- HAProxy Reverse Proxy 및 Load Balancing 적용 범위 정리
- 최종 아키텍처 다이어그램 수정 사항 정리
- SSH 관리 트래픽 방향과 사용자 트래픽 방향 구분
- 서브넷 분리 설계 방향 정리
- 멘토링용 압축 작업 순서 정리

---

## 3. 주요 논의 내용

### 3.1 구현 범위 표현 방식 변경

기존 등급 기반 구현 범위 표현은 프로젝트 진행 과정에서 세부 기준이 복잡해질 수 있으므로, Phase 기반 구현 로드맵으로 변경하기로 하였다.

변경된 기준은 다음과 같다.

| 구분 | 의미 |
|---|---|
| Phase 1 | 필수 구성 및 기본 검증 단계 |
| Phase 2 | 운영 확장 및 검증 고도화 단계 |
| Phase 3 | 도전 확장 단계 |
| Out of Scope | 제외 범위 |

Phase 1은 최종 발표와 제출을 위한 필수 성공 기준으로 정의한다.  
Phase 2와 Phase 3은 Phase 1이 안정적으로 완료된 이후 진행 가능한 확장 범위로 분리한다.

---

### 3.2 Phase 1 필수 구성 범위 확정

Phase 1에서는 OpenStack 기반 Ubuntu 인스턴스 위에 역할별 노드를 구성하고, Ansible을 통해 기본 운영 흐름을 자동화한다.

Phase 1의 필수 흐름은 다음과 같다.

~~~text
OpenStack Ubuntu Instance
→ Control / Proxy / Web / DB / Backup Node 분리
→ SSH 접속 확인
→ Ansible inventory 구성
→ ansible ping 검증
→ Proxy / Web Node Docker 설치
→ DB Node MariaDB 직접 설치 및 서비스 구성
→ Web Node Custom WordPress Container 배포
→ Proxy Node HAProxy HTTP Reverse Proxy 구성
→ Proxy Node 경유 WordPress 접속 확인
→ health_check.sh 실행
→ backup.sh 실행
→ MariaDB dump 및 WordPress files archive 생성
→ restore.md 기반 복구 절차 검증
→ 캡처, 트러블슈팅, 작업일지, 제출 문서 정리
~~~

Phase 1은 기능 개수보다 실행 가능성과 검증 증거 확보를 우선한다.

---

### 3.3 MariaDB 구성 방식 수정

기존 일부 문서에서는 MariaDB를 컨테이너로 구성하는 표현이 포함되어 있었으나, 실제 구현 기준은 DB Node에 MariaDB를 직접 설치하고 systemd 서비스로 운영하는 방식으로 수정하였다.

변경 기준은 다음과 같다.

| 구분 | 기존 방향 | 수정 방향 |
|---|---|---|
| DB 구성 | MariaDB 컨테이너 기반 구성 | MariaDB 직접 설치 |
| 설치 방식 | Docker Compose 기반 DB 실행 | apt 기반 mariadb-server 설치 |
| 서비스 관리 | Docker container 상태 확인 | systemctl mariadb 상태 확인 |
| 백업 방식 | 컨테이너 내부 DB dump | DB Node MariaDB 서비스 대상 dump |
| DB 배치 | Web Node 또는 DB Container 중심 | DB Node 분리 운영 |

최종 기준은 다음과 같다.

~~~text
Proxy Node
→ HAProxy Container

Web Node
→ Custom WordPress Container

DB Node
→ MariaDB Package Install
→ MariaDB systemd Service

Backup / Validation Node
→ health_check.sh
→ backup.sh
→ MariaDB dump
→ WordPress files archive
→ restore.md 검증
~~~

---

### 3.4 HAProxy 적용 범위 정리

HAProxy는 Phase 1부터 Proxy Node에 포함하기로 하였다.

Phase별 HAProxy 적용 범위는 다음과 같다.

| Phase | HAProxy 적용 기준 |
|---|---|
| Phase 1 | HTTP Reverse Proxy |
| Phase 2 | HTTPS self-signed, HTTP to HTTPS Redirect |
| Phase 3 | Web Node 1 / Web Node 2 대상 Load Balancing |

Phase 1에서는 Client가 Web Node에 직접 접근하지 않고 Proxy Node를 통해 WordPress 서비스에 접근하는 구조를 검증한다.

~~~text
Client
→ Proxy Node / HAProxy HTTP Reverse Proxy
→ Web Node / Custom WordPress Container
→ DB Node / MariaDB Service
~~~

---

### 3.5 Phase 2 운영 확장 범위 정리

Phase 2는 Phase 1 완료 후 가능한 범위에서 진행하는 운영 확장 단계로 정의하였다.

Phase 2 대상은 다음과 같다.

| 항목 | 기준 |
|---|---|
| HTTPS self-signed | HAProxy에서 HTTPS 접속 검증 |
| HTTP to HTTPS Redirect | 80에서 443으로 Redirect |
| Cinder Backup Volume | Backup Node에 attach 후 backup 저장소로 사용 |
| node_exporter | 서버 OS 메트릭 수집 |
| cAdvisor | 컨테이너 메트릭 수집 |
| Prometheus | 메트릭 수집 |
| Grafana | 대시보드 시각화 |
| backup / restore playbook화 | 운영 절차 자동화 개선 |
| Ansible roles 구조 분리 | 자동화 구조 개선 |

Cinder Volume은 DB 원본 저장소로 사용하지 않고, Backup / Validation Node의 백업 저장소로만 사용한다.

---

### 3.6 Phase 3 도전 확장 범위 정리

Phase 3은 Phase 1과 Phase 2가 조기에 안정화된 경우에만 진행하는 도전 확장 단계로 정의하였다.

Phase 3 목표 구조는 다음과 같다.

~~~text
Client
→ Proxy Node / HAProxy Load Balancer
→ Web Node 1 / WordPress
→ Web Node 2 / WordPress
→ DB Node / MariaDB Service
→ Backup / Validation Node
~~~

Phase 3 검증 기준은 다음과 같다.

| 항목 | 기준 |
|---|---|
| Web Node 2 구성 | 추가 WordPress 서비스 노드 구성 |
| HAProxy Round Robin | Web Node 1 / Web Node 2 대상 분산 |
| 공통 DB 연결 | 두 Web Node가 동일 DB Node MariaDB 서비스 사용 |
| 장애 테스트 | Web Node 1 중지 시 Web Node 2 응답 확인 |

WordPress files 자동 동기화, DB Replication, DB Clustering, OpenStack LBaaS / Octavia는 Phase 3에서도 제외한다.

---

## 4. 노드 구조 변경

최종 노드 구조는 다음과 같이 정리하였다.

| 노드 | 역할 | 구성 기준 |
|---|---|---|
| Control Node | Ansible 실행 및 Inventory / Playbook 관리 | Phase 1 |
| Proxy Node | HAProxy HTTP Reverse Proxy | Phase 1 |
| Web Node | Custom WordPress Container 운영 | Phase 1 |
| DB Node | MariaDB 직접 설치 및 systemd 서비스 운영 | Phase 1 |
| Backup / Validation Node | Health Check, Backup, Restore 검증 | Phase 1 |
| Monitoring Node | Prometheus / Grafana 운영 | Phase 2 |
| Web Node 2 | 추가 WordPress 서비스 노드 | Phase 3 |

Phase 1에서는 Control / Proxy / Web / DB / Backup Node를 기준으로 구현한다.  
Monitoring Node는 Phase 2에서 선택적으로 구성한다.  
Web Node 2는 Phase 3에서 도전 확장으로 구성한다.

---

## 5. 문서 수정 결정

Phase 기반 구조와 MariaDB 직접 설치 기준에 맞춰 주요 문서를 수정하기로 하였다.

| 문서 | 수정 내용 |
|---|---|
| README.md | Phase 기반 프로젝트 개요 및 최종 구조 반영 |
| docs/architecture.md | Proxy / Web / DB / Backup 분리 구조 반영 |
| docs/network-design.md | 서브넷, 보안그룹, 통신 흐름 정리 |
| docs/scope-control.md | Phase 1 / Phase 2 / Phase 3 / Out of Scope 범위 재정의 |
| docs/implementation-roadmap.md | Phase별 구현 순서 정리 |
| docs/server-setup.md | MariaDB 직접 설치 및 systemd 서비스 기준 반영 |
| docs/ansible-automation.md | MariaDB 설치 자동화 및 WordPress / HAProxy 배포 자동화 반영 |
| docs/validation-report.md | MariaDB dump, WordPress files backup 기준 반영 |
| docs/team-task-guide.md | 팀원별 작업 기준 정리 |
| docs/pre-run-checklist.md | 실행 전 점검 기준 정리 |
| docs/troubleshooting.md | 장애 대응 절차 정리 |
| docs/runbook.md | 실제 실행 절차 정리 |
| docs/final-deliverables.md | 최종 제출 산출물 기준 정리 |
| docs/review-checklist.md | 제출 전 최종 검수 기준 정리 |
| docs/submission-package.md | Google Drive 및 GitHub 제출 패키지 기준 정리 |
| presentation/presentation-outline.md | 발표 흐름을 Phase 기반 구조로 수정 |
| docker/wordpress/README.md | Custom WordPress Image 역할 정리 |

---

## 6. 결정 사항

| 번호 | 결정 내용 |
|---:|---|
| 1 | 기존 등급 기반 구현 범위 표현을 Phase 기반 로드맵으로 변경한다. |
| 2 | Phase 1은 최종 발표 및 제출의 필수 성공 기준으로 둔다. |
| 3 | Phase 2는 HTTPS, Cinder, Monitoring, Playbook 개선 등 운영 확장으로 둔다. |
| 4 | Phase 3은 Web Node 2대와 HAProxy Load Balancing 도전 확장으로 둔다. |
| 5 | Proxy Node는 HAProxy 컨테이너로 구성한다. |
| 6 | Web Node는 Custom WordPress 컨테이너로 구성한다. |
| 7 | DB Node는 MariaDB를 컨테이너가 아니라 직접 설치하여 systemd 서비스로 운영한다. |
| 8 | Backup / Validation Node는 health_check.sh, backup.sh, MariaDB dump, restore.md 검증을 담당한다. |
| 9 | Cinder Volume은 DB 원본 저장소가 아니라 Backup Node 백업 저장소로 사용한다. |
| 10 | 최종 아키텍처 다이어그램에서 DNS 구성은 제외한다. |
| 11 | SSH 관리 트래픽은 Control Node에서 각 노드로 향하는 방향으로 표시한다. |
| 12 | 사용자 트래픽, SSH 관리 트래픽, DB 트래픽, 백업/모니터링 트래픽을 구분하여 표현한다. |
| 13 | 192.168.4.0/24 대역은 /26 기준 4개 서브넷으로 나누는 설계를 사용한다. |
| 14 | 실제 구현이 복잡할 경우 단일 Private Network와 보안그룹 기반 논리 분리로 대체할 수 있다. |
| 15 | 멘토링 자료는 상세 문서 전체가 아니라 압축된 작업 순서 중심으로 보여준다. |

---

## 7. 다음 작업 계획

| 담당자 | 다음 작업 |
|---|---|
| 정주헌 | Phase 기반 문서 최종 검수, MariaDB 표현 정리, 아키텍처 이미지 배치, 발표 흐름 정리 |
| 백서빈 | OpenStack 인스턴스, 네트워크, 서브넷, 라우터, 보안그룹 구성 |
| 이진욱 | Proxy Node HAProxy, Web Node WordPress, DB Node MariaDB 직접 설치 구성 지원 |
| 조민석 | Ansible inventory, site.yml, MariaDB 설치 자동화, WordPress / HAProxy 배포 자동화 |
| 박재우 | health_check.sh, backup.sh, MariaDB dump, restore.md 검증, 모니터링 확장 검토 |

---

## 8. 회의 결과 요약

2026년 6월 16일 회의에서는 프로젝트 범위를 Phase 기반 로드맵으로 재정리하였다.

Phase 1은 OpenStack 인프라 구성, Control / Proxy / Web / DB / Backup Node 분리, Ansible 자동화, Custom WordPress 배포, MariaDB 직접 설치, HAProxy HTTP Reverse Proxy, 상태 점검, 백업, 복구 검증까지를 필수 성공 기준으로 확정하였다.

Phase 2는 HTTPS, Cinder Backup Volume, Prometheus/Grafana, Playbook 개선 등 운영 확장으로 정리하였다.

Phase 3은 Web Node 2대와 HAProxy Load Balancing을 통한 도전 확장으로 정리하였다.

또한 MariaDB는 컨테이너가 아니라 DB Node에 직접 설치하고 systemd 서비스로 운영하는 것으로 기준을 수정하였다. 최종 아키텍처 다이어그램에서는 DNS를 제외하고, SSH 관리 트래픽은 Control Node에서 각 노드로 향하도록 표시하기로 하였다.

---

## 9. 추가 결정 사항: 최종 아키텍처 다이어그램 정리

Phase별 아키텍처 다이어그램은 인프라 중심과 서비스 중심으로 분리하여 작성하기로 하였다.

총 6장의 Phase별 다이어그램과 1장의 최종 완성본 다이어그램을 사용한다.

| 구분 | 파일명 |
|---|---|
| 최종 아키텍처 완성본 | docs/assets/final-phase3-architecture.png |
| Phase 1 Infrastructure View | docs/assets/phase1-infrastructure-view.png |
| Phase 1 Service View | docs/assets/phase1-service-view.png |
| Phase 2 Infrastructure View | docs/assets/phase2-infrastructure-view.png |
| Phase 2 Service View | docs/assets/phase2-service-view.png |
| Phase 3 Infrastructure View | docs/assets/phase3-infrastructure-view.png |
| Phase 3 Service View | docs/assets/phase3-service-view.png |

발표자료에서는 전체 최종 아키텍처를 먼저 보여준 뒤, Phase 1 필수 구성과 Phase 3 확장 구조를 중심으로 설명한다.

---

## 10. 추가 결정 사항: SSH 화살표 방향 정리

최종 아키텍처 그림에서 SSH 관리 트래픽 방향은 다음 기준으로 표시한다.

~~~text
Control Node
→ SSH / Ansible
→ Proxy Node
→ Web Node 1
→ Web Node 2
→ DB Node
→ Backup / Validation Node
→ Monitoring Node
~~~

Control Node는 관리 주체이며, 나머지 노드는 관리 대상이다.

사용자 트래픽과 SSH 관리 트래픽은 다음과 같이 구분한다.

| 트래픽 유형 | 방향 |
|---|---|
| 사용자 트래픽 | User → Proxy Node → Web Node |
| DB 트래픽 | Web Node → DB Node |
| SSH 관리 트래픽 | Control Node → 각 관리 대상 노드 |
| 백업 트래픽 | Backup Node → Web Node / DB Node |
| 모니터링 트래픽 | Monitoring Node → 수집 대상 노드 |

---

## 11. 추가 결정 사항: 서브넷 분리 설계

프로젝트 설명용 서브넷 설계는 192.168.4.0/24 대역을 /26 단위로 나누는 방향으로 정리하였다.

| Subnet | CIDR | 용도 | 배치 노드 |
|---|---|---|---|
| Management Subnet | 192.168.4.0/26 | SSH / Ansible 관리 | Control Node |
| Service Subnet | 192.168.4.64/26 | 사용자 트래픽 / 웹 서비스 | Proxy Node, Web Node 1, Web Node 2 |
| Database Subnet | 192.168.4.128/26 | DB 통신 전용 | DB Node |
| Operations Subnet | 192.168.4.192/26 | 백업 / 검증 / 모니터링 | Backup Node, Monitoring Node |

설명 기준은 4개 서브넷 분리 구조로 잡되, 실제 구현 중 라우팅 복잡도나 리소스 문제가 발생할 경우 하나의 Private Network 안에서 보안그룹으로 논리 분리하는 방안도 허용한다.

---

## 12. 추가 결정 사항: 멘토링용 작업 순서 압축

멘토링에서는 상세 문서 전체를 보여주기보다 압축된 작업 순서를 중심으로 설명하기로 하였다.

멘토링용 작업 순서는 다음과 같다.

~~~text
1. OpenStack에서 Ubuntu 기반 인스턴스 생성
2. Control / Proxy / Web / DB / Backup Node 역할 분리
3. 네트워크, 라우터, 서브넷, 보안그룹 구성
4. Control Node에서 각 노드 SSH 접속 확인
5. Ansible inventory 구성 및 ansible ping 검증
6. Proxy / Web Node에 Docker 설치
7. DB Node에 MariaDB 직접 설치 및 서비스 구성
8. Web Node에 Custom WordPress 컨테이너 배포
9. Web Node의 WordPress가 DB Node MariaDB에 연결되는지 확인
10. Proxy Node에 HAProxy HTTP Reverse Proxy 구성
11. Proxy Node 경유 WordPress 접속 확인
12. health_check.sh로 서비스 상태 점검
13. backup.sh로 MariaDB dump 및 WordPress files 백업
14. restore.md 기준으로 복구 절차 검증
15. 캡처, 트러블슈팅, 작업일지, 제출 문서 정리
~~~

멘토링에서 확인받을 핵심 질문은 다음과 같다.

| 번호 | 질문 |
|---:|---|
| 1 | Phase 1 범위가 기본 프로젝트 평가 기준에 적절한가? |
| 2 | Proxy / Web / DB / Backup Node 분리 구조가 적절한가? |
| 3 | HAProxy HTTP Reverse Proxy를 Phase 1에 포함해도 되는가? |
| 4 | MariaDB를 DB Node에 직접 설치하는 방식이 적절한가? |
| 5 | Cinder Volume을 DB 원본 저장소가 아니라 백업 저장소로 사용하는 방향이 적절한가? |
| 6 | Prometheus / Grafana를 Phase 2로 분리해도 되는가? |
| 7 | Web Node 2대 + HAProxy Load Balancing을 Phase 3 도전 확장으로 두는 것이 적절한가? |

---

## 13. 추가 결정 사항: 금지 표현 및 문서 검수

문서 전체에서 오래된 구조나 현재 기준과 맞지 않는 표현을 제거하기로 하였다.

검수 대상 표현은 다음과 같다.

~~~text
기존 등급 명칭
MariaDB Container
MariaDB 컨테이너
dandelion-mariadb
docker/compose/db
mariadb:10.11
Nginx
nginx
web-test
중복된 mysqldump 표현
~~~

최종 문구는 다음 기준으로 통일한다.

| 항목 | 최종 표현 |
|---|---|
| DB 구성 | DB Node MariaDB Service |
| DB 설치 | MariaDB 직접 설치 및 서비스 구성 |
| DB 상태 | mariadb service active |
| DB 백업 | MariaDB dump |
| Web 구성 | Custom WordPress Container |
| Proxy 구성 | HAProxy Container |
| 범위 표현 | Phase 1 / Phase 2 / Phase 3 / Out of Scope |


---

## 14. 추가 결정 사항: OpenStack 인스턴스 리소스 산정

금일 추가 논의를 통해 Phase 1 기본 구현에 필요한 OpenStack 인스턴스별 리소스 산정 기준을 정리하였다.

기본 구성은 Control, HAProxy, Web, DB, Backup Node로 분리하며, 각 노드의 역할에 따라 vCPU, Disk, RAM을 차등 할당한다.

| Node | Role | vCPU | Disk | RAM |
|---|---|---:|---:|---:|
| control | Ansible Control Node | 2 Core | 20 GB | 2 GB |
| haproxy | HAProxy Reverse Proxy Node | 1 Core | 15 GB | 1 GB |
| web | Custom WordPress Web Node | 2 Core | 20 GB | 2 GB |
| db | MariaDB Service Node | 2 Core | 20 GB | 4 GB |
| backup | Backup / Validation Node | 1 Core | 80 GB | 2 GB |

기본 Phase 1 구성에 필요한 전체 리소스는 다음과 같다.

| Resource | Total |
|---|---:|
| vCPU | 8 Core |
| Disk | 155 GB |
| RAM | 11 GB |

DB Node는 MariaDB Service를 직접 운영하므로 Web Node보다 높은 RAM을 배정한다.

Backup / Validation Node는 MariaDB dump, WordPress files archive, restore 검증 자료를 보관해야 하므로 가장 큰 Disk 용량을 배정한다.

HAProxy Node는 Reverse Proxy 역할을 담당하는 경량 노드이므로 1 Core / 1 GB RAM 기준으로 산정한다.

Phase 3에서 Web Node 2를 추가할 경우 필요한 추가 리소스는 다음과 같다.

| Additional Node | vCPU | Disk | RAM |
|---|---:|---:|---:|
| web-2 | 2 Core | 20 GB | 2 GB |

Phase 3 확장 시 전체 예상 리소스는 다음과 같다.

| Resource | Total |
|---|---:|
| vCPU | 10 Core |
| Disk | 175 GB |
| RAM | 13 GB |

리소스 산정표는 별도 문서인 docs/resource-plan.md에 정리하고, README.md 및 docs/architecture.md에서 참조하도록 한다.

