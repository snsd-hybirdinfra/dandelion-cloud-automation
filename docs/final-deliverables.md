<!-- STATUS: COMPLETE -->

# Final Deliverables Checklist

## 1. 문서 목적

본 문서는 Team Dandelion 프로젝트의 최종 제출 산출물 기준을 정의한다.

본 프로젝트는 Phase 기반 구현 로드맵을 사용한다.

~~~text
Phase 1: 필수 구성 및 기본 검증 단계
Phase 2: 운영 확장 및 검증 고도화 단계
Phase 3: 도전 확장 단계
Out of Scope: 제외 범위
~~~

최종 제출은 Phase 1 필수 구성과 검증 결과를 기준으로 완성되어야 하며, Phase 2와 Phase 3은 시간이 남을 경우 추가 산출물로 포함한다.

---

## 2. 최종 제출 패키지 기준

최종 제출 패키지는 다음 항목을 포함한다.

| 구분 | 산출물 | 필수 여부 |
|---|---|---|
| 결과보고서 | 프로젝트 결과보고서 PPT / PDF | 필수 |
| 시연 영상 | 구현 및 검증 시연 영상 | 필수 |
| 소스 코드 | GitHub Repository 또는 압축 파일 | 필수 |
| 작업 일지 | 팀 회의록 / 작업일지 | 필수 |
| 기타 자료 | 캡처, 트러블슈팅 로그, 검증 자료 | 필수 |
| 발표자료 | 발표용 PPT / PDF | 필수 |
| 멘토링 자료 | 멘토링 질문 및 피드백 정리 | 선택 |
| 확장 검증 자료 | HTTPS / Cinder / Monitoring / LB 검증 자료 | 선택 |

---

## 3. Phase 1 필수 산출물

Phase 1은 최종 제출과 발표를 위해 반드시 확보해야 하는 기본 산출물이다.

## 3.1 인프라 산출물

| 체크 | 산출물 | 기준 |
|---|---|---|
| [ ] | OpenStack 인스턴스 목록 캡처 | Control / Proxy / Web / DB / Backup Node 확인 |
| [ ] | Ubuntu 이미지 사용 캡처 | 사용 이미지 확인 |
| [ ] | 네트워크 구성 캡처 | Network / Subnet / Router 확인 |
| [ ] | 보안그룹 캡처 | SSH / HTTP / DB 포트 정책 확인 |
| [ ] | Floating IP 또는 포트포워딩 구조 캡처 | 외부 접속 경로 설명 |
| [ ] | IP 주소표 | 각 노드 Private IP 및 접속 경로 정리 |

---

## 3.2 접속 및 Ansible 산출물

| 체크 | 산출물 | 기준 |
|---|---|---|
| [ ] | SSH 접속 성공 캡처 | Control Node에서 각 노드 접속 |
| [ ] | ansible --version 캡처 | Ansible 설치 확인 |
| [ ] | ansible-inventory --list 캡처 | proxy / web / db / backup 그룹 확인 |
| [ ] | ansible all -m ping 캡처 | 모든 Managed Node SUCCESS |
| [ ] | ansible-playbook site.yml --syntax-check 캡처 | 문법 검증 통과 |
| [ ] | ansible-playbook site.yml 실행 결과 캡처 | Playbook 실행 성공 |

---

## 3.3 서비스 배포 산출물

| 체크 | 산출물 | 기준 |
|---|---|---|
| [ ] | Docker 설치 확인 캡처 | docker --version |
| [ ] | Docker Compose 확인 캡처 | docker compose version |
| [ ] | DB Node MariaDB 서비스 캡처 | mariadb service active |
| [ ] | Web Node WordPress 컨테이너 캡처 | dandelion-wordpress running |
| [ ] | Proxy Node HAProxy 컨테이너 캡처 | dandelion-haproxy running |
| [ ] | 포트 확인 캡처 | ss -tulnp |
| [ ] | Web Node → DB Node 연결 확인 캡처 | 3306 연결 성공 |
| [ ] | Proxy Node 경유 WordPress 접속 캡처 | HTTP 응답 또는 브라우저 화면 |

---

## 3.4 상태 점검 / 백업 / 복구 산출물

| 체크 | 산출물 | 기준 |
|---|---|---|
| [ ] | health_check.sh 실행 결과 | Proxy / Web / DB 상태 확인 |
| [ ] | backup.sh 실행 결과 | DB dump 및 files archive 생성 |
| [ ] | MariaDB dump 파일 캡처 | wordpress_db.sql 생성 |
| [ ] | WordPress files archive 캡처 | wordpress_files.tar.gz 생성 |
| [ ] | restore.md | 복구 절차 문서화 |
| [ ] | Restore 검증 캡처 또는 결과 기록 | 복구 절차 검증 |
| [ ] | 장애 상황 1개 이상 정리 | 원인 / 조치 / 결과 포함 |

---

## 3.5 필수 문서 산출물

| 체크 | 문서 | 목적 |
|---|---|---|
| [ ] | README.md | 프로젝트 전체 소개 |
| [ ] | docs/architecture.md | 시스템 아키텍처 |
| [ ] | docs/network-design.md | 네트워크 및 보안그룹 |
| [ ] | docs/server-setup.md | 서버 및 Docker 구성 |
| [ ] | docs/ansible-automation.md | Ansible 자동화 |
| [ ] | docs/validation-report.md | 검증 기준 및 결과 |
| [ ] | docs/team-task-guide.md | 팀원별 작업 기준 |
| [ ] | docs/pre-run-checklist.md | 실행 전 점검 |
| [ ] | docs/troubleshooting.md | 장애 대응 |
| [ ] | docs/runbook.md | 실행 절차 |
| [ ] | docs/scope-control.md | 구현 범위 통제 |
| [ ] | docs/implementation-roadmap.md | Phase 기반 구현 순서 |
| [ ] | docs/final-deliverables.md | 최종 산출물 기준 |
| [ ] | docs/review-checklist.md | 제출 전 검수 기준 |
| [ ] | presentation/presentation-outline.md | 발표 흐름 |

---

## 4. Phase 2 선택 산출물

Phase 2는 Phase 1 완료 후 추가로 확보할 수 있는 운영 확장 산출물이다.

| 체크 | 산출물 | 기준 |
|---|---|---|
| [ ] | HTTPS 접속 캡처 | curl -k 또는 브라우저 HTTPS |
| [ ] | HTTP to HTTPS Redirect 캡처 | 301 또는 302 확인 |
| [ ] | self-signed 인증서 캡처 | 인증서 확인 |
| [ ] | Cinder Volume 생성 캡처 | openstack volume list |
| [ ] | Cinder Volume attach 캡처 | Backup Node attach 확인 |
| [ ] | /backup mount 캡처 | df -h |
| [ ] | Cinder Volume 백업 파일 캡처 | /backup 내 백업 파일 확인 |
| [ ] | node_exporter metrics 캡처 | /metrics 출력 |
| [ ] | cAdvisor metrics 캡처 | /metrics 출력 |
| [ ] | Prometheus Target UP 캡처 | Target 상태 UP |
| [ ] | Grafana Dashboard 캡처 | Dashboard 화면 |
| [ ] | backup playbook 실행 캡처 | ansible-playbook backup.yml |
| [ ] | validate playbook 실행 캡처 | ansible-playbook validate.yml |
| [ ] | Ansible roles 구조 캡처 | roles 디렉터리 구성 |

---

## 5. Phase 3 도전 산출물

Phase 3은 도전 확장 단계이며 필수 제출 범위가 아니다.

| 체크 | 산출물 | 기준 |
|---|---|---|
| [ ] | Web Node 2 인스턴스 캡처 | ACTIVE 상태 |
| [ ] | Web Node 2 Ansible ping 캡처 | SUCCESS |
| [ ] | Web Node 2 WordPress 컨테이너 캡처 | running |
| [ ] | HAProxy backend 2개 설정 캡처 | web1 / web2 등록 |
| [ ] | roundrobin 응답 분산 캡처 | Web-1 / Web-2 응답 분산 |
| [ ] | 공통 DB 연결 검증 캡처 | Web Node 1/2가 동일 DB Node 사용 |
| [ ] | Web Node 장애 테스트 캡처 | Web-1 중지 시 Web-2 응답 |

Phase 3에서는 다음 항목을 산출물로 요구하지 않는다.

~~~text
WordPress files 자동 동기화
wp-content/uploads 공유
plugin/theme 동기화
DB Replication
DB Clustering
OpenStack LBaaS / Octavia
Auto Scaling
~~~

---

## 6. Google Drive 제출 구조

최종 제출용 Google Drive는 다음 구조를 권장한다.

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
│   ├── OpenStack/
│   ├── Ansible/
│   ├── Docker/
│   ├── Proxy_Web_DB/
│   ├── Backup_Restore/
│   ├── Troubleshooting/
│   └── Optional_Phase2_Phase3/
└── 06. 기타자료/
    ├── 멘토링_질문.md
    └── 제출_체크리스트.md
~~~

---

## 7. GitHub Repository 제출 기준

GitHub Repository에는 다음 항목이 포함되어야 한다.

| 체크 | 항목 | 기준 |
|---|---|---|
| [ ] | README.md | 프로젝트 전체 설명 |
| [ ] | docs/ | 주요 문서 포함 |
| [ ] | ansible/ | ansible.cfg, inventory.ini, site.yml |
| [ ] | docker/wordpress/ | Dockerfile, custom.ini |
| [ ] | docker/compose/ | Web / MariaDB service configuration 파일 |
| [ ] | docker/proxy/ | HAProxy compose 및 haproxy.cfg |
| [ ] | scripts/ | health_check.sh, backup.sh |
| [ ] | screenshots/ | 주요 검증 캡처 |
| [ ] | presentation/ | 발표 개요 |
| [ ] | submission/ | 제출 패키지 정리 |
| [ ] | tools/ | 상태 자동 갱신 및 검증 스크립트 |
| [ ] | .github/workflows/ | GitHub Actions workflow |

---

## 8. 발표자료 포함 기준

결과보고서 또는 발표자료에는 다음 흐름이 들어가야 한다.

~~~text
1. 프로젝트 배경
2. 문제 정의
3. 목표
4. Phase 기반 구현 범위
5. 전체 아키텍처
6. OpenStack 인프라 구성
7. Ansible 자동화 구조
8. Docker Compose 기반 서비스 배포
9. Proxy / Web / DB / Backup Node 분리
10. HAProxy HTTP Reverse Proxy
11. WordPress / MariaDB 연결
12. Health Check
13. Backup / Restore
14. 장애 대응
15. Phase 2 확장 결과
16. Phase 3 도전 결과
17. 최종 결과 및 한계
~~~

Phase 2 또는 Phase 3을 수행하지 못한 경우에는 발표자료에서 다음과 같이 처리한다.

~~~text
Phase 1 필수 구성 및 기본 검증을 최종 성공 기준으로 제시하고,
Phase 2와 Phase 3은 추가 확장 계획 또는 도전 과제로 설명한다.
~~~

---

## 9. 시연 영상 포함 기준

시연 영상에는 다음 항목을 우선 포함한다.

| 순서 | 시연 항목 |
|---:|---|
| 1 | OpenStack 인스턴스 목록 |
| 2 | Control / Proxy / Web / DB / Backup Node 구조 설명 |
| 3 | ansible all -m ping |
| 4 | ansible-playbook site.yml 실행 |
| 5 | DB Node MariaDB 서비스 확인 |
| 6 | Web Node WordPress 컨테이너 확인 |
| 7 | Proxy Node HAProxy 컨테이너 확인 |
| 8 | Proxy Node 경유 WordPress HTTP 접속 |
| 9 | Web Node → DB Node 연결 확인 |
| 10 | health_check.sh 실행 |
| 11 | backup.sh 실행 |
| 12 | restore.md 복구 절차 설명 |
| 13 | 장애 상황 1개와 복구 결과 설명 |

선택 시연:

| Phase | 선택 시연 |
|---|---|
| Phase 2 | HTTPS, Cinder Backup Volume, Prometheus/Grafana |
| Phase 3 | Web Node 2대, HAProxy Load Balancing |

---

## 10. 제출 전 최종 검수

| 체크 | 검수 항목 |
|---|---|
| [ ] | Phase 1 필수 구성 완료 |
| [ ] | 필수 캡처 누락 없음 |
| [ ] | README 링크 정상 |
| [ ] | 문서 내 오래된 용어 제거 |
| [ ] | WordPress / MariaDB / HAProxy 기준 일관성 유지 |
| [ ] | Nginx 관련 표현 제거 |
| [ ] | web-test 관련 표현 제거 |
| [ ] | DB Node 분리 구조 반영 |
| [ ] | Proxy Node 경유 접속 구조 반영 |
| [ ] | Backup / Restore 검증 반영 |
| [ ] | Out of Scope 항목 명확히 정리 |
| [ ] | Google Drive 제출 폴더 정리 |
| [ ] | GitHub Repository 최신 상태 |
| [ ] | 결과보고서 PPT / PDF 생성 |
| [ ] | 시연 영상 업로드 |
| [ ] | 팀원별 작업일지 및 회의록 정리 |

---

## 11. 제출 가능 판단 기준

다음 조건을 만족하면 최종 제출 가능 상태로 판단한다.

| 기준 | 설명 |
|---|---|
| Phase 1 완성 | 필수 구성 및 기본 검증 완료 |
| Evidence 확보 | 핵심 검증 캡처 확보 |
| Runbook 확보 | 실행 절차 문서화 |
| Troubleshooting 확보 | 장애 상황 및 복구 절차 기록 |
| Source Code 확보 | Ansible / Docker / Scripts 정리 |
| Presentation 확보 | 발표자료 및 시연 흐름 정리 |
| Submission 확보 | Google Drive 제출 패키지 정리 |

---

## 12. 핵심 제출 메시지

~~~text
최종 제출의 핵심은 기능 개수보다 Phase 1 필수 운영 흐름을 끝까지 검증한 증거이다.

OpenStack 인프라 구성, Ansible 자동화, Proxy/Web/DB/Backup Node 분리,
WordPress와 MariaDB/HAProxy 배포, Proxy 경유 접속,
Health Check, Backup, Restore, Troubleshooting 결과가 모두 남아 있어야 한다.

Phase 2와 Phase 3은 추가 완성도를 보여주는 선택 산출물로 관리한다.
~~~



