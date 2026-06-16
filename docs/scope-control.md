<!-- STATUS: COMPLETE -->

# Scope Control Policy

## 1. 목적

본 문서는 Team Dandelion 프로젝트의 구현 범위를 통제하기 위한 기준을 정의한다.

프로젝트 진행 중 기능 범위가 과도하게 확장되어 구현, 검증, 발표, 제출 일정에 영향을 주는 것을 방지하고, 평가 기준에 맞는 핵심 흐름을 안정적으로 완성하는 것을 목적으로 한다.

본 프로젝트의 핵심은 기능을 많이 추가하는 것이 아니라, OpenStack 인프라 구성부터 Ansible 자동화, Docker Compose 기반 WordPress/MariaDB 서비스 배포, 상태 점검, 백업 및 복구 검증까지의 운영 흐름을 끝까지 완성하는 것이다.

---

## 2. 범위 통제 원칙

본 프로젝트는 기능 수를 늘리는 것보다, 인프라 구성부터 자동화, 서비스 배포, 검증, 제출까지의 흐름을 끝까지 완성하는 것을 우선한다.

구현 범위는 아래와 같이 A급, B급, B+ Stretch Goal, C급으로 구분한다.

~~~text
A급: 필수 구현 범위
B급: 선택 확장 범위
B+ : 추가 도전 범위
C급: 이번 프로젝트 제외 범위
~~~

A급이 완료되지 않으면 B급 확장 작업을 진행하지 않는다.

B급이 실패하더라도 A급 결과 중심으로 발표한다.

B+ Stretch Goal은 최종 발표에 필수로 포함하지 않는다.

---

## 3. A급: 필수 구현 범위

A급은 최종 발표와 시연을 위해 반드시 완료해야 하는 핵심 범위이다.

A급의 목표는 OpenStack 위에 Ubuntu 기반 인스턴스를 구성하고, Ansible을 통해 Docker 및 WordPress/MariaDB 서비스를 배포한 뒤, 상태 점검과 백업/복구 검증까지 완료하는 것이다.

| 구분 | 필수 구현 내용 |
|---|---|
| 인프라 | OpenStack 인프라 구성 |
| 인프라 | Ubuntu 이미지 기반 인스턴스 생성 |
| 인프라 | Control Node, Web Node, Backup / Validation Node 구분 |
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
| 서비스 | MariaDB 컨테이너 구성 |
| 서비스 | Docker Compose 기반 WordPress + MariaDB 배포 |
| 검증 | docker ps를 통한 WordPress / MariaDB 컨테이너 상태 확인 |
| 검증 | ss -tulnp 또는 포트 확인 명령으로 서비스 포트 확인 |
| 검증 | curl 또는 브라우저를 통한 WordPress HTTP 접속 확인 |
| 상태 점검 | health_check.sh 실행 |
| 백업 | backup.sh 실행 |
| 백업 | MariaDB dump 파일 생성 |
| 백업 | WordPress files archive 생성 |
| 보안 | HAProxy Reverse Proxy 구성 |
| 보안 | HAProxy 기반 HTTPS 적용 |
| 보안 | self-signed 인증서 기반 HTTPS 접속 확인 |
| 보안 | HTTP 80 → HTTPS 443 Redirect 구성 |
| 보안 | curl -k 또는 브라우저를 통한 HTTPS 접속 검증 |

---

## 4. B급: 선택 확장 범위

B급은 A급 구현과 캡처가 완료된 이후, 시간이 남을 경우 추가로 시도하는 확장 범위이다.

A급이 불안정한 상태에서는 B급 작업을 진행하지 않는다.  
B급이 실패하더라도 A급 결과 중심으로 발표한다.

B급의 목적은 A급의 기본 운영 흐름 위에 보안, 스토리지, 모니터링, 자동화 개선 요소를 추가하여 프로젝트의 전문성과 차별성을 높이는 것이다.

| 구분 | 선택 확장 내용 |
|---|---|
| 복구 | restore.md 기반 복구 절차 정리 |
| 복구 | Restore 절차 검증 |
| 장애 대응 | 간단한 장애 상황 1개와 복구 절차 정리 |
| 스토리지 | Cinder Volume 생성 테스트 |
| 스토리지 | Cinder Volume 인스턴스 attach 테스트 |
| 스토리지 | NFS 기반 백업 저장소 구성 시도 |
| 모니터링 | node_exporter 구성 |
| 모니터링 | cAdvisor 구성 |
| 모니터링 | Prometheus 구성 |
| 시각화 | Grafana 대시보드 구성 |
| 검증 | 간단한 모니터링 화면 캡처 |
| 자동화 개선 | Ansible playbook 역할 분리 개선 |
| 자동화 개선 | backup / restore 절차 playbook화 |
| 문서 | IP 주소표 정리 |
| 문서 | 보안그룹 및 포트표 정리 |
| 문서 | 담당자별 수행 내역 정리 |
| 문서 | 트러블슈팅 로그 정리 |
| 산출물 | 담당자별 캡처 및 문서 정리 |

---

## 5. B+ Stretch Goal: OpenStack CLI + Ansible End-to-End Automation

B+ Stretch Goal은 A급 필수 구현과 B급 주요 확장이 조기에 완료될 경우에만 시도하는 추가 도전 범위이다.

B+의 목표는 Ansible에서 OpenStack CLI를 호출하여 인프라 생성부터 서비스 배포, 검증까지 End-to-End 자동화 흐름을 구성하는 것이다.

B+는 필수 제출 범위가 아니며, 구현 중 문제가 발생할 경우 기존 A급 및 B급 산출물을 기준으로 발표한다.

### 목표

~~~text
Ansible 실행
→ OpenStack CLI 기반 인프라 생성
→ Network / Subnet / Router / Security Group 생성
→ Ubuntu Instance 생성
→ Floating IP 또는 접속 정보 확인
→ Inventory 반영
→ 서버 설정 자동화
→ WordPress/MariaDB 배포
→ HAProxy Reverse Proxy 구성
→ Prometheus/Grafana 모니터링 구성
→ Health Check / Backup / Restore 검증
~~~

### 포함 가능 범위

| 구분 | 내용 |
|---|---|
| OpenStack CLI | network, subnet, router, security group, server, floating ip 생성 |
| Ansible | OpenStack CLI 실행, 노드 접속 확인, 서버 설정 자동화 |
| Service | Custom WordPress + MariaDB 배포 |
| Proxy | HAProxy Reverse Proxy 및 HTTPS 구성 |
| Monitoring | Prometheus, Grafana, node_exporter, cAdvisor 구성 |
| Validation | health check, backup, restore 검증 |

### 진행 조건

- A급 필수 구현 완료
- A급 필수 캡처 확보
- B급 주요 확장 항목 완료 또는 발표 가능한 수준 확보
- 최종 발표 가능한 기본 산출물 확보
- 실패 시 A급/B급 결과 중심으로 발표 가능

### 제외 기준

B+ Stretch Goal은 필수 제출 범위가 아니다.  
구현 중 문제가 발생할 경우, 기존 A급 및 B급 산출물을 기준으로 발표한다.

---

## 6. C급: 이번 프로젝트 제외 범위

C급은 기본 프로젝트 기간과 팀 구현 안정성을 고려하여 이번 프로젝트 범위에서 제외한다.

C급 항목은 기술적으로 의미가 있더라도, 구현 난이도와 검증 부담이 높아 A급 완성도와 최종 제출 일정에 영향을 줄 수 있으므로 이번 프로젝트에서는 다루지 않는다.

| 제외 항목 |
|---|
| Docker Swarm |
| Kubernetes |
| Kolla-Ansible 전체 OpenStack 자동 구축 |
| Trove DBaaS 완성 구현 |
| Manila Shared File System 구현 |
| Ceph 연동 |
| Octavia / LBaaS 구성 |
| 오토스케일링 |
| 멀티 Web Node HA |
| DB Replication |
| DB Clustering |
| 복잡한 대시보드 개발 |
| 자체 Registry 운영 |
| GitHub Actions 기반 서비스 배포 자동화 CI/CD |
| 운영 수준의 백업 스케줄링 |
| 실서비스 도메인 및 공인 인증서 적용 |
| OpenStack 전체 API TLS 고도화 |
| Barbican 연동 |
| Vault 연동 |
| WAF 구성 |
| IDS/IPS 연동 |
| 인증서 자동 갱신 체계 |
| Zero Trust 구성 |

---

## 7. 진행 기준

| 조건 | 판단 |
|---|---|
| A급 미완료 | B급 진행 금지 |
| A급 완료 | B급 선택 진행 가능 |
| B급 실패 | A급 결과 중심으로 발표 |
| B+ 실패 | A급/B급 결과 중심으로 발표 |
| C급 요청 발생 | 이번 프로젝트 범위 제외로 처리 |
| HTTPS 적용 실패 | HTTP 기반 A급 서비스 검증 결과로 발표 |
| 보안그룹 미구성 | A급 미완료로 판단 |
| SSH 접속 실패 | A급 미완료로 판단 |
| Ansible ping 실패 | A급 미완료로 판단 |
| WordPress 접속 실패 | A급 미완료로 판단 |
| MariaDB 컨테이너 미실행 | A급 미완료로 판단 |
| 백업/복구 절차 미정리 | A급 미완료로 판단 |
| 백업 파일 미생성 | A급 미완료로 판단 |
| Restore 검증 불가 | A급 미완료로 판단 |

---

## 8. 발표 시 설명 기준

본 프로젝트는 기본 프로젝트 범위에 맞춰 인프라 운영 자동화의 핵심 흐름을 안정적으로 구현하는 것을 우선 목표로 설정하였다.

따라서 OpenStack 인프라 구성, Ubuntu 인스턴스 생성, Ansible 기반 자동화, Docker Compose 기반 WordPress/MariaDB 서비스 배포, 상태 점검, 백업 및 복구 검증까지의 운영 흐름을 완성하는 데 집중한다.

Prometheus, Grafana, HAProxy HTTPS, Cinder, NFS 등 확장 항목은 시간과 안정성을 고려하여 선택 확장 항목으로 분리한다.

OpenStack CLI + Ansible End-to-End 자동화는 추가 도전 범위로 관리하며, 최종 제출의 필수 성공 기준으로 보지 않는다.

---

## 9. 구현 일정 기준

| 구분 | 목표 완료일 | 기준 |
|---|---|---|
| A급 필수 구현 | 2026-06-26 | OpenStack, Ubuntu Instance, SSH, Ansible, Docker Compose, WordPress/MariaDB, Health Check, Backup/Restore, 필수 캡처 완료 |
| B급 선택 확장 | 2026-07-10 | HAProxy HTTPS, Cinder/NFS, node_exporter, cAdvisor, Prometheus/Grafana, Playbook 개선 중 가능한 항목만 수행 |
| 최종 정리 | 2026-07-14 | 결과보고서, 시연 영상, 소스코드, 작업일지, 회의록, Google Drive 제출자료 정리 |

A급 필수 구현은 2026-06-26까지 완료하는 것을 목표로 한다.  
B급 선택 확장은 A급 완료 후 2026-07-10까지 가능한 범위에서 진행한다.  
2026-07-10 이후에는 신규 기능 추가보다 발표자료, 시연 영상, 제출자료 정리에 집중한다.

---

## 10. 최종 성공 기준

| 구분 | 성공 기준 |
|---|---|
| 인프라 | OpenStack 기반 Ubuntu 인스턴스 생성 완료 |
| 접속 | SSH 접속 및 포트포워딩 또는 Floating IP 접속 확인 |
| Ansible | ansible ping 및 playbook 실행 성공 |
| Docker | Docker 설치 및 Docker Compose 실행 가능 |
| 서비스 | WordPress / MariaDB 컨테이너 running 상태 |
| 접속 검증 | WordPress HTTP 응답 확인 |
| 상태 점검 | health_check.sh 실행 결과 확보 |
| 백업 | MariaDB dump 및 WordPress files archive 생성 |
| 복구 | restore.md 기반 복구 절차 검증 |
| 문서 | 담당자별 문서, 캡처, 트러블슈팅 로그 정리 |
| 제출 | GitHub, Google Drive, 발표자료, 시연 영상 정리 |

---

## 11. 결론

Team Dandelion은 기능 확장보다 완성도와 시연 가능성을 우선한다.

A급 필수 구현 범위를 먼저 완료하고, 이후 여유가 있을 경우 B급 선택 확장 범위를 진행한다.

B+ Stretch Goal은 추가 도전 범위이며, 최종 제출의 필수 성공 기준으로 보지 않는다.

C급 항목은 기본 프로젝트 기간과 구현 안정성을 고려하여 이번 프로젝트 범위에서 제외한다.
