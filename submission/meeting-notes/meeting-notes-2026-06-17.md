<!-- STATUS: COMPLETE -->

# Team Dandelion 회의록

## 2026-06-17 회의록

## 1. 회의 정보

| 구분 | 내용 |
|---|---|
| 회의 일자 | 2026-06-17 |
| 회의 구분 | 인프라 구축 진행 현황 및 서비스 환경 구성 정리 |
| 회의 장소 | ZEP 팀 회의실 / Discord |
| 작성자 | 정주헌 |
| 참석자 | 정주헌, 백서빈, 이진욱, 조민석, 박재우 |

---

## 2. 회의 목적

- OpenStack 서브넷 및 보안그룹 생성 현황 확인
- 인스턴스 생성 진행 상황 공유
- 서비스 담당자의 노드별 기본 환경 구성 내용 정리
- Control / HAProxy / Web / DB / Backup Node 리소스 기준 조정
- Backup / Validation 관련 인스턴스 생성 이슈 공유
- 추후 DB Node 이중화 방향을 향후 확장 항목으로 정리
- 팀원별 후속 작업 범위 확인

---

## 3. 주요 논의 내용

### 3.1 금일 작업 중심 진행

금일은 신규 설계보다는 실제 OpenStack 환경 구성과 노드별 기본 패키지 설치 방향을 정리하는 작업 중심으로 진행하였다.

PM / Architecture 영역에서는 기존 Phase 기반 구조를 유지하고, 팀원별 실제 구현 결과가 문서 기준과 일치하는지 확인하는 방향으로 진행하였다.

---

### 3.2 백서빈 작업 현황

Cloud Infrastructure 담당자인 백서빈은 OpenStack 보안그룹 및 서브넷 생성을 진행하였다.

현재 전체 4개 서브넷 기준 중 3개 영역은 생성 및 기본 확인이 완료된 상태이며, Backup / Validation 또는 복구 검증 영역과 관련된 서브넷 또는 인스턴스 생성 과정에서 문제가 발생하여 조치 중이다.

| 담당자 | 작업 내용 | 상태 |
|---|---|---|
| 백서빈 | OpenStack 보안그룹 생성 | 진행 완료 |
| 백서빈 | OpenStack 서브넷 생성 | 4개 중 3개 완료 |
| 백서빈 | 인스턴스 생성 및 기본 검증 | 일부 완료 |
| 백서빈 | Backup / Validation 관련 서브넷 또는 인스턴스 생성 문제 조치 | 진행 중 |

현재 이슈는 Backup / Validation 영역의 인스턴스가 정상적으로 올라가지 않는 문제이며, 원인 확인 후 조치하기로 하였다.

검토 대상은 다음과 같다.

~~~text
1. 서브넷 IP 대역 충돌 여부
2. 라우터 연결 여부
3. 보안그룹 적용 여부
4. 인스턴스 flavor 리소스 부족 여부
5. 이미지 / 키페어 / 네트워크 연결 설정 오류 여부
6. OpenStack Compute 자원 부족 여부
~~~

---

### 3.3 이진욱 작업 내용 정리

Server / Virtualization 담당자인 이진욱은 노드별 기본 환경 구성 기준을 정리하였다.

우선 전체 노드의 리소스 기준은 다음과 같이 정리하였다.

| Node | vCPU | Disk | RAM |
|---|---:|---:|---:|
| control | 2 Core | 20 GB | 2 GB |
| haproxy | 1 Core | 15 GB | 2 GB |
| web | 2 Core | 20 GB | 2 GB |
| db | 2 Core | 20 GB | 4 GB |
| backup | 1 Core | 80 GB | 2 GB |

기존 산정에서는 HAProxy Node RAM을 1 GB로 검토하였으나, 실제 구성 안정성을 고려하여 2 GB로 조정하였다.

변경 후 Phase 1 기본 구성 총 리소스는 다음과 같다.

| Resource | Total |
|---|---:|
| vCPU | 8 Core |
| Disk | 155 GB |
| RAM | 12 GB |

---

### 3.4 공통 기본 설정

모든 노드에서 공통적으로 sudo 권한 설정과 기본 패키지 설치를 진행하는 방향으로 정리하였다.

~~~bash
echo "user1 ALL=(ALL) NOPASSWD: ALL" | sudo tee -a /etc/sudoers
sudo apt update && sudo apt install -y vim curl wget
~~~

해당 작업은 Ansible 자동화 전 수동 기본 점검 또는 초기 환경 구성 기준으로 활용한다.

---

### 3.5 Control Node 구성 기준

Control Node에는 Ansible을 설치하여 전체 노드 관리 및 자동화 실행 기준 노드로 사용한다.

~~~bash
sudo apt-add-repository --yes --update ppa:ansible/ansible
sudo apt update && sudo apt install -y ansible
~~~

Control Node는 관리자가 SSH로 접근하는 유일한 관리 진입점이며, 이후 Control Node가 Ansible과 SSH를 통해 Proxy, Web, DB, Backup Node를 관리한다.

---

### 3.6 HAProxy Node 구성 기준

HAProxy Node는 두 가지 구성 방식이 검토되었다.

첫 번째는 OS 패키지 기반 HAProxy 설치 방식이다.

~~~bash
sudo apt update && sudo apt install -y haproxy
~~~

두 번째는 Docker 기반 HAProxy Container 실행 방식이다.

최종 프로젝트 기준은 HAProxy Container 방식이므로, HAProxy Node에는 Docker Engine 및 Docker Compose Plugin 설치가 필요하다.

~~~bash
sudo apt remove $(dpkg --get-selections docker.io docker-compose docker-compose-v2 docker-doc podman-docker containerd runc | cut -f1)

sudo apt update
sudo apt install -y ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

sudo tee /etc/apt/sources.list.d/docker.sources <<EOF
Types: deb
URIs: https://download.docker.com/linux/ubuntu
Suites: $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}")
Components: stable
Architectures: $(dpkg --print-architecture)
Signed-By: /etc/apt/keyrings/docker.asc
EOF

sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo systemctl start docker
sudo systemctl enable docker
~~~

---

### 3.7 Web Node 구성 기준

Web Node는 Custom WordPress Container를 실행하는 서비스 노드이다.

Web Node에는 HAProxy Node와 동일한 Docker Engine 및 Docker Compose Plugin 설치 절차를 적용한다.

Web Node의 최종 역할은 다음과 같다.

| 항목 | 내용 |
|---|---|
| 서비스 | Custom WordPress Container |
| Base Image | wordpress:php8.2-apache |
| 서비스 포트 | HTTP 80 |
| DB 연결 | DB Node MariaDB Service TCP 3306 |
| 접근 방식 | 사용자는 직접 접근하지 않고 HAProxy Node를 통해 접근 |

---

### 3.8 DB Node 구성 기준

DB Node는 MariaDB를 컨테이너가 아니라 Ubuntu 패키지로 직접 설치하고 systemd 서비스로 운영한다.

~~~bash
sudo apt update && sudo apt install -y mariadb-server
sudo systemctl start mariadb
sudo systemctl enable mariadb
~~~

DB Node의 최종 역할은 다음과 같다.

| 항목 | 내용 |
|---|---|
| DB Service | MariaDB |
| 설치 방식 | apt 기반 직접 설치 |
| 서비스 관리 | systemctl mariadb |
| 접근 포트 | TCP 3306 |
| 접근 허용 | Web Node, Backup Node |
| 외부 공개 | 금지 |

---

### 3.9 Backup Node 구성 기준

Backup Node는 MariaDB dump를 수행하기 위해 mariadb-client를 설치한다.

~~~bash
sudo apt update && sudo apt install -y mariadb-client
~~~

Backup Node는 health_check.sh, backup.sh, restore.md 기반 검증을 담당한다.

| 항목 | 내용 |
|---|---|
| Health Check | health_check.sh |
| DB Backup | MariaDB dump |
| File Backup | WordPress files archive |
| Restore Guide | restore.md |
| 필요 패키지 | mariadb-client, curl, wget 등 |

---

## 4. 결정 사항

| 번호 | 결정 내용 |
|---:|---|
| 1 | 백서빈은 보안그룹 및 서브넷 생성을 진행하였고, 4개 중 3개 영역은 기본 구성이 완료된 것으로 정리한다. |
| 2 | Backup / Validation 관련 서브넷 또는 인스턴스 생성 문제는 원인 확인 후 조치한다. |
| 3 | 이진욱은 노드별 기본 패키지 설치 및 서비스 구성 기준을 정리하였다. |
| 4 | HAProxy Node RAM은 기존 1 GB 기준에서 2 GB 기준으로 조정한다. |
| 5 | Phase 1 기본 구성 총 리소스는 vCPU 8 Core, Disk 155 GB, RAM 12 GB로 정리한다. |
| 6 | Control Node는 Ansible 실행 및 전체 노드 관리 기준 노드로 유지한다. |
| 7 | HAProxy Node와 Web Node에는 Docker Engine 및 Docker Compose Plugin을 설치한다. |
| 8 | DB Node는 MariaDB를 직접 설치하고 systemd 서비스로 운영한다. |
| 9 | Backup Node에는 mariadb-client를 설치하여 MariaDB dump를 수행할 수 있도록 한다. |
| 10 | DB Node 이중화는 현재 구현 범위가 아니라 Post-Phase 확장 방향으로 정리한다. |

---

## 5. 다음 작업 계획

| 담당자 | 다음 작업 |
|---|---|
| 정주헌 | 회의록, 작업일지, 리소스 산정표, 문서 기준 정리 |
| 백서빈 | Backup / Validation 관련 서브넷 또는 인스턴스 생성 이슈 조치 |
| 이진욱 | 노드별 기본 환경 구성 명령 정리 및 실제 서비스 구성 준비 |
| 조민석 | 실제 IP 기준 inventory.ini, ansible.cfg, site.yml 반영 준비 |
| 박재우 | Backup Node 기준 health_check.sh, backup.sh, restore.md 검증 준비 |

---

## 6. 회의 결과 요약

2026년 6월 17일 회의에서는 신규 구조 설계보다 실제 OpenStack 환경 구축과 노드별 기본 환경 구성 기준을 정리하는 작업을 중심으로 진행하였다.

백서빈은 보안그룹 및 서브넷 생성을 진행하였으며, 전체 4개 영역 중 3개는 기본 구성이 완료된 상태이다. Backup / Validation 관련 서브넷 또는 인스턴스 생성 과정에서 문제가 발생하여 현재 조치 중이다.

이진욱은 Control, HAProxy, Web, DB, Backup Node의 리소스 기준과 기본 패키지 설치 절차를 정리하였다. 특히 HAProxy Node는 안정성을 위해 RAM을 2 GB로 조정하였으며, HAProxy Node와 Web Node에는 Docker Engine 및 Docker Compose Plugin 설치가 필요하다는 점을 정리하였다.

DB Node는 MariaDB를 직접 설치하고 systemd 서비스로 운영하며, Backup Node는 mariadb-client를 통해 MariaDB dump를 수행할 수 있도록 구성한다.

