# System Architecture

## 1. Architecture Overview

본 프로젝트는 Ansible Control Node를 중심으로 클라우드 인프라 서버의 초기 설정, Docker 기반 서비스 배포, 상태 점검, 백업 및 복구 검증을 자동화하는 구조로 설계한다.

Control Node는 Ansible 실행 서버이며, Managed Node는 자동화 대상 서버이다.

## 2. Architecture Diagram

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

## 3. Node Roles

| 구분 | 역할 | 설명 |
|---|---|---|
| Control Node | Ansible 실행 서버 | inventory.ini와 playbook을 관리하고 자동화 작업을 실행 |
| Web Node | 서비스 배포 대상 | Docker 기반 Nginx 컨테이너 실행 |
| Backup Node | 검증 대상 | 백업 및 복구 테스트 수행 |

## 4. Automation Flow

~~~text
Cloud Infrastructure Provisioning
→ SSH Access Configuration
→ Linux Package Setup
→ Docker Installation
→ Nginx Container Deployment
→ Health Check
→ Backup
→ Recovery Validation
~~~

## 5. Design Principle

이 프로젝트의 핵심 설계 기준은 단순 서버 구축이 아니라, 반복적인 수동 작업을 Ansible Playbook으로 자동화하고 그 결과를 검증 가능한 형태로 남기는 것이다.

## 6. 담당자 기준

| 이름 | 담당 영역 |
|---|---|
| 정주헌 | PM / Architecture |
| 백서빈 | Cloud Infrastructure |
| 이진욱 | Server / Virtualization |
| 조민석 | Ansible Automation |
| 박재우 | Monitoring / Backup / Validation |
