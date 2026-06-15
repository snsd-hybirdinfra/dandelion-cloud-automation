<!-- STATUS: COMPLETE -->
# Team Task Guide

## 1. 목적

이 문서는 Team Dandelion 프로젝트의 팀원별 작업 기준, GitHub 작업 방식, 제출 자료 형식, 캡처 파일 위치를 정리한다.

본 프로젝트의 전체 흐름은 다음과 같다.

~~~text
클라우드 인프라 준비
→ 서버 환경 구성
→ Ansible 자동화
→ Docker 서비스 배포
→ 상태 점검
→ 백업 / 복구 검증
→ 문서 / 발표자료 정리
~~~

---

## 2. 공통 Git 작업 규칙

작업 전에는 항상 최신 내용을 가져온다.

~~~bash
git pull
~~~

작업 후에는 변경사항을 확인한다.

~~~bash
git status
~~~

변경사항을 추가한다.

~~~bash
git add .
~~~

커밋 메시지는 아래 형식을 사용한다.

~~~bash
git commit -m "Update 담당파트 by 이름"
~~~

예시:

~~~bash
git commit -m "Update network design by Baek Seobin"
git commit -m "Update server setup by Lee Jinwook"
git commit -m "Update ansible automation by Cho Minseok"
git commit -m "Update validation report by Park Jaewoo"
~~~

GitHub에 업로드한다.

~~~bash
git push
~~~

---

## 3. 담당자별 작업 위치

| 담당자 | 역할 | 작업 파일 | 캡처 폴더 |
|---|---|---|---|
| 박재우 | 모니터링 / 백업 / 검증 | docs/validation-report.md, scripts/ | screenshots/validation/ |
| 백서빈 | 클라우드 인프라 | docs/network-design.md | screenshots/cloud-infra/ |
| 이진욱 | 서버 / 가상화 | docs/server-setup.md | screenshots/server/ |
| 정주헌 | PM / 아키텍처 | README.md, docs/architecture.md, presentation/ | presentation/ |
| 조민석 | Ansible 자동화 | ansible/, docs/ansible-automation.md | screenshots/ansible/ |

---

## 4. 공통 제출 형식

각 담당자는 본인 문서에 아래 내용을 정리한다.

1. 사용환경
2. 구현 내용
3. 사용 명령어
4. 설정 파일
5. 실행 결과 캡처
6. 문제 발생 및 해결 방법

---

## 5. 백서빈 - 클라우드 인프라 담당

### 작성 파일

~~~text
docs/network-design.md
~~~

### 캡처 저장 위치

~~~text
screenshots/cloud-infra/
~~~

### 제출 항목

- 사용 클라우드 플랫폼
- 리전 / 존
- 서버 목록
- Public IP / Private IP
- 네트워크 구성
- 보안그룹 정책
- SSH 접속 성공 결과

### 권장 캡처 파일명

~~~text
screenshots/cloud-infra/instance-list.png
screenshots/cloud-infra/network-subnet.png
screenshots/cloud-infra/security-group.png
screenshots/cloud-infra/ssh-test.png
~~~

---

## 6. 이진욱 - 서버 / 가상화 담당

### 작성 파일

~~~text
docs/server-setup.md
~~~

### 캡처 저장 위치

~~~text
screenshots/server/
~~~

### 제출 항목

- OS 정보
- Kernel 정보
- 사용자 계정
- 기본 패키지 설치 결과
- Docker 설치 결과
- Docker 서비스 상태
- WordPress/MariaDB 컨테이너 실행 결과
- curl 접속 결과

### 권장 캡처 파일명

~~~text
screenshots/server/os-info.png
screenshots/server/docker-status.png
screenshots/server/docker-ps.png
screenshots/server/curl-result.png
~~~

---

## 7. 조민석 - Ansible 자동화 담당

### 작성 파일

~~~text
ansible/ansible.cfg
ansible/inventory.ini
ansible/site.yml
docs/ansible-automation.md
~~~

### 캡처 저장 위치

~~~text
screenshots/ansible/
~~~

### 제출 항목

- Ansible 버전
- Python 버전
- ansible.cfg
- inventory.ini
- site.yml
- ansible all -m ping 성공 결과
- ansible-playbook 실행 결과
- Docker / WordPress 자동 배포 결과

### 권장 캡처 파일명

~~~text
screenshots/ansible/ansible-version.png
screenshots/ansible/inventory.png
screenshots/ansible/ping-test.png
screenshots/ansible/playbook-result.png
screenshots/ansible/wordpress-deploy-result.png
~~~

---

## 8. 박재우 - 모니터링 / 백업 / 검증 담당

### 작성 파일

~~~text
docs/validation-report.md
scripts/health_check.sh
scripts/backup.sh
scripts/restore.md
~~~

### 캡처 저장 위치

~~~text
screenshots/validation/
~~~

### 제출 항목

- 서버 상태 점검 결과
- Docker 상태 확인 결과
- WordPress HTTP 접속 결과
- 백업 스크립트 실행 결과
- 백업 파일 생성 결과
- 복구 테스트 결과
- 검증 체크리스트

### 권장 캡처 파일명

~~~text
screenshots/validation/health-check.png
screenshots/validation/docker-status.png
screenshots/validation/http-check.png
screenshots/validation/backup-created.png
screenshots/validation/recovery-result.png
~~~

---

## 9. 정주헌 - PM / 아키텍처 담당

### 작성 파일

~~~text
README.md
docs/architecture.md
docs/team-task-guide.md
presentation/presentation-outline.md
~~~

### 담당 항목

- 전체 프로젝트 목표 정리
- 시스템 아키텍처 정리
- 팀원별 역할 정리
- GitHub 저장소 구조 관리
- 팀원 자료 통합
- 발표 순서 정리
- 최종 발표 시작 / 마무리 담당

---

## 10. 작업 주의사항

- 작업 전에는 반드시 git pull을 먼저 실행한다.
- 다른 팀원 담당 파일은 수정하지 않는다.
- SSH Key, 비밀번호, .env 파일은 GitHub에 올리지 않는다.
- pem, key, ppk 파일은 업로드하지 않는다.
- 캡처 파일은 본인 담당 screenshots 폴더에 넣는다.
- 파일명은 가급적 영어 소문자와 하이픈을 사용한다.
- 최종 README와 발표자료 통합은 정주헌이 담당한다.

---

## 11. 팀원에게 공유할 기본 명령어

처음 저장소를 받을 때:

~~~bash
git clone https://github.com/snsd-hybirdinfra/dandelion-cloud-automation.git
cd dandelion-cloud-automation
~~~

작업 전:

~~~bash
git pull
~~~

작업 후:

~~~bash
git status
git add .
git commit -m "Update 담당파트 by 이름"
git push
~~~

---

## 12. 최종 제출 기준

최종 제출 시 저장소에는 아래 결과가 포함되어야 한다.

- README.md
- 전체 아키텍처 문서
- 클라우드 인프라 문서
- 서버 / Docker 구성 문서
- Ansible 자동화 파일
- 모니터링 / 백업 / 복구 검증 문서
- 실행 결과 캡처
- 발표 흐름 문서



---

## 백서빈 추가 작업: Ubuntu 인스턴스 구성

| 구분 | 작업 내용 | 산출물 |
|---|---|---|
| Image | Ubuntu 이미지 확인 | image list 캡처 |
| Instance | Ubuntu 인스턴스 생성 | instance 생성 캡처 |
| Status | 인스턴스 ACTIVE 상태 확인 | server list 캡처 |
| Network | Floating IP 연결 | FIP 연결 캡처 |
| Access | SSH 접속 확인 | ssh 접속 성공 캡처 |
| OS Check | Ubuntu 버전 확인 | lsb_release 또는 /etc/os-release 캡처 |

Ubuntu 인스턴스는 Ansible 자동화와 Docker 기반 WordPress/MariaDB 서비스 배포의 기본 실행 환경으로 사용한다.

