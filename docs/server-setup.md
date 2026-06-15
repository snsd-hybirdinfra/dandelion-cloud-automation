# Server Setup

## 1. 구성 목표

이 문서는 서버에 기본 패키지를 설치하고 Docker/Nginx를 배포하는 과정을 정리한다.

## 2. 기본 패키지 설치

```bash
sudo apt update
sudo apt install -y curl wget git vim net-tools
```

## 3. Docker 설치 및 실행

```bash
sudo apt install -y docker.io
sudo systemctl enable docker
sudo systemctl start docker
sudo systemctl status docker
docker --version
```

## 4. Nginx 컨테이너 배포 검증

```bash
docker run -d --name web-test -p 80:80 nginx
docker ps
curl http://localhost
```

## 5. 제출용 검증 항목

- OS 정보 캡처
- Docker 설치 및 상태 캡처
- 컨테이너 실행 결과 캡처
- HTTP 응답 캡처

## 6. 체크리스트

| 항목 | 상태 |
|---|---|
| OS 정보 정리 | 진행 필요 |
| Docker 설치 정리 | 진행 필요 |
| 컨테이너 실행 확인 | 진행 필요 |
| curl 결과 정리 | 진행 필요 |





