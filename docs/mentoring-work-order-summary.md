<!-- STATUS: COMPLETE -->

# Mentoring Work Order Summary

## 1. 목적

본 문서는 멘토링 시 프로젝트 작업 순서를 압축해서 설명하기 위한 요약 문서이다.

본 프로젝트는 Phase 기반으로 구현 범위를 나누고, Phase 1을 최우선 완료 대상으로 둔다.

~~~text
Phase 1: 필수 구성 및 기본 검증 단계
Phase 2: 운영 확장 및 검증 고도화 단계
Phase 3: 도전 확장 단계
Out of Scope: 제외 범위
~~~

---

## 2. Phase 1: 필수 구성 및 기본 검증

Phase 1은 최종 발표와 시연을 위해 반드시 완료해야 하는 핵심 범위이다.

~~~text
1. OpenStack에서 Ubuntu 기반 인스턴스 생성
2. Control / Proxy / Web / DB / Backup Node 역할 분리
3. 네트워크, 라우터, 서브넷, 보안그룹 구성
4. Control Node에서 각 노드 SSH 접속 확인
5. Ansible inventory 구성 및 ansible ping 검증
6. Ansible Playbook으로 Docker 설치
7. DB Node에 MariaDB 서비스 배포
8. Web Node에 Custom WordPress 컨테이너 배포
9. Web Node의 WordPress가 DB Node MariaDB에 연결되는지 확인
10. Proxy Node에 HAProxy HTTP Reverse Proxy 구성
11. Proxy Node 경유 WordPress 접속 확인
12. health_check.sh로 서비스 상태 점검
13. backup.sh로 MariaDB dump 및 WordPress files 백업
14. restore.md 기준으로 복구 절차 검증
15. 캡처, 트러블슈팅, 작업일지, 제출 문서 정리
~~~

---

## 3. Phase 2: 운영 확장 및 검증 고도화

Phase 2는 Phase 1이 안정적으로 완료된 이후 가능한 범위에서 진행한다.

~~~text
1. HAProxy HTTPS self-signed 적용
2. HTTP 80 → HTTPS 443 Redirect 구성
3. Cinder Volume을 Backup Node에 attach하여 백업 저장소로 사용
4. node_exporter / cAdvisor 구성
5. Prometheus / Grafana 모니터링 구성
6. backup / restore 절차 playbook화
7. Ansible roles 구조 분리
8. 상세 검증 리포트 고도화
~~~

---

## 4. Phase 3: 도전 확장

Phase 3은 Phase 1과 Phase 2가 조기에 완료될 경우에만 시도한다.

~~~text
1. Web Node 2대 구성
2. HAProxy backend에 Web Node 1 / Web Node 2 등록
3. roundrobin 방식 Load Balancing 검증
4. 두 Web Node가 공통 DB Node에 연결되는지 확인
5. Web Node 1 장애 시 Web Node 2 응답 여부 확인
~~~

---

## 5. 제외 범위

이번 프로젝트에서는 구현 안정성과 제출 완성도를 위해 다음 항목은 제외한다.

~~~text
Kubernetes
Docker Swarm
OpenStack LBaaS / Octavia
DB Replication / Clustering
Auto Scaling
WordPress files 자동 동기화
운영 수준의 고가용성 구성
실서비스 도메인 및 공인 인증서 자동 갱신
~~~

---

## 6. 멘토링 확인 질문

멘토링에서 확인받고 싶은 핵심은 다음과 같다.

~~~text
1. Phase 1 범위가 기본 프로젝트 평가 기준에 적절한지
2. Proxy / Web / DB / Backup Node 분리 구조가 적절한지
3. HAProxy HTTP Reverse Proxy를 Phase 1에 포함해도 되는지
4. Cinder Volume을 DB 원본 저장소가 아니라 백업 저장소로 사용하는 방향이 적절한지
5. Prometheus / Grafana를 Phase 2로 분리해도 되는지
6. Web Node 2대 + HAProxy Load Balancing을 Phase 3 도전 확장으로 두는 것이 적절한지
~~~

---

## 7. 멘토링 설명 핵심 문장

~~~text
본 프로젝트는 Phase 1을 필수 성공 기준으로 두고,
Phase 2와 Phase 3은 시간이 남을 경우 진행하는 확장 범위로 분리했습니다.

Phase 1에서는 OpenStack 인프라 구성부터 Ansible 자동화,
Proxy / Web / DB / Backup Node 분리,
WordPress / MariaDB / HAProxy 배포,
상태 점검, 백업, 복구 절차 검증까지 완료하는 것을 목표로 합니다.
~~~



