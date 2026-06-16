<!-- STATUS: COMPLETE -->

# Implementation Roadmap

## 1. 목적

본 문서는 Team Dandelion 프로젝트의 구현 단계를 A급 필수 구현, B급 선택 확장, B+ Stretch Goal로 구분하여 정리한다.

프로젝트의 핵심 방향은 기능을 무리하게 확장하는 것이 아니라, A급 필수 흐름을 안정적으로 완성한 뒤 운영 안정성, 관측 가능성, 확장성을 단계적으로 추가하는 것이다.

~~~text
A급: 단일 서비스 운영 자동화 완성
B급: 운영 안정성 및 관측 가능성 확장
B+: 분산 구조 및 확장 아키텍처 검증
~~~

---

## 2. 전체 구현 방향

본 프로젝트는 OpenStack 기반 Ubuntu 인스턴스 위에서 Ansible을 활용하여 서버 설정, Docker 설치, Docker Compose 기반 WordPress/MariaDB 서비스 배포, 상태 점검, 백업 및 복구 검증을 수행한다.

이후 선택 확장으로 HAProxy Reverse Proxy, HTTPS, Cinder 기반 Backup Storage, Prometheus/Grafana 모니터링을 추가한다.

A급과 B급이 안정화된 경우 B+ Stretch Goal로 Web Node 2대, DB Node 분리, HAProxy Load Balancing 구조를 검토한다.

~~~text
A급
OpenStack Ubuntu 인스턴스
→ Ansible
→ Docker Compose
→ WordPress + MariaDB
→ Health Check
→ Backup / Restore

B급
A급 구조 유지
→ HAProxy Reverse Proxy
→ HTTPS
→ Cinder Backup Volume
→ Prometheus / Grafana Monitoring

B+
A급/B급 구조 확장
→ Web Node 2대
→ DB Node 분리
→ HAProxy Load Balancing
→ 공통 DB 연결 검증
~~~

---

## 3. A급 필수 구현

## 3.1 A급 목표

A급의 목표는 OpenStack 위에 Ubuntu 기반 인스턴스를 생성하고, Ansible을 통해 Docker 환경을 구성한 뒤, WordPress/MariaDB 서비스를 배포하고, 상태 점검과 백업/복구 검증까지 완료하는 것이다.

A급은 최종 발표와 제출을 위한 최소 성공 기준이다.

---

## 3.2 A급 노드 구조

~~~text
Control Node
→ Ansible 실행
→ ansible.cfg / inventory.ini / site.yml 관리

Web Node
→ Docker 설치
→ Custom WordPress Image Build
→ WordPress Container
→ MariaDB Container
→ Docker Compose 실행

Backup / Validation Node
→ health_check.sh
→ backup.sh
→ restore.md
→ 백업 파일 보관 및 복구 검증
~~~

---

## 3.3 A급 구현 순서

| 순서 | 구현 항목 | 담당 영역 | 성공 기준 |
|---:|---|---|---|
| 1 | OpenStack Ubuntu 인스턴스 생성 | Cloud Infrastructure | 인스턴스 ACTIVE 상태 |
| 2 | 네트워크 / 보안그룹 / 포트포워딩 정리 | Cloud Infrastructure | SSH / HTTP 접속 경로 확보 |
| 3 | SSH 접속 확인 | Cloud Infrastructure | Control Node에서 대상 노드 접속 성공 |
| 4 | Ansible inventory 구성 | Ansible Automation | inventory.ini 작성 완료 |
| 5 | Ansible ping 테스트 | Ansible Automation | ansible all -m ping 성공 |
| 6 | Docker 설치 자동화 | Ansible Automation / Server | Docker 설치 및 서비스 실행 |
| 7 | Custom WordPress Image Build | Server / Virtualization | Dockerfile 기반 이미지 빌드 성공 |
| 8 | WordPress/MariaDB Docker Compose 배포 | Server / Ansible | 컨테이너 running 상태 |
| 9 | WordPress HTTP 접속 확인 | Validation | HTTP 200 또는 302 응답 |
| 10 | health_check.sh 실행 | Monitoring / Validation | 상태 점검 결과 확보 |
| 11 | backup.sh 실행 | Backup / Validation | DB dump 및 WordPress files backup 생성 |
| 12 | restore.md 기반 복구 절차 검증 | Backup / Validation | 복구 절차 문서화 및 검증 |
| 13 | 필수 캡처 확보 | 전체 | 담당자별 캡처 정리 |
| 14 | 문서 및 제출자료 정리 | PM / 전체 | GitHub 및 Google Drive 산출물 정리 |

---

## 3.4 A급 성공 기준

| 구분 | 성공 기준 |
|---|---|
| 인프라 | OpenStack 기반 Ubuntu 인스턴스 생성 |
| 접속 | SSH 접속 성공 |
| Ansible | ansible all -m ping 성공 |
| 자동화 | ansible-playbook 실행 성공 |
| Docker | Docker 설치 및 Docker Compose 실행 가능 |
| 서비스 | WordPress / MariaDB 컨테이너 running 상태 |
| 접속 검증 | WordPress HTTP 응답 확인 |
| 상태 점검 | health_check.sh 실행 결과 확보 |
| 백업 | MariaDB dump 및 WordPress files archive 생성 |
| 복구 | restore.md 기반 복구 절차 검증 |
| 산출물 | 문서, 캡처, 회의록, 작업일지 정리 |

---

## 4. B급 선택 확장

B급은 A급 필수 구현과 캡처가 완료된 이후 가능한 범위에서 진행한다.

B급의 목적은 A급 구조를 변경하거나 흔드는 것이 아니라, A급 구조 위에 운영 안정성, 보안성, 관측 가능성을 추가하는 것이다.

---

## 4.1 B급 전체 순서

| 우선순위 | 확장 항목 | 목적 | 실패 시 처리 |
|---:|---|---|---|
| 1 | HAProxy Reverse Proxy | 외부 접속 경로 분리 | A급 HTTP 직접 접속 기준 발표 |
| 2 | HTTPS self-signed | HTTPS 접속 검증 | HTTP 기반 A급 결과 발표 |
| 3 | Cinder Backup Volume | 백업 저장소 분리 | 로컬 백업 기준 발표 |
| 4 | node_exporter / cAdvisor | OS / Container 메트릭 수집 | health_check.sh 기준 발표 |
| 5 | Prometheus | 메트릭 수집 서버 구성 | exporter 결과만 발표 |
| 6 | Grafana | 대시보드 시각화 | Prometheus target 결과만 발표 |
| 7 | backup / restore playbook화 | 운영 절차 자동화 개선 | shell script 기준 발표 |
| 8 | Ansible roles 구조 분리 | playbook 구조 개선 | 단일 site.yml 기준 발표 |

---

## 4.2 B급 1단계: HAProxy Reverse Proxy

### 구조

~~~text
Client
→ HAProxy / Proxy Node
→ Web Node
   ├── WordPress
   └── MariaDB
~~~

### 목적

Web Node 직접 접속 구조에서 Proxy Node 경유 구조로 확장한다.

### 성공 기준

| 항목 | 기준 |
|---|---|
| HAProxy 실행 | dandelion-haproxy 컨테이너 running |
| Backend 연결 | Web Node 80번 포트 연결 |
| 접속 검증 | Proxy Node 접속 시 WordPress 응답 |
| 로그 확인 | HAProxy access log 확인 |

### 검증 명령어

~~~bash
curl -I http://PROXY_NODE_IP
curl -I http://WEB_NODE_IP
docker logs dandelion-haproxy --tail 50
~~~

---

## 4.3 B급 2단계: HTTPS self-signed

### 구조

~~~text
Client
→ HTTPS 443
→ HAProxy
→ HTTP 80
→ Web Node WordPress
~~~

### 목적

서비스 외부 접속 경로에 HTTPS 계층을 추가한다.

### 성공 기준

| 항목 | 기준 |
|---|---|
| 인증서 | self-signed 인증서 생성 |
| HTTPS | HAProxy 443 bind 성공 |
| 접속 | curl -k 기반 HTTPS 응답 |
| Redirect | HTTP 80 → HTTPS 443 Redirect |

### 검증 명령어

~~~bash
curl -k -I https://PROXY_NODE_IP
curl -I http://PROXY_NODE_IP
~~~

---

## 4.4 B급 3단계: Cinder Backup Volume

### 구조

~~~text
Backup / Validation Node
→ Cinder Volume attach
→ /backup mount
→ DB dump 저장
→ WordPress files backup 저장
~~~

### 목적

운영 데이터와 백업 데이터를 분리한다.

Cinder Volume은 MariaDB 원본 데이터 저장소가 아니라, Backup / Validation Node의 백업 저장소로 사용한다.

### 성공 기준

| 항목 | 기준 |
|---|---|
| Volume 생성 | Cinder Volume 생성 완료 |
| Attach | Backup Node에 Volume attach |
| Mount | /backup 경로에 mount |
| Backup | backup.sh 결과물이 /backup에 저장 |
| 검증 | df -h 및 백업 파일 캡처 확보 |

### 검증 명령어

~~~bash
openstack volume list
lsblk
df -h
ls -lh /backup
~~~

---

## 4.5 B급 4단계: node_exporter + cAdvisor

### 구조

~~~text
Web Node
→ node_exporter: OS metrics
→ cAdvisor: container metrics
~~~

### 목적

서버와 컨테이너 상태를 수집 가능한 형태로 만든다.

### 성공 기준

| 항목 | 기준 |
|---|---|
| node_exporter | 9100/metrics 응답 |
| cAdvisor | 8080/metrics 응답 |
| OS Metrics | CPU / Memory / Disk 수집 가능 |
| Container Metrics | Container CPU / Memory / I/O 수집 가능 |

### 검증 명령어

~~~bash
curl http://WEB_NODE_IP:9100/metrics
curl http://WEB_NODE_IP:8080/metrics
~~~

---

## 4.6 B급 5단계: Prometheus

### 구조

~~~text
Prometheus
→ Web Node node_exporter:9100
→ Web Node cAdvisor:8080
~~~

### 목적

Web Node와 컨테이너 메트릭을 수집한다.

### 성공 기준

| 항목 | 기준 |
|---|---|
| Prometheus 실행 | dandelion-prometheus 컨테이너 running |
| Target 등록 | prometheus.yml에 Web Node target 등록 |
| Target 상태 | Prometheus Targets 화면에서 UP |
| Query | 기본 메트릭 조회 가능 |

### 검증 명령어

~~~bash
curl http://MONITORING_NODE_IP:9090
~~~

---

## 4.7 B급 6단계: Grafana

### 구조

~~~text
Grafana
→ Prometheus Data Source
→ Dashboard
~~~

### 목적

수집된 메트릭을 시각화한다.

### 성공 기준

| 항목 | 기준 |
|---|---|
| Grafana 실행 | dandelion-grafana 컨테이너 running |
| 접속 | 3000 포트 접속 가능 |
| Data Source | Prometheus 연결 성공 |
| Dashboard | CPU / Memory / Disk / Container 상태 시각화 |

---

## 4.8 B급 7단계: backup / restore playbook화

### 목적

수동 스크립트 기반 backup / restore 검증 절차를 Ansible playbook으로 실행할 수 있도록 개선한다.

### 진행 기준

| 항목 | 기준 |
|---|---|
| backup.yml | backup.sh 실행 자동화 |
| validate.yml | health check 및 backup file 확인 자동화 |
| restore | restore는 위험도가 있으므로 문서 기반 검증 유지 가능 |

### 검증 명령어

~~~bash
ansible-playbook ansible/playbooks/backup.yml
ansible-playbook ansible/playbooks/validate.yml
~~~

---

## 4.9 B급 8단계: Ansible roles 구조 분리

### 목적

단일 site.yml로 완성한 자동화 구조를 roles 기반으로 정리한다.

### 권장 구조

~~~text
ansible/
├── site.yml
├── roles/
│   ├── docker/
│   ├── wordpress/
│   ├── backup/
│   ├── proxy/
│   └── monitoring/
~~~

### 기준

처음부터 roles 구조로 시작하지 않고, 단일 site.yml이 성공한 뒤 리팩터링한다.

---

## 5. B+ Stretch Goal

B+는 A급과 B급이 안정화된 뒤에만 시도한다.

B+의 목적은 단일 Web Node 기반 구조를 분산 구조로 확장하고, HAProxy를 통해 Load Balancing 동작을 검증하는 것이다.

---

## 5.1 B+ 목표 구조

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
→ restore 검증
~~~

---

## 5.2 B+ 구현 순서

| 순서 | 구현 항목 | 성공 기준 |
|---:|---|---|
| 1 | DB Node 분리 | MariaDB 단독 실행 |
| 2 | Web Node 1 구성 | WordPress가 DB Node 연결 |
| 3 | Web Node 2 구성 | WordPress가 DB Node 연결 |
| 4 | HAProxy backend 2개 등록 | Web-1 / Web-2 backend 등록 |
| 5 | Round Robin 검증 | 요청이 Web-1 / Web-2로 분산 |
| 6 | 공통 DB 연결 확인 | 두 Web Node가 같은 DB 사용 |
| 7 | 장애 테스트 | Web-1 중지 시 Web-2 응답 확인 |

---

## 5.3 B+ 제한 사항

WordPress는 DB뿐만 아니라 `wp-content/uploads`, plugins, themes 같은 파일도 로컬에 저장한다.

따라서 Web Node 2대 구성 시 WordPress 파일 동기화 문제가 발생할 수 있다.

이번 프로젝트에서는 아래 항목을 구현 범위에서 제외한다.

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

## 5.4 B+ 검증 방법

Web-1과 Web-2를 구분하기 위해 WordPress 자체를 수정하지 않고 간단한 health endpoint 또는 정적 식별 파일을 사용한다.

~~~text
Web-1: /health.html → web1
Web-2: /health.html → web2
~~~

검증 명령어:

~~~bash
curl http://LB_IP/health.html
curl http://LB_IP/health.html
curl http://LB_IP/health.html
~~~

예상 결과:

~~~text
web1
web2
web1
~~~

---

## 6. 제외 범위

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

---

## 7. 최종 권장 진행 순서

~~~text
Phase 1. A급 완성
1. OpenStack Ubuntu 인스턴스 생성
2. 네트워크 / 보안그룹 / 포트포워딩 정리
3. SSH 접속 확인
4. Ansible inventory 구성
5. ansible ping 성공
6. Docker 설치 playbook 실행
7. WordPress/MariaDB Docker Compose 배포
8. WordPress HTTP 접속 확인
9. health_check.sh 실행
10. backup.sh 실행
11. restore.md 정리 및 복구 검증
12. 필수 캡처 확보

Phase 2. B급 안정 확장
1. HAProxy Reverse Proxy
2. HTTPS self-signed
3. Cinder Volume Backup Storage
4. node_exporter / cAdvisor
5. Prometheus
6. Grafana
7. backup / restore playbook화
8. Ansible roles 구조 분리

Phase 3. B+ 도전
1. DB Node 분리
2. Web Node 2대 구성
3. HAProxy roundrobin LB
4. Web-1/Web-2 health 응답 분산 확인
5. 공통 DB 연결 확인
6. OpenStack CLI + Ansible End-to-End 자동화 검토
~~~

---

## 8. 발표용 설명 문장

본 프로젝트는 A급 필수 구현에서 단일 Web Node 기반 WordPress/MariaDB 서비스 배포와 백업/복구 검증을 먼저 완성한다.

이후 B급 선택 확장에서는 HAProxy Reverse Proxy, HTTPS, Cinder 기반 백업 저장소, Prometheus/Grafana 모니터링을 추가하여 운영 안정성과 관측 가능성을 확장한다.

A급과 B급이 안정화된 경우 B+ Stretch Goal로 Web Node 2대, DB Node 분리, HAProxy Load Balancing 구조를 검토한다.

단, WordPress 파일 자동 동기화와 공유 스토리지 구성은 프로젝트 범위를 과도하게 확장할 수 있으므로 이번 구현 범위에서는 제외하고 향후 확장 과제로 분리한다.
