<!-- STATUS: COMPLETE -->

# Team Dandelion 회의록

## 2026-06-19 회의록

## 1. 회의 정보

| 구분 | 내용 |
|---|---|
| 회의 일자 | 2026-06-19 |
| 회의 구분 | Phase 1 기본 구성 진행 및 Ansible / DB / Monitoring 초기 구성 |
| 회의 장소 | ZEP 팀 회의실 / Discord |
| 작성자 | 정주헌 |
| 참석자 | 정주헌, 백서빈, 이진욱, 조민석, 박재우 |

---

## 2. 회의 목적

- 2026-06-19 기준 팀원별 구축 진행 내용 공유
- OpenStack 인스턴스 생성 및 SSH 접속 검증 결과 확인
- Control Node 기반 Ansible 관리 구조 진행 상황 확인
- DB Node MariaDB 설치 및 초기 DB 설정 결과 확인
- Monitoring Node Prometheus 설치 및 운영 스크립트 등록 결과 확인
- 다음 작업 범위 및 담당자별 후속 작업 정리

---

## 3. 주요 진행 내용

### 3.1 백서빈 - OpenStack 인프라 구성 진행

백서빈은 OpenStack 인프라 구성 영역에서 디스크 용량 증설, 인스턴스 생성, SSH 접속 검증을 진행하였다.

| 작업 항목 | 진행 내용 | 상태 |
|---|---|---|
| Disk 용량 증설 | 전체 작업 가능 용량 300 GB 기준으로 증설 | 완료 |
| 인스턴스 생성 | 리소스표 기준 OpenStack 인스턴스 생성 | 완료 |
| SSH 접속 검증 | 생성 인스턴스 대상 SSH 접속 확인 | 완료 |

해당 작업을 통해 Phase 1 기본 구성에 필요한 인스턴스 기반 환경이 준비되었다.

---

### 3.2 이진욱 - 서버 기본 환경 및 DB 구성 진행

이진욱은 각 노드의 기본 서버 환경 구성과 DB Node의 MariaDB 초기 구성을 진행하였다.

| 작업 항목 | 진행 내용 | 상태 |
|---|---|---|
| /etc/hosts 작성 | 노드 간 이름 기반 접근을 위한 hosts 정보 작성 | 완료 |
| SSH config 설정 | Control Node 및 노드 간 SSH 접속 편의성 확보 | 완료 |
| 공통 패키지 설치 | 각 노드별 기본 운영 패키지 설치 | 완료 |
| DB 설치 및 설정 | DB Node에 MariaDB 설치 및 기본 설정 진행 | 완료 |
| DB 생성 | WordPress 연동을 위한 DB 생성 | 완료 |
| DB 계정 생성 | WordPress 연동용 DB 계정 생성 | 완료 |

DB Node는 MariaDB를 컨테이너 방식이 아니라 직접 설치 및 systemd 서비스 방식으로 운영하는 현재 프로젝트 기준에 맞춰 구성하였다.

---

### 3.3 조민석 - Ansible 기본 구성 진행

조민석은 Control Node에서 Ansible 기반 관리 구조를 구성하였다.

| 작업 항목 | 진행 내용 | 상태 |
|---|---|---|
| Ansible 설치 | Control Node에 Ansible 설치 | 완료 |
| Ansible 작업 디렉터리 생성 | Ansible 파일 관리를 위한 작업 디렉터리 구성 | 완료 |
| ansible.cfg 작성 | inventory, remote_user, private_key, become 설정 작성 | 완료 |
| inventory.ini 작성 | proxy, web, db, backup, monitoring 그룹 구성 | 완료 |
| Ansible Ping 검증 | managed 그룹 대상 ping 검증 | 완료 |
| sudo 권한 상승 검증 | become 기반 root 권한 실행 확인 | 완료 |
| site.yml 작성 | 전체 Playbook 진입점 작성 | 완료 |
| common.yml 작성 | 공통 패키지 설치 Playbook 작성 | 완료 |
| common.yml 문법 검사 | syntax-check 정상 확인 | 완료 |
| common.yml 실제 실행 | 다른 팀원 패키지 설치 작업과 충돌 방지를 위해 보류 | 보류 |

현재 Ansible 구조는 Control Node에서 관리 대상 노드를 중앙 관리하기 위한 기본 조건을 충족한 상태이다.

다만 각 노드에서 수동 패키지 설치 작업이 동시에 진행 중이므로, APT lock 충돌을 방지하기 위해 common.yml 실제 실행은 보류하였다.

---

### 3.4 박재우 - Monitoring 및 운영 스크립트 구성 진행

박재우는 Monitoring Node와 운영 자동화 스크립트 영역의 초기 구성을 진행하였다.

| 작업 항목 | 진행 내용 | 상태 |
|---|---|---|
| Prometheus 설치 | Monitoring Node에 Prometheus 설치 | 완료 |
| 운영 스크립트 작성 | 상태 점검 또는 운영 자동화 목적의 스크립트 작성 | 완료 |
| cron 등록 | 작성한 스크립트를 cron에 등록하여 주기 실행 구조 구성 | 완료 |

해당 작업을 통해 Phase 2 운영 확장 범위인 모니터링 및 주기적 운영 스크립트 실행 구조의 기초가 마련되었다.

---

### 3.5 정주헌 - PM / Architecture / Documentation 진행

정주헌은 금일 팀원별 작업 내용을 취합하고, 제출용 회의록 및 작업일지 작성 기준을 정리하였다.

| 작업 항목 | 진행 내용 | 상태 |
|---|---|---|
| 진행 내용 취합 | 백서빈, 이진욱, 조민석, 박재우 작업 내용 취합 | 완료 |
| 날짜 기준 정리 | 18일 내용과 19일 내용을 분리 | 완료 |
| 문서화 기준 정리 | 회의록 / 작업일지 반영 범위 정리 | 완료 |
| 아키텍처 정합성 확인 | Control Node 중심 관리 구조, DB 직접 설치 기준 재확인 | 완료 |

18일 기록은 리소스표 기반 인스턴스 생성 및 Control Node SSH 접속 검증으로 분리하고, 19일 기록은 Phase 1 기본 구성 진행 및 Ansible / DB / Monitoring 초기 구성으로 정리한다.

---

## 4. 금일 결정 사항

| 번호 | 결정 내용 |
|---:|---|
| 1 | 2026-06-19 기록은 Phase 1 기본 구성 진행 내용으로 작성한다. |
| 2 | 백서빈 작업은 디스크 300 GB 증설, 인스턴스 생성, SSH 접속 검증 완료로 기록한다. |
| 3 | 이진욱 작업은 /etc/hosts, SSH config, 공통 패키지 설치, DB 설치 및 계정 생성 완료로 기록한다. |
| 4 | 조민석 작업은 Ansible 기본 구성, inventory 작성, ping/sudo 검증, site.yml/common.yml 작성 및 문법 검사 완료로 기록한다. |
| 5 | common.yml 실제 실행은 다른 팀원 패키지 설치 작업과 충돌 방지를 위해 보류한 것으로 기록한다. |
| 6 | 박재우 작업은 Prometheus 설치, 운영 스크립트 작성, cron 등록 완료로 기록한다. |
| 7 | DB Node는 MariaDB 직접 설치 및 systemd 서비스 운영 기준을 유지한다. |
| 8 | Monitoring은 Prometheus 기반 초기 구성 완료로 기록한다. |
| 9 | 후속 작업은 Ansible Playbook 실제 실행, DB 접속 검증, Prometheus target 확인, 백업 스크립트 고도화로 진행한다. |

---

## 5. 이슈 및 대응

| 이슈 | 내용 | 대응 |
|---|---|---|
| Ansible common.yml 실행 보류 | 각 노드에서 수동 패키지 설치 작업이 진행 중이므로 APT lock 충돌 가능 | 문법 검사까지만 완료하고 실제 실행은 후속 작업으로 보류 |
| DB 연동 검증 필요 | DB 설치와 계정 생성은 완료되었으나 WordPress 연동 검증 필요 | Web Node 구성 후 DB 접속 테스트 진행 |
| Prometheus 설치 후 target 확인 필요 | Prometheus 설치는 완료되었으나 수집 대상 등록 및 상태 확인 필요 | Prometheus target 등록 및 Grafana 연동 확인 예정 |
| cron 등록 검증 필요 | 스크립트 cron 등록 완료 후 실행 로그 확인 필요 | cron 실행 로그 및 스크립트 결과 확인 예정 |

---

## 6. 다음 작업 계획

| 담당자 | 다음 작업 |
|---|---|
| 백서빈 | 생성 인스턴스 네트워크, 보안그룹, Floating IP, Cinder Volume 상태 캡처 정리 |
| 이진욱 | DB 접속 테스트, WordPress 연동용 DB 정보 전달, MariaDB 서비스 상태 캡처 정리 |
| 조민석 | common.yml 한 노드 시험 실행, 전체 managed 그룹 실행, docker.yml / database.yml / wordpress.yml 작성 |
| 박재우 | Prometheus target 등록 확인, cron 실행 로그 확인, backup / health check 스크립트 경로 정리 |
| 정주헌 | 19일 회의록 / 작업일지 작성, architecture.md / resource-plan.md / 발표자료 반영 |

---

## 7. 회의 결과 요약

2026년 6월 19일 회의에서는 Phase 1 기본 구성 진행 상황을 팀원별로 공유하였다.

백서빈은 디스크 용량을 300 GB 기준으로 증설하고, 리소스표 기준 인스턴스 생성 및 SSH 접속 검증을 완료하였다.

이진욱은 /etc/hosts 작성, SSH config 설정, 각 노드별 공통 패키지 설치, DB Node MariaDB 설치 및 설정, DB 생성과 계정 생성을 완료하였다.

조민석은 Control Node에서 Ansible 설치, ansible.cfg 및 inventory.ini 작성, Ansible Ping 및 sudo 권한 상승 검증, site.yml 및 common.yml 작성, common.yml 문법 검사를 완료하였다. common.yml 실제 실행은 다른 팀원의 패키지 설치 작업과 충돌 방지를 위해 보류하였다.

박재우는 Prometheus 설치, 운영 스크립트 작성, cron 등록을 완료하였다.

금일 작업을 통해 인스턴스 생성 이후 Phase 1 기본 서버 구성, DB 초기 구성, Ansible 관리 구조, Monitoring 초기 구성까지 진행되었으며, 후속 작업으로 Ansible Playbook 실제 실행, DB 연동 검증, Prometheus target 확인, cron 실행 로그 검증을 진행할 예정이다.
