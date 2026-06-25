# Dandelion 백업 및 모니터링 작업 문서

# 1. Cron 등록

## Backup 서버

백업 작업 스크립트 실행

```bash
crontab -e
```

예시

```cron
0 * * * * /home/ubuntu/dandelion/backup.sh
```

---

## Monitoring 서버

헬스체크 스크립트 실행

```bash
crontab -e
```

예시

```cron
*/5 * * * * /home/ubuntu/dandelion/health-check.sh
```

### 확인 사항

* cron 시간 형식 검토
* 쉘 실행 권한 확인

```bash
chmod +x *.sh
```

---

# 2. Command Substitution 확인

현재 사용 예정인 구문

```bash
$(ls -td /tmp/backup/* | head -n 1)
```

확인 항목

* 작은 따옴표('') 내부에서는 명령어 치환이 수행되지 않음
* 원격 SSH 명령에서 변수 확장 위치 확인 필요
* 백업 디렉터리 선택 로직 검증

예시

```bash
ssh ubuntu@backup "ls -td /tmp/backup/* | head -n 1"
```

---

# 3. hosts 파일 수정

backup 서버와 monitoring 서버 모두 수정

```bash
sudo vi /etc/hosts
```

추가

```text
192.168.4.134 backup
192.168.4.179 monitoring
192.168.4.201 db
192.168.4.89  control
192.168.4.32  proxy
192.168.4.4   web1
192.168.4.35  web2
```

목적

* ping
* ssh

등의 명령에서 호스트명 사용

---

# 4. 스크립트 분리

## Backup

현재

```text
backup.sh
```

분리

```text
db-backup.sh
web-backup.sh
backup.sh
```

### 역할

#### db-backup.sh

DB 덤프 생성

```bash
mysqldump ...
```

#### web-backup.sh

웹 데이터 압축

```bash
tar -czf ...
```

#### backup.sh

백업 작업 통합 실행

```bash
source db-backup.sh
source web-backup.sh
```

---

## Health Check

현재

```text
health-check.sh
```

분리

```text
backup-check.sh
control-check.sh
db-check.sh
proxy-check.sh
web1-check.sh
web2-check.sh
health-check.sh
```

### health-check.sh 역할

각 서버별 상태 점검 스크립트 실행

```bash
source ./web1-check.sh
source ./web2-check.sh
source ./db-check.sh
source ./proxy-check.sh
source ./backup-check.sh
source ./control-check.sh
```

결과 저장

```text
/tmp/monitoring/YYYY-MM-DD/check_results.txt
```

---

# 5. SSH Timeout 제한

모든 헬스체크 스크립트에 적용

```bash
-o ConnectTimeout=2
```

예시

```bash
ssh \
-o ConnectTimeout=2 \
-i /home/ubuntu/.ssh/dandelion.pem \
ubuntu@db \
'free -mh'
```

목적

* 장애 서버 대기 시간 감소
* 전체 헬스체크 수행 시간 단축

---

# 6. 임시 복구 작업

## DB 복구

최신 백업본으로 DB 복원

```bash
ssh -i /home/ubuntu/.ssh/dandelion.pem \
ubuntu@backup \
"cat $(ls -td /tmp/backup/* | head -n 1)/backup.sql" \
| ssh ubuntu@db \
"mysql -u사용자이름 -p'비밀번호' wordpress"
```

### TODO

* 사용자명 적용
* 비밀번호 적용
* 백업 경로 검증

---

## WEB 복구

최신 웹 백업본으로 복원

### web2 복구

```bash
ssh -i /home/ubuntu/.ssh/dandelion.pem \
ubuntu@backup \
"cat $(ls -td /tmp/backup/* | head -n 1)/backup-web2.tar.gz" \
| ssh ubuntu@web2 \
"tar -xzf - -C /var/www/html/"
```

### TODO

* web1 복구 절차 추가
* 압축 파일 존재 여부 검증
* 복구 전 백업 수행 여부 검토
* 복구 시나리오 별 케이스 작성

### Advanced
* 로그 관리
* 오픈 스택 등 인증 백업
* DB 이중화 또는 클러스터링

---

# 향후 개선 사항

## Backup

### DB

* 백업 성공 여부 확인
* 덤프 무결성 검증

### WEB

* 백업 파일 크기 검증
* 압축 오류 확인

### Storage

* Cinder Volume 기준 사용량 확인
* 저장 공간 임계치 초과 시 알림

---

## Monitoring

### Resource Check

추가 예정

```bash
free -mh
df -h
```

확인 항목

* Memory
* Disk
* CPU

### Auto Recovery

DB 장애 시

```bash
sudo systemctl restart mysql
```

실패 시

* 최신 백업본 자동 복원


