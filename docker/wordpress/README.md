<!-- STATUS: COMPLETE -->

# Custom WordPress Image

Dandelion 프로젝트에서 사용하는 **커스텀 WordPress 컨테이너 이미지** 정의 디렉터리이다.

이 이미지는 Docker Hub 공식 WordPress 이미지를 기반으로 하며, 웹 애플리케이션 개발이 아니라 **운영 설정 커스터마이징과 컨테이너 배포 검증**을 목적으로 한다.

---

## 1. Base Image

사용하는 기본 이미지는 Docker Hub 공식 WordPress 이미지이다.

~~~text
wordpress:php8.2-apache
~~~

Dockerfile에서는 다음과 같이 공식 이미지를 Base Image로 사용한다.

~~~dockerfile
FROM wordpress:php8.2-apache
~~~

---

## 2. Customization Scope

이번 프로젝트에서의 커스터마이징 범위는 **운영 설정 수준**으로 제한한다.

### Included

- PHP upload size 설정
- PHP post size 설정
- PHP memory limit 설정
- Image metadata label 추가
- 프로젝트 식별용 이미지 구성

### Excluded

- WordPress plugin 개발
- WordPress theme 개발
- PHP 기반 웹 애플리케이션 개발
- 복잡한 DB schema 변경
- WordPress 기능 커스터마이징

---

## 3. Files

| 파일 | 설명 |
|---|---|
| Dockerfile | WordPress 공식 이미지를 기반으로 커스텀 이미지를 생성하는 파일 |
| custom.ini | PHP 실행 환경 설정 파일 |
| README.md | 커스텀 이미지 목적과 범위 설명 문서 |

---

## 4. custom.ini Settings

~~~ini
upload_max_filesize=64M
post_max_size=64M
memory_limit=256M
max_execution_time=300
~~~

위 설정은 WordPress 운영 시 필요한 기본 PHP 제한값을 조정하기 위한 것이다.

---

## 5. Image Purpose

이 커스텀 이미지는 다음 내용을 검증하기 위해 사용한다.

- Docker Hub 공식 Base Image 활용
- Dockerfile 기반 Custom Image 작성
- Docker Compose 기반 서비스 배포
- WordPress와 MariaDB 연동
- Ansible을 통한 배포 자동화
- Health Check 검증
- Backup / Restore 절차 검증

---

## 6. Deployment Flow

서비스 배포 흐름은 다음과 같다.

~~~text
Ansible Control Node
→ Web Node 접속
→ Docker 설치
→ Custom WordPress Image Build
→ MariaDB Container 실행
→ WordPress Container 실행
→ HTTP 접속 확인
→ Health Check
→ Backup / Restore 검증
~~~

---

## 7. Operational Boundary

본 프로젝트는 WordPress 기능 개발을 목표로 하지 않는다.

WordPress는 다음 목적을 위한 서비스 대상이다.

- 컨테이너 기반 웹 서비스 배포 대상
- MariaDB 연동 검증 대상
- 백업 및 복구 검증 대상
- Ansible 자동화 검증 대상
- OpenStack 인프라 위 서비스 운영 검증 대상

따라서 프로젝트의 핵심은 웹 개발이 아니라 **클라우드 인프라 자동화 및 운영 검증**이다.
