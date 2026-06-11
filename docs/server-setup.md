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

## 4. Nginx Container Test

~~~bash
docker run -d --name web-test -p 80:80 nginx
docker ps
curl http://localhost
~~~

## 5. Evidence

- OS 정보 캡처
- Docker 설치 캡처
- Docker 서비스 상태 캡처
- Nginx 컨테이너 실행 캡처
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

### 6.3 Nginx Container Running

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
| Nginx 컨테이너 실행 캡처 | TBD |
| curl 접속 결과 캡처 | TBD |
