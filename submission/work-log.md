<!-- STATUS: TEMPLATE -->

# Team Dandelion 작업일지

## 2026-06-11 작업일지

## 1. 작업 개요

| 구분 | 내용 |
|---|---|
| 작업 일자 | 2026-06-11 |
| 작업 구분 | 프로젝트 초기 기획 |
| 작성자 | 정주헌 |
| 관련 회의록 | 2026-06-11 회의록 |

---

## 2. 주요 작업 내용

| 번호 | 작업 내용 | 담당 | 상태 |
|---:|---|---|---|
| 1 | 팀명 Dandelion 확정 | 전체 | 완료 |
| 2 | 프로젝트 주제 확정 | 전체 | 완료 |
| 3 | 팀원별 역할 분담 | 전체 | 완료 |
| 4 | GitHub Repository 운영 방향 논의 | 정주헌 | 완료 |
| 5 | 산출물 관리 방식 논의 | 정주헌 | 완료 |
| 6 | Google Drive 제출 자료 관리 방식 확인 | 정주헌 | 진행 중 |
| 7 | 평가 기준 기반 프로젝트 방향 검토 | 정주헌 | 진행 중 |

---

## 3. 프로젝트 주제

Ansible 기반 클라우드 인프라 자동화 및 운영 최적화 시스템 구축

---

## 4. 팀원별 역할 정리

| 이름 | 역할 | 담당 작업 |
|---|---|---|
| 정주헌 | PM / 아키텍처 | GitHub 구조, README, 문서 통합, 발표자료, 제출 패키지 |
| 백서빈 | 클라우드 인프라 | OpenStack 인스턴스, 네트워크, 보안그룹 |
| 이진욱 | 서버 / 가상화 | Linux 서버 환경, Docker, Nginx |
| 조민석 | Ansible 자동화 | inventory, ansible.cfg, site.yml |
| 박재우 | 모니터링 / 백업 / 검증 | health_check, backup, restore |

---

## 5. 산출물 관리 기준

GitHub에는 프로젝트 원본 자료를 관리한다.

~~~text
README.md
docs/
ansible/
scripts/
screenshots/
presentation/
submission/
tools/
.github/workflows/
~~~

Google Drive에는 강사님 및 멘토님 확인을 위한 중간 산출물과 최종 제출 자료를 업로드한다.

---

## 6. 금일 결정된 작업 방향

| 구분 | 내용 |
|---|---|
| 인프라 | OpenStack 기반 클라우드 인프라 구성 |
| 자동화 | Ansible 기반 서버 설정 및 Docker/Nginx 배포 |
| 검증 | 상태 점검, 백업, 복구 검증 |
| 문서화 | README, Architecture, Runbook, Troubleshooting, Validation Report 작성 |
| 제출 | PPT/PDF, 시연 영상, 소스코드 ZIP, 작업일지, 회의록, 캡처 자료 정리 |

---

## 7. 이슈 및 확인 필요 사항

| 이슈 | 내용 | 후속 조치 |
|---|---|---|
| 실제 인프라 미구성 | OpenStack 서버 생성 전 단계 | 백서빈 작업 후 캡처 반영 |
| Ansible 실행 결과 없음 | Managed Node IP 미확정 | IP 확정 후 inventory 반영 |
| Docker/Nginx 결과 없음 | 서버 구성 전 단계 | 이진욱 작업 후 캡처 반영 |
| 백업/복구 검증 전 | 서비스 배포 전 단계 | 박재우 검증 후 반영 |
| 제출 자료 기준 정리 필요 | Google Drive 전체 산출물 업로드 필요 | submission-package.md 기준으로 관리 |

---

## 8. 다음 작업 계획

| 담당자 | 다음 작업 |
|---|---|
| 정주헌 | GitHub 구조 정리, README 작성, 제출 패키지 기준 정리 |
| 백서빈 | OpenStack 인스턴스 및 네트워크 구성 준비 |
| 이진욱 | 서버 환경 및 Docker 구성 준비 |
| 조민석 | Ansible 파일 구조 및 실행 방식 준비 |
| 박재우 | 상태 점검 및 백업/복구 검증 방식 준비 |

---

## 9. 작업 요약

2026년 6월 11일에는 프로젝트 초기 기획을 진행하였다.  
팀명, 프로젝트 주제, 팀원별 역할을 확정하였고, GitHub와 Google Drive를 활용한 산출물 관리 방향을 정리하였다.  
실제 구현 작업은 이후 OpenStack 인프라 구성부터 단계적으로 진행할 예정이다.
