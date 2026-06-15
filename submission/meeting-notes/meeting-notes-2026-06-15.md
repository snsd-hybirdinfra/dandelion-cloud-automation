<!-- STATUS: COMPLETE -->

# Team Dandelion 회의록

## 2026-06-15 회의록

## 1. 회의 정보

| 구분 | 내용 |
|---|---|
| 회의 일자 | 2026-06-15 |
| 회의 구분 | 서비스 구조 변경 및 확장 범위 재정리 |
| 회의 장소 | ZEP 팀 회의실 / Discord |
| 작성자 | 정주헌 |
| 참석자 | 정주헌, 백서빈, 이진욱, 조민석, 박재우 |

---

## 2. 회의 목적

- 기존 단일 웹서버 컨테이너 구조 재검토
- Docker Hub 기본 이미지를 활용한 커스텀 서비스 구조 확정
- WordPress + MariaDB 기반 서비스 구성 방향 정리
- DB 볼륨 및 백업 저장 위치 기준 확정
- 강사 피드백에 따른 LB / Reverse Proxy 구성 검토
- 모니터링 확장 범위 정리
- README 및 architecture 문서 수정 방향 정리

---

## 3. 주요 논의 내용

### 3.1 서비스 구조 변경

기존에는 Docker 기반 단일 웹서버 컨테이너 배포를 A급 서비스 대상으로 검토하였다.  
그러나 백업/복구 검증의 의미와 Docker Hub 이미지 활용, Dockerfile 기반 커스텀 이미지 작성 근거를 강화하기 위해 서비스 대상을 변경하기로 하였다.

변경된 서비스 기준은 다음과 같다.

| 구분 | 기존 방향 | 변경 방향 |
|---|---|---|
| 웹 서비스 | 단일 웹서버 컨테이너 | Custom WordPress Container |
| DB 구성 | 없음 | MariaDB Container |
| 배포 방식 | Docker run 또는 단순 컨테이너 실행 | Docker Compose |
| 이미지 활용 | 기본 웹서버 이미지 | Docker Hub 공식 WordPress 이미지 기반 커스텀 이미지 |
| 백업 대상 | 정적 파일 중심 | MariaDB dump + WordPress files |
| 복구 검증 | 제한적 | DB 및 파일 백업 기반 복구 절차 검증 |

이에 따라 프로젝트의 서비스 기준은 Custom WordPress + MariaDB로 변경한다.

---

### 3.2 Custom WordPress Image 기준 확정

WordPress 이미지는 Docker Hub 공식 이미지를 그대로 실행하는 방식이 아니라, 공식 이미지를 Base Image로 사용하여 운영 설정 수준의 커스터마이징을 적용하기로 하였다.

| 항목 | 기준 |
|---|---|
| Base Image | wordpress:php8.2-apache |
| Custom File | Dockerfile, custom.ini |
| Custom Scope | PHP upload size, memory limit, execution time 등 운영 설정 |
| 제외 범위 | WordPress plugin 개발, theme 개발, PHP 웹 애플리케이션 개발 |

본 프로젝트에서 WordPress는 웹 개발 대상이 아니라, Ansible 기반 배포 자동화와 백업/복구 검증을 위한 컨테이너 서비스 대상으로 사용한다.

---

### 3.3 DB 배치 및 백업 기준

MariaDB는 Web Node 내에서 WordPress와 함께 Docker Compose로 실행한다.  
DB 원본 볼륨은 Web Node에 두고, Backup / Validation Node에는 원본 볼륨을 직접 두지 않는다.

| 구분 | 위치 | 기준 |
|---|---|---|
| WordPress Container | Web Node | 외부 HTTP 서비스 제공 |
| MariaDB Container | Web Node | WordPress 데이터 저장 |
| DB 원본 볼륨 | Web Node | 운영 데이터 원본 |
| WordPress files volume | Web Node | WordPress 파일 데이터 |
| DB dump 백업본 | Backup / Validation Node | 백업 파일 보관 |
| WordPress files 백업본 | Backup / Validation Node | 백업 파일 보관 |

DB 볼륨을 Backup / Validation Node에 직접 두는 방식은 NFS, 권한, 파일 락, 네트워크 장애 문제로 인해 기본 프로젝트 범위에서는 제외한다.

---

### 3.4 LB / Reverse Proxy 구성 검토

강사 피드백에 따라 LB 구성을 검토하였다.  
단, OpenStack Octavia / LBaaS나 멀티 Web Node 기반 HA 구성은 범위가 크기 때문에 제외한다.

대신 B급 선택 확장으로 WordPress 서비스용 HAProxy 기반 Reverse Proxy를 구성하는 방향을 검토한다.

| 구분 | 기준 |
|---|---|
| Reverse Proxy 대상 | Web Node의 WordPress HTTP 서비스 |
| Reverse Proxy 방식 | HAProxy Container |
| HTTPS 처리 | HAProxy에서 TLS Termination |
| HTTP 처리 | 80 → 443 Redirect |
| Backend | Web Node WordPress HTTP 80 |
| 확장 의미 | 향후 다중 Web Node LB 구조로 확장 가능 |

정확한 표현은 “WordPress 기반 리버스 프록시”가 아니라 “WordPress 서비스용 HAProxy 기반 Reverse Proxy”로 정리한다.

---

### 3.5 모니터링 확장 범위 정리

모니터링 도구는 A급 필수가 아니라 B급 선택 확장으로 분류한다.

| 도구 | 역할 | 배치 기준 | 등급 |
|---|---|---|---|
| health_check.sh | 기본 상태 점검 | Backup / Validation Node | A급 |
| docker ps / curl | 컨테이너 및 HTTP 확인 | Web Node / Control Node | A급 |
| node_exporter | 서버 OS 메트릭 수집 | Web Node 또는 Monitoring Node | B급 |
| cAdvisor | 컨테이너 메트릭 수집 | Web Node | B급 |
| Prometheus | 메트릭 수집 | Backup / Validation / Monitoring Node | B급 |
| Grafana | 대시보드 시각화 | Backup / Validation / Monitoring Node | B급 |

A급 완료 전에는 Prometheus, Grafana, node_exporter, cAdvisor 구현을 필수로 진행하지 않는다.

---

## 4. 노드 구조 변경

최종 노드 구조는 다음 방향으로 정리한다.

| 노드 | 역할 |
|---|---|
| Control Node | Ansible 실행, Inventory / Playbook 관리 |
| Web Node | Custom WordPress + MariaDB 서비스 운영 |
| Backup / Validation / Monitoring Node | Health Check, Backup, Restore, Monitoring 확장 |
| LB / Reverse Proxy Node | HAProxy 기반 HTTPS Reverse Proxy, B급 선택 확장 |

A급에서는 Control Node, Web Node, Backup / Validation Node 중심으로 구현한다.  
LB / Reverse Proxy Node는 강사 피드백 반영 항목으로 B급 확장에서 검토한다.

---

## 5. 문서 수정 결정

서비스 구조가 변경됨에 따라 기존 wordpress 기준 문서를 Custom WordPress + MariaDB 기준으로 수정한다.

| 문서 | 수정 내용 |
|---|---|
| README.md | wordpress 기준 제거, Custom WordPress + MariaDB 기준 반영 |
| docs/architecture.md | Web Node 구조, DB 볼륨, Backup Node 역할 수정 |
| docs/scope-control.md | A급/B급/C급 범위 재정의 |
| docs/server-setup.md | Docker Compose 기반 WordPress/MariaDB 구성 반영 |
| docs/ansible-automation.md | Docker Compose 배포 자동화 흐름 반영 |
| docs/validation-report.md | DB dump, WordPress files backup 기준 반영 |
| presentation/presentation-outline.md | 발표 흐름을 WordPress/MariaDB 기준으로 수정 |

---

## 6. 결정 사항

| 번호 | 결정 내용 |
|---:|---|
| 1 | 단일 웹서버 컨테이너는 사용하지 않는다. |
| 2 | 서비스 기준은 Custom WordPress + MariaDB로 변경한다. |
| 3 | WordPress 이미지는 Docker Hub 공식 이미지를 기반으로 커스텀한다. |
| 4 | 커스터마이징 범위는 운영 설정 수준으로 제한한다. |
| 5 | MariaDB는 Web Node에서 WordPress와 함께 Docker Compose로 실행한다. |
| 6 | DB 원본 볼륨은 Web Node에 두고, 백업본만 Backup / Validation Node로 전송한다. |
| 7 | Prometheus, Grafana, node_exporter, cAdvisor는 B급 선택 확장으로 둔다. |
| 8 | 강사 피드백을 반영하여 HAProxy 기반 Reverse Proxy를 B급 확장으로 검토한다. |
| 9 | OpenStack Octavia / LBaaS, 멀티 Web Node HA, Auto Scaling은 C급 제외 범위로 유지한다. |
| 10 | README와 architecture 문서를 현재 구조에 맞게 수정한다. |

---

## 7. 다음 작업 계획

| 담당자 | 다음 작업 |
|---|---|
| 정주헌 | README.md, architecture.md, scope-control.md 구조 수정 및 발표 흐름 반영 |
| 백서빈 | OpenStack 네트워크, 보안그룹, Floating IP 구성 기준 정리 |
| 이진욱 | Dockerfile, custom.ini, docker-compose.yml 기반 WordPress/MariaDB 구성 준비 |
| 조민석 | Ansible Playbook에서 Docker 설치 및 Compose 배포 자동화 방향 정리 |
| 박재우 | health_check.sh, backup.sh, restore.md를 WordPress/MariaDB 기준으로 수정 |

---

## 8. 회의 결과 요약

2026년 6월 15일 회의에서는 기존 단일 웹서버 컨테이너 기반 서비스 구조를 폐기하고, Docker Hub 공식 WordPress 이미지를 기반으로 한 Custom WordPress Image와 MariaDB Container를 Docker Compose로 배포하는 구조로 변경하였다.

또한 DB 원본 볼륨은 Web Node에 두고, DB dump 및 WordPress files 백업본만 Backup / Validation Node로 전송하는 구조를 확정하였다.

강사 피드백을 반영하여 HAProxy 기반 Reverse Proxy와 HTTPS 적용은 B급 선택 확장으로 검토하기로 하였으며, Prometheus, Grafana, node_exporter, cAdvisor 역시 A급 완료 후 진행 가능한 B급 모니터링 확장으로 분류하였다.

---

## 9. 추가 결정 사항: 접속 방식 및 OpenStack CLI 기반 구축 목표

금일 추가 논의를 통해 외부 접속 방식과 최종 구축 목표를 다음과 같이 정리하였다.

### 9.1 포트포워딩 기반 접속 기준

실습 환경의 외부 접근 제약을 고려하여, 초기 접속 검증은 공유기 포트포워딩 기반으로 진행한다.

| 구분 | 접속 대상 | 기준 |
|---|---|---|
| SSH | Control Node / Web Node / Backup-Validation Node | 공유기 포트포워딩을 통한 SSH 접속 검증 |
| HTTP | WordPress Service | Web Node 또는 Reverse Proxy Node로 HTTP 접속 검증 |
| HTTPS | HAProxy Reverse Proxy | B급 확장 시 443 포트 기반 HTTPS 접속 검증 |
| Monitoring | Grafana / Prometheus | B급 확장 시 관리자 접근 대역 기준으로 제한 |

포트포워딩은 실습 환경에서 외부 접속 가능성을 확보하기 위한 접근 방식이며, 운영 환경에서는 Floating IP, 보안그룹, Bastion 또는 LB 기반 접근 구조로 확장 가능하도록 문서화한다.

### 9.2 OpenStack CLI 기반 노드 구축 목표

최종 목표는 Horizon 대시보드 수동 생성에만 의존하지 않고, OpenStack CLI 명령어를 통해 노드 생성 및 네트워크 구성을 수행하는 것이다.

| 단계 | 목표 |
|---|---|
| 네트워크 생성 | openstack network create 명령 기반 네트워크 생성 |
| 서브넷 생성 | openstack subnet create 명령 기반 서브넷 생성 |
| 라우터 구성 | openstack router create / router add subnet 명령 기반 라우팅 구성 |
| 보안그룹 구성 | openstack security group rule create 명령 기반 포트 정책 구성 |
| 인스턴스 생성 | openstack server create 명령 기반 Control/Web/Backup 노드 생성 |
| Floating IP 연결 | openstack floating ip create / server add floating ip 명령 기반 외부 접속 구성 |

이를 통해 프로젝트는 단순 대시보드 기반 구축이 아니라, 명령어 기반 인프라 구성과 Ansible 기반 서버 자동화를 연결하는 구조로 확장한다.

### 9.3 수정된 최종 구현 흐름

~~~text
공유기 포트포워딩 기반 접속 검증
→ OpenStack CLI 기반 네트워크 / 보안그룹 / 인스턴스 생성
→ Control Node에서 Ansible 실행
→ Web Node에 Docker / Custom WordPress / MariaDB 배포
→ Backup / Validation Node에서 Health Check / Backup / Restore 검증
→ B급 확장으로 HAProxy Reverse Proxy / HTTPS / Monitoring 구성
~~~


---

## 11. 추가 결정 사항: 백서빈 담당 Ubuntu 인스턴스 구성 추가

금일 추가 논의를 통해 Cloud Infrastructure 담당자인 백서빈의 작업 범위에 Ubuntu 기반 인스턴스 구성 작업을 추가하였다.

OpenStack 환경에서는 운영체제를 직접 설치하는 방식이 아니라, Ubuntu 이미지를 기반으로 인스턴스를 생성하고 부팅 및 접속 상태를 확인하는 방식으로 진행한다.

| 담당자 | 추가 작업 | 산출물 |
|---|---|---|
| 백서빈 | Ubuntu 이미지 기반 인스턴스 생성 | 인스턴스 생성 캡처 |
| 백서빈 | Ubuntu 인스턴스 부팅 상태 확인 | ACTIVE 상태 캡처 |
| 백서빈 | Floating IP 연결 | FIP 할당 캡처 |
| 백서빈 | SSH 접속 확인 | SSH 접속 성공 캡처 |
| 백서빈 | Ubuntu 버전 확인 | lsb_release 또는 /etc/os-release 캡처 |

Ubuntu 인스턴스 구성은 이후 Ansible 자동화, Docker 설치, WordPress/MariaDB 배포가 진행될 기반 노드로 사용한다.

