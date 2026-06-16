<!-- STATUS: COMPLETE -->

# Submission Package Guide

## 1. 문서 목적

본 문서는 Team Dandelion 프로젝트의 최종 제출 패키지 구성 기준을 정의한다.

본 프로젝트는 Phase 기반 구현 로드맵을 사용한다.

~~~text
Phase 1: 필수 구성 및 기본 검증 단계
Phase 2: 운영 확장 및 검증 고도화 단계
Phase 3: 도전 확장 단계
Out of Scope: 제외 범위
~~~

최종 제출 패키지는 Phase 1 필수 구성 및 기본 검증 결과를 중심으로 구성하며, Phase 2와 Phase 3 결과는 선택 확장 산출물로 포함한다.

---

## 2. 최종 제출 대상

최종 제출 대상은 다음과 같다.

| 구분 | 제출 자료 | 필수 여부 |
|---|---|---|
| 결과보고서 | PPT 및 PDF | 필수 |
| 시연 영상 | 구현 및 검증 시연 영상 | 필수 |
| 소스 코드 | GitHub Repository URL 또는 zip 파일 | 필수 |
| 작업 일지 | 팀원별 작업 내용 및 회의록 | 필수 |
| 캡처 자료 | 인프라, 자동화, 서비스, 검증 결과 캡처 | 필수 |
| 트러블슈팅 자료 | 장애 상황, 원인, 조치, 결과 | 필수 |
| 멘토링 자료 | 멘토링 질문 및 피드백 정리 | 선택 |
| Phase 2 자료 | HTTPS, Cinder, Monitoring 등 | 선택 |
| Phase 3 자료 | Web Node 2대, HAProxy LB 등 | 선택 |

---

## 3. Google Drive 권장 제출 구조

Google Drive 최종 제출 폴더는 다음 구조를 권장한다.

~~~text
02. [기본 프로젝트] 결과 산출물_260714/
├── 01. 결과보고서/
│   ├── Dandelion_결과보고서.pptx
│   └── Dandelion_결과보고서.pdf
├── 02. 시연영상/
│   └── Dandelion_시연영상.mp4
├── 03. 소스코드/
│   ├── GitHub_URL.txt
│   └── source-code.zip
├── 04. 작업일지_회의록/
│   ├── 회의록/
│   └── 작업일지/
├── 05. 캡처_검증자료/
│   ├── 01_OpenStack/
│   ├── 02_Ansible/
│   ├── 03_Docker/
│   ├── 04_Proxy_Web_DB/
│   ├── 05_Health_Check/
│   ├── 06_Backup_Restore/
│   ├── 07_Troubleshooting/
│   └── 08_Optional_Phase2_Phase3/
└── 06. 기타자료/
    ├── 멘토링_질문.md
    ├── 제출_체크리스트.md
    └── 참고자료.md
~~~

---

## 4. GitHub Repository 제출 기준

GitHub Repository는 코드와 문서를 함께 관리하는 공식 산출물 저장소이다.

| 체크 | 경로 | 포함 내용 |
|---|---|---|
| [ ] | README.md | 프로젝트 전체 개요 |
| [ ] | docs/ | 아키텍처, 네트워크, 서버, 자동화, 검증 문서 |
| [ ] | ansible/ | ansible.cfg, inventory.ini, site.yml |
| [ ] | docker/wordpress/ | Dockerfile, custom.ini, README |
| [ ] | docker/compose/ | Web / DB Docker Compose 파일 |
| [ ] | docker/proxy/ | HAProxy Docker Compose 및 haproxy.cfg |
| [ ] | docker/monitoring/ | Phase 2 monitoring compose 및 prometheus.yml |
| [ ] | scripts/ | health_check.sh, backup.sh |
| [ ] | screenshots/ | 검증 캡처 |
| [ ] | presentation/ | 발표 흐름 |
| [ ] | submission/ | 제출 패키지 정리 |
| [ ] | tools/ | 상태 생성 및 검증 스크립트 |
| [ ] | .github/workflows/ | GitHub Actions workflow |

---

## 5. Phase 1 필수 제출 자료

Phase 1은 최종 제출의 핵심 기준이다.

## 5.1 인프라 자료

| 체크 | 자료 | 기준 |
|---|---|---|
| [ ] | OpenStack 인스턴스 목록 | Control / Proxy / Web / DB / Backup Node 확인 |
| [ ] | Ubuntu 이미지 사용 근거 | 사용 이미지 확인 |
| [ ] | 네트워크 구성 | Network / Subnet / Router 확인 |
| [ ] | 보안그룹 정책 | SSH / HTTP / DB 포트 정책 확인 |
| [ ] | 외부 접속 경로 | Floating IP 또는 포트포워딩 구조 설명 |
| [ ] | IP 주소표 | 각 노드 Private IP 및 접속 경로 정리 |

---

## 5.2 Ansible 자료

| 체크 | 자료 | 기준 |
|---|---|---|
| [ ] | ansible.cfg | 설정 파일 포함 |
| [ ] | inventory.ini | proxy / web / db / backup 그룹 포함 |
| [ ] | site.yml | Docker 및 역할별 서비스 배포 포함 |
| [ ] | ansible --version 결과 | Ansible 설치 확인 |
| [ ] | ansible-inventory --list 결과 | Inventory 파싱 확인 |
| [ ] | ansible all -m ping 결과 | 모든 Managed Node SUCCESS |
| [ ] | syntax check 결과 | site.yml 문법 검증 |
| [ ] | playbook 실행 결과 | site.yml 실행 성공 |

---

## 5.3 서비스 자료

| 체크 | 자료 | 기준 |
|---|---|---|
| [ ] | Docker 설치 결과 | docker --version |
| [ ] | Docker Compose 결과 | docker compose version |
| [ ] | MariaDB 서비스 결과 | DB Node에서 mariadb service active |
| [ ] | WordPress 컨테이너 결과 | Web Node에서 dandelion-wordpress running |
| [ ] | HAProxy 컨테이너 결과 | Proxy Node에서 dandelion-haproxy running |
| [ ] | 포트 확인 결과 | ss -tulnp |
| [ ] | DB 연결 결과 | Web Node에서 DB Node 3306 연결 |
| [ ] | Proxy 접속 결과 | Proxy Node 경유 WordPress HTTP 접속 |

---

## 5.4 검증 자료

| 체크 | 자료 | 기준 |
|---|---|---|
| [ ] | health_check.sh 실행 결과 | Proxy / Web / DB 상태 확인 |
| [ ] | backup.sh 실행 결과 | DB dump 및 WordPress files archive 생성 |
| [ ] | MariaDB dump 파일 | wordpress_db.sql |
| [ ] | WordPress files archive | wordpress_files.tar.gz |
| [ ] | restore.md | DB / files 복구 절차 정리 |
| [ ] | Restore 검증 결과 | 절차 검증 또는 테스트 결과 |
| [ ] | 장애 대응 기록 | 장애 1개 이상, 원인 / 조치 / 결과 포함 |

---

## 6. Phase 2 선택 제출 자료

Phase 2는 Phase 1 완료 이후 추가 제출 가능한 운영 확장 자료이다.

| 체크 | 자료 | 기준 |
|---|---|---|
| [ ] | HTTPS 접속 결과 | curl -k 또는 브라우저 HTTPS |
| [ ] | HTTP to HTTPS Redirect 결과 | 301 또는 302 확인 |
| [ ] | self-signed 인증서 자료 | 인증서 적용 근거 |
| [ ] | Cinder Volume 생성 결과 | openstack volume list |
| [ ] | Cinder Volume attach 결과 | Backup Node attach 확인 |
| [ ] | /backup mount 결과 | df -h |
| [ ] | Cinder 백업 저장 결과 | /backup 경로 백업 파일 |
| [ ] | node_exporter 결과 | metrics 출력 |
| [ ] | cAdvisor 결과 | metrics 출력 |
| [ ] | Prometheus 결과 | Target UP |
| [ ] | Grafana 결과 | Dashboard 화면 |
| [ ] | backup playbook 결과 | ansible-playbook backup.yml |
| [ ] | validate playbook 결과 | ansible-playbook validate.yml |
| [ ] | roles 구조 | ansible/roles 디렉터리 |

---

## 7. Phase 3 도전 제출 자료

Phase 3은 도전 확장 자료이며 필수 제출 범위가 아니다.

| 체크 | 자료 | 기준 |
|---|---|---|
| [ ] | Web Node 2 인스턴스 | ACTIVE 상태 |
| [ ] | Web Node 2 Ansible ping | SUCCESS |
| [ ] | Web Node 2 WordPress | 컨테이너 running |
| [ ] | HAProxy backend 2개 | web1 / web2 등록 |
| [ ] | Round Robin 결과 | Web-1 / Web-2 응답 분산 |
| [ ] | 공통 DB 연결 결과 | 두 Web Node가 동일 DB Node 연결 |
| [ ] | Web Node 장애 테스트 | Web-1 중지 시 Web-2 응답 |

Phase 3 제출 자료에는 다음 항목을 포함하지 않는다.

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

---

## 8. 결과보고서 포함 기준

결과보고서에는 다음 내용을 포함한다.

| 순서 | 항목 | 내용 |
|---:|---|---|
| 1 | 프로젝트 개요 | 팀명, 주제, 기간, 목표 |
| 2 | 문제 정의 | 수동 운영, 설정 편차, 검증 누락 |
| 3 | Phase 전략 | Phase 1 / 2 / 3 / Out of Scope |
| 4 | 시스템 아키텍처 | Control / Proxy / Web / DB / Backup Node |
| 5 | OpenStack 구성 | 인스턴스, 네트워크, 보안그룹 |
| 6 | Ansible 자동화 | inventory, site.yml, 실행 결과 |
| 7 | 서비스 배포 | HAProxy, WordPress, MariaDB |
| 8 | 검증 결과 | SSH, Ansible, Docker, HTTP, DB |
| 9 | 백업/복구 | health_check, backup, restore |
| 10 | 장애 대응 | 장애 상황과 복구 절차 |
| 11 | 확장 결과 | Phase 2 또는 Phase 3 결과 |
| 12 | 한계 및 제외 범위 | Out of Scope |
| 13 | 결론 | 최종 성공 기준과 기대 효과 |

---

## 9. 시연 영상 포함 기준

시연 영상은 Phase 1 필수 흐름을 중심으로 구성한다.

| 순서 | 시연 내용 |
|---:|---|
| 1 | OpenStack 인스턴스 목록 확인 |
| 2 | Control / Proxy / Web / DB / Backup Node 설명 |
| 3 | SSH 또는 Ansible 접속 구조 설명 |
| 4 | ansible all -m ping |
| 5 | ansible-playbook site.yml 실행 결과 |
| 6 | DB Node MariaDB 서비스 확인 |
| 7 | Web Node WordPress 컨테이너 확인 |
| 8 | Proxy Node HAProxy 컨테이너 확인 |
| 9 | Proxy Node 경유 WordPress HTTP 접속 |
| 10 | Web Node → DB Node 3306 연결 확인 |
| 11 | health_check.sh 실행 |
| 12 | backup.sh 실행 |
| 13 | restore.md 복구 절차 설명 |
| 14 | 장애 상황 1개와 복구 절차 설명 |

선택 시연:

| Phase | 시연 항목 |
|---|---|
| Phase 2 | HTTPS, Cinder Backup Volume, Prometheus/Grafana |
| Phase 3 | Web Node 2대, HAProxy Load Balancing |

---

## 10. 작업일지 및 회의록 기준

작업일지와 회의록은 다음 기준으로 정리한다.

| 항목 | 기준 |
|---|---|
| 날짜 | 작업일 기준 |
| 참석자 | 팀원 이름 |
| 작업 내용 | 담당 영역별 진행 내용 |
| 결정 사항 | 범위, 구조, 기술 선택 |
| 이슈 | 발생 문제 |
| 조치 | 해결 방법 |
| 다음 작업 | 후속 작업 |
| 캡처 | 관련 증거 자료 |

---

## 11. 제출 전 확인 명령어

문서 내 오래된 표현 확인:

~~~powershell
Select-String -Path README.md, docs\*.md, presentation\*.md -Pattern "A급|B급|B\+|C급|Nginx|nginx|web-test|docker run"
~~~

프로젝트 상태 갱신:

~~~powershell
python tools\generate_project_status.py
python tools\validate_repository.py
~~~

Git 상태 확인:

~~~powershell
git status
~~~

---

## 12. 제출 가능 기준

다음 조건을 만족하면 제출 가능 상태로 판단한다.

| 체크 | 조건 |
|---|---|
| [ ] | Phase 1 필수 구성 완료 |
| [ ] | Phase 1 필수 검증 완료 |
| [ ] | 결과보고서 PPT / PDF 준비 |
| [ ] | 시연 영상 준비 |
| [ ] | GitHub Repository 최신 상태 |
| [ ] | Google Drive 제출 폴더 정리 |
| [ ] | 팀원별 작업일지 정리 |
| [ ] | 회의록 정리 |
| [ ] | 캡처 자료 정리 |
| [ ] | 트러블슈팅 자료 정리 |
| [ ] | 제출 링크 확인 |

---

## 13. 핵심 제출 메시지

~~~text
최종 제출 패키지는 Phase 1 필수 운영 흐름의 완성도와 검증 증거를 중심으로 구성한다.

OpenStack 인프라 구성, Ansible 자동화, Proxy/Web/DB/Backup Node 분리,
HAProxy/WordPress와 MariaDB 설치 및 구성, Proxy 경유 접속,
Health Check, Backup, Restore, Troubleshooting 자료가 모두 연결되어야 한다.

Phase 2와 Phase 3은 추가 확장 결과로 제출하며,
필수 제출 범위는 Phase 1 기준으로 완성한다.
~~~



