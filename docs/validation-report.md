# Validation Report

## 1. 검증 목적

이 문서는 Ansible 자동화와 서비스 배포 결과를 실제로 확인하기 위한 상태 점검, 서비스 검증, 백업 및 복구 테스트 결과를 정리한다.

## 2. 상태 점검 항목

| 검증 항목 | 명령어 | 기대 결과 |
|---|---|---|
| Hostname 확인 | hostname | 정상 출력 |
| Uptime 확인 | uptime | 서버 가동 시간 출력 |
| Memory 확인 | free -h | 메모리 사용량 확인 |
| Disk 확인 | df -h | 디스크 사용량 확인 |
| Docker 상태 확인 | systemctl status docker | active 상태 |
| Container 확인 | docker ps | Nginx 컨테이너 실행 |
| HTTP 확인 | curl http://localhost | HTML 응답 확인 |

## 3. 백업 및 복구 검증

| 항목 | 내용 |
|---|---|
| Backup Source | /var/www/html |
| Backup Directory | /backup |
| Backup File | web_backup_DATE.tar.gz |
| Recovery Action | 삭제된 파일 복원 |

## 4. 최종 체크리스트

| 검증 항목 | 상태 |
|---|---|
| SSH 접속 확인 | 진행 필요 |
| Docker 설치 확인 | 진행 필요 |
| Nginx 컨테이너 실행 확인 | 진행 필요 |
| HTTP 접속 확인 | 진행 필요 |
| 백업 생성 확인 | 진행 필요 |
| 복구 성공 확인 | 진행 필요 |

## 5. 제출용 증빙 자료

- 서버 상태 점검 캡처
- Docker 상태 캡처
- HTTP 응답 캡처
- 백업 파일 생성 캡처
- 복구 성공 캡처





