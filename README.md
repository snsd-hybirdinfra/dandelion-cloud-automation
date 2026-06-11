<!-- STATUS: COMPLETE -->
# Team Dandelion - Cloud Infrastructure Automation

## 1. 프로젝트 주제

Ansible 기반 클라우드 인프라 자동화 및 운영 최적화 시스템 구축

## 2. 프로젝트 목표

본 프로젝트는 Ansible을 활용하여 클라우드 서버의 초기 설정, Docker 기반 서비스 배포, 상태 점검, 백업 및 복구 검증을 자동화하는 것을 목표로 한다.

단순히 서버를 수동으로 구축하는 것이 아니라, 반복적인 인프라 운영 작업을 Ansible Playbook으로 자동화하고, 자동화 결과를 모니터링, 백업, 복구 검증까지 연결하는 것이 핵심이다.

## 3. 팀 구성

| 이름 | 역할 | 담당 영역 |
|---|---|---|
| 박재우 | 모니터링 / 백업 / 검증 | 상태 점검, 백업 스크립트, 복구 테스트 |
| 백서빈 | 클라우드 인프라 | 서버 생성, 네트워크, 보안그룹, SSH 접속 |
| 이진욱 | 서버 / 가상화 | Linux 기본 설정, Docker 설치, Nginx 컨테이너 |
| 정주헌 | PM / 아키텍처 | 전체 구조 설계, 문서 통합, 발표 흐름 정리 |
| 조민석 | Ansible 자동화 | inventory, ansible.cfg, playbook 작성 및 실행 |

## 4. 시스템 아키텍처

~~~text
[PM / Architecture: 정주헌]
        |
        v
[Control Node: Ansible 실행 서버]
        |
        | SSH Key 기반 자동화
        v
+-------------------------------+
| Managed Nodes                 |
|                               |
| - Web Node                    |
| - Docker Node                 |
| - Backup / Validation Target  |
+-------------------------------+
~~~

## 5. 구성 요소

| 구성 요소 | 설명 |
|---|---|
| Control Node | Ansible을 설치하고 Playbook을 실행하는 서버 |
| Managed Node | Ansible에 의해 설정되는 대상 서버 |
| Inventory | 관리 대상 서버 정보를 정의하는 파일 |
| Playbook | 서버 설정, Docker 설치, 서비스 배포 자동화 파일 |
| Docker | Nginx 웹 서비스를 컨테이너로 실행 |
| Health Check | 서버 및 서비스 상태 점검 |
| Backup / Restore | 웹 데이터 백업 및 복구 검증 |

## 6. 작업 흐름

~~~text
클라우드 인프라 준비
→ 서버 접속 환경 구성
→ Linux / Docker 환경 구성
→ Ansible Inventory 작성
→ Ansible Playbook 실행
→ Docker 기반 Nginx 서비스 배포
→ 상태 점검
→ 백업 / 복구 검증
→ 문서 및 발표자료 정리
~~~

## 7. 디렉터리 구조

~~~text
dandelion-cloud-automation/
├── README.md
├── docs/
│   ├── architecture.md
│   ├── network-design.md
│   ├── server-setup.md
│   ├── ansible-automation.md
│   ├── validation-report.md
│   └── team-task-guide.md
├── ansible/
│   ├── ansible.cfg
│   ├── inventory.ini
│   └── site.yml
├── scripts/
│   ├── health_check.sh
│   ├── backup.sh
│   └── restore.md
├── screenshots/
│   ├── cloud-infra/
│   ├── server/
│   ├── ansible/
│   └── validation/
└── presentation/
    └── presentation-outline.md
~~~

## 8. 주요 자동화 범위

| 작업 | 자동화 여부 | 담당 |
|---|---|---|
| 서버 기본 패키지 설치 | Yes | Ansible |
| Docker 설치 | Yes | Ansible |
| Docker 서비스 실행 | Yes | Ansible |
| Nginx 컨테이너 배포 | Yes | Ansible |
| 서버 상태 점검 | Script | Monitoring |
| 백업 생성 | Script | Backup |
| 복구 검증 | Manual / Script | Validation |

## 9. 문서 목록

| 문서 | 설명 |
|---|---|
| [Architecture](./docs/architecture.md) | 전체 시스템 아키텍처 |
| [Network Design](./docs/network-design.md) | 클라우드 인프라 및 네트워크 구성 |
| [Server Setup](./docs/server-setup.md) | 서버 및 Docker 구성 |
| [Ansible Automation](./docs/ansible-automation.md) | Ansible 자동화 구성 |
| [Validation Report](./docs/validation-report.md) | 모니터링, 백업, 복구 검증 |
| [Team Task Guide](./docs/team-task-guide.md) | 팀원별 작업 기준 |
| [Presentation Outline](./presentation/presentation-outline.md) | 발표 흐름 및 멘트 |

## 10. 최종 결과

본 프로젝트를 통해 다음 결과를 확인한다.

- 클라우드 서버 인프라 구성
- SSH 기반 Ansible 원격 제어 구성
- Ansible Playbook 기반 서버 초기 설정 자동화
- Docker 기반 Nginx 서비스 배포
- 서버 및 서비스 상태 점검
- 백업 파일 생성
- 복구 테스트 및 검증
- 팀 프로젝트 산출물 통합 관리

## 11. 프로젝트 핵심 요약

이 프로젝트의 핵심은 다음과 같다.

~~~text
수동 서버 구축 작업을 Ansible로 자동화했다.
자동화 결과를 모니터링, 백업, 복구 검증으로 확인했다.
~~~

## 팀 작업 기준

팀원별 작업 위치와 GitHub 사용 규칙은 아래 문서를 기준으로 한다.

- [Team Task Guide](./docs/team-task-guide.md)

## 실행 전 체크리스트

Ansible 실행 전 서버, SSH, sudo, Python, Inventory 상태는 아래 문서를 기준으로 확인한다.

- [Pre-Run Checklist](./docs/pre-run-checklist.md)

## 문제 해결 문서

실습 중 SSH, Ansible, Docker, HTTP, Backup 오류가 발생하면 아래 문서를 기준으로 확인한다.

- [Troubleshooting Guide](./docs/troubleshooting.md)

## 실행 방법

프로젝트 실행 절차는 아래 문서를 기준으로 한다.

- [Project Runbook](./docs/runbook.md)

기본 실행 흐름은 다음과 같다.

~~~bash
git clone https://github.com/snsd-hybirdinfra/dandelion-cloud-automation.git
cd dandelion-cloud-automation/ansible

ansible all -m ping
ansible-playbook --syntax-check site.yml
ansible-playbook site.yml
~~~

## 최종 산출물 체크리스트

최종 제출 전 산출물 누락 여부는 아래 문서를 기준으로 확인한다.

- [Final Deliverables Checklist](./docs/final-deliverables.md)

## 검수 기준

팀원 자료 업로드 후 최종 검수는 아래 문서를 기준으로 한다.

- [Review Checklist](./docs/review-checklist.md)

<!-- AUTO_STATUS_START -->
## 자동 생성 프로젝트 상태

아래 상태는 팀원이 파일을 push할 때 자동으로 갱신된다.

## 2. 전체 진행률

| 완료 | 전체 | 진행률 |
|---:|---:|---:|
| 3 | 37 | 8% |

## 담당자별 진행 상태

| 영역 | 담당자 | 완료 | 전체 | 진행률 | 상태 |
|---|---|---:|---:|---:|---|
| PM / Architecture | 정주헌 | 3 | 9 | 33% | 🟡 진행 중 |
| Cloud Infrastructure | 백서빈 | 0 | 5 | 0% | ❌ 미착수 |
| Server / Virtualization | 이진욱 | 0 | 5 | 0% | ❌ 미착수 |
| Ansible Automation | 조민석 | 0 | 9 | 0% | ❌ 미착수 |
| Monitoring / Backup / Validation | 박재우 | 0 | 9 | 0% | ❌ 미착수 |

상세 상태는 [Project Status](./docs/project-status.md) 문서에서 확인한다.

<!-- AUTO_STATUS_END -->

## 자동 검수 결과

저장소 구조, 필수 파일, 민감정보 파일 여부는 아래 문서에서 확인한다.

- [Validation Summary](./docs/validation-summary.md)

