<!-- STATUS: TEMPLATE -->
# TEMP: 팀원 실제 작업 결과 반영 필요

# Network Design

## 1. Cloud Environment

| 항목 | 내용 |
|---|---|
| Cloud Platform | TBD |
| Region / Zone | TBD |
| VPC / Network CIDR | TBD |
| Subnet | TBD |

## 2. Server List

| 서버명 | 역할 | Public IP | Private IP | 비고 |
|---|---|---|---|---|
| control-node | Ansible Control Node | TBD | TBD | Ansible 실행 |
| web-node | Web Service Node | TBD | TBD | Docker / Nginx |
| backup-node | Backup / Validation Node | TBD | TBD | 백업 / 복구 검증 |

## 3. Security Group / Firewall Policy

| 포트 | 프로토콜 | 용도 | 허용 대상 |
|---:|---|---|---|
| 22 | TCP | SSH / Ansible | 관리자 IP |
| 80 | TCP | HTTP / Nginx | 전체 또는 테스트 IP |
| 9100 | TCP | Node Exporter | Control / Monitoring Node |
| 9090 | TCP | Prometheus | 관리자 IP |
| 3000 | TCP | Grafana | 관리자 IP |

## 4. Evidence

- 인스턴스 생성 화면 캡처
- IP 정보 캡처
- 보안그룹 캡처
- SSH 접속 성공 캡처

## 5. Screenshots

### 5.1 Cloud Instance List

이미지 파일 위치:

~~~text
screenshots/cloud-infra/instance-list.png
~~~

### 5.2 Network / Subnet Configuration

이미지 파일 위치:

~~~text
screenshots/cloud-infra/network-subnet.png
~~~

### 5.3 Security Group Policy

이미지 파일 위치:

~~~text
screenshots/cloud-infra/security-group.png
~~~

### 5.4 SSH Connection Test

이미지 파일 위치:

~~~text
screenshots/cloud-infra/ssh-test.png
~~~

## 6. 담당자 제출 체크리스트

| 항목 | 완료 여부 |
|---|---|
| 클라우드 플랫폼 정리 | TBD |
| 서버 목록 정리 | TBD |
| Public IP / Private IP 정리 | TBD |
| 보안그룹 정책 정리 | TBD |
| SSH 접속 성공 캡처 | TBD |

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





