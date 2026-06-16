<!-- STATUS: COMPLETE -->

# Presentation Outline

## 1. 문서 목적

본 문서는 Team Dandelion 프로젝트의 최종 발표 흐름을 정의한다.

본 프로젝트는 Phase 기반 구현 로드맵을 사용한다.

~~~text
Phase 1: 필수 구성 및 기본 검증 단계
Phase 2: 운영 확장 및 검증 고도화 단계
Phase 3: 도전 확장 단계
Out of Scope: 제외 범위
~~~

발표의 핵심은 기능을 많이 나열하는 것이 아니라, OpenStack 인프라 구성부터 Ansible 자동화, 서비스 배포, Proxy 경유 접속, 상태 점검, 백업, 복구 검증까지 하나의 운영 흐름으로 설명하는 것이다.

---

## 2. 발표 핵심 메시지

~~~text
Team Dandelion 프로젝트는 OpenStack 기반 클라우드 인프라 환경에서
Ansible을 활용하여 반복적인 서버 설정, 서비스 배포, 상태 점검, 백업 및 복구 절차를 자동화하는 프로젝트입니다.

단순히 WordPress를 배포하는 것이 아니라,
Control Node, Proxy Node, Web Node, DB Node, Backup / Validation Node를 분리하고,
HAProxy, WordPress, MariaDB를 역할별로 구성하여
클라우드 인프라 운영 자동화 흐름을 검증하는 것이 핵심입니다.
~~~

---

## 3. 발표 전체 구성

| 순서 | 슬라이드 주제 | 핵심 내용 |
|---:|---|---|
| 1 | 프로젝트 소개 | 팀명, 주제, 목표 |
| 2 | 문제 정의 | 수동 인프라 운영의 반복성, 설정 오류, 검증 누락 |
| 3 | 프로젝트 목표 | Ansible 기반 자동화, 서비스 배포, 백업/복구 검증 |
| 4 | Phase 기반 구현 전략 | Phase 1 / 2 / 3 / Out of Scope |
| 5 | 전체 아키텍처 | Control / Proxy / Web / DB / Backup Node |
| 6 | OpenStack 인프라 구성 | 인스턴스, 네트워크, 보안그룹 |
| 7 | Ansible 자동화 구조 | inventory, site.yml, 역할별 배포 |
| 8 | 서비스 구성 | HAProxy, WordPress, MariaDB |
| 9 | Proxy / Web / DB 통신 흐름 | Proxy 경유 접속, DB 연결 |
| 10 | 검증 결과 | SSH, Ansible, Docker, HTTP, DB |
| 11 | Health Check / Backup / Restore | 상태 점검, 백업, 복구 절차 |
| 12 | 장애 대응 | 장애 시나리오와 트러블슈팅 |
| 13 | Phase 2 운영 확장 | HTTPS, Cinder, Monitoring |
| 14 | Phase 3 도전 확장 | Web Node 2대, HAProxy LB |
| 15 | Out of Scope 및 한계 | 제외 범위와 이유 |
| 16 | 최종 결과 | 성공 기준, 산출물, 기대 효과 |

---

## 4. Slide 1: 프로젝트 소개

## 제목

~~~text
Ansible 기반 클라우드 인프라 자동화 및 운영 최적화 시스템 구축
~~~

## 포함 내용

| 항목 | 내용 |
|---|---|
| 팀명 | Dandelion |
| 프로젝트 기간 | 2026.06.11 ~ 2026.07.14 |
| 핵심 기술 | OpenStack, Ubuntu, Ansible, Docker Compose, WordPress, MariaDB, HAProxy |
| 목표 | 클라우드 인프라 구성, 서비스 배포, 상태 점검, 백업 및 복구 검증 자동화 |

## 발표 멘트

~~~text
저희 Dandelion 팀은 OpenStack 기반 클라우드 인프라 환경에서 Ansible을 활용하여 서버 설정, 서비스 배포, 상태 점검, 백업 및 복구 절차를 자동화하는 프로젝트를 진행했습니다.
~~~

---

## 5. Slide 2: 문제 정의

## 제목

~~~text
수동 인프라 운영의 반복성과 검증 누락 문제
~~~

## 포함 내용

| 문제 | 설명 |
|---|---|
| 반복 작업 | 서버 생성, 패키지 설치, 서비스 배포가 반복됨 |
| 설정 편차 | 팀원 또는 서버마다 설정 방식이 달라질 수 있음 |
| 검증 누락 | 접속 확인, 포트 확인, 백업 확인이 누락될 수 있음 |
| 장애 대응 어려움 | 장애 발생 시 원인 추적 절차가 정리되어 있지 않음 |
| 산출물 관리 부담 | 캡처, 문서, 결과물을 수동으로 관리해야 함 |

## 발표 멘트

~~~text
기존 수동 방식에서는 서버별 설정 편차가 발생하기 쉽고, 서비스가 실행되더라도 접속, 백업, 복구 검증이 누락될 수 있습니다. 그래서 저희는 인프라 구성 이후 운영 검증까지 하나의 자동화 흐름으로 정리하는 것을 목표로 했습니다.
~~~

---

## 6. Slide 3: 프로젝트 목표

## 제목

~~~text
자동화 가능한 클라우드 운영 흐름 구현
~~~

## 포함 내용

~~~text
OpenStack 인프라 구성
→ Ubuntu 인스턴스 생성
→ Control / Proxy / Web / DB / Backup Node 분리
→ Ansible 자동화
→ Docker Compose 기반 서비스 배포
→ HAProxy HTTP Reverse Proxy
→ WordPress / MariaDB 연결
→ Health Check
→ Backup
→ Restore 검증
→ Troubleshooting 정리
~~~

## 발표 멘트

~~~text
프로젝트 목표는 단순히 서비스를 띄우는 것이 아니라, OpenStack 기반 인프라 위에서 Ansible을 통해 역할별 서버를 구성하고, WordPress와 MariaDB 서비스 배포 이후 상태 점검, 백업, 복구까지 검증하는 것입니다.
~~~

---

## 7. Slide 4: Phase 기반 구현 전략

## 제목

~~~text
Phase 기반 구현 로드맵
~~~

## 포함 내용

| Phase | 의미 | 구현 범위 |
|---|---|---|
| Phase 1 | 필수 구성 및 기본 검증 | OpenStack, Ansible, Docker, WordPress, MariaDB, HAProxy HTTP Reverse Proxy, Health Check, Backup, Restore |
| Phase 2 | 운영 확장 및 검증 고도화 | HTTPS, Cinder Backup Volume, Prometheus/Grafana, Playbook 개선 |
| Phase 3 | 도전 확장 | Web Node 2대, HAProxy Load Balancing, 공통 DB 연결 |
| Out of Scope | 제외 범위 | Kubernetes, Docker Swarm, DB Replication, OpenStack LBaaS/Octavia, WordPress files 자동 동기화 |

## 발표 멘트

~~~text
저희 프로젝트는 기능을 무리하게 확장하지 않기 위해 Phase 기반으로 범위를 나누었습니다. Phase 1은 반드시 완료해야 하는 필수 구성이고, Phase 2는 운영 확장, Phase 3은 도전 확장으로 정의했습니다.
~~~

---

## 8. Slide 5: 전체 시스템 아키텍처

## 제목

~~~text
Control / Proxy / Web / DB / Backup Node 분리 구조
~~~

## 포함 내용

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
   ├── mysqldump 기반 MariaDB dump
   ├── WordPress files archive
   └── restore.md 검증

Control Node
→ Ansible 실행
→ Proxy / Web / DB / Backup Node 관리
~~~

## 발표 멘트

~~~text
전체 구조는 Control Node가 Ansible을 실행하고, Proxy Node는 HAProxy, Web Node는 WordPress, DB Node는 MariaDB, Backup Node는 상태 점검과 백업/복구 검증을 담당하는 방식으로 분리했습니다.
~~~

---

## 9. Slide 6: OpenStack 인프라 구성

## 제목

~~~text
OpenStack 기반 Ubuntu 인스턴스 및 네트워크 구성
~~~

## 포함 내용

| 구성 요소 | 설명 |
|---|---|
| Instance | Control / Proxy / Web / DB / Backup Node |
| Image | Ubuntu 기반 이미지 |
| Network | Private Network |
| Subnet | 내부 통신용 Subnet |
| Router | External Network 연결 |
| Security Group | SSH / HTTP / DB 접근 제어 |
| External Access | Floating IP 또는 포트포워딩 |

## 발표 멘트

~~~text
OpenStack에서는 Ubuntu 기반 인스턴스를 역할별로 생성하고, 네트워크와 보안그룹을 통해 필요한 통신만 허용했습니다. Web Node와 DB Node는 외부에 직접 노출하지 않고 Proxy Node를 통해 접속하도록 구성했습니다.
~~~

---

## 10. Slide 7: Ansible 자동화 구조

## 제목

~~~text
Control Node 기반 Ansible 자동화
~~~

## 포함 내용

~~~text
Control Node
├── ansible.cfg
├── inventory.ini
└── site.yml

inventory groups:
- proxy
- web
- db
- backup

site.yml:
- Docker 설치
- DB Node MariaDB 설치 및 구성
- Web Node WordPress 배포
- Proxy Node HAProxy 배포
- Backup / Validation 준비
~~~

## 발표 멘트

~~~text
Ansible은 Control Node에서 실행되며, inventory를 통해 Proxy, Web, DB, Backup Node를 그룹별로 관리합니다. site.yml은 Docker 설치와 역할별 컨테이너 배포를 자동화합니다.
~~~

---

## 11. Slide 8: 서비스 구성

## 제목

~~~text
Docker Compose 기반 HAProxy / WordPress / MariaDB 구성
~~~

## 포함 내용

| Node | Service | Image / Role |
|---|---|---|
| Proxy Node | HAProxy | HTTP Reverse Proxy |
| Web Node | Custom WordPress | wordpress:php8.2-apache 기반 |
| DB Node | MariaDB | mariadb:10.11 |
| Backup Node | Scripts | health_check.sh, backup.sh |

## 발표 멘트

~~~text
서비스는 Docker Compose 기반으로 구성했습니다. WordPress는 공식 이미지를 기반으로 커스터마이징하고, MariaDB는 DB Node에 분리 배치했습니다. HAProxy는 Phase 1에서 HTTP Reverse Proxy 역할을 수행합니다.
~~~

---

## 12. Slide 9: Proxy / Web / DB 통신 흐름

## 제목

~~~text
Proxy 경유 접속과 DB 분리 구조
~~~

## 포함 내용

~~~text
User / Browser
→ Proxy Node:80
→ HAProxy
→ Web Node:80
→ WordPress
→ DB Node:3306
→ MariaDB
~~~

## 강조점

| 항목 | 설명 |
|---|---|
| Client | Web Node에 직접 접근하지 않음 |
| Proxy Node | 외부 HTTP 진입점 |
| Web Node | WordPress 실행 |
| DB Node | MariaDB 분리 실행 |
| Security Group | DB 3306 전체 공개 금지 |

## 발표 멘트

~~~text
사용자는 Web Node에 직접 접근하지 않고 Proxy Node를 통해 WordPress에 접근합니다. WordPress는 DB Node의 MariaDB에 연결하며, DB 포트는 전체 공개하지 않고 Web Node와 Backup Node에서만 접근하도록 제한했습니다.
~~~

---

## 13. Slide 10: Phase 1 검증 결과

## 제목

~~~text
Phase 1 필수 검증 결과
~~~

## 포함 내용

| 검증 항목 | 성공 기준 |
|---|---|
| OpenStack | 인스턴스 ACTIVE |
| SSH | Control Node에서 각 노드 접속 |
| Ansible | ansible all -m ping SUCCESS |
| Playbook | site.yml 실행 성공 |
| Docker | Docker / Compose 설치 확인 |
| DB | MariaDB 서비스 running |
| Web | WordPress 컨테이너 running |
| Proxy | HAProxy 컨테이너 running |
| HTTP | Proxy Node 경유 WordPress 접속 |
| DB 연결 | Web Node → DB Node 3306 연결 |

## 발표 멘트

~~~text
Phase 1 검증에서는 OpenStack 인스턴스 상태, SSH 접속, Ansible ping, Playbook 실행, Docker 컨테이너 상태, Proxy 경유 HTTP 접속, DB 연결을 확인했습니다.
~~~

---

## 14. Slide 11: Health Check / Backup / Restore

## 제목

~~~text
상태 점검, 백업, 복구 절차 검증
~~~

## 포함 내용

| 항목 | 내용 |
|---|---|
| Health Check | Proxy / Web / DB 상태 확인 |
| DB Backup | mysqldump 기반 MariaDB dump 생성 |
| Files Backup | WordPress files archive 생성 |
| Restore | restore.md 기반 복구 절차 검증 |
| Evidence | 실행 결과 캡처 및 문서화 |

## 발표 멘트

~~~text
서비스 실행 이후에는 health_check.sh로 Proxy, Web, DB 상태를 점검하고, backup.sh를 통해 mysqldump 기반 MariaDB dump와 WordPress files archive를 생성했습니다. 복구는 restore.md 기준으로 절차를 검증했습니다.
~~~

---

## 15. Slide 12: 장애 대응 및 트러블슈팅

## 제목

~~~text
운영 중 장애 대응 절차
~~~

## 포함 내용

| 장애 유형 | 확인 방향 |
|---|---|
| SSH 접속 실패 | Key, Security Group, IP, Port Forwarding |
| Ansible 실패 | inventory, remote_user, key path, syntax |
| HAProxy 장애 | haproxy.cfg, backend IP, container logs |
| WordPress 장애 | container logs, DB host, HTTP port |
| DB 연결 실패 | 3306, security group, env, MariaDB logs |
| Backup 실패 | disk, permission, DB connection, backup path |
| Resource 부족 | free, df, docker stats, image cleanup |

## 발표 멘트

~~~text
장애 대응은 OpenStack, SSH, Ansible, Docker, Proxy, Web, DB, Backup 순서로 원인을 좁히는 방식으로 정리했습니다. 최소 1개 이상의 장애 상황과 복구 절차를 산출물에 포함합니다.
~~~

---

## 16. Slide 13: Phase 2 운영 확장

## 제목

~~~text
Phase 2 운영 확장 및 검증 고도화
~~~

## 포함 내용

| 확장 항목 | 목적 |
|---|---|
| HTTPS self-signed | HTTPS 접속 검증 |
| HTTP to HTTPS Redirect | 접속 보안 흐름 개선 |
| Cinder Backup Volume | 백업 저장소 분리 |
| node_exporter / cAdvisor | OS / Container Metrics |
| Prometheus | Metrics 수집 |
| Grafana | Dashboard 시각화 |
| backup / restore playbook화 | 운영 절차 자동화 |
| Ansible roles 구조 | 자동화 구조 개선 |

## 발표 멘트

~~~text
Phase 2는 Phase 1이 안정적으로 완료된 이후 진행하는 운영 확장 단계입니다. HTTPS, Cinder Backup Volume, Prometheus/Grafana, Ansible 구조 개선 등을 통해 운영성을 강화합니다.
~~~

---

## 17. Slide 14: Phase 3 도전 확장

## 제목

~~~text
Web Node 2대와 HAProxy Load Balancing
~~~

## 포함 내용

~~~text
Client
→ Proxy Node / HAProxy Load Balancer
→ Web Node 1 / WordPress
→ Web Node 2 / WordPress
→ DB Node / MariaDB
~~~

| 검증 항목 | 기준 |
|---|---|
| Web Node 2 | WordPress 컨테이너 running |
| HAProxy LB | web1 / web2 backend 등록 |
| Round Robin | Web-1 / Web-2 응답 분산 |
| Common DB | 두 Web Node가 동일 DB Node 연결 |
| 장애 테스트 | Web-1 중지 시 Web-2 응답 |

## 발표 멘트

~~~text
Phase 3는 도전 확장으로 Web Node를 2대로 늘리고 HAProxy roundrobin 방식으로 분산을 검증하는 단계입니다. 단, WordPress files 자동 동기화는 범위에서 제외하고 LB 동작과 공통 DB 연결 검증에 집중합니다.
~~~

---

## 18. Slide 15: Out of Scope 및 한계

## 제목

~~~text
범위 통제를 통한 구현 안정성 확보
~~~

## 포함 내용

| 제외 항목 | 제외 이유 |
|---|---|
| Kubernetes | 프로젝트 범위 초과 |
| Docker Swarm | Docker Compose 중심 범위와 불일치 |
| OpenStack LBaaS / Octavia | OpenStack 서비스 의존성 및 난이도 증가 |
| DB Replication / Clustering | 데이터 정합성 검증 범위 확대 |
| Auto Scaling | 모니터링, 이미지, 배포 자동화까지 범위 확대 |
| WordPress files 자동 동기화 | 공유 스토리지 및 파일 충돌 문제 |
| Production-level HTTPS | 공인 도메인 및 인증서 자동 갱신 필요 |

## 발표 멘트

~~~text
이번 프로젝트에서는 구현 안정성과 제출 완성도를 위해 과도한 기능 확장을 제외했습니다. 핵심은 운영 수준의 모든 기능을 구현하는 것이 아니라, 기본 클라우드 운영 자동화 흐름을 끝까지 검증하는 것입니다.
~~~

---

## 19. Slide 16: 최종 결과 및 기대 효과

## 제목

~~~text
클라우드 인프라 운영 자동화 흐름 완성
~~~

## 포함 내용

| 결과 | 설명 |
|---|---|
| 인프라 | OpenStack 기반 노드 구성 |
| 자동화 | Ansible 기반 서버 설정 및 서비스 배포 |
| 서비스 | HAProxy / WordPress / MariaDB 구성 |
| 검증 | Proxy 접속, DB 연결, Health Check |
| 백업 | mysqldump 기반 MariaDB dump, WordPress files archive |
| 복구 | restore.md 기반 절차 검증 |
| 운영 | 장애 대응 및 트러블슈팅 문서화 |
| 관리 | GitHub 및 Google Drive 산출물 관리 |

## 발표 멘트

~~~text
최종적으로 OpenStack 인프라 구성부터 Ansible 자동화, 서비스 배포, Proxy 경유 접속, DB 연결, 상태 점검, 백업, 복구 절차 검증까지 하나의 운영 자동화 흐름으로 정리했습니다.
~~~

---

## 20. 시연 순서

최종 시연은 다음 순서로 진행한다.

~~~text
1. OpenStack 인스턴스 목록 확인
2. Control / Proxy / Web / DB / Backup Node 설명
3. ansible all -m ping 실행
4. ansible-playbook site.yml 실행 결과 확인
5. DB Node MariaDB 서비스 확인
6. Web Node WordPress 컨테이너 확인
7. Proxy Node HAProxy 컨테이너 확인
8. Proxy Node 경유 WordPress HTTP 접속 확인
9. Web Node → DB Node 3306 연결 확인
10. health_check.sh 실행
11. backup.sh 실행
12. restore.md 복구 절차 설명
13. 장애 상황 1개와 복구 과정 설명
14. Phase 2 또는 Phase 3 결과가 있으면 추가 설명
~~~

---

## 21. 발표 시 주의할 표현

## 사용해야 할 표현

~~~text
Phase 1 필수 구성 및 기본 검증
Phase 2 운영 확장 및 검증 고도화
Phase 3 도전 확장
Control / Proxy / Web / DB / Backup Node 분리
HAProxy HTTP Reverse Proxy
Custom WordPress
MariaDB
Backup / Restore 검증
Out of Scope
~~~

## 사용하지 않을 표현

~~~text
A급
B급
B+
C급
Nginx
web-test
단순 웹서버 배포
OpenStack LBaaS 필수 구현
운영 수준 고가용성 완성
~~~

---

## 22. 최종 발표 마무리 멘트

~~~text
저희 프로젝트는 기능을 무리하게 확장하기보다,
OpenStack 인프라 위에서 Ansible을 통해 반복 가능한 운영 자동화 흐름을 구현하는 데 집중했습니다.

Proxy, Web, DB, Backup 계층을 분리하고,
서비스 배포 이후 상태 점검, 백업, 복구 절차까지 검증함으로써
기본 클라우드 인프라 운영 자동화의 전체 흐름을 완성했습니다.
~~~

