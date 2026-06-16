<!-- STATUS: COMPLETE -->

# Scope Control Policy

## 1. 목적

본 문서는 Team Dandelion 프로젝트의 구현 범위를 Phase 기반으로 정의한다.

기존 A급 / B급 / B+ 표현 대신 다음 기준을 사용한다.

~~~text
Phase 1: 필수 구성 및 기본 검증 단계
Phase 2: 운영 확장 및 검증 고도화 단계
Phase 3: 도전 확장 단계
Out of Scope: 제외 범위
~~~

본 프로젝트의 핵심은 기능을 무리하게 확장하는 것이 아니라, Phase 1 필수 구성을 안정적으로 완성한 뒤 Phase 2와 Phase 3을 단계적으로 확장하는 것이다.

---

## 2. Phase 기반 구현 전략

본 프로젝트는 OpenStack 기반 Ubuntu 인스턴스 위에서 Ansible을 활용하여 서버 설정, Docker 설치, Docker Compose 기반 서비스 배포, 상태 점검, 백업 및 복구 검증을 수행한다.

Phase 1에서는 Proxy Node, Web Node, DB Node, Backup / Validation Node를 분리한 기본 클라우드 운영 구조를 구현한다.

Phase 2에서는 HTTPS, Cinder Backup Volume, Prometheus/Grafana, 자동화 구조 개선을 통해 운영성을 강화한다.

Phase 3에서는 Web Node 2대와 HAProxy Load Balancing을 통해 확장성을 검증한다.

~~~text
Phase 1
필수 구성 및 기본 검증
→ Proxy / Web / DB / Backup 계층 분리
→ WordPress / MariaDB / HAProxy HTTP Reverse Proxy
→ Health Check / Backup / Restore
→ 필수 문서 및 캡처 정리

Phase 2
운영 확장 및 검증 고도화
→ HTTPS
→ Cinder Backup Volume
→ Prometheus / Grafana
→ Ansible 구조 개선
→ 상세 검증 리포트 고도화

Phase 3
도전 확장
→ Web Node 2대
→ HAProxy roundrobin Load Balancing
→ 공통 DB Node 연결 검증
→ Web Node 장애 대응 검증
~~~

---

## 3. Phase 1: 필수 구성 및 기본 검증 단계

Phase 1은 최종 발표와 시연을 위해 반드시 완료해야 하는 필수 구성 단계이다.

Phase 1의 목표는 OpenStack 위에 Ubuntu 기반 인스턴스를 구성하고, Control Node, Proxy Node, Web Node, DB Node, Backup / Validation Node를 분리한 뒤, Ansible을 통해 Docker 기반 서비스를 배포하고, 상태 점검과 백업/복구 검증까지 완료하는 것이다.

Phase 1은 단순 WordPress 배포가 아니라, Proxy 계층, Web 계층, DB 계층, Backup / Validation 계층을 분리한 기본 클라우드 운영 구조를 구현하는 범위이다.

---

## 3.1 Phase 1 필수 구조

~~~text
Client
→ Proxy Node
   └── HAProxy HTTP Reverse Proxy

→ Web Node
   └── Custom WordPress Container

→ DB Node
   └── MariaDB Service

→ Backup / Validation Node
   ├── health_check.sh
   ├── backup.sh
   ├── mysqldump 기반 mysqldump 기반 MariaDB dump
   ├── WordPress files archive
   └── restore.md 검증

Control Node
→ Ansible 실행
→ Proxy / Web / DB / Backup Node 관리
~~~

---

## 3.2 Phase 1 필수 구성사항

| 구분 | 필수 구현 내용 |
|---|---|
| 인프라 | OpenStack 인프라 구성 |
| 인프라 | Ubuntu 이미지 기반 인스턴스 생성 |
| 인프라 | Control Node, Proxy Node, Web Node, DB Node, Backup / Validation Node 구분 |
| 네트워크 | 네트워크, 라우터, 서브넷 구성 |
| 네트워크 | Floating IP 또는 포트포워딩 기반 외부 접속 확인 |
| 보안 | 보안그룹을 통한 SSH 및 HTTP 접근 제어 |
| 보안 | SSH 접속은 관리자 또는 허용된 대역에서만 접근하도록 제한 |
| 접속 | SSH 접속 확인 |
| Ansible | ansible.cfg 작성 |
| Ansible | inventory.ini 작성 |
| Ansible | ansible all -m ping 성공 |
| Ansible | site.yml 또는 playbook 실행 |
| 서비스 | Docker 설치 |
| 서비스 | Docker Compose 사용 |
| 서비스 | Docker Hub 공식 WordPress 이미지 기반 Custom WordPress Image 구성 |
| 서비스 | DB Node에 MariaDB 서비스 구성 |
| 서비스 | Web Node에 WordPress 컨테이너 구성 |
| 서비스 | Web Node의 WordPress가 DB Node의 MariaDB에 연결 |
| 서비스 | Proxy Node에 HAProxy HTTP Reverse Proxy 구성 |
| 검증 | systemctl status mariadb 서비스 상태 확인 |
| 검증 | ss -tulnp 또는 포트 확인 명령으로 서비스 포트 확인 |
| 검증 | curl 또는 브라우저를 통한 Proxy Node 경유 WordPress HTTP 접속 확인 |
| 검증 | Web Node에서 DB Node MariaDB 연결 확인 |
| 상태 점검 | health_check.sh 실행 |
| 백업 | backup.sh 실행 |
| 백업 | DB Node mysqldump 기반 mysqldump 기반 MariaDB dump 파일 생성 |
| 백업 | Web Node WordPress files archive 생성 |
| 복구 | restore.md 기반 복구 절차 정리 |
| 복구 | Restore 절차 검증 |
| 장애 대응 | 간단한 장애 상황 1개와 복구 절차 정리 |
| 문서 | IP 주소표 정리 |
| 문서 | 보안그룹 및 포트표 정리 |
| 문서 | 담당자별 수행 내역 정리 |
| 문서 | 트러블슈팅 로그 정리 |
| 산출물 | 담당자별 캡처 및 문서 정리 |

---

## 3.3 Phase 1 범위 제한

Phase 1의 HAProxy는 HTTP Reverse Proxy까지만 포함한다.

~~~text
Client
→ Proxy Node / HAProxy HTTP Reverse Proxy
→ Web Node / WordPress
→ DB Node / MariaDB
~~~

다음 항목은 Phase 1에 포함하지 않는다.

~~~text
HTTPS
HTTP to HTTPS Redirect
Cinder Backup Volume
Prometheus / Grafana
Web Node 2대 Load Balancing
WordPress files 자동 동기화
OpenStack LBaaS / Octavia
~~~

---

## 4. Phase 2: 운영 확장 및 검증 고도화 단계

Phase 2는 Phase 1 구현과 필수 캡처가 완료된 이후, 시간이 남을 경우 추가로 시도하는 운영 확장 단계이다.

Phase 1이 불안정한 상태에서는 Phase 2 작업을 진행하지 않는다.

Phase 2가 실패하더라도 Phase 1 결과 중심으로 발표한다.

Phase 2의 목적은 Phase 1의 기본 운영 흐름 위에 보안 강화, 스토리지 분리, 모니터링, 자동화 개선 요소를 추가하여 프로젝트의 전문성과 차별성을 높이는 것이다.

---

## 4.1 Phase 2 서브 구성사항

| 구분 | 서브 구성사항 |
|---|---|
| 보안 | HAProxy 기반 HTTPS 적용 |
| 보안 | self-signed 인증서 기반 HTTPS 접속 확인 |
| 보안 | HTTP 80 → HTTPS 443 Redirect 구성 |
| 보안 | curl -k 또는 브라우저를 통한 HTTPS 접속 검증 |
| 스토리지 | Cinder Volume 생성 테스트 |
| 스토리지 | Backup / Validation Node에 Cinder Volume attach 테스트 |
| 스토리지 | Cinder Volume을 /backup 경로에 마운트 |
| 스토리지 | backup.sh 결과물을 Cinder Volume에 저장 |
| 스토리지 | NFS 기반 백업 저장소 구성 시도 |
| 모니터링 | node_exporter 구성 |
| 모니터링 | cAdvisor 구성 |
| 모니터링 | Prometheus 구성 |
| 시각화 | Grafana 대시보드 구성 |
| 검증 | 간단한 모니터링 화면 캡처 |
| 자동화 개선 | Ansible playbook 역할 분리 개선 |
| 자동화 개선 | backup / restore 절차 playbook화 |
| 자동화 개선 | Ansible roles 구조 분리 |
| 문서 | 상세 검증 리포트 고도화 |
| 문서 | 운영 장애 시나리오 확장 정리 |

---

## 4.2 Phase 2 Cinder 처리 기준

Phase 2의 Cinder Volume은 DB 원본 데이터 저장소가 아니라, Backup / Validation Node의 백업 저장소로 사용한다.

~~~text
DB Node
→ MariaDB 운영 데이터 보관

Backup / Validation Node
→ Cinder Volume attach
→ /backup mount
→ mysqldump 기반 mysqldump 기반 MariaDB dump 및 WordPress files backup 저장
~~~

DB Node의 MariaDB 원본 데이터를 Cinder Volume에 직접 올리는 방식은 이번 범위에서 제외한다.

제외 이유는 다음과 같다.

| 항목 | 이유 |
|---|---|
| Docker Volume 경로 | MariaDB 데이터 경로와 Cinder mount 경로가 꼬일 수 있음 |
| 권한 문제 | MariaDB 파일 권한 및 ownership 문제가 발생할 수 있음 |
| 복구 복잡도 | Volume detach / attach 기반 복구는 검증 부담이 커짐 |
| 발표 안정성 | backup.sh 기반 dump 복구보다 시연 위험도가 높음 |

---

## 5. Phase 3: 도전 확장 단계

Phase 3은 Phase 1 필수 구성과 Phase 2 주요 서브 구성사항이 조기에 완료될 경우에만 시도하는 도전 확장 단계이다.

Phase 3의 목표는 기존 Phase 1 구조를 유지하면서 Web Node를 2대로 확장하고, HAProxy를 통해 roundrobin 방식의 Load Balancing을 검증하는 것이다.

Phase 3은 필수 제출 범위가 아니며, 구현 중 문제가 발생할 경우 기존 Phase 1 및 Phase 2 산출물을 기준으로 발표한다.

---

## 5.1 Phase 3 목표 구조

~~~text
Client
→ Proxy Node / HAProxy Load Balancer
→ Web Node 1 / WordPress
→ Web Node 2 / WordPress
→ DB Node / MariaDB
→ Backup / Validation Node
~~~

---

## 5.2 Phase 3 포함 가능 범위

| 구분 | 내용 |
|---|---|
| 확장 | Web Node 2대 구성 |
| Proxy | HAProxy roundrobin Load Balancing 구성 |
| Service | Web Node 1 / Web Node 2에 WordPress 컨테이너 배포 |
| Database | 두 Web Node가 공통 DB Node의 MariaDB에 연결 |
| Validation | Web-1 / Web-2 응답 분산 확인 |
| 장애 대응 | Web Node 1 중지 시 Web Node 2 응답 확인 |
| 자동화 | OpenStack CLI + Ansible End-to-End 자동화 검토 |

---

## 5.3 Phase 3 진행 조건

| 조건 | 내용 |
|---|---|
| Phase 1 완료 | 필수 구성사항 완료 |
| Phase 1 캡처 | 필수 캡처 확보 |
| Phase 2 상태 | 주요 확장 항목 완료 또는 발표 가능한 수준 확보 |
| 발표 안정성 | 최종 발표 가능한 기본 산출물 확보 |
| 실패 대응 | 실패 시 Phase 1 / Phase 2 결과 중심으로 발표 가능 |

---

## 5.4 Phase 3 제외 기준

Phase 3에서도 아래 항목은 제외한다.

~~~text
WordPress files 자동 동기화
wp-content/uploads 공유
plugin/theme 동기화
NFS 기반 WordPress shared storage
Object Storage 연동
DB Replication
DB Clustering
OpenStack LBaaS / Octavia
Auto Scaling
~~~

Phase 3 시연은 운영 수준의 완전한 고가용성 구현이 아니라, HAProxy 분산 동작과 공통 DB 연결 검증으로 제한한다.

---

## 6. Out of Scope: 제외 범위

Out of Scope 항목은 기본 프로젝트 기간과 팀 구현 안정성을 고려하여 이번 프로젝트 범위에서 제외한다.

다음 항목은 기술적으로 의미가 있더라도, 구현 난이도와 검증 부담이 높아 Phase 1 완성도와 최종 제출 일정에 영향을 줄 수 있으므로 이번 프로젝트에서는 다루지 않는다.

| 구분 | 제외 항목 |
|---|---|
| 컨테이너 오케스트레이션 | Docker Swarm |
| 컨테이너 오케스트레이션 | Kubernetes |
| OpenStack | Kolla-Ansible 전체 OpenStack 자동 구축 |
| OpenStack | Trove DBaaS 완성 구현 |
| OpenStack | Octavia / LBaaS 구성 |
| 스토리지 | Manila Shared File System 구현 |
| 스토리지 | Ceph 연동 |
| 스토리지 | NFS 기반 WordPress shared storage |
| DB | DB Replication |
| DB | DB Clustering |
| 확장성 | 오토스케일링 |
| 확장성 | 운영 수준의 멀티 Web Node HA |
| WordPress | WordPress files 자동 동기화 |
| WordPress | wp-content/uploads 공유 |
| 모니터링 | 복잡한 대시보드 개발 |
| CI/CD | GitHub Actions 기반 서비스 배포 자동화 CI/CD |
| 운영 | 운영 수준의 백업 스케줄링 |
| 운영 | 실서비스 도메인 및 공인 인증서 적용 |
| 보안 | OpenStack 전체 API TLS 고도화 |
| 보안 | Barbican 연동 |
| 보안 | Vault 연동 |
| 보안 | WAF 구성 |
| 보안 | IDS/IPS 연동 |
| 보안 | 인증서 자동 갱신 체계 |
| 보안 | Zero Trust 구성 |

---

## 7. 핵심 기준

본 프로젝트의 범위 기준은 다음과 같다.

~~~text
Phase 1:
Proxy Node, Web Node, DB Node, Backup / Validation Node를 분리한 기본 운영 구조를 완성한다.

Phase 2:
HTTPS, Cinder Backup Volume, Monitoring, 자동화 개선처럼 Phase 1 위에 추가하는 운영 보강 기능으로 정의한다.

Phase 3:
Web Node 2대와 HAProxy Load Balancing을 통한 확장성 검증으로 제한한다.

Out of Scope:
프로젝트 기간과 팀 구현 안정성을 고려하여 과도한 고가용성, 클러스터링, 오케스트레이션, 운영 보안 고도화 항목은 제외한다.
~~~


