<!-- STATUS: COMPLETE -->

# Mentoring Questions

## 1. 프로젝트 범위 관련 질문

### Q1. 기본 프로젝트 범위에서 현재 A급 필수 구현 범위가 적절한가?

현재 필수 구현 범위는 아래와 같이 설정하였다.

~~~text
OpenStack 인프라 구성
→ Ubuntu 인스턴스 생성
→ SSH 접속
→ Ansible ping
→ Playbook 실행
→ Docker Compose 기반 WordPress/MariaDB 배포
→ Health Check
→ Backup / Restore 검증
→ 산출물 정리
~~~

이 정도 범위가 기본 프로젝트 평가 기준에 적절한지 확인받고 싶다.

특히 기능을 많이 추가하는 것보다, 인프라 구성부터 자동화, 서비스 배포, 검증, 제출자료 정리까지 하나의 흐름으로 완성하는 방향이 평가 관점에서 적절한지 확인하고 싶다.

---

### Q2. Prometheus / Grafana는 필수로 포함해야 하는가?

평가 기준에 모니터링 도구 활용이 포함되어 있어 Prometheus, Grafana, node_exporter, cAdvisor 도입을 검토 중이다.

다만 프로젝트 완성도를 우선하기 위해 현재는 B급 선택 확장 범위로 분리하였다.

멘토님 관점에서 Prometheus / Grafana를 반드시 구현해야 하는지, 아니면 A급에서는 health_check.sh와 docker ps, curl, backup 결과 중심으로 검증하고, Prometheus / Grafana는 선택 확장으로 두어도 충분한지 확인하고 싶다.

---

### Q3. HAProxy Reverse Proxy / HTTPS 구성을 B급으로 분리한 것이 적절한가?

현재 A급은 WordPress HTTP 접속과 백업/복구 검증까지로 정의하고, HAProxy Reverse Proxy 및 HTTPS 적용은 B급 선택 확장으로 분리하였다.

~~~text
A급: WordPress HTTP 접속 검증
B급: HAProxy Reverse Proxy + HTTPS + HTTP to HTTPS Redirect
~~~

이 범위 구분이 적절한지 확인받고 싶다.

특히 HTTPS 적용이 실패하더라도 HTTP 기반 A급 결과로 발표하는 전략이 괜찮은지 조언을 받고 싶다.

---

## 2. 인프라 구성 관련 질문

### Q4. Control Node 1대 + Managed Node 2대 구성이 적절한가?

현재 예상 구조는 다음과 같다.

~~~text
Control Node
→ Ansible 실행 서버

Web Node
→ Docker Compose 기반 WordPress/MariaDB 서비스 대상

Backup / Validation Node
→ health_check.sh, backup.sh, restore 검증 대상
~~~

기본 프로젝트에서 이 구성이 적절한지, 또는 Web Node와 Backup / Validation Node를 단순화하는 것이 나은지 확인받고 싶다.

---

### Q5. OpenStack 네트워크 구성을 어느 수준까지 보여주는 것이 좋은가?

현재는 인스턴스, 네트워크, 보안그룹, SSH 접속 성공을 필수 캡처 대상으로 잡고 있다.

추가로 라우터, 서브넷, Floating IP, 보안그룹 포트 정책, 포트포워딩 구조까지 명확히 보여주는 것이 좋은지 확인하고 싶다.

특히 현재 실습 환경에서는 백서빈 컴퓨터를 기준으로 포트포워딩 및 터널링 방식 접속을 고려하고 있는데, 이 방식을 프로젝트 설명에 포함해도 되는지 확인받고 싶다.

---

### Q6. 자원 부족이 발생할 경우 어떤 조치 방향이 적절한가?

OpenStack 인스턴스 또는 실습 PC의 CPU, Memory, Disk 자원이 부족할 경우 다음과 같은 문제가 발생할 수 있다고 보고 있다.

~~~text
Instance 생성 실패
Docker image build 실패
WordPress 접속 지연
MariaDB 응답 지연
backup.sh 실패
컨테이너 재시작
~~~

이 경우 flavor 상향, 불필요한 Docker image 정리, 백업 파일 정리, 서비스 단순화, B급 기능 제외 중 어떤 순서로 대응하는 것이 적절한지 확인받고 싶다.

---

## 3. Ansible 자동화 관련 질문

### Q7. Ansible Playbook 범위는 Docker/WordPress 배포까지가 적절한가?

현재 site.yml은 Docker 설치와 Custom WordPress 및 MariaDB 컨테이너 실행까지 자동화하는 것을 목표로 한다.

추가로 health_check, backup까지 Ansible Playbook에 포함하는 것이 좋은지, 아니면 스크립트로 분리하는 것이 좋은지 확인하고 싶다.

현재 계획은 아래와 같다.

~~~text
A급:
- Docker 설치 자동화
- Docker Compose 배포 자동화
- WordPress/MariaDB 실행 자동화

B급:
- health_check / backup / restore 절차 일부 playbook화
- roles 구조 분리
~~~

이 방향이 적절한지 확인받고 싶다.

---

### Q8. Playbook을 단일 site.yml로 구성해도 되는가?

기본 프로젝트에서는 단일 site.yml로 시작하고, 시간이 남으면 roles 구조로 분리하려고 한다.

평가 관점에서 단일 playbook으로도 충분한지, roles 분리를 권장하는지 확인하고 싶다.

특히 팀원별 난이도와 기간을 고려했을 때, 처음부터 roles 구조로 가는 것이 좋은지 아니면 단일 playbook으로 완성한 뒤 개선하는 것이 좋은지 조언을 받고 싶다.

---

### Q9. OpenStack CLI + Ansible End-to-End 자동화는 추가 도전 범위로 적절한가?

A급과 B급이 조기에 완료될 경우, Ansible에서 OpenStack CLI를 실행하여 네트워크, 보안그룹, 인스턴스 생성까지 자동화하는 B+ Stretch Goal을 검토 중이다.

~~~text
Ansible 실행
→ OpenStack CLI 기반 인프라 생성
→ Inventory 반영
→ 서버 설정 자동화
→ WordPress/MariaDB 배포
→ Health Check / Backup / Restore 검증
~~~

이 구성을 최종 필수 범위로 두기에는 부담이 크다고 판단하여 B+ Stretch Goal로 분리하였다.

이 판단이 적절한지 확인받고 싶다.

---

## 4. 운영 및 장애 대응 관련 질문

### Q10. 운영 중 발생할 수 있는 장애 시나리오는 어떤 것을 포함하는 것이 좋은가?

현재 프로젝트에서는 운영 중 발생 가능한 시나리오를 아래와 같이 정리하려고 한다.

~~~text
SSH 접속 실패
포트포워딩 장애
보안그룹 포트 미허용
WordPress 접속 실패
MariaDB 연결 실패
Docker Compose 실행 실패
Backup 실패
Restore 실패
리소스 부족
HAProxy Reverse Proxy 장애
Prometheus / Grafana 수집 장애
OpenStack 인스턴스 장애
~~~

기본 프로젝트 수준에서 이 정도 장애 시나리오를 정리하면 충분한지, 또는 반드시 포함해야 할 장애 유형이 더 있는지 확인하고 싶다.

---

### Q11. 리소스 부족 시 트러블슈팅 절차는 어떻게 잡는 것이 적절한가?

현재 리소스 부족 시에는 아래 순서로 확인하는 절차를 문서화하려고 한다.

~~~text
서비스 접속 상태 확인
→ 서버 CPU / Memory / Disk 확인
→ Docker 컨테이너 상태 확인
→ Docker Volume / Disk 사용량 확인
→ MariaDB 로그 확인
→ Backup 가능 여부 확인
→ 임시 조치
→ 구조 개선 또는 리소스 증설
~~~

확인 명령어는 `free -h`, `df -h`, `top`, `docker stats`, `docker system df`, `docker logs` 등을 사용할 계획이다.

이 절차가 실무적인 트러블슈팅 흐름으로 적절한지 확인받고 싶다.

---

## 5. 프로젝트 관리 및 산출물 관련 질문

### Q12. GitHub Actions 기반 산출물 상태 자동 갱신은 차별성으로 어필해도 되는가?

팀원별 문서와 캡처 상태를 자동으로 갱신하는 구조를 만들었다.

이 기능을 핵심 구현 기능으로 보기보다는 프로젝트 관리와 산출물 관리 자동화 관점에서 설명하려고 한다.

이 방향이 적절한지 확인받고 싶다.

---

### Q13. 제출 산출물에서 GitHub 문서와 Google Drive 자료를 어떻게 연결하는 것이 좋은가?

최종 제출 자료는 Google Drive에 결과보고서, 시연 영상, 작업일지, 소스코드, 기타 자료를 정리하고, GitHub에는 소스코드와 문서, 캡처 기준을 관리하려고 한다.

멘토님 관점에서 최종 발표 시 GitHub Repository를 중심으로 설명하는 것이 좋은지, 아니면 Google Drive 제출 구조를 중심으로 설명하는 것이 좋은지 확인받고 싶다.

---

## 6. 최종 확인 질문

### Q14. 현재 프로젝트에서 반드시 줄여야 할 범위가 있는가?

구현 안정성과 발표 완성도를 위해 제외해야 할 기능이 있다면 조언을 받고 싶다.

현재 제외 후보는 아래와 같다.

~~~text
Kubernetes
Docker Swarm
OpenStack Octavia / LBaaS
DB Clustering
Auto Scaling
운영 수준의 백업 스케줄링
실서비스 도메인 및 공인 인증서 적용
~~~

이 제외 기준이 적절한지 확인받고 싶다.

---

### Q15. 현재 프로젝트에서 추가하면 평가에 도움이 될 최소 기능이 있는가?

A급 구현 완료 후 시간이 남는 경우, 가장 효과적인 추가 기능이 무엇인지 확인받고 싶다.

현재 추가 후보는 아래와 같다.

~~~text
1. HAProxy Reverse Proxy + HTTPS
2. Prometheus / Grafana 모니터링
3. Cinder Volume 기반 백업 저장소
4. Ansible roles 구조 분리
5. backup / restore playbook화
~~~

이 중 평가 대비 효율이 가장 높은 기능이 무엇인지 조언을 받고 싶다.

---

## 7. 멘토링 요청 요약

이번 멘토링에서 확인받고 싶은 핵심은 다음과 같다.

| 구분 | 확인 요청 |
|---|---|
| 범위 | A급 / B급 / B+ / C급 구분이 적절한지 |
| 인프라 | Control / Web / Backup-Validation Node 구성이 적절한지 |
| 접속 | 포트포워딩 및 터널링 기반 접속 설명이 적절한지 |
| 자동화 | Ansible playbook 범위가 적절한지 |
| 서비스 | WordPress/MariaDB 기반 서비스 대상 선정이 적절한지 |
| 운영 | 리소스 부족 및 운영 중 장애 시나리오 정리가 충분한지 |
| 확장 | HAProxy, Prometheus/Grafana, Cinder 중 우선순위가 무엇인지 |
| 산출물 | GitHub Actions 기반 상태 자동 갱신을 차별성으로 설명해도 되는지 |
