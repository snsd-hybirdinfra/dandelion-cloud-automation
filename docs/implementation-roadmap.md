<!-- STATUS: COMPLETE -->

# Implementation Roadmap

## 1. 목적

본 문서는 Team Dandelion 프로젝트의 구현 단계를 Phase 기반으로 정리한다.

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

Phase 1에서는 Control Node, Proxy Node, Web Node, DB Node, Backup / Validation Node를 분리한 기본 클라우드 운영 구조를 구현한다.

Phase 2에서는 HTTPS, Cinder Backup Volume, Prometheus/Grafana, 자동화 구조 개선을 통해 운영성을 강화한다.

Phase 3에서는 Web Node 2대와 HAProxy Load Balancing을 통해 확장성을 검증한다.

~~~text
Phase 1
필수 구성 및 기본 검증
→ OpenStack Ubuntu Instance
→ Control / Proxy / Web / DB / Backup Node
→ Ansible
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

## 3. 전체 목표 구조

## 3.1 Phase 1 기본 구조

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
   ├── MariaDB dump
   ├── WordPress files archive
   └── restore.md 검증

Control Node
→ Ansible 실행
→ Proxy / Web / DB / Backup Node 관리
~~~

---

## 3.2 Phase 2 확장 구조

~~~text
Phase 1 기본 구조
+ HAProxy HTTPS
+ HTTP to HTTPS Redirect
+ Cinder Backup Volume
+ node_exporter
+ cAdvisor
+ Prometheus
+ Grafana
+ backup / restore playbook
+ Ansible roles
~~~

---

## 3.3 Phase 3 도전 구조

~~~text
Client
→ Proxy Node / HAProxy Load Balancer
→ Web Node 1 / WordPress
→ Web Node 2 / WordPress
→ DB Node / MariaDB
→ Backup / Validation Node
~~~

Phase 3는 운영 수준의 완전한 고가용성 구현이 아니라, HAProxy 분산 동작과 공통 DB 연결 검증을 목표로 한다.

---

## 4. Phase 1: 필수 구성 및 기본 검증 단계

## 4.1 Phase 1 목표

Phase 1의 목표는 OpenStack 기반 Ubuntu 인스턴스를 구성하고, Control Node, Proxy Node, Web Node, DB Node, Backup / Validation Node를 분리한 뒤, Ansible을 통해 Docker 기반 서비스를 배포하고, 상태 점검과 백업/복구 검증까지 완료하는 것이다.

Phase 1은 최종 발표와 시연을 위한 최소 성공 기준이다.

Phase 1은 단일 Web/DB 통합 구조가 아니라, Proxy 계층, Web 계층, DB 계층, Backup / Validation 계층을 분리한 기본 운영 구조로 정의한다.

---

## 4.2 Phase 1 구현 순서

| 순서 | 구현 항목 | 담당 영역 | 성공 기준 |
|---:|---|---|---|
| 1 | OpenStack 인프라 구성 | Cloud Infrastructure | OpenStack 대시보드 또는 CLI에서 리소스 확인 |
| 2 | Ubuntu 이미지 기반 인스턴스 생성 | Cloud Infrastructure | 인스턴스 ACTIVE 상태 |
| 3 | Control / Proxy / Web / DB / Backup Node 구분 | Cloud Infrastructure / PM | 노드 역할표 작성 |
| 4 | 네트워크 / 라우터 / 서브넷 구성 | Cloud Infrastructure | 네트워크 통신 가능 |
| 5 | Floating IP 또는 포트포워딩 접속 경로 구성 | Cloud Infrastructure | 외부 접속 경로 확보 |
| 6 | 보안그룹 SSH / HTTP 포트 정책 구성 | Cloud Infrastructure | 허용 포트 기준 정리 |
| 7 | SSH 접속 확인 | Cloud Infrastructure / Ansible | Control Node에서 대상 노드 접속 성공 |
| 8 | ansible.cfg 작성 | Ansible Automation | Ansible 설정 파일 작성 |
| 9 | inventory.ini 작성 | Ansible Automation | Proxy / Web / DB / Backup Node 등록 |
| 10 | Ansible ping 테스트 | Ansible Automation | ansible all -m ping 성공 |
| 11 | Docker 설치 자동화 | Ansible / Server | 대상 노드 Docker 설치 완료 |
| 12 | DB Node MariaDB 설치 및 구성 | Server / Ansible | MariaDB 서비스 running |
| 13 | Web Node Custom WordPress 배포 | Server / Ansible | WordPress 컨테이너 running |
| 14 | Web Node → DB Node 연결 확인 | Server / Validation | WordPress가 DB Node MariaDB에 연결 |
| 15 | Proxy Node HAProxy HTTP Reverse Proxy 구성 | Server / Ansible | Proxy Node 80 → Web Node 80 연결 |
| 16 | Proxy Node 경유 WordPress HTTP 접속 확인 | Validation | curl 또는 브라우저 접속 성공 |
| 17 | systemctl status mariadb 서비스 running |
| 18 | ss -tulnp 또는 포트 확인 | Validation | 서비스 포트 listening 확인 |
| 19 | health_check.sh 실행 | Monitoring / Validation | 상태 점검 결과 확보 |
| 20 | backup.sh 실행 | Backup / Validation | DB dump 및 WordPress files archive 생성 |
| 21 | restore.md 기반 복구 절차 검증 | Backup / Validation | 복구 절차 문서화 및 검증 |
| 22 | 장애 상황 1개와 복구 절차 정리 | Validation / PM | 트러블슈팅 로그 작성 |
| 23 | IP 주소표 / 보안그룹 / 포트표 정리 | PM / Cloud Infrastructure | 제출 문서 반영 |
| 24 | 담당자별 캡처 및 문서 정리 | 전체 | GitHub 및 Google Drive 산출물 정리 |

---

## 4.3 Phase 1 성공 기준

| 구분 | 성공 기준 |
|---|---|
| 인프라 | OpenStack 기반 Ubuntu 인스턴스 생성 |
| 노드 | Control / Proxy / Web / DB / Backup Node 역할 구분 |
| 접속 | SSH 접속 성공 |
| Ansible | ansible all -m ping 성공 |
| 자동화 | site.yml 또는 playbook 실행 성공 |
| Docker | Docker 설치 및 Docker Compose 실행 가능 |
| DB | DB Node에서 MariaDB 서비스 running |
| Web | Web Node에서 Custom WordPress 컨테이너 running |
| Proxy | Proxy Node에서 HAProxy HTTP Reverse Proxy 동작 |
| 연결 | Web Node WordPress가 DB Node MariaDB에 연결 |
| 접속 검증 | Proxy Node 경유 WordPress HTTP 응답 확인 |
| 상태 점검 | health_check.sh 실행 결과 확보 |
| 백업 | MariaDB dump 및 WordPress files archive 생성 |
| 복구 | restore.md 기반 복구 절차 검증 |
| 장애 대응 | 최소 장애 상황 1개와 복구 절차 정리 |
| 문서 | 필수 문서, 캡처, 회의록, 작업일지 정리 |

---

## 4.4 Phase 1 캡처 기준

| 영역 | 캡처 예시 |
|---|---|
| OpenStack | 인스턴스 목록, 네트워크, 라우터, 서브넷 |
| 보안그룹 | SSH / HTTP 허용 정책 |
| 접속 | SSH 접속 성공 |
| Ansible | ansible all -m ping 결과 |
| Playbook | site.yml 또는 playbook 실행 결과 |
| Docker | docker version, docker compose version |
| DB Node | MariaDB 서비스 running |
| Web Node | WordPress 컨테이너 running |
| Proxy Node | HAProxy 컨테이너 running |
| HTTP 검증 | Proxy Node 경유 WordPress 접속 |
| 포트 검증 | ss -tulnp 또는 포트 확인 결과 |
| 상태 점검 | health_check.sh 실행 결과 |
| 백업 | MariaDB dump, WordPress files archive |
| 복구 | restore 절차 검증 결과 |
| 트러블슈팅 | 장애 상황 및 복구 과정 |

---

## 5. Phase 2: 운영 확장 및 검증 고도화 단계

## 5.1 Phase 2 목표

Phase 2는 Phase 1 구현과 필수 캡처가 완료된 이후 가능한 범위에서 진행한다.

Phase 2의 목적은 Phase 1의 기본 운영 흐름 위에 보안 강화, 스토리지 분리, 모니터링, 자동화 개선 요소를 추가하여 프로젝트의 전문성과 차별성을 높이는 것이다.

Phase 2가 실패하더라도 Phase 1 결과 중심으로 발표할 수 있도록 범위를 분리한다.

---

## 5.2 Phase 2 우선순위

| 우선순위 | 확장 항목 | 목적 | 실패 시 처리 |
|---:|---|---|---|
| 1 | HTTPS self-signed | HTTPS 접속 검증 | HTTP 기반 Phase 1 결과 발표 |
| 2 | HTTP to HTTPS Redirect | 접속 보안 흐름 개선 | HTTPS 결과만 발표 |
| 3 | Cinder Backup Volume | 백업 저장소 분리 | 로컬 백업 기준 발표 |
| 4 | node_exporter / cAdvisor | OS / Container 메트릭 수집 | health_check.sh 기준 발표 |
| 5 | Prometheus | 메트릭 수집 서버 구성 | exporter 결과만 발표 |
| 6 | Grafana | 대시보드 시각화 | Prometheus target 결과만 발표 |
| 7 | backup / restore playbook화 | 운영 절차 자동화 개선 | shell script 기준 발표 |
| 8 | Ansible roles 구조 분리 | playbook 구조 개선 | 단일 site.yml 기준 발표 |
| 9 | 상세 검증 리포트 고도화 | 발표 근거 강화 | Phase 1 기본 검증표 사용 |
| 10 | 운영 장애 시나리오 확장 | 운영성 어필 | 장애 1개 기준 발표 |

---

## 5.3 Phase 2 상세 항목

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

## 5.4 Phase 2 Cinder 처리 기준

Phase 2의 Cinder Volume은 DB 원본 데이터 저장소가 아니라, Backup / Validation Node의 백업 저장소로 사용한다.

~~~text
DB Node
→ MariaDB 운영 데이터 보관

Backup / Validation Node
→ Cinder Volume attach
→ /backup mount
→ MariaDB dump 및 WordPress files backup 저장
~~~

DB Node의 MariaDB 원본 데이터를 Cinder Volume에 직접 올리는 방식은 이번 범위에서 제외한다.

---

## 6. Phase 3: 도전 확장 단계

## 6.1 Phase 3 목표

Phase 3은 Phase 1 필수 구성과 Phase 2 주요 서브 구성사항이 조기에 완료될 경우에만 시도하는 도전 확장 단계이다.

Phase 3의 목표는 기존 Phase 1 구조를 유지하면서 Web Node를 2대로 확장하고, HAProxy를 통해 roundrobin 방식의 Load Balancing을 검증하는 것이다.

Phase 3은 필수 제출 범위가 아니며, 구현 중 문제가 발생할 경우 기존 Phase 1 및 Phase 2 산출물을 기준으로 발표한다.

---

## 6.2 Phase 3 목표 구조

~~~text
Client
→ Proxy Node / HAProxy Load Balancer
→ Web Node 1 / WordPress
→ Web Node 2 / WordPress
→ DB Node / MariaDB
→ Backup / Validation Node
~~~

---

## 6.3 Phase 3 구현 순서

| 순서 | 구현 항목 | 성공 기준 |
|---:|---|---|
| 1 | Web Node 2 생성 | OpenStack 인스턴스 ACTIVE |
| 2 | Web Node 2 SSH 접속 | Control Node에서 접속 가능 |
| 3 | Web Node 2 Ansible inventory 반영 | ansible ping 성공 |
| 4 | Web Node 2 WordPress 배포 | WordPress 컨테이너 running |
| 5 | Web Node 2 → DB Node 연결 | 공통 DB Node MariaDB 연결 |
| 6 | HAProxy backend 2개 등록 | Web-1 / Web-2 backend 등록 |
| 7 | HAProxy roundrobin 설정 | 요청 분산 동작 |
| 8 | Web-1 / Web-2 응답 구분 | health.html 또는 식별 응답 확인 |
| 9 | Web Node 장애 테스트 | Web-1 중지 시 Web-2 응답 |
| 10 | 결과 문서화 | Phase 3 검증 결과 정리 |

---

## 6.4 Phase 3 제한 사항

WordPress는 DB뿐만 아니라 `wp-content/uploads`, plugins, themes 같은 파일도 로컬에 저장한다.

따라서 Web Node 2대 구성 시 WordPress files 동기화 문제가 발생할 수 있다.

이번 프로젝트에서는 아래 항목을 구현 범위에서 제외한다.

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

Phase 3 시연은 HAProxy roundrobin, Web-1/Web-2 응답 분산, 공통 DB Node 연결 확인 수준으로 제한한다.

---

## 7. Out of Scope

다음 항목은 프로젝트 범위를 과도하게 확장할 수 있으므로 이번 구현 범위에서는 제외한다.

| 제외 항목 | 제외 이유 |
|---|---|
| OpenStack LBaaS / Octavia | OpenStack 서비스 의존성과 설정 난이도가 높음 |
| DB Replication | DB 복제 검증 범위가 별도 프로젝트 수준으로 확장됨 |
| DB Clustering | 장애 대응 및 데이터 정합성 검증 부담 증가 |
| Auto Scaling | 모니터링, 이미지, 배포 자동화까지 범위 확장 |
| Kubernetes | 현재 프로젝트의 Ansible / Docker Compose 중심과 범위 불일치 |
| Docker Swarm | Docker Compose 기반 실습 범위를 벗어남 |
| WordPress files 자동 동기화 | 파일 충돌, 권한, 공유 스토리지 이슈 발생 |
| Production-level HTTPS | 공인 도메인 및 인증서 자동 갱신 범위 필요 |
| Kolla-Ansible 전체 OpenStack 자동 구축 | 기본 프로젝트 범위를 과도하게 초과함 |
| Trove DBaaS 완성 구현 | DBaaS 운영 검증 부담이 큼 |
| Manila / Ceph 연동 | 공유 스토리지 운영 범위가 별도 프로젝트 수준임 |
| GitHub Actions 기반 서비스 배포 CI/CD | 서비스 배포 자동화 범위가 과도하게 확장됨 |
| WAF / IDS / IPS / Zero Trust | 보안 운영 고도화 범위가 과도하게 큼 |

---

## 8. 최종 진행 순서

~~~text
Phase 1. 필수 구성 및 기본 검증
1. OpenStack Ubuntu 인스턴스 생성
2. Control / Proxy / Web / DB / Backup Node 구분
3. 네트워크 / 보안그룹 / 포트포워딩 정리
4. SSH 접속 확인
5. Ansible inventory 구성
6. ansible ping 성공
7. Docker 설치 playbook 실행
8. DB Node MariaDB 설치 및 구성
9. Web Node WordPress 배포
10. Web Node → DB Node 연결 확인
11. Proxy Node HAProxy HTTP Reverse Proxy 구성
12. Proxy Node 경유 WordPress HTTP 접속 확인
13. health_check.sh 실행
14. backup.sh 실행
15. restore.md 정리 및 복구 검증
16. 필수 캡처 및 문서 정리

Phase 2. 운영 확장 및 검증 고도화
1. HTTPS self-signed
2. HTTP to HTTPS Redirect
3. Cinder Volume Backup Storage
4. node_exporter / cAdvisor
5. Prometheus
6. Grafana
7. backup / restore playbook화
8. Ansible roles 구조 분리
9. 상세 검증 리포트 고도화
10. 운영 장애 시나리오 확장

Phase 3. 도전 확장
1. Web Node 2 생성
2. Web Node 2 WordPress 배포
3. HAProxy backend 2개 등록
4. HAProxy roundrobin LB
5. Web-1/Web-2 health 응답 분산 확인
6. 공통 DB Node 연결 확인
7. Web Node 장애 대응 검증
8. OpenStack CLI + Ansible End-to-End 자동화 검토
~~~

---

## 9. 발표용 설명 문장

본 프로젝트는 Phase 기반 구현 로드맵으로 범위를 정의한다.

Phase 1은 최종 발표와 시연을 위해 반드시 완료해야 하는 필수 구성 및 기본 검증 단계이다. Control Node, Proxy Node, Web Node, DB Node, Backup / Validation Node를 분리하고, Ansible을 통해 WordPress, MariaDB, HAProxy HTTP Reverse Proxy를 배포한다. 이후 상태 점검, 백업, 복구 절차 검증, 필수 문서 및 캡처 정리까지 완료한다.

Phase 2는 Phase 1이 안정화된 이후 추가하는 운영 확장 및 검증 고도화 단계이다. HTTPS, Cinder Backup Volume, Prometheus/Grafana, Ansible 구조 개선 등을 통해 보안성, 저장소 분리, 관측 가능성, 자동화 품질을 강화한다.

Phase 3은 도전 확장 단계이다. Web Node 2대와 HAProxy Load Balancing을 통해 확장성을 검증하되, WordPress files 자동 동기화나 OpenStack LBaaS/Octavia는 제외한다.

Out of Scope 항목은 프로젝트 기간과 팀 구현 안정성을 고려하여 이번 구현 범위에서 제외한다.



