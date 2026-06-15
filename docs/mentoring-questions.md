<!-- STATUS: COMPLETE -->

# Mentoring Questions

## 1. 프로젝트 범위 관련 질문

### Q1. 기본 프로젝트 범위에서 현재 A급 필수 구현 범위가 적절한가?

현재 필수 구현 범위는 아래와 같이 설정하였다.

~~~text
OpenStack 인프라 구성
→ SSH 접속
→ Ansible ping
→ Playbook 실행
→ Docker / WordPress 배포
→ Health Check
→ Backup / Restore 검증
→ 산출물 정리
~~~

이 정도 범위가 기본 프로젝트 평가 기준에 적절한지 확인받고 싶다.

---

### Q2. Prometheus / Grafana는 필수로 포함해야 하는가?

평가 기준에 모니터링 도구 활용이 포함되어 있어 Prometheus, Grafana, node_exporter 도입을 검토 중이다.

다만 프로젝트 완성도를 우선하기 위해 현재는 B급 선택 확장 범위로 분리하였다.

멘토님 관점에서 모니터링 도구를 반드시 구현해야 하는지, 아니면 시도 흔적과 상태 점검 스크립트 중심으로도 충분한지 확인하고 싶다.

---

## 2. 인프라 구성 관련 질문

### Q3. Control Node 1대 + Managed Node 2대 구성이 적절한가?

현재 예상 구조는 다음과 같다.

~~~text
Control Node: Ansible 실행 서버
Web Node: Docker Compose 기반 WordPress/MariaDB 서비스 대상
Backup or Validation Node: 백업 / 복구 / 검증 대상
~~~

기본 프로젝트에서 이 구성이 적절한지, 또는 단순화하는 것이 나은지 확인받고 싶다.

---

### Q4. OpenStack 네트워크 구성을 어느 수준까지 보여주는 것이 좋은가?

현재는 인스턴스, 네트워크, 보안그룹, SSH 접속 성공을 필수 캡처 대상으로 잡고 있다.

추가로 라우터, 플로팅 IP, 스토리지까지 명확히 보여주는 것이 좋은지 확인하고 싶다.

---

## 3. Ansible 자동화 관련 질문

### Q5. Ansible Playbook 범위는 Docker/WordPress 배포까지가 적절한가?

현재 site.yml은 Docker 설치와 Custom WordPress 및 MariaDB 컨테이너 실행까지 자동화하는 것을 목표로 한다.

추가로 health_check, backup까지 Ansible Playbook에 포함하는 것이 좋은지, 아니면 스크립트로 분리하는 것이 좋은지 확인하고 싶다.

---

### Q6. Playbook을 단일 site.yml로 구성해도 되는가?

기본 프로젝트에서는 단일 site.yml로 시작하고, 시간이 남으면 roles 구조로 분리하려고 한다.

평가 관점에서 단일 playbook으로도 충분한지, roles 분리를 권장하는지 확인하고 싶다.

---

## 4. 발표 및 평가 관련 질문

### Q7. 최종 발표에서 어떤 흐름을 가장 강조해야 하는가?

현재 발표 흐름은 다음과 같이 구성하려고 한다.

~~~text
문제 정의
→ OpenStack 인프라 구성
→ Ansible 자동화
→ Docker / WordPress 배포
→ 상태 점검
→ 백업 / 복구 검증
→ GitHub / Google Drive 산출물 관리
~~~

이 흐름이 평가자에게 논리적으로 전달될 수 있는지 확인받고 싶다.

---

### Q8. GitHub Actions 기반 산출물 상태 자동 갱신은 차별성으로 어필해도 되는가?

팀원별 문서와 캡처 상태를 자동으로 갱신하는 구조를 만들었다.

이 기능을 핵심 구현 기능으로 보기보다는 프로젝트 관리와 산출물 관리 자동화 관점에서 설명하려고 한다.

이 방향이 적절한지 확인받고 싶다.

---

## 5. 최종 확인 질문

### Q9. 현재 프로젝트에서 반드시 줄여야 할 범위가 있는가?

구현 안정성과 발표 완성도를 위해 제외해야 할 기능이 있다면 조언을 받고 싶다.

---

### Q10. 현재 프로젝트에서 추가하면 평가에 도움이 될 최소 기능이 있는가?

A급 구현 완료 후 시간이 남는 경우, 가장 효과적인 추가 기능이 무엇인지 확인받고 싶다.

