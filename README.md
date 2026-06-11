# Team Dandelion - Cloud Infrastructure Automation

## 프로젝트 주제

Ansible 기반 클라우드 인프라 자동화 및 운영 최적화 시스템 구축

## 프로젝트 목표

본 프로젝트는 Ansible을 활용하여 클라우드 서버의 초기 설정, Docker 기반 서비스 배포, 상태 점검, 백업 및 복구 검증을 자동화하는 것을 목표로 한다.

## 팀 구성

| 이름 | 역할 |
|---|---|
| 박재우 | 모니터링 / 백업 / 검증 |
| 백서빈 | 클라우드 인프라 |
| 이진욱 | 서버 / 가상화 |
| 정주헌 | PM / 아키텍처 |
| 조민석 | Ansible 자동화 |

## 시스템 아키텍처

Control Node에서 Ansible Playbook을 실행하고, SSH Key 기반으로 Managed Node에 접속하여 서버 설정, Docker 설치, 서비스 배포, 상태 점검 작업을 수행한다.

~~~text
[Control Node: Ansible 실행 서버]
        |
        | SSH Key 기반 자동화
        v
[Managed Nodes]
        |
        |-- Web Node
        |-- Docker Node
        |-- Backup / Validation Target
~~~

## 작업 흐름

1. 클라우드 인프라 구성
2. 서버 접속 환경 구성
3. Linux / Docker 환경 구성
4. Ansible Inventory 작성
5. Ansible Playbook 실행
6. 서비스 배포
7. 모니터링 / 백업 / 복구 검증
8. 캡처 / 문서 / 발표자료 정리

## 디렉터리 구조

~~~text
dandelion-cloud-automation/
├── README.md
├── docs/
├── ansible/
├── scripts/
├── screenshots/
└── presentation/
~~~

## 핵심 결과

- Ansible 기반 서버 초기 설정 자동화
- Docker 기반 Nginx 서비스 배포
- 서버 상태 점검 자동화
- 백업 및 복구 검증
- 팀 프로젝트 산출물 통합 관리
