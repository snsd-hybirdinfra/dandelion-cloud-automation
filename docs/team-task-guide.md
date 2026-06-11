# Team Task Guide

## 공통 작업 규칙

작업 전에는 항상 최신 내용을 가져온다.

~~~bash
git pull
~~~

작업 후에는 변경사항을 커밋하고 업로드한다.

~~~bash
git status
git add .
git commit -m "Update 담당파트 by 이름"
git push
~~~

## 담당자별 작업 위치

| 담당자 | 역할 | 작업 파일 / 폴더 |
|---|---|---|
| 박재우 | 모니터링 / 백업 / 검증 | scripts/, docs/validation-report.md, screenshots/validation/ |
| 백서빈 | 클라우드 인프라 | docs/network-design.md, screenshots/cloud-infra/ |
| 이진욱 | 서버 / 가상화 | docs/server-setup.md, screenshots/server/ |
| 정주헌 | PM / 아키텍처 | README.md, docs/architecture.md, presentation/ |
| 조민석 | Ansible 자동화 | ansible/, docs/ansible-automation.md, screenshots/ansible/ |

## 공통 제출 형식

각 담당자는 아래 내용을 정리한다.

1. 사용환경
2. 구현 내용
3. 사용 명령어
4. 설정 파일
5. 실행 결과 캡처
6. 문제 발생 및 해결 방법

## 작업 주의사항

- 다른 팀원 담당 파일은 수정하지 않는다.
- 작업 전에는 반드시 git pull을 먼저 실행한다.
- SSH Key, 비밀번호, .env 파일은 GitHub에 올리지 않는다.
- 캡처 파일은 본인 담당 screenshots 폴더에 넣는다.
- 최종 README와 발표자료 통합은 정주헌이 담당한다.

## 최종 프로젝트 흐름

~~~text
클라우드 인프라 준비
→ 서버 환경 구성
→ Ansible 자동화
→ Docker 서비스 배포
→ 상태 점검
→ 백업/복구 검증
~~~
