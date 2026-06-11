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
