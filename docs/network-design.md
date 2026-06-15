# Network Design

## 1. 구성 목표

이 문서는 OpenStack 기반 인프라에서 Ansible 자동화 대상 서버와 네트워크 경계를 정리하기 위한 기준 문서이다.

## 2. 기본 네트워크 구성

| 항목 | 권장 내용 |
|---|---|
| Cloud Platform | OpenStack 기반 인스턴스 구성 |
| Network Scope | 관리용/서비스용 분리 구성 |
| Access Pattern | SSH, HTTP, 관리 포트 허용 |
| Server Role | Control Node / Web Node / Validation Node |

## 3. 서버 구성 예시

| 서버명 | 역할 | 주요 포트 | 비고 |
|---|---|---|---|
| control-node | Ansible 실행 서버 | 22 | inventory 및 playbook 실행 |
| web-node | Docker/Nginx 서비스 서버 | 22, 80 | 웹 서비스 제공 |
| backup-node | 백업/복구 검증 서버 | 22 | 상태 점검 및 백업 대상 |

## 4. 보안그룹 권장 정책

| 포트 | 프로토콜 | 용도 | 허용 범위 |
|---:|---|---|---|
| 22 | TCP | SSH | 관리자 IP 또는 허용된 관리망 |
| 80 | TCP | HTTP | 테스트/관리망 |
| 9100 | TCP | Node Exporter | 관리 노드 |
| 9090 | TCP | Prometheus | 관리 노드 |
| 3000 | TCP | Grafana | 관리 노드 |

## 5. 검증용 산출물

- 인스턴스 생성 결과 캡처
- 네트워크/서브넷 구성 캡처
- 보안그룹 설정 캡처
- SSH 접속 성공 캡처

## 6. 제출용 체크리스트

| 항목 | 상태 |
|---|---|
| 클라우드 플랫폼 정리 | 진행 필요 |
| 서버 목록 정리 | 진행 필요 |
| IP 정보 정리 | 진행 필요 |
| 보안그룹 정책 정리 | 진행 필요 |
| 검증 캡처 정리 | 진행 필요 |

<!-- AUTO_IMAGES_START -->
## 자동 반영 이미지

아래 이미지는 screenshots/ 폴더에 파일이 업로드되면 자동으로 표시된다.

### Cloud Instance List

../screenshots/cloud-infra/instance-list.png 이미지가 아직 업로드되지 않았다.

### Network / Subnet Configuration

../screenshots/cloud-infra/network-subnet.png 이미지가 아직 업로드되지 않았다.

### Security Group Policy

../screenshots/cloud-infra/security-group.png 이미지가 아직 업로드되지 않았다.

### SSH Connection Test

../screenshots/cloud-infra/ssh-test.png 이미지가 아직 업로드되지 않았다.
<!-- AUTO_IMAGES_END -->
