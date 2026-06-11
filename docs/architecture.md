# System Architecture

## 1. Architecture Overview

본 프로젝트는 Ansible Control Node를 중심으로 클라우드 인프라 서버의 초기 설정, Docker 기반 서비스 배포, 상태 점검, 백업 및 복구 검증을 자동화하는 구조로 설계한다.

정주헌은 PM / 아키텍처 담당으로서 전체 시스템 구조를 설계하고, 팀원별 작업 범위를 정의하며, 클라우드 인프라 구성부터 검증 단계까지 하나의 운영 자동화 흐름으로 연결되도록 통합 관리한다.

## 2. Architecture Goal

본 아키텍처의 목표는 다음과 같다.

| 목표 | 설명 |
|---|---|
| 자동화 중심 구조 | 반복적인 서버 설정 작업을 Ansible Playbook으로 자동화 |
| 역할 분리 | 클라우드, 서버, 자동화, 검증 담당을 분리하여 작업 명확화 |
| 검증 가능성 확보 | 단순 구축이 아니라 상태 점검, 백업, 복구 결과까지 확인 |
| 발표 흐름 정리 | 각 담당자의 작업이 하나의 시스템 흐름으로 보이도록 구성 |

## 3. Logical Architecture

~~~text
[PM / Architecture: 정주헌]
        |
        | 전체 구조 설계 / 작업 범위 정의 / 산출물 통합
        v
[Control Node: Ansible 실행 서버]
        |
        | SSH Key 기반 자동화
        v
+------------------------------------------------+
| Managed Nodes                                  |
|                                                |
|  [Web Node]                                    |
|   - Docker 설치 대상                           |
|   - Nginx 컨테이너 실행 대상                   |
|                                                |
|  [Backup / Validation Node]                    |
|   - 상태 점검 대상                             |
|   - 백업 및 복구 검증 대상                     |
+------------------------------------------------+
~~~

## 4. Component Description

| 구성 요소 | 역할 | 담당 |
|---|---|---|
| Cloud Infrastructure | 서버, 네트워크, 보안그룹 구성 | 백서빈 |
| Control Node | Ansible 설치 및 Playbook 실행 | 조민석 |
| Managed Node | Docker, Nginx, 백업/검증 대상 | 이진욱 / 박재우 |
| Ansible Inventory | 관리 대상 서버 정보 정의 | 조민석 |
| Ansible Playbook | 서버 설정 및 서비스 배포 자동화 | 조민석 |
| Docker / Nginx | 컨테이너 기반 웹 서비스 실행 | 이진욱 |
| Health Check | 서버 및 서비스 상태 확인 | 박재우 |
| Backup / Restore | 백업 생성 및 복구 검증 | 박재우 |
| Documentation / Presentation | 문서 통합 및 발표 흐름 정리 | 정주헌 |

## 5. Automation Flow

~~~text
1. Cloud Infrastructure Provisioning
   ↓
2. SSH Access Configuration
   ↓
3. Linux Basic Package Setup
   ↓
4. Docker Installation
   ↓
5. Nginx Container Deployment
   ↓
6. Health Check
   ↓
7. Backup Execution
   ↓
8. Recovery Validation
   ↓
9. Documentation / Presentation
~~~

## 6. Team Role Mapping

| 이름 | 역할 | 주요 산출물 |
|---|---|---|
| 정주헌 | PM / Architecture | README.md, architecture.md, presentation outline |
| 백서빈 | Cloud Infrastructure | network-design.md, cloud-infra screenshots |
| 이진욱 | Server / Virtualization | server-setup.md, Docker/Nginx screenshots |
| 조민석 | Ansible Automation | ansible.cfg, inventory.ini, site.yml |
| 박재우 | Monitoring / Backup / Validation | health_check.sh, backup.sh, validation-report.md |

## 7. Design Boundary

본 프로젝트는 복잡한 엔터프라이즈 수준의 오케스트레이션 시스템을 구현하는 것이 아니라, 학습 프로젝트 범위에서 다음 기능을 명확하게 검증하는 데 집중한다.

| 포함 범위 | 제외 범위 |
|---|---|
| Ansible 기반 서버 설정 자동화 | Kubernetes 기반 대규모 오케스트레이션 |
| Docker 기반 Nginx 서비스 배포 | 복잡한 마이크로서비스 배포 |
| 서버 상태 점검 | 고도화된 APM 구성 |
| 백업 및 복구 검증 | 실시간 DR 자동 전환 |
| GitHub 기반 산출물 관리 | 상용 CI/CD 파이프라인 전체 구축 |

## 8. Operational Meaning

이 프로젝트의 운영적 의미는 다음과 같다.

~~~text
수동으로 서버를 설정하는 방식에서 벗어나,
Ansible Playbook을 통해 반복 가능한 서버 구성 방식을 만들고,
서비스 배포 후 상태 점검과 백업/복구 검증까지 연결한다.
~~~

즉, 단순 구축 실습이 아니라 인프라 운영 자동화의 기본 흐름을 구현하는 프로젝트이다.

## 9. Final Architecture Summary

최종 아키텍처는 아래 흐름으로 요약된다.

~~~text
Cloud Infrastructure
→ Control Node
→ Ansible Inventory
→ Ansible Playbook
→ Managed Nodes
→ Docker / Nginx Service
→ Health Check
→ Backup / Restore Validation
~~~

정주헌은 이 흐름이 발표와 문서에서 끊기지 않도록 전체 구조를 통합 관리한다.
