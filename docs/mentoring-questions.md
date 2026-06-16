<!-- STATUS: COMPLETE -->

# Mentoring Questions

## 1. 프로젝트 범위 관련 질문

### Q1. Phase 1 필수 구성 범위가 기본 프로젝트 평가 기준에 적절한가?

현재 Phase 1 필수 구성 범위는 아래와 같이 설정하였다.

~~~text
OpenStack 인프라 구성
→ Ubuntu 인스턴스 생성
→ Control / Proxy / Web / DB / Backup Node 분리
→ SSH 접속
→ Ansible ping
→ Playbook 실행
→ DB Node MariaDB 설치 및 구성
→ Web Node Custom WordPress 배포
→ Proxy Node HAProxy HTTP Reverse Proxy 구성
→ Proxy Node 경유 WordPress HTTP 접속 확인
→ Health Check
→ Backup / Restore 검증
→ 필수 문서 및 산출물 정리
~~~

이 정도 범위가 기본 프로젝트 평가 기준에 적절한지 확인받고 싶다.

특히 기능을 많이 추가하는 것보다, 인프라 구성부터 자동화, 서비스 배포, 검증, 제출자료 정리까지 하나의 흐름으로 완성하는 방향이 평가 관점에서 적절한지 확인하고 싶다.

---

### Q2. HAProxy HTTP Reverse Proxy를 Phase 1에 포함하는 것이 적절한가?

현재 Phase 1에서는 Proxy Node를 별도로 구성하고, HAProxy를 HTTP Reverse Proxy 용도로 배치하려고 한다.

~~~text
Client
→ Proxy Node / HAProxy HTTP Reverse Proxy
→ Web Node / WordPress
→ DB Node / MariaDB
~~~

HTTPS는 Phase 2로 분리하고, Phase 1에서는 HTTP Reverse Proxy 경유 WordPress 접속 검증까지만 포함하려고 한다.

멘토님 관점에서 HAProxy HTTP Reverse Proxy를 Phase 1 필수 구성에 포함하는 것이 적절한지 확인받고 싶다.

---

### Q3. Phase 2 운영 확장 기능의 우선순위가 적절한가?

현재 Phase 2 운영 확장 순서는 아래와 같이 설정하였다.

~~~text
1. HTTPS self-signed
2. HTTP 80 → HTTPS 443 Redirect
3. Cinder Backup Volume
4. node_exporter / cAdvisor
5. Prometheus
6. Grafana
7. backup / restore playbook화
8. Ansible roles 구조 분리
9. 상세 검증 리포트 고도화
10. 운영 장애 시나리오 확장
~~~

Phase 1 안정성을 해치지 않으면서 평가에 도움이 되는 순서로 구성하려고 한다.

멘토님 관점에서 위 순서가 적절한지, 또는 HTTPS, Cinder, Prometheus/Grafana 중 우선순위를 조정하는 것이 좋은지 확인받고 싶다.

---

### Q4. Prometheus / Grafana는 필수인지, Phase 2 운영 확장으로 두어도 되는가?

평가 기준에 모니터링 도구 활용이 포함되어 있어 Prometheus, Grafana, node_exporter, cAdvisor 도입을 검토 중이다.

다만 프로젝트 완성도를 우선하기 위해 현재는 Phase 2 운영 확장 범위로 분리하였다.

멘토님 관점에서 Prometheus / Grafana를 반드시 Phase 1에 포함해야 하는지, 아니면 Phase 1에서는 health_check.sh, docker ps, curl, backup 결과 중심으로 검증하고, Prometheus / Grafana는 Phase 2로 두어도 충분한지 확인하고 싶다.

---

### Q5. HTTPS 구성을 Phase 2로 분리한 것이 적절한가?

현재 Phase 1은 Proxy Node 경유 WordPress HTTP 접속과 백업/복구 검증까지로 정의하고, HTTPS 적용은 Phase 2 운영 확장으로 분리하였다.

~~~text
Phase 1:
HAProxy HTTP Reverse Proxy

Phase 2:
HAProxy HTTPS
self-signed certificate
HTTP 80 → HTTPS 443 Redirect
~~~

이 범위 구분이 적절한지 확인받고 싶다.

특히 HTTPS 적용이 실패하더라도 HTTP 기반 Phase 1 결과로 발표하는 전략이 괜찮은지 조언을 받고 싶다.

---

## 2. 인프라 구성 관련 질문

### Q6. Control / Proxy / Web / DB / Backup Node 구성이 적절한가?

현재 Phase 1 예상 구조는 다음과 같다.

~~~text
Control Node
→ Ansible 실행 서버

Proxy Node
→ HAProxy HTTP Reverse Proxy

Web Node
→ Custom WordPress Container

DB Node
→ MariaDB Service

Backup / Validation Node
→ health_check.sh, backup.sh, restore 검증 대상
~~~

기본 프로젝트에서 이 구성이 적절한지, 또는 노드 수를 줄이는 것이 나은지 확인받고 싶다.

---

### Q7. DB Node를 처음부터 분리하는 방향이 적절한가?

현재는 WordPress와 MariaDB를 같은 Web Node에 두지 않고, Phase 1부터 DB Node를 분리하려고 한다.

~~~text
Web Node
→ WordPress Container

DB Node
→ MariaDB Service

Web Node WordPress
→ DB Node MariaDB 연결
~~~

이 구조는 서비스 계층과 데이터 계층을 분리할 수 있어 인프라 구조 설명에는 유리하지만, 네트워크와 보안그룹, DB 접속 설정이 추가된다.

기본 프로젝트 범위에서 DB Node를 처음부터 분리하는 것이 적절한지 확인받고 싶다.

---

### Q8. OpenStack 네트워크 구성을 어느 수준까지 보여주는 것이 좋은가?

현재는 인스턴스, 네트워크, 라우터, 서브넷, 보안그룹, SSH 접속 성공을 필수 캡처 대상으로 잡고 있다.

추가로 Floating IP, 포트포워딩 구조, 보안그룹 포트 정책, Proxy → Web → DB 통신 흐름까지 명확히 보여주는 것이 좋은지 확인하고 싶다.

특히 현재 실습 환경에서는 특정 팀원 PC를 기준으로 포트포워딩 및 터널링 방식 접속을 고려하고 있는데, 이 방식을 프로젝트 설명에 포함해도 되는지 확인받고 싶다.

---

### Q9. 자원 부족이 발생할 경우 어떤 조치 방향이 적절한가?

OpenStack 인스턴스 또는 실습 PC의 CPU, Memory, Disk 자원이 부족할 경우 다음과 같은 문제가 발생할 수 있다고 보고 있다.

~~~text
Instance 생성 실패
Docker image build 실패
WordPress 접속 지연
MariaDB 응답 지연
backup.sh 실패
컨테이너 재시작
Prometheus / Grafana 실행 불가
~~~

이 경우 flavor 상향, 불필요한 Docker image 정리, 백업 파일 정리, 서비스 단순화, Phase 2 기능 제외 중 어떤 순서로 대응하는 것이 적절한지 확인받고 싶다.

---

### Q10. Cinder Volume은 백업 저장소로 사용하는 방향이 적절한가?

현재 Cinder Volume은 MariaDB 원본 데이터 저장소가 아니라 Backup / Validation Node의 백업 저장소로 사용하는 방향을 검토하고 있다.

~~~text
DB Node
→ MariaDB 운영 데이터는 Docker Volume 또는 로컬 디스크 사용

Backup / Validation Node
→ Cinder Volume attach
→ /backup mount
→ DB dump 및 WordPress files backup 저장
~~~

DB 원본 데이터를 Cinder에 직접 올리는 방식은 Docker Volume 경로, DB 권한, 마운트 안정성 문제로 인해 제외하고자 한다.

Cinder를 백업 저장소로만 사용하는 이 범위가 기본 프로젝트 수준에서 적절한지 확인받고 싶다.

---

## 3. Ansible 자동화 관련 질문

### Q11. Ansible Playbook 범위는 WordPress / MariaDB / HAProxy 배포까지가 적절한가?

현재 site.yml은 Docker 설치와 Custom WordPress, MariaDB, HAProxy HTTP Reverse Proxy 실행까지 자동화하는 것을 목표로 한다.

현재 계획은 아래와 같다.

~~~text
Phase 1:
- Docker 설치 자동화
- DB Node MariaDB 설치 및 구성 자동화
- Web Node WordPress 배포 자동화
- Proxy Node HAProxy HTTP Reverse Proxy 배포 자동화

Phase 2:
- health_check / backup / restore 절차 일부 playbook화
- roles 구조 분리
~~~

이 방향이 적절한지 확인받고 싶다.

---

### Q12. health_check와 backup은 Playbook에 포함하는 것이 좋은가?

Phase 1에서는 health_check.sh와 backup.sh를 스크립트로 실행하고, Phase 2에서 이를 Ansible Playbook으로 감싸는 방향을 고려하고 있다.

~~~text
Phase 1:
health_check.sh
backup.sh
restore.md 기반 검증

Phase 2:
backup.yml
validate.yml
roles 구조 분리
~~~

멘토님 관점에서 health_check와 backup을 Phase 1부터 Playbook에 포함하는 것이 좋은지, 아니면 스크립트로 분리한 뒤 Phase 2에서 playbook화하는 것이 적절한지 확인받고 싶다.

---

### Q13. Playbook을 단일 site.yml로 구성해도 되는가?

기본 프로젝트에서는 단일 site.yml로 시작하고, 시간이 남으면 roles 구조로 분리하려고 한다.

평가 관점에서 단일 playbook으로도 충분한지, roles 분리를 권장하는지 확인하고 싶다.

특히 팀원별 난이도와 기간을 고려했을 때, 처음부터 roles 구조로 가는 것이 좋은지 아니면 단일 playbook으로 완성한 뒤 개선하는 것이 좋은지 조언을 받고 싶다.

---

### Q14. OpenStack CLI + Ansible End-to-End 자동화는 후순위 추가 도전으로 두어도 되는가?

Ansible에서 OpenStack CLI를 실행하여 네트워크, 보안그룹, 인스턴스 생성까지 자동화하는 구성을 검토하고 있다.

~~~text
Ansible 실행
→ OpenStack CLI 기반 인프라 생성
→ Inventory 반영
→ 서버 설정 자동화
→ WordPress / MariaDB / HAProxy 배포
→ Health Check / Backup / Restore 검증
~~~

다만 이 구성은 인증 정보, OpenStack CLI 환경, 중복 리소스 처리, inventory 반영 등 변수가 많아 현재는 Phase 3의 핵심이 아니라 후순위 추가 도전으로 분리하려고 한다.

이 판단이 적절한지 확인받고 싶다.

---

## 4. Phase 3 도전 확장 관련 질문

### Q15. Web Node 2대 + HAProxy Load Balancing을 Phase 3 도전 확장으로 두는 것이 적절한가?

Phase 1과 Phase 2가 조기에 안정화될 경우, 아래와 같은 확장 구조를 Phase 3 도전 확장으로 검토하고 있다.

~~~text
Client
→ Proxy Node / HAProxy Load Balancer
→ Web Node 1 / WordPress
→ Web Node 2 / WordPress
→ DB Node / MariaDB
→ Backup / Validation Node
~~~

이 구조는 단일 Web Node 구조보다 확장성 설명에는 유리하지만, 구현 난이도와 검증 범위가 커질 수 있어 필수 구현이 아닌 Phase 3로 분리하였다.

이 범위 설정이 적절한지 확인받고 싶다.

---

### Q16. WordPress files 자동 동기화는 제외하는 것이 적절한가?

Web Node 2대를 구성할 경우 WordPress는 DB뿐만 아니라 `wp-content/uploads`, plugins, themes 같은 파일도 각 Web Node 로컬에 저장한다.

따라서 Web Node 2대 구성에서 WordPress files 자동 동기화까지 구현하려면 NFS, Object Storage, rsync, 공유 스토리지 등 추가 구성이 필요하다.

이번 프로젝트에서는 아래 항목을 제외하려고 한다.

~~~text
WordPress files 자동 동기화
wp-content/uploads 공유
plugin/theme 동기화
NFS 기반 WordPress shared storage
Object Storage 연동
DB Replication
Auto Scaling
~~~

대신 Phase 3 시연은 HAProxy roundrobin, Web-1/Web-2 응답 분산, 공통 DB 연결 확인 수준으로 제한하려고 한다.

이 범위 통제가 적절한지 확인받고 싶다.

---

### Q17. OpenStack LBaaS / Octavia를 제외하고 HAProxy 컨테이너 기반으로 검증하는 것이 적절한가?

OpenStack LBaaS / Octavia까지 구현하면 전문성은 높아질 수 있지만, amphora image, management network, listener, pool, health monitor 등 OpenStack 서비스 의존성이 커질 수 있다고 판단하였다.

따라서 이번 프로젝트에서는 OpenStack LBaaS / Octavia를 제외하고, HAProxy 컨테이너 기반 HTTP Reverse Proxy 또는 간단한 Load Balancing으로 검증하려고 한다.

이 판단이 적절한지 확인받고 싶다.

---

## 5. 운영 및 장애 대응 관련 질문

### Q18. 운영 중 발생할 수 있는 장애 시나리오는 어떤 것을 포함하는 것이 좋은가?

현재 프로젝트에서는 운영 중 발생 가능한 시나리오를 아래와 같이 정리하려고 한다.

~~~text
SSH 접속 실패
포트포워딩 장애
보안그룹 포트 미허용
Proxy Node 장애
HAProxy Reverse Proxy 장애
WordPress 접속 실패
DB Node MariaDB 연결 실패
Docker Compose 실행 실패
Backup 실패
Restore 실패
리소스 부족
Prometheus / Grafana 수집 장애
OpenStack 인스턴스 장애
~~~

기본 프로젝트 수준에서 이 정도 장애 시나리오를 정리하면 충분한지, 또는 반드시 포함해야 할 장애 유형이 더 있는지 확인하고 싶다.

---

### Q19. 리소스 부족 시 트러블슈팅 절차는 어떻게 잡는 것이 적절한가?

현재 리소스 부족 시에는 아래 순서로 확인하는 절차를 문서화하려고 한다.

~~~text
서비스 접속 상태 확인
→ 서버 CPU / Memory / Disk 확인
→ Docker 컨테이너 상태 확인
→ Docker Volume / Disk 사용량 확인
→ MariaDB 로그 확인
→ HAProxy 로그 확인
→ Backup 가능 여부 확인
→ 임시 조치
→ 구조 개선 또는 리소스 증설
~~~

확인 명령어는 `free -h`, `df -h`, `top`, `docker stats`, `docker system df`, `docker logs`, `ss -tulnp` 등을 사용할 계획이다.

이 절차가 실무적인 트러블슈팅 흐름으로 적절한지 확인받고 싶다.

---

## 6. 프로젝트 관리 및 산출물 관련 질문

### Q20. GitHub Actions 기반 산출물 상태 자동 갱신은 차별성으로 어필해도 되는가?

팀원별 문서와 캡처 상태를 자동으로 갱신하는 구조를 만들었다.

이 기능을 핵심 구현 기능으로 보기보다는 프로젝트 관리와 산출물 관리 자동화 관점에서 설명하려고 한다.

이 방향이 적절한지 확인받고 싶다.

---

### Q21. 제출 산출물에서 GitHub 문서와 Google Drive 자료를 어떻게 연결하는 것이 좋은가?

최종 제출 자료는 Google Drive에 결과보고서, 시연 영상, 작업일지, 소스코드, 기타 자료를 정리하고, GitHub에는 소스코드와 문서, 캡처 기준을 관리하려고 한다.

멘토님 관점에서 최종 발표 시 GitHub Repository를 중심으로 설명하는 것이 좋은지, 아니면 Google Drive 제출 구조를 중심으로 설명하는 것이 좋은지 확인받고 싶다.

---

## 7. 최종 확인 질문

### Q22. 현재 프로젝트에서 반드시 줄여야 할 범위가 있는가?

구현 안정성과 발표 완성도를 위해 제외해야 할 기능이 있다면 조언을 받고 싶다.

현재 제외 후보는 아래와 같다.

~~~text
Kubernetes
Docker Swarm
OpenStack Octavia / LBaaS
WordPress files 자동 동기화
DB Clustering
DB Replication
Auto Scaling
운영 수준의 백업 스케줄링
실서비스 도메인 및 공인 인증서 적용
~~~

이 제외 기준이 적절한지 확인받고 싶다.

---

### Q23. 현재 프로젝트에서 추가하면 평가에 도움이 될 최소 기능이 있는가?

Phase 1 구현 완료 후 시간이 남는 경우, 가장 효과적인 추가 기능이 무엇인지 확인받고 싶다.

현재 추가 후보는 아래와 같다.

~~~text
1. HTTPS self-signed + Redirect
2. Cinder Volume 기반 백업 저장소
3. Prometheus / Grafana 모니터링
4. Ansible roles 구조 분리
5. backup / restore playbook화
6. Web Node 2대 + HAProxy Load Balancing
~~~

이 중 평가 대비 효율이 가장 높은 기능이 무엇인지 조언을 받고 싶다.

---

## 8. 멘토링 요청 요약

이번 멘토링에서 확인받고 싶은 핵심은 다음과 같다.

| 구분 | 확인 요청 |
|---|---|
| 범위 | Phase 1 / Phase 2 / Phase 3 / Out of Scope 구분이 적절한지 |
| 인프라 | Control / Proxy / Web / DB / Backup-Validation Node 구성이 적절한지 |
| DB | DB Node를 처음부터 분리하는 방향이 적절한지 |
| 접속 | 포트포워딩 및 터널링 기반 접속 설명이 적절한지 |
| Proxy | HAProxy HTTP Reverse Proxy를 Phase 1에 포함하는 것이 적절한지 |
| 스토리지 | Cinder Volume을 Backup Storage로 사용하는 방향이 적절한지 |
| 자동화 | Ansible playbook 범위가 적절한지 |
| 서비스 | WordPress/MariaDB 기반 서비스 대상 선정이 적절한지 |
| 운영 | 리소스 부족 및 운영 중 장애 시나리오 정리가 충분한지 |
| 확장 | HTTPS, Cinder Backup Volume, Prometheus/Grafana 중 우선순위가 무엇인지 |
| Phase 3 | Web Node 2대 + HAProxy LB를 도전 확장 단계로 두는 것이 적절한지 |
| 제외 | WordPress files 자동 동기화와 OpenStack LBaaS/Octavia를 제외하는 것이 적절한지 |
| 산출물 | GitHub Actions 기반 상태 자동 갱신을 차별성으로 설명해도 되는지 |

