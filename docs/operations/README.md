# Backup Node Restic 자동화 인수인계

## 1. 목적

Backup Node에서 수동으로 검증한 Restic 기반 백업/복구 구성을 Ansible Playbook으로 자동화한다.

수동 검증 완료 항목은 다음과 같다.

- Cinder Volume을 /backup 경로로 마운트
- /backup/restic-repo에 Restic Repository 구성
- Docker Swarm WordPress replica volume 수집
- MariaDB wordpress_db dump 생성
- HAProxy 설정 파일 수집
- Prometheus 백업 예정 경로 및 README placeholder 생성
- Evidence 파일 생성
- Restic backup 실행
- restic snapshots 확인
- restic check 확인
- restore-test 복구 검증

---

## 2. Ansible 자동화 대상

대상 노드:

- backup

자동화 범위:

1. restic 설치
2. mariadb-client 설치
3. rsync 설치
4. /backup 하위 디렉터리 생성
5. /etc/restic 디렉터리 생성
6. /etc/restic/restic.env 생성
7. /etc/restic/restic-password 생성
8. /etc/mysql/backup/wp_backup.cnf 생성
9. dandelion-restic-backup.sh 배포
10. dandelion-restic-restore-test.sh 배포
11. 스크립트 실행 권한 부여
12. Restic Repository init 여부 확인
13. root crontab 등록
14. 백업 스크립트 수동 실행 검증
15. restore-test 스크립트 수동 실행 검증

---

## 3. 생성해야 할 디렉터리

Backup Node 기준:

/backup/restic-repo
/backup/restic-cache
/backup/staging/db
/backup/staging/wordpress
/backup/staging/haproxy
/backup/staging/prometheus
/backup/staging/evidence
/backup/logs
/backup/scripts
/backup/restore-test
/etc/restic
/etc/mysql/backup

---

## 4. 배포해야 할 설정 파일

### /etc/restic/restic.env

내용 예시:

export RESTIC_REPOSITORY=/backup/restic-repo
export RESTIC_PASSWORD_FILE=/etc/restic/restic-password
export RESTIC_CACHE_DIR=/backup/restic-cache

권한:

- /etc/restic: 700
- /etc/restic/restic.env: 644
- /etc/restic/restic-password: 600

### /etc/mysql/backup/wp_backup.cnf

내용 예시:

[client]
host=192.168.4.195
user=wp_backup
password=<vault 또는 변수 처리>

권한:

- /etc/mysql/backup: 700 또는 root 전용
- /etc/mysql/backup/wp_backup.cnf: 600

---

## 5. 배포해야 할 스크립트

### /backup/scripts/dandelion-restic-backup.sh

역할:

- WordPress Swarm replica volume 수집
- MariaDB wordpress_db dump 생성
- HAProxy 설정 수집
- Prometheus placeholder 생성
- Evidence 파일 생성
- Restic backup 실행
- restic snapshots 확인
- restic check 실행

### /backup/scripts/dandelion-restic-restore-test.sh

역할:

- 최신 Restic snapshot을 /backup/restore-test로 복구
- 복구 파일 목록 출력
- 복구 검증 로그 생성

권한:

chmod +x /backup/scripts/dandelion-restic-backup.sh
chmod +x /backup/scripts/dandelion-restic-restore-test.sh

---

## 6. cron 등록

root crontab에 다음 작업을 등록한다.

0 2 * * * /backup/scripts/dandelion-restic-backup.sh >> /backup/logs/restic-cron.log 2>&1

---

## 7. 완료 기준

Ansible Playbook 완료 기준은 다음과 같다.

- backup node에 restic 설치 확인
- backup node에 mariadb-client 설치 확인
- /backup/restic-repo 경로 존재
- /etc/restic/restic.env 존재
- /etc/restic/restic-password 존재
- /etc/mysql/backup/wp_backup.cnf 존재
- /backup/scripts/dandelion-restic-backup.sh 존재
- /backup/scripts/dandelion-restic-restore-test.sh 존재
- dandelion-restic-backup.sh 수동 실행 성공
- restic snapshots 조회 성공
- restic check 성공
- restore-test 복구 성공
- root crontab 등록 확인

---

## 8. 주의사항

비밀번호는 Playbook에 평문으로 고정하지 않는다.

다음 값은 ansible-vault 또는 별도 secret vars로 분리한다.

- restic password
- DB backup user password

Prometheus는 아직 실제 구성이 완료되지 않았으므로, 현재는 /backup/staging/prometheus/README.md placeholder만 생성한다.

Prometheus 구성이 완료되면 추후 prometheus.yml, rule files, exporter config를 백업 대상으로 추가한다.
