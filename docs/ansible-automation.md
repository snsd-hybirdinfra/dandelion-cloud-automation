# Ansible Automation

## 1. 목표

이 문서는 Control Node에서 Ansible을 사용해 Managed Node에 대한 자동화를 실행하는 흐름을 정리한다.

## 2. 실행 환경

| 항목 | 내용 |
|---|---|
| Ansible Version | 설치 후 확인 필요 |
| Python Version | 설치 후 확인 필요 |
| Inventory File | ansible/inventory.ini |
| Playbook File | ansible/site.yml |

## 3. 주요 실행 명령

```bash
ansible all -m ping
ansible-playbook site.yml
```

## 4. 자동화 범위

| 작업 | 상태 |
|---|---|
| 패키지 업데이트 | 자동화 대상 |
| 기본 패키지 설치 | 자동화 대상 |
| Docker 설치 | 자동화 대상 |
| Docker 서비스 시작 | 자동화 대상 |
| Nginx 컨테이너 배포 | 자동화 대상 |

## 5. 제출용 증빙 자료

- ansible 버전 캡처
- inventory.ini 캡처
- ansible.cfg 캡처
- site.yml 캡처
- ping 성공 결과 캡처
- playbook 실행 결과 캡처

## 6. 체크리스트

| 항목 | 상태 |
|---|---|
| Ansible 버전 확인 | 진행 필요 |
| inventory 작성 | 진행 필요 |
| playbook 작성 | 진행 필요 |
| ping 성공 확인 | 진행 필요 |
| playbook 실행 확인 | 진행 필요 |





