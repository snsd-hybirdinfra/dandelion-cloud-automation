<!-- STATUS: COMPLETE -->

# Team Dandelion - Cloud Infrastructure Automation

## 1. 프로젝트 주제

Ansible 기반 클라우드 인프라 자동화 및 운영 최적화 시스템 구축

---

## 2. 프로젝트 개요

본 프로젝트는 OpenStack 기반 클라우드 인프라 환경에서 Ubuntu 인스턴스를 구성하고, Ansible을 활용하여 서버 설정, Docker 설치, Docker Compose 기반 WordPress/MariaDB 서비스 배포, 상태 점검, 백업 및 복구 검증을 자동화하는 것을 목표로 한다.

단순한 서버 생성이나 애플리케이션 배포가 아니라, 반복적인 인프라 운영 작업을 코드화하고, 자동화 결과를 검증 가능한 산출물로 남기는 데 중점을 둔다.

서비스 계층은 Docker Hub 공식 WordPress 이미지를 기반으로 생성한 **Custom WordPress Image**와 **MariaDB Container**를 Docker Compose로 구성한다.

본 프로젝트에서 WordPress는 웹 개발 대상이 아니라, Ansible 기반 배포 자동화, HTTP 상태 점검, MariaDB dump, WordPress files 백업, Restore 검증을 위한 컨테이너 서비스 대상이다.

---

## 3. 핵심 목표

~~~text
OpenStack 인프라 구성
→ Ubuntu 인스턴스 생성
→ SSH 접속 환경 구성
→ Ansible Inventory 작성
→ Ansible Playbook 실행
→ Docker 설치
→ Docker Compose 기반 WordPress/MariaDB 배포
→ WordPress HTTP 접속 확인
→ Health Check
→ MariaDB dump 및 WordPress files 백업
→ Restore 절차 검증
→ GitHub 및 Google Drive 산출물 관리
~~~

---

## 4. 평가 기준 대응 전략

| 평가항목 | 배점 | 프로젝트 대응 방향 |
|------|---:|---|
| 전문성 | 25 | OpenStack 인프라, Ubuntu Instance, Ansible IaC, Docker Compose, Custom WordPress Image, MariaDB 연동, 백업/복구 검증 |
| 차별성 | 25 | 수동 운영 편차 문제를 Ansible 표준화, Dockerfile 기반 이미지 커스터마이징, GitHub Actions 기반 산출물 상태 자동 갱신으로 개선 |
| 완성도 | 25 | SSH 접속, Ansible ping, Playbook 실행, WordPress/MariaDB 배포, Health Check, Backup/Restore 성공 검증 |
| 프로젝트 관리 | 15 | GitHub Repository, 문서화, 팀원별 산출물 분리, 회의록/작업일지/제출자료 관리 |
| 발표 및 시연 | 10 | 인프라 구현 → 자동화 → 서비스 배포 → 상태 점검 → 백업/복구 검증 흐름 중심 시연 |

---

## 5. 팀 구성

| 이름 | 역할 | 담당 영역 |
|-----|---|-------|
| 정주헌 | PM / 아키텍처 | 전체 구조 설계, GitHub 관리, 문서 통합, 발표 흐름 정리 |
| 백서빈 | 클라우드 인프라 | OpenStack 인스턴스, Ubuntu 이미지, 네트워크, 보안그룹, Floating IP 또는 포트포워딩 접속 구성 |
| 이진욱 | 서버 / 가상화 | Linux 기본 설정, Docker 설치, Custom WordPress / MariaDB 컨테이너 구성 |
| 조민석 | Ansible 자동화 | ansible.cfg, inventory.ini, site.yml 작성 및 실행 |
| 박재우 | 모니터링 / 백업 / 검증 | health_check, backup, restore 검증 및 결과 정리 |

---

## 6. 시스템 아키텍처 다이어그램

![System Architecture](./docs/assets/system-architecture.png)

---

## 7. 시스템 구성

본 프로젝트는 A급 필수 구현 기준으로 다음 노드 구조를 사용한다.

~~~text
Control Node
→ Ansible 실행
→ inventory.ini / ansible.cfg / site.yml 관리

Web Node
→ Docker 설치
→ Custom WordPress Image Build
→ WordPress + MariaDB Docker Compose 배포
→ WordPress HTTP 80 서비스 제공

Backup / Validation Node
→ health_check.sh 실행
→ backup.sh 실행 결과 보관
→ MariaDB dump 백업
→ WordPress files 백업
→ restore 절차 검증
~~~

B급 선택 확장에서는 다음 구성을 추가할 수 있다.

~~~text
Proxy Node
→ HAProxy Reverse Proxy
→ HTTPS 443
→ HTTP 80 to HTTPS 443 Redirect

Monitoring Node
→ Prometheus
→ Grafana
→ node_exporter
→ cAdvisor
~~~

---

## 8. 서비스 배포 구조

본 프로젝트는 Docker Hub 공식 WordPress 이미지를 기반으로 커스텀 이미지를 생성하고, MariaDB와 함께 Docker Compose로 배포한다.

| Component | Description |
|--------|-----|
| Custom WordPress Image | Docker Hub 공식 WordPress 이미지를 기반으로 생성한 커스텀 이미지 |
| MariaDB Container | WordPress 데이터 저장을 위한 DB 컨테이너 |
| Docker Compose | WordPress와 MariaDB를 함께 배포하기 위한 서비스 정의 |
| Docker Volumes | WordPress 파일과 MariaDB 데이터를 저장 |
| Backup Script | DB dump와 WordPress 파일 백업 생성 |
| Validation / Backup Node | 백업본 보관, 상태 점검, 복구 절차 검증 |

서비스 구조는 다음과 같다.

~~~text
Web Node
├── Custom WordPress Container
│   └── Base Image: wordpress:php8.2-apache
├── MariaDB Container
│   └── Image: mariadb:10.11
├── wordpress_data volume
└── db_data volume

Backup / Validation Node
├── health_check.sh
├── backup.sh result
├── DB dump backup
├── WordPress files backup
└── restore procedure validation
~~~

---

## 9. 주요 기능

| 구분 | 구현 내용 | 평가 연결 |
|--------|---|---|
| 인프라 구성 | OpenStack 인스턴스, 네트워크, 보안그룹 구성 | 전문성 |
| 접속 구성 | SSH, Floating IP 또는 포트포워딩 기반 접속 검증 | 완성도 |
| IaC 자동화 | Ansible inventory / ansible.cfg / site.yml 구성 | 전문성 / 완성도 |
| 이미지 커스터마이징 | Docker Hub 공식 WordPress 이미지를 기반으로 Custom Image 생성 | 전문성 / 차별성 |
| 서비스 배포 | Docker Compose 기반 WordPress + MariaDB 컨테이너 실행 | 전문성 / 완성도 |
| 상태 점검 | health_check.sh 기반 서버 및 서비스 확인 | 완성도 |
| 백업 / 복구 | MariaDB dump, WordPress files backup, restore 절차 검증 | 완성도 |
| 운영 시나리오 | 리소스 부족, 접속 장애, DB 장애, Backup 실패 등 트러블슈팅 정리 | 전문성 / 완성도 |
| 프로젝트 관리 | GitHub Actions 기반 상태 자동 갱신 | 프로젝트 관리 / 차별성 |

---

## 10. 프로젝트 범위

### A급 필수 구현

| 구분 | 필수 구현 |
|-----|---|
| 인프라 | OpenStack 기반 Ubuntu 인스턴스 생성 |
| 노드 구성 | Control Node, Web Node, Backup / Validation Node 구분 |
| 접속 | SSH 접속 및 포트포워딩 또는 Floating IP 접속 검증 |
| Ansible | ansible.cfg, inventory.ini, site.yml 작성 |
| Ansible 검증 | ansible all -m ping 성공 |
| 서비스 | Docker 설치 및 Docker Compose 실행 |
| 서비스 배포 | Custom WordPress + MariaDB 배포 |
| 접속 검증 | WordPress HTTP 응답 확인 |
| 상태 점검 | health_check.sh 실행 |
| 백업 | MariaDB dump 및 WordPress files archive 생성 |
| 복구 | restore.md 기반 복구 절차 검증 |
| 문서 | 작업 내역, 트러블슈팅, 캡처, 제출자료 정리 |

### B급 선택 확장

| 구분 | 선택 확장 |
|---|---|
| Reverse Proxy | HAProxy 기반 Reverse Proxy 구성 |
| HTTPS | self-signed 인증서 기반 HTTPS 적용 |
| Redirect | HTTP 80 → HTTPS 443 Redirect |
| Storage | Cinder Volume 또는 NFS 백업 저장소 시도 |
| Monitoring | node_exporter, cAdvisor, Prometheus, Grafana 구성 |
| Automation | Ansible roles 구조 분리 |
| Validation | backup / restore 절차 playbook화 |

### B+ Stretch Goal

A급과 B급이 조기에 완료될 경우, OpenStack CLI와 Ansible을 결합한 End-to-End 자동 구축을 시도한다.

~~~text
Ansible 실행
→ OpenStack CLI 기반 Network / Subnet / Router / Security Group 생성
→ Ubuntu Instance 생성
→ Floating IP 또는 접속 정보 확인
→ Inventory 반영
→ 서버 설정 자동화
→ WordPress/MariaDB 배포
→ HAProxy Reverse Proxy 구성
→ Prometheus/Grafana 모니터링 구성
→ Health Check / Backup / Restore 검증
~~~

B+ Stretch Goal은 필수 제출 범위가 아니며, 구현 중 문제가 발생할 경우 A급/B급 결과 중심으로 발표한다.

### C급 제외 범위

- WordPress plugin development
- WordPress theme development
- Custom PHP application development
- DB replication
- DB clustering
- Trove DBaaS 완성 구현
- Kubernetes
- Docker Swarm
- OpenStack Octavia / LBaaS
- Production-level WordPress hardening
- 멀티 Web Node HA
- 오토스케일링
- 운영 수준의 백업 스케줄링
- 실서비스 도메인 및 공인 인증서 적용

---

## 11. 운영 중 발생 가능한 장애 시나리오

구현 후 운영 중 발생 가능한 장애 시나리오는 다음 기준으로 정리한다.

| 시나리오 | 주요 확인 |
|------|---|
| SSH 접속 실패 | SSH Key, 보안그룹, 포트포워딩 확인 |
| 포트포워딩 장애 | 공유기 포트포워딩, 내부 IP, 보안그룹 확인 |
| WordPress 접속 실패 | docker ps, curl, WordPress logs 확인 |
| MariaDB 연결 실패 | DB logs, 환경변수, Docker network 확인 |
| Docker Compose 실패 | docker compose config, docker compose logs 확인 |
| Backup 실패 | backup.sh, df -h, DB logs 확인 |
| Restore 실패 | 백업 파일, volume, 복구 순서 확인 |
| 리소스 부족 | CPU, Memory, Disk, Docker stats 확인 |
| HAProxy 장애 | haproxy.cfg, backend IP, 인증서 확인 |
| Prometheus/Grafana 장애 | exporter, target, dashboard 접속 확인 |
| OpenStack 인스턴스 장애 | server list/show, console log 확인 |

---

## 12. 디렉터리 구조

~~~text
dandelion-cloud-automation/
├── README.md
├── docs/
├── ansible/
├── docker/
│   ├── wordpress/
│   │   ├── Dockerfile
│   │   ├── custom.ini
│   │   └── README.md
│   ├── compose/
│   │   └── docker-compose.yml
│   ├── proxy/
│   │   ├── docker-compose.yml
│   │   └── haproxy.cfg
│   └── monitoring/
│       ├── docker-compose.yml
│       └── prometheus.yml
├── scripts/
├── screenshots/
├── presentation/
├── submission/
├── tools/
└── .github/workflows/
~~~

---

## 13. 문서 목록

| 문서 | 설명 |
|-------|---|
| [Architecture](./docs/architecture.md) | 전체 시스템 아키텍처 |
| [Network Design](./docs/network-design.md) | 클라우드 인프라 및 네트워크 구성 |
| [Server Setup](./docs/server-setup.md) | 서버 및 Docker 구성 |
| [Ansible Automation](./docs/ansible-automation.md) | Ansible 자동화 구성 |
| [Validation Report](./docs/validation-report.md) | 모니터링, 백업, 복구 검증 |
| [Team Task Guide](./docs/team-task-guide.md) | 팀원별 작업 기준 |
| [Pre-Run Checklist](./docs/pre-run-checklist.md) | 실행 전 점검 기준 |
| [Troubleshooting Guide](./docs/troubleshooting.md) | 문제 해결 기준 |
| [Project Runbook](./docs/runbook.md) | 실행 절차 |
| [Scope Control Policy](./docs/scope-control.md) | 필수 구현 / 선택 확장 / 제외 범위 기준 |
| [Mentoring Brief](./docs/mentoring-brief.md) | 멘토링용 프로젝트 현황 요약 |
| [Mentoring Questions](./docs/mentoring-questions.md) | 멘토링 질문 목록 |
| [Final Deliverables Checklist](./docs/final-deliverables.md) | 최종 산출물 체크리스트 |
| [Review Checklist](./docs/review-checklist.md) | 팀원 자료 검수 기준 |
| [Project Status](./docs/project-status.md) | 자동 생성 프로젝트 상태 |
| [Validation Summary](./docs/validation-summary.md) | 자동 검수 결과 |
| [Presentation Outline](./presentation/presentation-outline.md) | 발표 흐름 및 멘트 |
| [Submission Package](./docs/submission-package.md) | Google Drive 최종 제출 산출물 기준 |
| [Custom WordPress Image](./docker/wordpress/README.md) | 커스텀 WordPress 이미지 설명 |

---

## 14. 최종 성공 기준

| 단계 | 성공 기준 |
|---|---|
| 인프라 | OpenStack 기반 Ubuntu 인스턴스 생성 완료 |
| 접속 | Control Node에서 Managed Node SSH 접속 성공 |
| Ansible | ansible all -m ping 성공 |
| 자동화 | ansible-playbook site.yml 실행 성공 |
| 이미지 | Dockerfile 기반 Custom WordPress Image build 성공 |
| 서비스 | WordPress + MariaDB 컨테이너 running 상태 |
| 검증 | WordPress HTTP 응답, health_check, backup, restore 결과 확인 |
| 운영 | 주요 장애 시나리오와 트러블슈팅 절차 정리 |
| 관리 | GitHub 상태표 및 산출물 자동 갱신 확인 |

---

## 15. 구현 일정 기준

| 구분 | 목표 완료일 | 기준 |
|---|---|---|
| A급 필수 구현 | 2026-06-26 | OpenStack, Ubuntu Instance, SSH, Ansible, Docker Compose, WordPress/MariaDB, Health Check, Backup/Restore, 필수 캡처 완료 |
| B급 선택 확장 | 2026-07-10 | HAProxy HTTPS, Cinder/NFS, node_exporter, cAdvisor, Prometheus/Grafana, Playbook 개선 중 가능한 항목 |
| 최종 정리 | 2026-07-14 | 결과보고서, 시연 영상, 소스코드, 작업일지, 회의록, Google Drive 제출자료 정리 |

---

## 16. 프로젝트 핵심 메시지

~~~text
OpenStack 인프라 구성부터 Ansible 자동화, Docker Compose 기반 WordPress/MariaDB 서비스 배포,
상태 점검, DB 및 파일 백업, 복구 절차 검증, 운영 중 장애 시나리오 정리,
GitHub 기반 산출물 관리까지 하나의 인프라 운영 자동화 흐름으로 연결한다.
~~~

<!-- AUTO_STATUS_START -->
## 자동 생성 프로젝트 상태

아래 상태는 팀원이 파일을 push할 때 자동으로 갱신된다.

## 2. 전체 진행률

| 완료 | 전체 | 진행률 |
|---:|---:|---:|
| 17 | 51 | 33% |

## 담당자별 진행 상태

| 영역 | 담당자 | 완료 | 전체 | 진행률 | 상태 |
|---|---|---:|---:|---:|---|
| PM / Architecture | 정주헌 | 12 | 12 | 100% | ✅ 완료 |
| Cloud Infrastructure | 백서빈 | 0 | 5 | 0% | ❌ 미착수 |
| Server / Virtualization | 이진욱 | 0 | 5 | 0% | ❌ 미착수 |
| Ansible Automation | 조민석 | 0 | 9 | 0% | ❌ 미착수 |
| Monitoring / Backup / Validation | 박재우 | 0 | 9 | 0% | ❌ 미착수 |
| Submission Package | 정주헌 | 5 | 11 | 45% | 🟡 진행 중 |

상세 상태는 [Project Status](./docs/project-status.md) 문서에서 확인한다.

<!-- AUTO_STATUS_END -->
