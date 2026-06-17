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

WordPress files 자동 동기화, DB Clustering, OpenStack LBaaS / Octavia는 Phase 3 구현 범위에서 제외한다. 단, DB Replication / DB Node 이중화 및 DB Node 이중화는 멘토링 이후 추후 확장 방향으로 검토한다.

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



---

## 15. 추가 결정 사항: 멘토링 결과 기반 DB Node 이중화 확장 방향

멘토링 진행 결과, 현재 프로젝트의 기본 구현 범위에서는 단일 DB Node를 유지하되, 추후 확장 방향으로 DB Node 이중화를 검토하기로 하였다.

현재 Phase 기준에서 DB Node는 MariaDB를 직접 설치하여 systemd 서비스로 운영하는 단일 DB 구조이다.

다만 서비스 안정성 및 운영 확장성을 고려할 경우, 향후에는 DB Node를 이중화하여 장애 발생 시 데이터 계층의 가용성을 높이는 방향이 필요하다는 피드백을 반영하였다.

| 구분 | 현재 기준 | 추후 확장 방향 |
|---|---|---|
| DB 구성 | 단일 DB Node | DB Node 이중화 |
| DB 서비스 | MariaDB 직접 설치 + systemd Service | MariaDB Replication 또는 Primary / Replica 구조 |
| 장애 대응 | DB Node 장애 시 수동 복구 | Replica DB 또는 Failover 구조 검토 |
| 백업 | MariaDB dump 기반 백업 | Dump 백업 + 이중화 기반 복구 전략 |
| 프로젝트 반영 | Phase 1 필수 범위 | Post-Phase 확장 방향 |

본 프로젝트에서는 일정과 구현 안정성을 고려하여 Phase 1~3 범위에서는 단일 DB Node 구조를 유지한다.

단, 발표 및 최종 문서에서는 “현재 한계 및 향후 개선 방향” 항목에 DB Node 이중화를 포함하여, 단일 DB 구조의 한계와 확장 가능성을 설명하기로 하였다.

향후 DB 이중화 후보 구조는 다음과 같다.

| 확장 방식 | 설명 |
|---|---|
| MariaDB Primary / Replica | Primary DB에서 Replica DB로 데이터 복제 |
| Backup 기반 복구 고도화 | MariaDB dump와 restore 절차를 자동화하여 복구 시간 단축 |
| DB Failover 구조 검토 | 장애 시 Replica 또는 대체 DB Node로 전환하는 구조 검토 |
| Monitoring 연계 | DB 상태를 Prometheus / Grafana와 연계하여 장애 감지 |

최종 정리 기준은 다음과 같다.

~~~text
Phase 1:
단일 DB Node + MariaDB Service + Backup / Restore 검증

Phase 2:
Monitoring 및 Backup 고도화

Phase 3:
Web Node 2대 + HAProxy Load Balancing

Post-Phase Extension:
DB Node 이중화 / MariaDB Replication / DB Failover 검토
~~~


---

## 16. 추가 결정 사항: 금일 팀원별 작업 진행 현황 정리

금일은 멘토링 이후 정리된 Phase 기반 구조를 바탕으로 각 담당자별 실제 구축 작업을 진행하였다.

전체 구조는 Control / HAProxy / Web / DB / Backup Node 기준으로 유지하며, 세부 구축은 서비스 담당과 자동화 담당, 검증 담당 중심으로 진행하였다.

### 16.1 백서빈 작업 현황

백서빈은 OpenStack 인프라 담당으로 보안그룹 및 서브넷 구성을 진행하였다.

현재 4개 서브넷 중 3개 서브넷에 대한 구성 및 검증을 완료하였으며, Backup / Validation 관련 서브넷 또는 인스턴스가 정상적으로 올라가지 않는 문제를 조치 중이다.

| 항목 | 진행 상태 |
|---|---|
| 보안그룹 생성 | 진행 완료 |
| 서브넷 생성 | 4개 중 3개 완료 |
| 인스턴스 생성 | 일부 완료 |
| 검증 / 복구 서브넷 인스턴스 | 생성 또는 부팅 문제 조치 중 |
| 후속 작업 | 원인 확인 후 인스턴스 재생성 또는 네트워크 설정 점검 |

확인할 항목은 다음과 같다.

~~~text
1. 서브넷 CIDR 중복 여부
2. 라우터 연결 여부
3. 보안그룹 SSH / HTTP / DB 포트 허용 여부
4. 인스턴스 flavor 리소스 부족 여부
5. Floating IP 또는 포트포워딩 접속 가능 여부
6. 인스턴스 ACTIVE 상태 확인
~~~

---

### 16.2 이진욱 작업 현황

이진욱은 서버 초기 환경 구성 및 노드별 패키지 설치 기준을 정리하였다.

노드별 리소스 기준은 다음과 같이 정리하였다.

| Node | vCPU | Disk | RAM |
|---|---:|---:|---:|
| control | 2 Core | 20 GB | 2 GB |
| haproxy | 1 Core | 15 GB | 2 GB |
| web | 2 Core | 20 GB | 2 GB |
| db | 2 Core | 20 GB | 4 GB |
| backup | 1 Core | 80 GB | 2 GB |

기존 리소스 산정에서 HAProxy Node RAM은 1 GB로 검토하였으나, 실제 구성 안정성을 고려하여 2 GB로 조정 가능성을 반영한다.

이진욱이 정리한 공통 초기 설정은 다음과 같다.

~~~text
1. sudoers 파일에 user1 NOPASSWD 권한 추가
2. 모든 노드 공통 패키지 설치
   - vim
   - curl
   - wget
3. Control Node에 Ansible 설치
4. HAProxy Node에 HAProxy 또는 Docker 설치
5. Web Node에 Docker 설치
6. DB Node에 mariadb-server 설치
7. Backup Node에 mariadb-client 설치
~~~

최종 기준은 다음과 같이 정리한다.

| Node | 설치 기준 |
|---|---|
| control | ansible |
| haproxy | docker 또는 haproxy container 실행 환경 |
| web | docker, docker compose plugin |
| db | mariadb-server, systemd service |
| backup | mariadb-client, backup.sh, health_check.sh |

---

### 16.3 조민석 작업 현황

조민석은 Ansible 자동화 담당으로 inventory.ini 및 ansible.cfg 구성을 진행하였다.

현재 inventory는 proxy, web, db, backup 그룹을 분리하고 managed 그룹으로 묶는 구조로 작성되었다.

~~~text
[proxy]
proxy-node ansible_host=PROXY_NODE_PRIVATE_IP

[web]
web-node ansible_host=WEB_NODE_PRIVATE_IP

[db]
db-node ansible_host=DB_NODE_PRIVATE_IP

[backup]
backup-node ansible_host=BACKUP_NODE_PRIVATE_IP

[managed:children]
proxy
web
db
backup
~~~

ansible.cfg는 inventory.ini를 기본 inventory로 사용하고, remote_user와 SSH key, become 설정을 포함하는 구조로 작성되었다.

후속 작업은 실제 OpenStack 인스턴스의 Private IP를 inventory에 반영하고, Control Node에서 ansible ping을 수행하는 것이다.

~~~text
ansible all -m ping
ansible managed -m ping
~~~

확인할 항목은 다음과 같다.

| 항목 | 확인 기준 |
|---|---|
| inventory IP | 실제 노드 Private IP 반영 |
| SSH Key | Control Node에서 접근 가능한 키 사용 |
| remote_user | ubuntu 또는 실제 접속 사용자와 일치 |
| become | sudo 권한 정상 동작 |
| ping 검증 | ansible all -m ping 성공 |

---

### 16.4 박재우 작업 현황

박재우는 검증 및 백업 담당으로 healthcheck-example.sh와 backup.sh 초안을 작성하였다.

healthcheck-example.sh는 web1, web2, db, proxy, backup 노드에 대해 ping, curl, ssh 기반 상태 확인을 수행하는 구조로 작성되었다.

backup.sh는 DB Node에 SSH 접속하여 mysqldump를 수행하고 날짜별 백업 디렉터리에 SQL 백업 파일을 저장하는 구조로 작성되었다.

현재 스크립트는 초안 단계이므로 최종 아키텍처 기준에 맞게 다음 항목을 수정한다.

| 항목 | 현재 초안 | 수정 방향 |
|---|---|---|
| DB 서비스명 | mysqld | mariadb |
| Proxy 점검 | systemctl haproxy | HAProxy Container 기준 또는 최종 실행 방식 기준으로 정리 |
| Web2 재시작 | root@web1에서 web2 restart | root@web2에서 web2 restart로 수정 |
| 백업 경로 | /tmp/YYYY-MM-DD | /backup/YYYY-MM-DD 또는 제출 기준 경로 |
| DB 인증정보 | 사용자이름 / 비밀번호 placeholder | 실제 테스트 계정 또는 변수화 |
| SSH 사용자 | root | ubuntu 또는 실제 운영 사용자 기준 정리 |

검증 담당 후속 작업은 다음과 같다.

~~~text
1. healthcheck-example.sh를 현재 노드명과 서비스명에 맞게 수정
2. backup.sh 백업 저장 경로를 /backup 기준으로 수정
3. DB 접속 계정 및 비밀번호 변수화
4. MariaDB dump 파일 생성 여부 검증
5. WordPress files archive 추가
6. restore.md 기준 복구 절차와 연결
~~~

---

### 16.5 금일 진행 요약

| 담당자 | 주요 작업 | 상태 |
|---|---|---|
| 백서빈 | 보안그룹 및 서브넷 생성, 인스턴스 구성 | 4개 중 3개 구성 완료, Backup / Validation 관련 인스턴스 문제 조치 중 |
| 이진욱 | 노드별 환경 구성 및 패키지 설치 기준 정리 | 진행 |
| 조민석 | inventory.ini, ansible.cfg 작성 | 초안 작성 완료 |
| 박재우 | healthcheck-example.sh, backup.sh 작성 | 초안 작성 완료, 현재 구조 기준 수정 필요 |
| 정주헌 | 회의록, 작업일지, 문서 기준 정리 및 구조 검수 | 진행 |

