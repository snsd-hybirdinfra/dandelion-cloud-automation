<!-- STATUS: TEMPLATE -->
# TEMP: 팀원 실제 작업 결과 반영 필요

# Validation Report

## 1. Validation Scope

본 문서는 Ansible 자동화 결과가 정상적으로 적용되었는지 확인하기 위한 상태 점검, 서비스 검증, 백업 및 복구 테스트 결과를 정리한다.

## 2. Health Check

| 검증 항목 | 명령어 | 결과 |
|---|---|---|
| Hostname 확인 | hostname | TBD |
| Uptime 확인 | uptime | TBD |
| Memory 확인 | free -h | TBD |
| Disk 확인 | df -h | TBD |
| Docker 상태 확인 | systemctl status docker | TBD |
| Container 확인 | docker ps | TBD |
| HTTP 확인 | curl http://localhost | TBD |

## 3. Backup Test

| 항목 | 내용 |
|---|---|
| Backup Source | /var/www/html |
| Backup Directory | /backup |
| Backup File | web_backup_DATE.tar.gz |
| Result | TBD |

## 4. Recovery Test

| 항목 | 내용 |
|---|---|
| 장애 상황 | index.html 삭제 |
| 복구 방식 | tar archive restore |
| 복구 결과 | TBD |

## 5. Final Checklist

| 검증 항목 | 결과 |
|---|---|
| SSH 접속 확인 | TBD |
| Docker 설치 확인 | TBD |
| Nginx 컨테이너 실행 확인 | TBD |
| HTTP 접속 확인 | TBD |
| 백업 생성 확인 | TBD |
| 복구 성공 확인 | TBD |

## 6. Evidence

- 서버 상태 점검 캡처
- Docker 상태 캡처
- Nginx 접속 캡처
- 백업 파일 생성 캡처
- 복구 성공 캡처

<!-- AUTO_IMAGES_START -->
## 자동 반영 이미지
<<<<<<< HEAD

아래 이미지는 screenshots/ 폴더에 파일이 업로드되면 자동으로 표시된다.

### Host Health Check

../screenshots/validation/health-check.png 이미지가 아직 업로드되지 않았다.

### Docker Status Check

../screenshots/validation/docker-status.png 이미지가 아직 업로드되지 않았다.

### HTTP Service Check

../screenshots/validation/http-check.png 이미지가 아직 업로드되지 않았다.

### Backup File Created

../screenshots/validation/backup-created.png 이미지가 아직 업로드되지 않았다.

### Recovery Test Result

../screenshots/validation/recovery-result.png 이미지가 아직 업로드되지 않았다.
<!-- AUTO_IMAGES_END -->

=======
>>>>>>> f45a1ee164fe5136961f2866f96f39f209cd2490

아래 이미지는 screenshots/ 폴더에 파일이 업로드되면 자동으로 표시된다.

### Host Health Check

../screenshots/validation/health-check.png 이미지가 아직 업로드되지 않았다.

### Docker Status Check

../screenshots/validation/docker-status.png 이미지가 아직 업로드되지 않았다.

### HTTP Service Check

../screenshots/validation/http-check.png 이미지가 아직 업로드되지 않았다.

### Backup File Created

../screenshots/validation/backup-created.png 이미지가 아직 업로드되지 않았다.

### Recovery Test Result

../screenshots/validation/recovery-result.png 이미지가 아직 업로드되지 않았다.
<!-- AUTO_IMAGES_END -->
