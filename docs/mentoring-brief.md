<!-- STATUS: COMPLETE -->

# Mentoring Brief

## 1. 프로젝트 개요

| 구분 | 내용 |
|---|---|
| 팀명 | Dandelion |
| 프로젝트명 | Ansible 기반 클라우드 인프라 자동화 및 운영 최적화 시스템 구축 |
| 프로젝트 기간 | 2026.06.11 ~ 2026.07.14 |
| 핵심 목표 | OpenStack 기반 클라우드 인프라 구성 이후 Ansible을 활용하여 서버 설정, Docker Compose 기반 WordPress/MariaDB 서비스 배포, 상태 점검, 백업 및 복구 검증을 자동화 |

---

## 2. 프로젝트 방향

본 프로젝트는 단순한 서버 생성이나 애플리케이션 배포가 아니라, 클라우드 인프라 운영 과정에서 반복적으로 발생하는 설정, 배포, 점검, 백업, 복구 절차를 자동화하고 문서화하는 것을 목표로 한다.

서비스 계층은 Docker Compose 기반으로 구성하며, Docker Hub 공식 WordPress 이미지를 기반으로 Custom WordPress Image를 만들고 MariaDB 컨테이너와 연동한다.

WordPress는 웹 개발 대상이 아니라, Ansible 자동화, Docker Compose 배포, HTTP 상태 점검, DB dump, 파일 백업, 복구 검증을 위한 운영 서비스 대상이다.

핵심 구현 흐름은 다음과 같다.

~~~text
OpenStack 인프라 구성
→ Ubuntu 인스턴스 생성
→ SSH 접속 환경 구성
→ Ansible Inventory 작성
→ Ansible Playbook 실행
→ Docker 설치
→ Docker Compose 기반 WordPress/MariaDB 배포
→ WordPress HTTP 접속 확인
→ Health Check
→ MariaDB dump 및 WordPress files 백업
→ Restore 절차 검증
→ GitHub 및 Google Drive 산출물 관리
~~~

---

## 3. 현재 진행 현황

| 구분 | 진행 상태 |
|---|---|
| 팀명 및 주제 선정 | 완료 |
| 팀원 역할 분담 | 완료 |
| GitHub Repository 구조 생성 | 완료 |
| README 및 기본 문서 구조 작성 | 진행 중 |
| 평가 기준 분석 | 완료 |
| 구현 범위 통제 기준 작성 | 완료 |
| A급 / B급 / B+ 구현 로드맵 작성 | 완료 |
| 운영 중 장애 시나리오 및 트러블슈팅 정리 | 진행 중 |
| OpenStack 인프라 구성 | 진행 예정 |
| Ubuntu 인스턴스 생성 | 진행 예정 |
| Ansible 실행 검증 | 진행 예정 |
| Docker Compose 기반 WordPress/MariaDB 배포 | 진행 예정 |
| Health Check / Backup / Restore 검증 | 진행 예정 |
| Google Drive 산출물 관리 | 진행 중 |

---

## 4. 팀원 역할

| 이름 | 역할 | 담당 업무 |
|---|---|---|
| 정주헌 | PM / 아키텍처 | 전체 구조 설계, GitHub 관리, README 및 발표자료 통합, 제출 패키지 관리 |
| 백서빈 | 클라우드 인프라 | OpenStack 인스턴스, Ubuntu 이미지, 네트워크, 보안그룹, Floating IP 또는 포트포워딩 접속 구성 |
| 이진욱 | 서버 / 가상화 | Linux 서버 환경 구성, Docker 설치, Custom WordPress 및 MariaDB 컨테이너 실행 |
| 조민석 | Ansible 자동화 | ansible.cfg, inventory.ini, site.yml 작성 및 실행 |
| 박재우 | 모니터링 / 백업 / 검증 | health_check, backup, restore 검증 및 결과 정리 |

---

## 5. 구현 범위 기준

| 등급 | 기준 |
|---|---|
| A급 | 필수 구현 범위. OpenStack, Ubuntu Instance, SSH, Ansible, Docker Compose, WordPress/MariaDB, Health Check, Backup/Restore, 산출물 정리 |
| B급 | 선택 확장 범위. HAProxy Reverse Proxy, HTTPS, Cinder Backup Volume, node_exporter, cAdvisor, Prometheus, Grafana, Playbook 역할 분리 |
| B+ | 추가 도전 범위. Web Node 2대, DB Node 분리, HAProxy Load Balancing, 공통 DB 연결 검증 |
| C급 | 제외 범위. OpenStack LBaaS/Octavia, Docker Swarm, Kubernetes, DB Clustering, Auto Scaling, WordPress files 자동 동기화 |

A급 필수 구현을 먼저 완료하고, 이후 시간이 남을 경우 B급 선택 확장 범위를 시도한다.

B+ Stretch Goal은 필수 제출 범위가 아니며, A급과 B급이 조기에 안정화되었을 때만 시도한다.

---

## 6. A급 필수 구현 기준

A급은 최종 발표와 시연을 위해 반드시 완료해야 하는 핵심 범위이다.

| 구분 | 필수 구현 내용 |
|---|---|
| 인프라 | OpenStack 기반 Ubuntu 인스턴스 생성 |
| 노드 구성 | Control Node, Web Node, Backup / Validation Node 구분 |
| 접속 | SSH 접속 및 포트포워딩 또는 Floating IP 접속 검증 |
| Ansible | ansible.cfg, inventory.ini, site.yml 작성 |
| Ansible 검증 | ansible all -m ping 성공 |
| 서비스 | Docker 설치 및 Docker Compose 실행 |
| 서비스 배포 | Custom WordPress + MariaDB 배포 |
| 접속 검증 | WordPress HTTP 응답 확인 |
| 상태 점검 | health_check.sh 실행 |
| 백업 | MariaDB dump 및 WordPress files archive 생성 |
| 복구 | restore.md 기반 복구 절차 검증 |
| 문서 | 작업 내역, 트러블슈팅, 캡처, 제출자료 정리 |

---

## 7. B급 선택 확장 기준

B급은 A급 구현과 캡처가 완료된 이후 가능한 범위에서 진행한다.

B급은 A급 구조를 변경하는 것이 아니라, A급 구조 위에 운영 안정성, 보안성, 관측 가능성을 추가하는 방향으로 진행한다.

| 우선순위 | 선택 확장 내용 | 목적 |
|---:|---|---|
| 1 | HAProxy Reverse Proxy | 외부 접속 경로 분리 |
| 2 | self-signed HTTPS | HTTPS 접속 검증 |
| 3 | Cinder Backup Volume | 백업 저장소 분리 |
| 4 | node_exporter / cAdvisor | OS / Container 메트릭 수집 |
| 5 | Prometheus | 메트릭 수집 서버 구성 |
| 6 | Grafana | 대시보드 시각화 |
| 7 | backup / restore 절차 playbook화 | 운영 절차 자동화 개선 |
| 8 | Ansible roles 구조 분리 | playbook 구조 개선 |

B급이 실패하더라도 A급 결과를 기준으로 발표할 수 있도록 범위를 분리한다.

---

## 8. B+ Stretch Goal

A급과 B급이 조기에 완료될 경우, Web Node 2대, DB Node 분리, HAProxy Load Balancing 구조를 추가 도전 범위로 검토한다.

~~~text
Client
→ HAProxy LB Node
→ Web Node 1
   └── WordPress

→ Web Node 2
   └── WordPress

DB Node
→ MariaDB

Backup / Validation Node
→ DB dump
→ WordPress files backup
→ Restore 검증
~~~

B+ 목표는 운영 수준의 완전한 고가용성 구현이 아니라, 다음 항목을 검증하는 것이다.

| 항목 | 검증 기준 |
|---|---|
| Web Node 2대 구성 | Web-1 / Web-2 모두 WordPress 응답 |
| DB Node 분리 | 두 Web Node가 동일 DB Node에 연결 |
| HAProxy LB | roundrobin 기반 Web-1 / Web-2 분산 |
| 장애 확인 | Web-1 중지 시 Web-2 응답 가능 여부 확인 |
| 공통 DB 연결 | 두 Web Node가 동일 DB를 바라보는 구조 확인 |

단, WordPress는 DB뿐만 아니라 `wp-content/uploads`, plugins, themes 같은 파일도 로컬에 저장하므로 Web Node 2대 구성 시 파일 동기화 문제가 발생할 수 있다.

따라서 이번 프로젝트에서는 아래 항목을 제외한다.

~~~text
WordPress files 자동 동기화
wp-content/uploads 공유
plugin/theme 동기화
NFS 기반 WordPress shared storage
Object Storage 연동
DB Replication
Auto Scaling
OpenStack LBaaS / Octavia
~~~

B+ 시연은 HAProxy roundrobin, Web-1/Web-2 응답 분산, 공통 DB 연결 확인 수준으로 제한한다.

---

## 9. 멘토링에서 확인받고 싶은 부분

이번 멘토링에서 확인받고 싶은 핵심은 다음과 같다.

| 구분 | 확인 요청 |
|---|---|
| 범위 | A급 / B급 / B+ / C급 구분이 적절한지 |
| 인프라 | Control / Web / Backup-Validation Node 구성이 적절한지 |
| 접속 | 포트포워딩 및 터널링 기반 접속 설명이 적절한지 |
| 자동화 | Ansible playbook 범위가 적절한지 |
| 서비스 | WordPress/MariaDB 기반 서비스 대상 선정이 적절한지 |
| 운영 | 리소스 부족 및 운영 중 장애 시나리오 정리가 충분한지 |
| 확장 | HAProxy, Cinder Backup Volume, Prometheus/Grafana 중 우선순위가 무엇인지 |
| B+ | Web Node 2대 + DB Node 분리 + HAProxy LB를 추가 도전 범위로 두는 것이 적절한지 |
| 제외 | OpenStack LBaaS/Octavia와 WordPress files 자동 동기화를 제외하는 것이 적절한지 |
| 산출물 | GitHub Actions 기반 상태 자동 갱신을 차별성으로 설명해도 되는지 |

---

## 10. 현재 고민

현재 가장 큰 고민은 구현 범위를 넓히는 것보다, 필수 흐름을 안정적으로 완성하는 것이다.

Prometheus/Grafana, HAProxy HTTPS, Cinder Backup Volume 같은 확장 기능을 추가하면 전문성은 높아질 수 있다. 그러나 OpenStack 인프라 구성, Ansible 실행, Docker Compose 기반 WordPress/MariaDB 배포, 백업/복구 검증이 안정적으로 완료되지 않은 상태에서 범위를 확장하면 프로젝트 완성도가 떨어질 수 있다.

따라서 현재는 A급 필수 구현을 먼저 완료하고, 이후 시간이 남을 경우 B급 선택 확장을 진행하는 방향으로 범위를 통제하고 있다.

B+로 Web Node 2대와 DB Node 분리, HAProxy Load Balancing을 검토하고 있으나, WordPress files 자동 동기화까지 포함하면 범위가 과도하게 커질 수 있으므로 해당 항목은 제외하고 공통 DB 연결과 LB 동작 검증 수준으로 제한하려고 한다.

---

## 11. 운영 중 장애 시나리오 정리 방향

구현 후 운영 중 발생 가능한 장애 시나리오는 다음 기준으로 정리하고 있다.

| 시나리오 | 확인 방향 |
|---|---|
| SSH 접속 실패 | SSH Key, 보안그룹, 포트포워딩 확인 |
| 포트포워딩 장애 | 공유기 포트포워딩, 내부 IP, 보안그룹 확인 |
| WordPress 접속 실패 | docker ps, curl, WordPress logs 확인 |
| MariaDB 연결 실패 | DB logs, 환경변수, Docker network 확인 |
| Docker Compose 실패 | docker compose config, docker compose logs 확인 |
| Backup 실패 | backup.sh, df -h, DB logs 확인 |
| Restore 실패 | 백업 파일, volume, 복구 순서 확인 |
| 리소스 부족 | CPU, Memory, Disk, Docker stats 확인 |
| HAProxy 장애 | haproxy.cfg, backend IP, 인증서 확인 |
| Prometheus/Grafana 장애 | exporter, target, dashboard 접속 확인 |
| OpenStack 인스턴스 장애 | server list/show, console log 확인 |

멘토링에서는 위 시나리오 구성이 기본 프로젝트 수준에서 충분한지 확인받고자 한다.

---

## 12. 구현 일정 계획

| 구분 | 목표 완료일 | 내용 |
|---|---|---|
| A급 필수 구현 | 2026-06-26 | OpenStack, Ubuntu Instance, SSH, Ansible, Docker Compose, WordPress/MariaDB, Health Check, Backup/Restore, 필수 캡처 완료 |
| B급 선택 확장 | 2026-07-10 | HAProxy HTTPS, Cinder Backup Volume, node_exporter, cAdvisor, Prometheus/Grafana, Playbook 개선 중 가능한 항목 |
| B+ 추가 도전 | 2026-07-10 이전 여유 시 | Web Node 2대, DB Node 분리, HAProxy Load Balancing, 공통 DB 연결 검증 |
| 최종 발표 및 제출 | 2026-07-14 | 결과보고서, 시연 영상, 소스코드, 작업일지, 회의록, 제출자료 정리 |

멘토링에서는 위 일정 기준이 기본 프로젝트 범위와 평가 기준에 적절한지 확인받고자 한다.

---

## 13. 멘토링 질문 요약

| 번호 | 질문 |
|---|---|
| Q1 | A급 필수 구현 범위가 기본 프로젝트 평가 기준에 적절한가? |
| Q2 | Prometheus/Grafana는 필수인지, 선택 확장으로 두어도 되는가? |
| Q3 | HAProxy Reverse Proxy / HTTPS 구성을 B급으로 분리한 것이 적절한가? |
| Q4 | Control Node 1대 + Managed Node 2대 구성이 적절한가? |
| Q5 | OpenStack 네트워크 구성과 포트포워딩 구조를 어느 수준까지 보여줘야 하는가? |
| Q6 | 자원 부족 발생 시 어떤 조치 방향이 적절한가? |
| Q7 | Ansible Playbook 범위는 Docker Compose 기반 WordPress/MariaDB 배포까지가 적절한가? |
| Q8 | 단일 site.yml로 시작하고 이후 roles 구조로 개선하는 방향이 적절한가? |
| Q9 | Web Node 2대 + DB Node 분리 + HAProxy LB를 B+ Stretch Goal로 두어도 되는가? |
| Q10 | WordPress files 자동 동기화와 OpenStack LBaaS/Octavia를 제외하는 것이 적절한가? |
| Q11 | 운영 중 장애 시나리오와 트러블슈팅 항목이 충분한가? |
| Q12 | GitHub Actions 기반 산출물 상태 자동 갱신을 차별성으로 설명해도 되는가? |
