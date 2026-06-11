<!-- STATUS: COMPLETE -->

# Mentoring Brief

## 1. 프로젝트 개요

| 구분 | 내용 |
|---|---|
| 팀명 | Dandelion |
| 프로젝트명 | Ansible 기반 클라우드 인프라 자동화 및 운영 최적화 시스템 구축 |
| 프로젝트 기간 | 2026.06.11 ~ 2026.07.14 |
| 핵심 목표 | OpenStack 기반 클라우드 인프라 구성 이후 Ansible을 활용하여 서버 설정, Docker 서비스 배포, 상태 점검, 백업 및 복구 검증을 자동화 |

---

## 2. 프로젝트 방향

본 프로젝트는 단순한 서버 생성이나 애플리케이션 배포가 아니라, 클라우드 인프라 운영 과정에서 반복적으로 발생하는 설정, 배포, 점검, 백업, 복구 절차를 자동화하고 문서화하는 것을 목표로 한다.

핵심 구현 흐름은 다음과 같다.

~~~text
OpenStack 인프라 구성
→ SSH 접속 환경 구성
→ Ansible Inventory 작성
→ Ansible Playbook 실행
→ Docker / Nginx 서비스 배포
→ 상태 점검
→ 백업 / 복구 검증
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
| OpenStack 인프라 구성 | 진행 예정 |
| Ansible 실행 검증 | 진행 예정 |
| Docker / Nginx 배포 | 진행 예정 |
| Health Check / Backup / Restore 검증 | 진행 예정 |
| Google Drive 산출물 관리 | 진행 중 |

---

## 4. 팀원 역할

| 이름 | 역할 | 담당 업무 |
|---|---|---|
| 정주헌 | PM / 아키텍처 | 전체 구조 설계, GitHub 관리, README 및 발표자료 통합, 제출 패키지 관리 |
| 백서빈 | 클라우드 인프라 | OpenStack 인스턴스, 네트워크, 보안그룹 구성 |
| 이진욱 | 서버 / 가상화 | Linux 서버 환경 구성, Docker 설치, Nginx 컨테이너 실행 |
| 조민석 | Ansible 자동화 | ansible.cfg, inventory.ini, site.yml 작성 및 실행 |
| 박재우 | 모니터링 / 백업 / 검증 | health_check, backup, restore 검증 및 결과 정리 |

---

## 5. 구현 범위 기준

| 등급 | 기준 |
|---|---|
| A급 | 필수 구현 범위. OpenStack, SSH, Ansible, Docker/Nginx, Health Check, Backup/Restore, 산출물 정리 |
| B급 | 선택 확장 범위. node_exporter, Prometheus, Grafana, Playbook 역할 분리 |
| C급 | 제외 범위. Docker Swarm, Kubernetes, Kolla-Ansible 전체 구축, 오토스케일링, 멀티노드 HA |

A급 필수 구현을 먼저 완료하고, 이후 시간이 남을 경우 B급 선택 확장 범위를 시도한다.

---

## 6. 멘토링에서 확인받고 싶은 부분

- 기본 프로젝트 범위에서 현재 구현 범위가 적절한지
- OpenStack 서버 구성 규모가 적절한지
- Ansible 자동화 범위를 어디까지 잡는 것이 좋은지
- 모니터링 도구를 필수로 넣어야 하는지, 선택 확장으로 두어도 되는지
- 최종 발표에서 어떤 흐름을 강조하는 것이 평가에 유리한지

---

## 7. 현재 고민

현재 가장 큰 고민은 구현 범위를 넓히는 것보다, 필수 흐름을 안정적으로 완성하는 것이다.

Prometheus/Grafana 같은 모니터링 도구를 추가하면 전문성은 높아질 수 있지만, OpenStack 인프라 구성, Ansible 실행, Docker/Nginx 배포, 백업/복구 검증이 안정적으로 완료되지 않은 상태에서 범위를 확장하면 프로젝트 완성도가 떨어질 수 있다.

따라서 멘토링을 통해 필수 구현 범위와 선택 확장 범위의 적절성을 확인받고자 한다.
