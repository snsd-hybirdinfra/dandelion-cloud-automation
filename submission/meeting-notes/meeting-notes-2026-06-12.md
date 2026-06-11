<!-- STATUS: TEMPLATE -->

# Team Dandelion 회의록

## 2026-06-12 회의록

## 1. 회의 정보

| 구분 | 내용 |
|---|---|
| 회의 일자 | 2026-06-12 |
| 회의 구분 | 구현 범위 및 산출물 기준 정리 |
| 회의 장소 | ZEP 팀 회의실 / Discord |
| 작성자 | 정주헌 |
| 참석자 | 정주헌, 백서빈, 이진욱, 조민석, 박재우 |

---

## 2. 회의 목적

- 평가 기준 기반 프로젝트 범위 재정리
- A급 / B급 / C급 구현 범위 확정
- 팀원별 산출물 파일명 기준 공유
- Google Drive 수시 업로드 기준 공유
- 멘토링 준비 방향 정리

---

## 3. 결정 사항

| 구분 | 결정 내용 |
|---|---|
| A급 필수 구현 | OpenStack, SSH, Ansible, Docker/Nginx, Health Check, Backup/Restore, 산출물 정리 |
| B급 선택 확장 | node_exporter, Prometheus, Grafana, Playbook 역할 분리 |
| C급 제외 범위 | Docker Swarm, Kubernetes, Kolla-Ansible 전체 구축, 오토스케일링, 멀티노드 HA |
| 산출물 기준 | 담당자별 문서와 캡처 파일명을 고정하여 관리 |
| Google Drive | 강사님 및 멘토님 확인을 위해 중간 산출물 수시 업로드 |

---

## 4. 담당자별 작업 기준

| 담당자 | 담당 영역 | 우선 작업 |
|---|---|---|
| 정주헌 | PM / 아키텍처 | 문서, 발표자료, 제출 패키지, 멘토링 자료 |
| 백서빈 | 클라우드 인프라 | OpenStack 인스턴스, 네트워크, 보안그룹, SSH 캡처 |
| 이진욱 | 서버 / 가상화 | OS 확인, Docker 설치, Nginx 컨테이너 실행 |
| 조민석 | Ansible 자동화 | inventory, ansible.cfg, site.yml, ping/playbook 캡처 |
| 박재우 | 모니터링 / 백업 / 검증 | health_check, backup, restore 검증 |

---

## 5. 회의 결과 요약

2026년 6월 12일 회의에서는 프로젝트 구현 범위를 A급 필수 구현, B급 선택 확장, C급 제외 범위로 나누어 정리하였다.

팀은 기능 확장보다 A급 필수 구현의 완성도와 시연 가능성을 우선하기로 하였다.

또한 팀원별 산출물 위치와 캡처 파일명을 고정하여 GitHub와 Google Drive에서 동일한 기준으로 관리하기로 하였다.
