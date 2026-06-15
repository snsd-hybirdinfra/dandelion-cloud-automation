<!-- STATUS: TEMPLATE -->
# TEMP: 팀원 실제 작업 결과 반영 필요

# Server Setup

## 1. OS Information

| 항목 | 내용 |
|---|---|
| OS | TBD |
| Kernel | TBD |
| User | TBD |
| Package Manager | apt |

## 2. Basic Package Setup

~~~bash
sudo apt update
sudo apt install -y curl wget git vim net-tools
~~~

## 3. Docker Setup

~~~bash
sudo apt install -y docker.io
sudo systemctl enable docker
sudo systemctl start docker
sudo systemctl status docker
docker --version
~~~

## 4. WordPress/MariaDB Container Test

~~~bash
docker compose up -d
docker ps
curl http://localhost
~~~

## 5. Evidence

- OS 정보 캡처
- Docker 설치 캡처
- Docker 서비스 상태 캡처
- Custom WordPress 및 MariaDB 컨테이너 실행 캡처
- curl 접속 결과 캡처

## 6. Screenshots

### 6.1 OS Information

이미지 파일 위치:

~~~text
screenshots/server/os-info.png
~~~

### 6.2 Docker Service Status

이미지 파일 위치:

~~~text
screenshots/server/docker-status.png
~~~

### 6.3 WordPress/MariaDB Containers Running

이미지 파일 위치:

~~~text
screenshots/server/docker-ps.png
~~~

### 6.4 HTTP Test Result

이미지 파일 위치:

~~~text
screenshots/server/curl-result.png
~~~

## 7. 담당자 제출 체크리스트

| 항목 | 완료 여부 |
|---|---|
| OS 정보 정리 | TBD |
| Kernel 정보 정리 | TBD |
| Docker 설치 명령어 정리 | TBD |
| Docker 서비스 상태 캡처 | TBD |
| Custom WordPress 및 MariaDB 컨테이너 실행 캡처 | TBD |
| curl 접속 결과 캡처 | TBD |

<!-- AUTO_IMAGES_START -->
## 자동 반영 이미지

아래 이미지는 screenshots/ 폴더에 파일이 업로드되면 자동으로 표시된다.

### OS Information

../screenshots/server/os-info.png 이미지가 아직 업로드되지 않았다.

### Docker Service Status

../screenshots/server/docker-status.png 이미지가 아직 업로드되지 않았다.

### WordPress/MariaDB Containers Running

../screenshots/server/docker-ps.png 이미지가 아직 업로드되지 않았다.

### HTTP Test Result

../screenshots/server/curl-result.png 이미지가 아직 업로드되지 않았다.
<!-- AUTO_IMAGES_END -->

<!-- AUTO_IMAGES_START -->
## 자동 반영 이미지

아래 이미지는 screenshots/ 폴더에 파일이 업로드되면 자동으로 표시된다.

### OS Information

../screenshots/server/os-info.png 이미지가 아직 업로드되지 않았다.

### Docker Service Status

../screenshots/server/docker-status.png 이미지가 아직 업로드되지 않았다.

### WordPress/MariaDB Containers Running

../screenshots/server/docker-ps.png 이미지가 아직 업로드되지 않았다.

### HTTP Test Result

../screenshots/server/curl-result.png 이미지가 아직 업로드되지 않았다.


