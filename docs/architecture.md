<!-- STATUS: COMPLETE -->

# System Architecture

## 1. Architecture Overview

본 프로젝트는 Ansible Control Node를 중심으로 OpenStack 기반 클라우드 인프라 서버의 초기 설정, Docker 기반 서비스 배포, 상태 점검, 백업 및 복구 검증을 자동화하는 구조로 설계한다.

서비스 계층은 단순 웹서버 컨테이너가 아니라, Docker Hub 공식 WordPress 이미지를 기반으로 생성한 **Custom WordPress Image**와 **MariaDB Container**를 Docker Compose로 구성한다.

WordPress는 웹 개발 대상이 아니라, Ansible 기반 배포 자동화, 서비스 상태 점검, DB 백업, 파일 백업, 복구 절차 검증을 위한 컨테이너 서비스 대상이다.

정주헌은 PM / Architecture 담당으로서 전체 시스템 구조를 설계하고, 팀원별 작업 범위를 정의하며, 클라우드 인프라 구성부터 검증 단계까지 하나의 운영 자동화 흐름으로 연결되도록 통합 관리한다.

---

## 2. Architecture Goal

본 아키텍처의 목표는 다음과 같다.

| 목표 | 설명 |
|---|---|
| 자동화 중심 구조 | 반복적인 서버 설정 작업을 Ansible Playbook으로 자동화 |
| 서비스 현실성 확보 | Custom WordPress + MariaDB 기반 최소 웹서비스 구성 |
| 역할 분리 | 클라우드, 서버, 자동화, 검증 담당을 분리하여 작업 명확화 |
| 검증 가능성 확보 | 단순 구축이 아니라 상태 점검, 백업, 복구 결과까지 확인 |
| 산출물 관리 | GitHub와 Google Drive를 분리하여 코드, 문서, 제출자료 관리 |
| 발표 흐름 정리 | 각 담당자의 작업이 하나의 시스템 흐름으로 보이도록 구성 |

---

## 3. Logical Architecture

~~~text
[PM / Architecture]
        |
        | 전체 구조 설계 / 작업 범위 정의 / 산출물 통합
        v
[GitHub Repository] <---- 관리 / 연동 ----> [PM / Architecture] <---- 관리 / 연동 ----> [Google Drive]
        |
        | 코드 / 문서 / 자동 검증
        v
+--------------------------------------------------------------------------------+
| OpenStack Cloud Environment                                                     |
|                                                                                |
|  [Network / Security]                                                           |
|   - VPC / Network                                                               |
|   - Subnet                                                                      |
|   - Router                                                                      |
|   - Security Group                                                              |
|   - Floating IP                                                                 |
|                                                                                |
|  [Control Node]                                                                 |
|   - Ansible Control                                                             |
|   - Inventory / Playbook 관리                                                   |
|   - SSH Key 관리                                                                |
|   - 자동화 실행 및 로그 확인                                                    |
|                                                                                |
|  [Web Node]                                                                     |
|   - Docker 설치                                                                 |
|   - Custom WordPress Image Build                                                |
|   - WordPress + MariaDB 배포                                                     |
|   - 웹 서비스 운영 HTTP 80                                                      |
|   - WordPress files volume                                                      |
|   - MariaDB data volume                                                         |
|                                                                                |
|  [Backup / Validation Node]                                                     |
|   - Health Check 실행                                                           |
|   - Backup Script 실행                                                          |
|   - DB dump 백업본 저장                                                         |
|   - WordPress files 백업본 저장                                                 |
|   - Restore 절차 검증                                                           |
|                                                                                |
|  [Shared Resources]                                                             |
|   - Image                                                                       |
|   - Volume                                                                      |
|   - Key Pair                                                                    |
|   - Floating IP                                                                 |
+--------------------------------------------------------------------------------+
~~~

---

## 4. Component Description

| 구성 요소 | 역할 | 담당 |
|---|---|---|
| Cloud Infrastructure | OpenStack 서버, 네트워크, 라우터, 보안그룹, Floating IP 구성 | 백서빈 |
| Control Node | Ansible 설치 및 Playbook 실행 | 조민석 |
| Web Node | Docker 설치, Custom WordPress Image Build, WordPress + MariaDB 실행 | 이진욱 |
| Backup / Validation Node | 상태 점검, 백업본 저장, 복구 절차 검증 | 박재우 |
| Ansible Inventory | 관리 대상 서버 정보 정의 | 조민석 |
| Ansible Playbook | 서버 설정 및 서비스 배포 자동화 | 조민석 |
| Custom WordPress Image | Docker Hub 공식 WordPress 이미지를 기반으로 생성한 커스텀 이미지 | 이진욱 / 조민석 |
| MariaDB Container | WordPress 데이터 저장용 DB 컨테이너 | 이진욱 |
| Docker Compose | WordPress와 MariaDB를 함께 배포하기 위한 서비스 정의 | 이진욱 / 조민석 |
| Health Check | 서버 및 WordPress HTTP 응답 상태 확인 | 박재우 |
| Backup / Restore | MariaDB dump, WordPress files 백업, 복구 절차 검증 | 박재우 |
| Documentation / Presentation | 문서 통합, 산출물 관리, 발표 흐름 정리 | 정주헌 |

---

## 5. Automation Flow

~~~text
1. Cloud Infrastructure Provisioning
   ↓
2. Network / Security Group Configuration
   ↓
3. SSH Access Configuration
   ↓
4. Ansible Inventory Configuration
   ↓
5. Ansible Playbook Execution
   ↓
6. Docker Installation
   ↓
7. Custom WordPress Image Build
   ↓
8. WordPress + MariaDB Deployment by Docker Compose
   ↓
9. WordPress HTTP Health Check
   ↓
10. MariaDB Dump Backup
   ↓
11. WordPress Files Backup
   ↓
12. Backup Transfer to Backup / Validation Node
   ↓
13. Restore Procedure Validation
   ↓
14. Documentation / Presentation
~~~

---

## 6. Team Role Mapping

| 이름 | 역할 | 주요 산출물 |
|---|---|---|
| 정주헌 | PM / Architecture | README.md, architecture.md, scope-control.md, presentation outline |
| 백서빈 | Cloud Infrastructure | network-design.md, cloud-infra screenshots |
| 이진욱 | Server / Virtualization | server-setup.md, Docker / WordPress screenshots |
| 조민석 | Ansible Automation | ansible.cfg, inventory.ini, site.yml, playbook result screenshots |
| 박재우 | Monitoring / Backup / Validation | health_check.sh, backup.sh, restore.md, validation-report.md |

---

## 7. Design Boundary

| 포함 범위 | 제외 범위 |
|---|---|
| Ansible 기반 서버 설정 자동화 | Kubernetes 기반 대규모 오케스트레이션 |
| Docker Compose 기반 WordPress + MariaDB 배포 | Docker Swarm |
| Custom WordPress Image 생성 | WordPress plugin 개발 |
| MariaDB 컨테이너 연동 | WordPress theme 개발 |
| WordPress HTTP 상태 점검 | 복잡한 PHP 웹 애플리케이션 개발 |
| MariaDB dump 백업 | DB replication |
| WordPress files 백업 | DB clustering |
| 백업 및 복구 절차 검증 | 실시간 DR 자동 전환 |
| GitHub 기반 산출물 관리 | 상용 CI/CD 파이프라인 전체 구축 |

---

## 8. Final Architecture Summary

~~~text
Cloud Infrastructure
→ Control Node
→ Ansible Inventory
→ Ansible Playbook
→ Web Node
→ Custom WordPress + MariaDB Service
→ Health Check
→ DB Dump Backup
→ WordPress Files Backup
→ Backup / Validation Node
→ Restore Procedure Validation
~~~

---

## 9. System Architecture Diagram

![System Architecture](./assets/system-architecture.png)

본 다이어그램은 Team Dandelion 프로젝트의 전체 시스템 구조를 나타낸다.

- GitHub Repository를 통한 코드 및 문서 관리
- Google Drive를 통한 중간 산출물 및 최종 제출 자료 관리
- OpenStack 기반 클라우드 인프라 구성
- Control Node에서 Ansible 자동화 실행
- Web Node에 Custom WordPress + MariaDB 서비스 배포
- Backup / Validation Node를 통한 Health Check, Backup, Restore 기반 운영 검증

