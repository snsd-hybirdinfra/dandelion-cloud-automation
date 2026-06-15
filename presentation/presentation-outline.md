<!-- STATUS: COMPLETE -->

# Presentation Outline

## 0. 제출 기준 반영

본 발표자료는 1차 기본 프로젝트 결과보고서 목차 기준에 맞춰 구성한다.

필수 구성:
1. 프로젝트 개요
2. 프로젝트 팀 구성 및 역할
3. 프로젝트 수행 절차 및 방법
4. 프로젝트 수행 경과
5. 자체 평가 의견

---

## 1. 표지

### 제목

Ansible 기반 클라우드 인프라 자동화 및 운영 최적화 시스템 구축

### 포함 내용

- Team Dandelion
- 팀원명
- 강사 / 멘토
- 프로젝트 기간

---

## 2. 목차

1. 프로젝트 개요
2. 프로젝트 팀 구성 및 역할
3. 프로젝트 수행 절차 및 방법
4. 프로젝트 수행 경과
5. 자체 평가 의견

---

## 3. 프로젝트 개요

### 핵심 내용

- 프로젝트 주제
- 선정 배경
- 기획 의도
- 기존 수동 인프라 운영의 문제점
- 프로젝트 기대 효과

### 발표 메시지

수동 서버 설정은 반복 작업이 많고 팀원별 설정 편차가 발생할 수 있다.  
본 프로젝트는 OpenStack 인프라 구성 이후 Ansible을 활용하여 서버 초기 설정, Docker 서비스 배포, 상태 점검, 백업 및 복구 검증을 자동화하는 것을 목표로 한다.

---

## 4. 평가 기준 대응 전략

| 평가항목 | 대응 내용 |
|---|---|
| 전문성 | OpenStack, Ansible, Docker, 상태 점검, 백업/복구 |
| 차별성 | 수동 운영 편차 개선, GitHub Actions 기반 산출물 상태 자동화 |
| 완성도 | SSH, ping, playbook, Docker, HTTP, backup/restore 성공 흐름 |
| 프로젝트 관리 | GitHub Repository, 문서화, 팀원별 산출물 관리 |
| 발표 및 시연 | 인프라 구현부터 검증까지 논리적 흐름으로 시연 |

---

## 5. 팀 구성 및 역할

| 이름 | 역할 | 담당 업무 |
|---|---|---|
| 박재우 | 모니터링 / 백업 / 검증 | health check, backup, restore 검증 |
| 백서빈 | 클라우드 인프라 | OpenStack 인스턴스, 네트워크, 보안그룹 |
| 이진욱 | 서버 / 가상화 | Linux 환경, Docker, Nginx 컨테이너 |
| 정주헌 | PM / 아키텍처 | 구조 설계, GitHub 관리, 문서 통합, 발표 흐름 |
| 조민석 | Ansible 자동화 | inventory, ansible.cfg, site.yml, playbook 실행 |

---

## 6. 전체 아키텍처
### 사용 이미지

~~~text
docs/assets/system-architecture.png
~~~

### 설명 포인트

- OpenStack 기반 클라우드 인프라 구성
- Control Node에서 Ansible 자동화 실행
- Managed Node에 Docker / Nginx 배포
- Health Check / Backup / Restore 검증
- GitHub와 Google Drive 기반 산출물 관리


~~~text
OpenStack Cloud
   ↓
Control Node
   ↓ SSH Key
Managed Nodes
   ├─ Web Node: Docker / Nginx
   └─ Backup Node: Health Check / Backup / Restore
~~~

### 발표 포인트

Control Node를 중심으로 Ansible Playbook을 실행하고, Managed Node에 대해 서버 설정, Docker 설치, Nginx 배포, 상태 점검 및 백업/복구 검증을 수행한다.

---

## 7. 수행 절차 및 방법

| 단계 | 수행 내용 | 담당 |
|---|---|---|
| 1 | OpenStack 인프라 구성 | 백서빈 |
| 2 | 서버 접속 및 기본 환경 확인 | 이진욱 |
| 3 | Ansible Inventory / Config 작성 | 조민석 |
| 4 | Playbook 기반 Docker / Nginx 배포 | 조민석 |
| 5 | 상태 점검 및 백업/복구 검증 | 박재우 |
| 6 | GitHub 문서 및 발표자료 통합 | 정주헌 |

---

## 8. GitHub 기반 프로젝트 관리

### 핵심 내용

- 팀원별 담당 폴더 분리
- README / docs / ansible / scripts / screenshots 구조화
- GitHub Actions 기반 프로젝트 상태 자동 갱신
- 산출물 누락 여부 자동 확인

### 발표 메시지

프로젝트 관리 항목에 대응하기 위해 GitHub Repository를 중심으로 팀 산출물을 관리하고, 팀원이 파일을 업로드하면 README와 project-status 문서가 자동으로 갱신되도록 구성했다.

---

## 9. 수행 경과 - 인프라 구성

### 포함 자료

- OpenStack 인스턴스 목록
- 네트워크 / 보안그룹
- SSH 접속 성공 캡처

### 담당

백서빈

---

## 10. 수행 경과 - 서버 및 Docker 구성

### 포함 자료

- OS 정보
- Docker 설치 결과
- Docker 서비스 상태
- Nginx 컨테이너 실행
- curl 접속 결과

### 담당

이진욱

---

## 11. 수행 경과 - Ansible 자동화

### 포함 자료

- ansible.cfg
- inventory.ini
- site.yml
- ansible all -m ping 결과
- ansible-playbook 실행 결과

### 담당

조민석

---

## 12. 수행 경과 - 모니터링 / 백업 / 복구 검증

### 포함 자료

- health_check.sh 실행 결과
- Docker / HTTP 확인
- backup.sh 실행 결과
- restore 테스트 결과
- Validation Checklist

### 담당

박재우

---

## 13. 문제점 및 해결 과정

### 포함할 내용

- SSH 접속 문제
- 보안그룹 포트 문제
- Ansible inventory IP 문제
- Docker 권한 문제
- 백업/복구 경로 문제

### 발표 포인트

평가 기준상 완성도와 차별성을 위해, 단순 성공 결과뿐 아니라 어떤 문제가 있었고 어떻게 해결했는지를 짧게 설명한다.

---

## 14. 최종 결과

| 결과 | 상태 |
|---|---|
| OpenStack 인프라 구성 | 진행 / 완료 |
| Ansible ping | 진행 / 완료 |
| Playbook 실행 | 진행 / 완료 |
| Docker / Nginx 배포 | 진행 / 완료 |
| 상태 점검 | 진행 / 완료 |
| 백업 / 복구 검증 | 진행 / 완료 |
| GitHub 자동 상태 관리 | 완료 |

---

## 15. 자체 평가 의견

### 잘한 점

- GitHub 기반 산출물 구조를 초기에 정리했다.
- 팀원별 담당 영역을 명확히 분리했다.
- 자동 상태 갱신을 통해 진행상황을 관리할 수 있게 했다.

### 아쉬운 점

- 실제 인프라 구성과 자동화 검증 결과가 늦게 들어오면 완성도 확보가 어려워질 수 있다.
- 모니터링 도구 적용 범위를 시간 내에 조정해야 한다.

### 개선 방향

- 실제 실행 결과를 문서와 캡처로 연결해 완성도를 높인다.
- 발표 시에는 구현 흐름과 검증 결과를 중심으로 간결하게 전달한다.
- 향후에는 백업/복구 자동화와 모니터링 확장을 이어서 발전시킨다.

- Prometheus / Grafana 또는 node_exporter 기반 모니터링 시도
- Ansible Playbook 역할 분리
- 백업/복구 검증 절차 자동화 확대

---

## 16. 발표 마무리 멘트

저희 팀은 단순히 서버를 생성하고 서비스를 배포하는 데서 끝내지 않고,  
OpenStack 인프라 구성부터 Ansible 기반 자동화, Docker 서비스 배포, 상태 점검, 백업/복구 검증, GitHub 기반 산출물 관리까지 하나의 운영 흐름으로 연결했습니다.

