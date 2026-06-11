<!-- STATUS: COMPLETE -->
# Review Checklist

## 1. 목적

이 문서는 팀원들이 GitHub에 업로드한 문서, 설정 파일, 스크립트, 캡처 자료를 검수하기 위한 기준이다.

정주헌은 PM / 아키텍처 담당으로서 각 담당자의 결과물이 전체 프로젝트 흐름에 맞게 정리되었는지 확인한다.

---

## 2. 전체 검수 흐름

~~~text
GitHub 최신화 확인
→ 담당자별 파일 확인
→ 문서 내용 확인
→ 설정 파일 확인
→ 캡처 파일 확인
→ 실행 결과 확인
→ README / 발표자료 반영
~~~

---

## 3. 공통 검수 기준

| 검수 항목 | 기준 | 상태 |
|---|---|---|
| 담당 파일 위치가 맞는가 | 지정된 docs, ansible, scripts, screenshots 폴더 사용 | TBD |
| 문서가 비어 있지 않은가 | TBD 또는 빈 항목 최소화 | TBD |
| 명령어가 포함되어 있는가 | 사용한 명령어 기록 | TBD |
| 실행 결과가 포함되어 있는가 | 성공 결과 또는 캡처 포함 | TBD |
| 캡처 파일명이 맞는가 | 지정된 파일명 기준 | TBD |
| 민감정보가 없는가 | SSH Key, 비밀번호, pem 파일 제외 | TBD |
| 발표에 쓸 수 있는가 | 설명 가능한 결과물인지 확인 | TBD |

---

## 4. 백서빈 - Cloud Infrastructure 검수

### 대상 파일

~~~text
docs/network-design.md
screenshots/cloud-infra/
~~~

### 검수 항목

| 항목 | 확인 기준 | 상태 |
|---|---|---|
| 클라우드 플랫폼 명시 | OpenStack, AWS 등 사용 환경 작성 | TBD |
| 리전 / 존 작성 | 사용 위치 또는 Zone 작성 | TBD |
| 서버 목록 작성 | control-node, web-node, backup-node | TBD |
| IP 정보 작성 | Public IP / Private IP 구분 | TBD |
| 네트워크 구성 작성 | Subnet, Router, Security Group 등 | TBD |
| 보안그룹 정책 작성 | 22, 80 포트 기준 | TBD |
| SSH 접속 결과 | 접속 성공 캡처 포함 | TBD |
| 캡처 파일 위치 | screenshots/cloud-infra/ | TBD |

### 확인할 캡처

~~~text
screenshots/cloud-infra/instance-list.png
screenshots/cloud-infra/network-subnet.png
screenshots/cloud-infra/security-group.png
screenshots/cloud-infra/ssh-test.png
~~~

---

## 5. 이진욱 - Server / Virtualization 검수

### 대상 파일

~~~text
docs/server-setup.md
screenshots/server/
~~~

### 검수 항목

| 항목 | 확인 기준 | 상태 |
|---|---|---|
| OS 정보 작성 | cat /etc/os-release 결과 | TBD |
| Kernel 정보 작성 | uname -r 결과 | TBD |
| 사용자 계정 작성 | whoami 결과 | TBD |
| 기본 패키지 설치 기록 | apt install 명령어 포함 | TBD |
| Docker 설치 기록 | docker.io 또는 Docker CE 설치 결과 | TBD |
| Docker 서비스 상태 | active 상태 확인 | TBD |
| Nginx 컨테이너 실행 | docker ps 결과 | TBD |
| HTTP 접속 확인 | curl 결과 포함 | TBD |

### 확인할 캡처

~~~text
screenshots/server/os-info.png
screenshots/server/docker-status.png
screenshots/server/docker-ps.png
screenshots/server/curl-result.png
~~~

---

## 6. 조민석 - Ansible Automation 검수

### 대상 파일

~~~text
ansible/ansible.cfg
ansible/inventory.ini
ansible/site.yml
docs/ansible-automation.md
screenshots/ansible/
~~~

### 검수 항목

| 항목 | 확인 기준 | 상태 |
|---|---|---|
| ansible.cfg 존재 | inventory 경로와 privilege 설정 포함 | TBD |
| inventory.ini 존재 | 실제 IP와 사용자 계정 반영 | TBD |
| site.yml 존재 | 패키지, Docker, Nginx 자동화 포함 | TBD |
| Ansible 버전 작성 | ansible --version 결과 | TBD |
| Python 버전 작성 | python3 --version 결과 | TBD |
| Ping 테스트 성공 | ansible all -m ping 결과 pong | TBD |
| Syntax Check 성공 | ansible-playbook --syntax-check site.yml | TBD |
| Playbook 실행 성공 | failed=0 결과 | TBD |
| Nginx 자동 배포 확인 | docker ps 또는 curl 결과 | TBD |

### 확인할 캡처

~~~text
screenshots/ansible/ansible-version.png
screenshots/ansible/inventory.png
screenshots/ansible/ping-test.png
screenshots/ansible/playbook-result.png
screenshots/ansible/nginx-deploy-result.png
~~~

---

## 7. 박재우 - Monitoring / Backup / Validation 검수

### 대상 파일

~~~text
scripts/health_check.sh
scripts/backup.sh
scripts/restore.md
docs/validation-report.md
screenshots/validation/
~~~

### 검수 항목

| 항목 | 확인 기준 | 상태 |
|---|---|---|
| health_check.sh 존재 | hostname, uptime, free, df, docker ps, curl 포함 | TBD |
| backup.sh 존재 | /var/www/html → /backup 백업 | TBD |
| restore.md 존재 | 장애 생성, 복구, 검증 절차 포함 | TBD |
| 서버 상태 점검 결과 | CPU/Memory/Disk 확인 | TBD |
| Docker 상태 확인 | active 상태 | TBD |
| HTTP 확인 | curl 성공 | TBD |
| 백업 파일 생성 | /backup에 tar.gz 생성 | TBD |
| 복구 테스트 성공 | index.html 복구 확인 | TBD |
| 검증 체크리스트 작성 | validation-report.md 표 작성 | TBD |

### 확인할 캡처

~~~text
screenshots/validation/health-check.png
screenshots/validation/docker-status.png
screenshots/validation/http-check.png
screenshots/validation/backup-created.png
screenshots/validation/recovery-result.png
~~~

---

## 8. 민감정보 검수

GitHub에 올라가면 안 되는 파일과 정보는 아래와 같다.

| 금지 항목 | 예시 |
|---|---|
| SSH Private Key | *.pem, *.key, id_rsa |
| 비밀번호 | password, passwd |
| 환경변수 파일 | .env |
| 개인 인증정보 | Access Key, Secret Key |
| 불필요한 로그 | 대량 로그 파일 |

확인 명령어:

~~~bash
git status
git ls-files
~~~

민감정보 의심 파일이 있으면 즉시 제거한다.

~~~bash
git rm --cached 파일명
git commit -m "Remove sensitive file"
git push
~~~

---

## 9. README 반영 기준

팀원 자료가 들어오면 README에는 아래 내용만 요약 반영한다.

| 반영 위치 | 내용 |
|---|---|
| 팀 구성 | 담당자 역할 유지 |
| 구성 요소 | 실제 서버 구성 반영 |
| 작업 흐름 | 변경 없으면 유지 |
| 최종 결과 | 성공한 결과만 요약 |
| 문서 목록 | 링크 유지 |

README에는 너무 많은 명령어를 넣지 않는다.  
상세 명령어는 각 docs 문서에 둔다.

---

## 10. 발표자료 반영 기준

발표자료에는 아래 자료를 우선 사용한다.

| 발표 파트 | 우선 반영 자료 |
|---|---|
| 프로젝트 개요 | README.md |
| 아키텍처 | docs/architecture.md |
| 클라우드 인프라 | docs/network-design.md + screenshots/cloud-infra/ |
| 서버 / Docker | docs/server-setup.md + screenshots/server/ |
| Ansible 자동화 | docs/ansible-automation.md + screenshots/ansible/ |
| 검증 | docs/validation-report.md + screenshots/validation/ |
| 최종 결과 | docs/final-deliverables.md |

---

## 11. 최종 검수 기준

최종 제출 전 아래 조건을 만족해야 한다.

| 기준 | 상태 |
|---|---|
| README에서 프로젝트 목적이 명확하게 보인다 | TBD |
| docs 문서가 모두 존재한다 | TBD |
| ansible 파일이 존재한다 | TBD |
| scripts 파일이 존재한다 | TBD |
| screenshots 폴더에 결과 캡처가 있다 | TBD |
| 발표 흐름이 정리되어 있다 | TBD |
| 민감정보가 올라가지 않았다 | TBD |
| 실행 결과가 검증 가능하다 | TBD |

---

## 12. 최종 판단

최종 제출 가능 상태는 아래 한 문장으로 판단한다.

~~~text
GitHub 저장소만 봐도 프로젝트 목표, 아키텍처, 실행 방법, 자동화 결과, 검증 결과, 발표 흐름이 확인된다.
~~~


