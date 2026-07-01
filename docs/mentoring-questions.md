<!-- STATUS: CURRENT -->

# Mentoring Questions

## 1. 문서 목적

본 문서는 멘토링 당일 확인받을 질문을 정리한다.

질문 목적은 다음과 같다.

```text
1. 현재 구현 방향이 프로젝트 주제에 적합한지 확인
2. 남은 기간 동안 우선순위 조정
3. Provisioning 자동화 범위 확인
4. Docker Swarm / DB Replica / Monitoring / Backup 범위 적정성 확인
5. 최종 발표에서 강조할 포인트 확인
```

---

## 2. 프로젝트 현재 설명

```text
현재 프로젝트는 OpenStack 기반 인프라 위에 Web, DB, Proxy, Monitoring, Backup / Recovery 구성 요소를 배치하고,
Control Node에서 Ansible을 통해 구성 자동화와 운영 검증 자동화를 수행하는 구조입니다.

현재까지는 생성된 인스턴스 기반으로 서비스 구성, 모니터링, 백업 및 복구 검증을 구현했습니다.

최종 목표는 OpenStack 인스턴스 생성부터 Ansible Playbook으로 연결하는 것이며,
이를 위해 ansible/provision.yml, wait-ssh.yml, validate.yml을 추가 보완 범위로 정리했습니다.
```

---

## 3. 핵심 질문

### Q1. 현재 프로젝트 방향이 주제에 적합한가?

```text
프로젝트 주제는 “Ansible 기반 클라우드 인프라 자동화 및 운영 최적화 시스템 구축”입니다.

현재 구성은 OpenStack 인프라, Ansible 구성 자동화, Docker Swarm 기반 Web, HAProxy, MariaDB, Prometheus / Grafana / Alertmanager, Restic 백업 및 복구 검증으로 구성되어 있습니다.

현재 방향이 주제에 적합한지 확인받고 싶습니다.
```

---

### Q2. Provisioning 자동화는 어느 수준까지 구현해야 하는가?

```text
최종 목표는 Control Node에서 Ansible Playbook을 실행하여 OpenStack 인스턴스 생성부터 서비스 구성까지 연결하는 것입니다.

현재 ansible/provision.yml 기준으로 Security Group, Instance, Cinder Volume, Volume Attach, SSH Wait 범위까지 최소 구현 골격을 작성했습니다.

남은 기간을 고려했을 때 이 정도 최소 구현과 실행 검증이면 충분한지,
아니면 Network / Subnet / Router 생성까지 포함해야 하는지 확인받고 싶습니다.
```

---

### Q3. site.yml은 어느 수준으로 완성해야 하는가?

```text
현재 ansible/site.yml은 nginx 예시 템플릿을 제거하고 최신 오케스트레이션 기준 파일로 정리했습니다.

최종 목표는 provision.yml → wait-ssh.yml → common → service → monitoring → backup → validate 흐름입니다.

멘토링 기준에서 site.yml은 실제 전체 import_playbook 구조로 완성해야 하는지,
아니면 현재처럼 baseline 실행과 개별 Playbook 검증 구조로 충분한지 확인받고 싶습니다.
```

---

### Q4. Docker Swarm 사용 범위가 적절한가?

```text
Web Node는 단일 Web Node 위 Docker Swarm 기반 서비스 구조로 재구성했습니다.

실습 환경과 남은 기간을 고려할 때 단일 노드 Swarm을 서비스 배포 구조로 설명해도 적절한지,
또는 Docker Compose 기반으로 단순화하는 것이 더 안전한지 확인받고 싶습니다.
```

---

### Q5. DB Replica는 핵심 구현인가, 확장 검증인가?

```text
DB는 MariaDB 기반으로 구성했고 Replica 이중화 검증을 진행 중입니다.

최종 발표에서 DB Replica를 핵심 구현으로 강조해야 할지,
아니면 확장 검증 항목으로 분리하는 것이 적절한지 확인받고 싶습니다.
```

---

### Q6. Monitoring은 어느 수준까지 증빙해야 하는가?

```text
Prometheus, node_exporter, cAdvisor, mysqld_exporter, blackbox_exporter, Grafana, Alertmanager는 설치했습니다.

최종 평가 기준에서 모든 Dashboard와 Alert Rule까지 완성해야 하는지,
또는 Prometheus Target UP, 대표 Dashboard, Alertmanager 접속 및 기본 Rule 정도면 충분한지 확인받고 싶습니다.
```

---

### Q7. Backup / Recovery는 캡처와 문서 중 어디에 집중해야 하는가?

```text
Restic 기반 Web / DB / Proxy 백업과 복구 테스트를 진행했고,
복구 시나리오 5종을 구성했습니다.

최종 평가에서 실제 복구 캡처와 복구 절차 문서 중 어느 쪽을 더 중점적으로 준비해야 하는지 확인받고 싶습니다.
```

---

### Q8. 남은 기간 우선순위가 적절한가?

```text
남은 기간 우선순위는 다음으로 잡고 있습니다.

1. README / 최신 문서 기준 통일
2. Provisioning 최소 구현 검증
3. site.yml / validate.yml 문법 및 실행 검증
4. Grafana / Alertmanager 설정 보완
5. Restic 복구 시나리오 문서화
6. 최종 발표자료와 캡처 정리

이 우선순위가 적절한지 확인받고 싶습니다.
```

---

## 4. 멘토에게 최종적으로 확인받을 결론

```text
1. 현재 프로젝트 범위가 과하지 않은지
2. Provisioning 자동화 최소 구현 범위가 적절한지
3. Docker Swarm / DB Replica / Monitoring / Backup 범위를 어떻게 발표해야 하는지
4. 남은 기간에는 구현 보완과 문서/증빙 중 어디에 더 집중해야 하는지
5. 최종 발표에서 가장 강조해야 할 평가 포인트가 무엇인지
```
