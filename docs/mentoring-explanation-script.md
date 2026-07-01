<!-- STATUS: CURRENT -->

# Mentoring Explanation Script

## 1. 문서 목적

본 문서는 멘토링 당일 프로젝트 설명 흐름을 정리한다.

멘토링 시간에는 모든 문서를 길게 설명하지 않고, 다음 순서로 간결하게 설명한다.

```text
프로젝트 목표
→ 현재 구조
→ 구현 완료 범위
→ 진행 중 범위
→ 남은 이슈
→ 멘토에게 확인받을 질문
```

---

## 2. 시작 설명

```text
안녕하세요. Team Dandelion 프로젝트는
“Ansible 기반 클라우드 인프라 자동화 및 운영 최적화 시스템 구축”을 주제로 진행하고 있습니다.

OpenStack 기반 인프라 위에 Web, DB, Proxy, Monitoring, Backup / Recovery 구성 요소를 배치하고,
Control Node에서 Ansible Playbook을 실행하여 구성 자동화와 운영 검증 자동화를 수행하는 구조입니다.
```

---

## 3. 최종 목표 설명

```text
최종 목표는 Control Node에서 Ansible Playbook을 실행하여
OpenStack 인스턴스 생성부터 서비스 구성, 모니터링, 백업 및 복구 검증까지 연결하는 것입니다.

실행 흐름은 다음과 같이 잡았습니다.

Control Node
→ OpenStack Provisioning
→ SSH Wait
→ Inventory 구성
→ 공통 환경 설정
→ Web / DB / Proxy 구성
→ Monitoring 구성
→ Restic 백업
→ 복구 검증
→ 운영 상태 검증
```

---

## 4. 현재 구현 상태 설명

```text
현재까지는 생성된 OpenStack 인스턴스를 기반으로
서비스 구성, 모니터링, 백업 및 복구 검증 자동화를 우선 구현했습니다.

Web 영역은 단일 Web Node 위 Docker Swarm 기반으로 재구성했고,
Proxy는 HAProxy 기반으로 구성했습니다.

DB는 MariaDB 기반으로 구성했으며 Replica 검증을 진행 중입니다.

Monitoring은 Prometheus, node_exporter, cAdvisor, mysqld_exporter, blackbox_exporter, Grafana, Alertmanager를 설치했고,
Grafana와 Alertmanager 세부 설정을 진행 중입니다.

Backup / Recovery는 Restic 기반으로 Web / DB / Proxy 백업과 복구 테스트를 진행했고,
복구 시나리오 5종을 문서화하고 있습니다.
```

---

## 5. Ansible 자동화 설명

```text
Ansible은 Control Node에서 실행하는 구조입니다.

최종 목표는 ansible-playbook -i inventory.ini site.yml 명령으로 전체 흐름을 실행하는 것입니다.

현재 site.yml은 기존 nginx 예시 템플릿을 제거하고,
현재 아키텍처에 맞는 오케스트레이션 기준 파일로 정리했습니다.

추가로 ansible/provision.yml, wait-ssh.yml, validate.yml을 만들어서
Provisioning, SSH 준비 확인, 운영 검증 흐름을 분리했습니다.
```

---

## 6. Provisioning 보완 설명

```text
Provisioning 자동화는 프로젝트 주제인 “클라우드 인프라 자동화”를 직접 증명하는 범위라고 보고 있습니다.

그래서 ansible/provision.yml 기준으로
Security Group 생성, Instance 생성, Cinder Volume 생성, Volume Attach, SSH Wait까지 최소 구현 범위로 잡았습니다.

다만 실제 OpenStack 환경의 image, flavor, network, key_name 값이 필요하기 때문에
ansible/vars/provisioning.yml에서 환경 값을 분리했고,
멘토링 이후 실제 환경 값 반영과 실행 검증을 진행하려고 합니다.
```

---

## 7. 문서 정리 설명

```text
기존 문서에는 작업 당시 기준의 구조가 남아 있어서,
최신 기준 문서와 과거 기록 문서를 분리했습니다.

최신 기준은 README, docs/current-status.md, docs/architecture.md,
docs/automation-scope.md, docs/ansible-execution-design.md,
docs/provisioning-playbook-design.md를 기준으로 잡았습니다.

과거 회의록과 작업일지는 당시 진행 기록으로 보존하고,
최신 구조와 충돌하지 않도록 document-cleanup-policy.md에서 기준을 정리했습니다.
```

---

## 8. 남은 작업 설명

```text
남은 작업은 기능을 무리하게 확장하기보다
최종 목표와 현재 구현 사이의 연결성을 강화하는 방향으로 잡았습니다.

우선순위는 다음과 같습니다.

1. Provisioning 최소 구현 실행 검증
2. site.yml / validate.yml 문법 및 실행 검증
3. Grafana / Alertmanager 설정 보완
4. DB Replica 검증 결과 정리
5. Restic 복구 시나리오 5종 문서화
6. 최종 발표자료와 캡처 정리
```

---

## 9. 멘토에게 물어볼 질문 연결

```text
오늘 멘토링에서는 크게 세 가지를 확인받고 싶습니다.

첫째, 현재 프로젝트 범위가 주제에 적합한지입니다.

둘째, 남은 기간에 OpenStack Provisioning 자동화를 어느 수준까지 구현해야 하는지입니다.

셋째, Docker Swarm, DB Replica, Monitoring, Backup / Recovery 중 최종 발표에서 무엇을 핵심으로 강조하고 무엇을 확장 검증으로 분리하는 것이 좋은지입니다.
```

---

## 10. 짧은 버전

시간이 부족하면 다음처럼 설명한다.

```text
저희 프로젝트는 OpenStack 위에 Web, DB, Proxy, Monitoring, Backup / Recovery 구조를 만들고,
Control Node에서 Ansible로 구성 자동화와 운영 검증 자동화를 수행하는 프로젝트입니다.

현재는 생성된 인스턴스 기반의 서비스 구성, 모니터링, 백업 및 복구 검증을 구현했고,
최종 목표인 인스턴스 생성 자동화를 위해 provision.yml을 별도 보완 범위로 작성했습니다.

멘토링에서는 Provisioning 자동화 최소 범위가 적절한지,
그리고 남은 기간에 구현과 문서/증빙 중 어디에 집중하는 것이 좋은지 확인받고 싶습니다.
```
