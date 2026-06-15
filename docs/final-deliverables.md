<!-- STATUS: COMPLETE -->
# Final Deliverables Checklist

## 1. 목적

이 문서는 Team Dandelion 프로젝트의 최종 제출 산출물을 확인하기 위한 체크리스트이다.

최종 제출 기준은 단순 코드 제출이 아니라, 인프라 구성, Ansible 자동화, 서비스 배포, 상태 점검, 백업 및 복구 검증, 발표자료까지 포함한다.

---

## 2. 최종 제출 구조

~~~text
dandelion-cloud-automation/
├── README.md
├── docs/
│   ├── architecture.md
│   ├── network-design.md
│   ├── server-setup.md
│   ├── ansible-automation.md
│   ├── validation-report.md
│   ├── team-task-guide.md
│   ├── pre-run-checklist.md
│   ├── troubleshooting.md
│   ├── runbook.md
│   └── final-deliverables.md
├── ansible/
│   ├── ansible.cfg
│   ├── inventory.ini
│   └── site.yml
├── scripts/
│   ├── health_check.sh
│   ├── backup.sh
│   └── restore.md
├── screenshots/
│   ├── cloud-infra/
│   ├── server/
│   ├── ansible/
│   └── validation/
└── presentation/
    └── presentation-outline.md
~~~

---

## 3. 공통 제출 체크리스트

| 항목 | 설명 | 완료 여부 |
|---|---|---|
| README.md | 프로젝트 개요, 목표, 구조 정리 | TBD |
| Architecture 문서 | 전체 시스템 아키텍처 정리 | TBD |
| Network Design 문서 | 클라우드 인프라 구성 정리 | TBD |
| Server Setup 문서 | 서버 및 Docker 구성 정리 | TBD |
| Ansible Automation 문서 | Ansible 설정 및 실행 결과 정리 | TBD |
| Validation Report 문서 | 상태 점검, 백업, 복구 검증 정리 | TBD |
| Runbook | 실행 절차 정리 | TBD |
| Troubleshooting | 오류 대응 방법 정리 | TBD |
| Presentation Outline | 발표 흐름 및 멘트 정리 | TBD |
| Screenshots | 실행 결과 캡처 정리 | TBD |

---

## 4. 정주헌 - PM / Architecture 산출물

| 산출물 | 위치 | 완료 여부 |
|---|---|---|
| 프로젝트 README | README.md | TBD |
| 전체 아키텍처 문서 | docs/architecture.md | TBD |
| 팀 작업 기준 문서 | docs/team-task-guide.md | TBD |
| 실행 전 체크리스트 | docs/pre-run-checklist.md | TBD |
| Runbook | docs/runbook.md | TBD |
| Troubleshooting Guide | docs/troubleshooting.md | TBD |
| 최종 산출물 체크리스트 | docs/final-deliverables.md | TBD |
| 발표 흐름 문서 | presentation/presentation-outline.md | TBD |

---

## 5. 백서빈 - Cloud Infrastructure 산출물

| 산출물 | 위치 | 완료 여부 |
|---|---|---|
| 클라우드 플랫폼 정보 | docs/network-design.md | TBD |
| 서버 목록 | docs/network-design.md | TBD |
| Public IP / Private IP | docs/network-design.md | TBD |
| 네트워크 구성 | docs/network-design.md | TBD |
| 보안그룹 정책 | docs/network-design.md | TBD |
| 인스턴스 목록 캡처 | screenshots/cloud-infra/instance-list.png | TBD |
| 네트워크 / 서브넷 캡처 | screenshots/cloud-infra/network-subnet.png | TBD |
| 보안그룹 캡처 | screenshots/cloud-infra/security-group.png | TBD |
| SSH 접속 성공 캡처 | screenshots/cloud-infra/ssh-test.png | TBD |

---

## 6. 이진욱 - Server / Virtualization 산출물

| 산출물 | 위치 | 완료 여부 |
|---|---|---|
| OS 정보 | docs/server-setup.md | TBD |
| Kernel 정보 | docs/server-setup.md | TBD |
| 기본 패키지 설치 결과 | docs/server-setup.md | TBD |
| Docker 설치 결과 | docs/server-setup.md | TBD |
| Docker 서비스 상태 | docs/server-setup.md | TBD |
| WordPress/MariaDB 컨테이너 실행 결과 | docs/server-setup.md | TBD |
| OS 정보 캡처 | screenshots/server/os-info.png | TBD |
| Docker 상태 캡처 | screenshots/server/docker-status.png | TBD |
| docker ps 캡처 | screenshots/server/docker-ps.png | TBD |
| curl 결과 캡처 | screenshots/server/curl-result.png | TBD |

---

## 7. 조민석 - Ansible Automation 산출물

| 산출물 | 위치 | 완료 여부 |
|---|---|---|
| ansible.cfg | ansible/ansible.cfg | TBD |
| inventory.ini | ansible/inventory.ini | TBD |
| site.yml | ansible/site.yml | TBD |
| Ansible 버전 정리 | docs/ansible-automation.md | TBD |
| Python 버전 정리 | docs/ansible-automation.md | TBD |
| ansible ping 결과 | docs/ansible-automation.md | TBD |
| playbook 실행 결과 | docs/ansible-automation.md | TBD |
| Ansible 버전 캡처 | screenshots/ansible/ansible-version.png | TBD |
| Inventory 캡처 | screenshots/ansible/inventory.png | TBD |
| Ping 테스트 캡처 | screenshots/ansible/ping-test.png | TBD |
| Playbook 실행 캡처 | screenshots/ansible/playbook-result.png | TBD |
| WordPress/MariaDB 배포 결과 캡처 | screenshots/ansible/wordpress-deploy-result.png | TBD |

---

## 8. 박재우 - Monitoring / Backup / Validation 산출물

| 산출물 | 위치 | 완료 여부 |
|---|---|---|
| health_check.sh | scripts/health_check.sh | TBD |
| backup.sh | scripts/backup.sh | TBD |
| restore.md | scripts/restore.md | TBD |
| 검증 보고서 | docs/validation-report.md | TBD |
| 서버 상태 점검 결과 | docs/validation-report.md | TBD |
| Docker 상태 확인 결과 | docs/validation-report.md | TBD |
| HTTP 확인 결과 | docs/validation-report.md | TBD |
| 백업 실행 결과 | docs/validation-report.md | TBD |
| 복구 테스트 결과 | docs/validation-report.md | TBD |
| Health Check 캡처 | screenshots/validation/health-check.png | TBD |
| Docker 상태 캡처 | screenshots/validation/docker-status.png | TBD |
| HTTP 확인 캡처 | screenshots/validation/http-check.png | TBD |
| 백업 생성 캡처 | screenshots/validation/backup-created.png | TBD |
| 복구 결과 캡처 | screenshots/validation/recovery-result.png | TBD |

---

## 9. 발표자료 체크리스트

| 항목 | 담당 | 완료 여부 |
|---|---|---|
| 프로젝트 개요 | 정주헌 | TBD |
| 전체 아키텍처 | 정주헌 | TBD |
| 클라우드 인프라 구성 | 백서빈 | TBD |
| 서버 / Docker 구성 | 이진욱 | TBD |
| Ansible 자동화 구현 | 조민석 | TBD |
| 모니터링 / 백업 / 복구 검증 | 박재우 | TBD |
| 최종 결과 및 기대효과 | 정주헌 | TBD |
| GitHub 저장소 화면 | 정주헌 | TBD |
| 실행 결과 캡처 정리 | 전체 | TBD |

---

## 10. 최종 성공 기준

아래 조건을 만족하면 프로젝트 최종 제출 가능 상태로 본다.

| 성공 기준 | 확인 방법 | 완료 여부 |
|---|---|---|
| GitHub 저장소 구조 완성 | Repository 확인 | TBD |
| 서버 3대 구성 완료 | Cloud Console 확인 | TBD |
| SSH 접속 성공 | ssh 명령어 확인 | TBD |
| Ansible Ping 성공 | ansible all -m ping | TBD |
| Playbook 실행 성공 | ansible-playbook site.yml | TBD |
| Docker 서비스 실행 | systemctl status docker | TBD |
| Custom WordPress 및 MariaDB 컨테이너 실행 | docker ps | TBD |
| HTTP 응답 성공 | curl -I http://server-ip | TBD |
| 백업 파일 생성 성공 | ls -lh /backup | TBD |
| 복구 테스트 성공 | cat /var/www/html/index.html | TBD |
| 발표 흐름 정리 완료 | presentation-outline.md 확인 | TBD |

---

## 11. 최종 요약

본 프로젝트의 최종 산출물은 다음 흐름을 증명해야 한다.

~~~text
클라우드 인프라 준비
→ 서버 환경 구성
→ Ansible 자동화
→ Docker 서비스 배포
→ 상태 점검
→ 백업 / 복구 검증
→ 문서 / 발표자료 통합
~~~

최종 제출 시에는 기능 구현 결과뿐 아니라, 각 단계별 캡처와 문서가 함께 정리되어 있어야 한다.



