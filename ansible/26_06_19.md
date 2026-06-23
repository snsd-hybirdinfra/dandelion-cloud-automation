<!-- STATUS: COMPLETE -->

# Phase 1 Ansible 기본 구성 및 common.yml 작성 정리

## 1. 문서 목적

OpenStack 기반 Team Dandelion 프로젝트에서 Control Node를 이용하여 관리 대상 노드를 Ansible로 통합 관리하기 위한 기본 구성을 정리한다.

본 문서는 다음 작업까지 포함한다.

```text
Ansible 설치
→ Ansible 작업 디렉터리 생성
→ ansible.cfg 작성
→ inventory.ini 작성
→ Ansible Ping 및 sudo 권한 검증
→ site.yml 작성
→ playbooks/common.yml 작성
→ common.yml 문법 검사
```

현재 `common.yml`은 작성 및 문법 검사까지 완료하였으며, 다른 팀원이 각 노드에서 패키지 설치 작업을 진행 중이므로 실제 실행은 보류한 상태이다.

---

## 2. 구성 환경

### 2.1 인스턴스 구성

| 인스턴스 | 역할 | 내부 IP | 외부 접속 IP | 이미지 |
|---|---|---:|---:|---|
| control | Ansible Control Node | 192.168.4.89 | 172.16.8.164 | Ubuntu 24.04 |
| proxy | HAProxy Node | 192.168.4.32 | 172.16.8.169 | Ubuntu 24.04 |
| web1 | WordPress Web Node 1 | 192.168.4.4 | 없음 | Ubuntu 24.04 |
| web2 | WordPress Web Node 2 | 192.168.4.35 | 없음 | Ubuntu 24.04 |
| db | MariaDB DB Node | 192.168.4.201 | 없음 | Ubuntu 24.04 |
| backup | Backup / Validation Node | 192.168.4.134 | 없음 | Ubuntu 24.04 |
| monitoring | Monitoring Node | 192.168.4.179 | 없음 | Ubuntu 24.04 |

### 2.2 Ansible 작업 정보

| 항목 | 설정값 |
|---|---|
| Ansible 실행 노드 | Control Node |
| 원격 접속 사용자 | `ubuntu` |
| SSH 개인키 | `~/.ssh/dandelion.pem` |
| 프로젝트 디렉터리 | `~/dandeliondir` |
| Ansible 디렉터리 | `~/dandeliondir/ansible` |
| Inventory 파일 | `~/dandeliondir/ansible/inventory.ini` |
| Ansible 설정 파일 | `~/dandeliondir/ansible/ansible.cfg` |
| 전체 Playbook 진입점 | `~/dandeliondir/ansible/site.yml` |
| 공통 환경 Playbook | `~/dandeliondir/ansible/playbooks/common.yml` |

---

## 3. Ansible 설치

Control Node에서 패키지 목록을 갱신하고 Ansible을 설치하였다.

```bash
sudo apt update
sudo apt install -y ansible
```

설치 결과는 다음 명령으로 확인하였다.

```bash
ansible --version
which ansible
```

확인 항목:

- Ansible 버전 정상 출력
- Ansible 실행 파일 경로 `/usr/bin/ansible` 확인
- 현재 프로젝트의 `ansible.cfg` 인식 여부 확인

---

## 4. Ansible 작업 디렉터리 생성

프로젝트 디렉터리 아래에 Ansible 작업 디렉터리를 생성하였다.

```bash
mkdir -p ~/dandeliondir/ansible
cd ~/dandeliondir/ansible
```

현재 위치를 확인하였다.

```bash
pwd
```

확인 경로:

```text
/home/ubuntu/dandeliondir/ansible
```

Playbook 파일을 저장할 디렉터리도 생성하였다.

```bash
mkdir -p ~/dandeliondir/ansible/playbooks
```

---

## 5. ansible.cfg 작성

파일 위치:

```text
~/dandeliondir/ansible/ansible.cfg
```

작성 내용:

```ini
[defaults]
inventory = ./inventory.ini
host_key_checking = False
remote_user = ubuntu
private_key_file = ~/.ssh/dandelion.pem
retry_files_enabled = False
interpreter_python = auto_silent

[privilege_escalation]
become = True
become_method = sudo
become_user = root

[ssh_connection]
pipelining = True
```

### 주요 설정 설명

| 설정 | 설명 |
|---|---|
| `inventory` | 기본 Inventory 파일로 `inventory.ini` 사용 |
| `host_key_checking` | 최초 SSH 접속 시 호스트 키 확인 질문 비활성화 |
| `remote_user` | 관리 노드 SSH 접속 계정을 `ubuntu`로 지정 |
| `private_key_file` | SSH 개인키 경로 지정 |
| `retry_files_enabled` | 실패 시 `.retry` 파일 생성을 비활성화 |
| `interpreter_python` | 관리 노드의 Python 인터프리터를 자동 탐색 |
| `become` | sudo 권한 상승 사용 |
| `become_user` | 권한 상승 대상 사용자를 `root`로 지정 |
| `pipelining` | SSH 통신 횟수를 줄여 실행 성능 개선 |

SSH 개인키 권한은 다음과 같이 설정하였다.

```bash
chmod 600 ~/.ssh/dandelion.pem
```

설정 적용 여부는 다음 명령으로 확인하였다.

```bash
ansible --version
ansible-config view
```

---

## 6. inventory.ini 작성

파일 위치:

```text
~/dandeliondir/ansible/inventory.ini
```

작성 내용:

```ini
[proxy]
proxy-node ansible_host=192.168.4.32

[web]
web1-node ansible_host=192.168.4.4
web2-node ansible_host=192.168.4.35

[db]
db-node ansible_host=192.168.4.201

[backup]
backup-node ansible_host=192.168.4.134

[monitoring]
monitoring-node ansible_host=192.168.4.179

[managed:children]
proxy
web
db
backup
monitoring
```

### 그룹 구성

| 그룹 | 노드 | 역할 |
|---|---|---|
| `proxy` | proxy-node | HAProxy |
| `web` | web1-node, web2-node | WordPress Web 서비스 |
| `db` | db-node | MariaDB |
| `backup` | backup-node | 백업 및 복구 검증 |
| `monitoring` | monitoring-node | 모니터링 |
| `managed` | 위 그룹 전체 | 모든 Ansible 관리 대상 |

Inventory 구조는 다음 명령으로 확인하였다.

```bash
ansible-inventory --graph
ansible-inventory --list
```

이후 전체 관리 노드를 대상으로 하는 Playbook에는 다음 그룹명을 사용한다.

```yaml
hosts: managed
```

`managed_nodes`는 현재 Inventory에 존재하지 않으므로 사용하지 않는다.

---

## 7. Ansible 접속 검증

모든 관리 대상 노드에 Ansible Ping을 실행하였다.

```bash
ansible managed -m ping
```

확인 결과:

```text
proxy-node      | SUCCESS => ping: pong
web1-node       | SUCCESS => ping: pong
web2-node       | SUCCESS => ping: pong
db-node         | SUCCESS => ping: pong
backup-node     | SUCCESS => ping: pong
monitoring-node | SUCCESS => ping: pong
```

이를 통해 다음 항목을 검증하였다.

- Control Node에서 관리 노드로 SSH 접속 가능
- SSH 개인키 인증 정상
- 관리 노드에서 Python 실행 가능
- Ansible 모듈 실행 가능
- 실행 결과 반환 정상

---

## 8. sudo 권한 상승 검증

관리 노드에서 Ansible이 비밀번호 없이 root 권한을 사용할 수 있는지 확인하였다.

```bash
ansible managed -m command -a "whoami" --become
```

모든 노드에서 다음 결과가 출력되었다.

```text
root
```

따라서 다음 설정이 정상적으로 동작함을 확인하였다.

- `ubuntu` 사용자의 비밀번호 없는 sudo 권한
- `ansible.cfg`의 privilege escalation 설정
- 관리 노드에서 root 권한 명령 실행

---

## 9. site.yml 작성

파일 위치:

```text
~/dandeliondir/ansible/site.yml
```

작성 내용:

```yaml
---
# Phase 1 전체 자동화 실행 진입점

- name: 모든 노드 공통 환경 구성 실행
  import_playbook: playbooks/common.yml

- name: Docker 설치 자동화 실행
  import_playbook: playbooks/docker.yml

- name: MariaDB 서비스 구성 실행
  import_playbook: playbooks/database.yml

- name: Custom WordPress 배포 실행
  import_playbook: playbooks/wordpress.yml

- name: HAProxy Reverse Proxy 구성 실행
  import_playbook: playbooks/proxy.yml

- name: 백업 및 검증 환경 구성 실행
  import_playbook: playbooks/backup.yml
```

실행 순서:

```text
common.yml
→ docker.yml
→ database.yml
→ wordpress.yml
→ proxy.yml
→ backup.yml
```

현재 `common.yml` 외 나머지 개별 Playbook은 아직 작성 중이므로 전체 `site.yml`은 아직 실행하지 않는다.

---

## 10. common.yml 작성

파일 위치:

```text
~/dandeliondir/ansible/playbooks/common.yml
```

최종 작성 내용:

```yaml
---
- name: 모든 관리 노드 공통 환경 구성
  hosts: managed
  become: true
  gather_facts: true

  tasks:
    - name: APT 패키지 캐시 갱신
      ansible.builtin.apt:
        update_cache: true
        cache_valid_time: 3600

    - name: 공통 관리 패키지 설치
      ansible.builtin.apt:
        name:
          - curl
          - wget
          - git
          - vim
          - unzip
          - ca-certificates
          - gnupg
          - lsb-release
          - jq
          - net-tools
        state: present
```

### common.yml 역할

`common.yml`은 모든 관리 대상 노드의 기본 환경을 동일하게 맞추는 Playbook이다.

실행 대상:

```text
proxy-node
web1-node
web2-node
db-node
backup-node
monitoring-node
```

적용 작업:

1. APT 패키지 캐시 갱신
2. 공통 관리 패키지 설치 여부 확인
3. 설치되지 않은 패키지만 설치

---

## 11. common.yml 주요 설정 설명

### `hosts: managed`

Inventory의 `[managed:children]`에 포함된 모든 그룹을 실행 대상으로 지정한다. Control Node는 실행 대상이 아니다.

### `become: true`

APT 패키지 관리에는 root 권한이 필요하므로 관리 노드에서 sudo 권한을 사용한다.

### `gather_facts: true`

Playbook 실행 전에 관리 노드의 운영체제, IP, CPU, 메모리, Python 경로 등의 정보를 수집한다.

### APT 캐시 갱신

```yaml
ansible.builtin.apt:
  update_cache: true
  cache_valid_time: 3600
```

수동 명령의 다음 작업과 유사하다.

```bash
sudo apt update
```

`cache_valid_time: 3600`은 최근 1시간 안에 APT 캐시가 갱신되었다면 다시 갱신하지 않도록 한다.

### 공통 패키지 설치

```yaml
state: present
```

각 패키지가 설치된 상태인지를 보장한다.

```text
패키지가 없으면 설치
패키지가 이미 있으면 유지
강제 재설치하지 않음
자동 업그레이드하지 않음
기존 설정 파일을 초기화하지 않음
```

따라서 이미 패키지가 설치된 노드에서 실행해도 문제가 없다.

### 설치 패키지 용도

| 패키지 | 용도 |
|---|---|
| `curl` | HTTP 요청 및 Health Check |
| `wget` | 파일 다운로드 |
| `git` | GitHub 저장소 및 버전 관리 |
| `vim` | 서버 설정 파일 편집 |
| `unzip` | ZIP 파일 압축 해제 |
| `ca-certificates` | HTTPS 인증서 검증 |
| `gnupg` | 외부 저장소 GPG 키 검증 |
| `lsb-release` | Ubuntu 배포판 정보 확인 |
| `jq` | JSON 데이터 처리 |
| `net-tools` | `netstat`, `ifconfig` 등 네트워크 점검 |

---

## 12. 공통 작업 디렉터리를 제외한 이유

처음에는 모든 관리 노드에 `/opt/dandelion`을 만드는 Task를 검토했지만, 모든 노드가 해당 경로를 공통으로 사용할 필요가 확정되지 않아 제외하였다.

필요한 경우 이후 역할별 Playbook에서 필요한 노드에만 디렉터리를 생성한다.

```text
wordpress.yml → Web 노드에 WordPress 작업 디렉터리 생성
proxy.yml     → Proxy 노드에 HAProxy 설정 디렉터리 생성
backup.yml    → Backup 노드에 백업 저장 디렉터리 생성
```

이 방식이 불필요한 빈 디렉터리 생성을 줄이고 역할별 책임을 명확하게 한다.

---

## 13. common.yml 문법 검사

처음에는 다음 위치에서 문법 검사를 실행하였다.

```text
~/dandeliondir/ansible/playbooks
```

실행 명령:

```bash
ansible-playbook --syntax-check common.yml
```

출력:

```text
[WARNING]: No inventory was parsed, only implicit localhost is available
[WARNING]: provided hosts list is empty, only localhost is available
[WARNING]: Could not match supplied host pattern, ignoring: managed

playbook: common.yml
```

### 경고 원인

`ansible.cfg`와 `inventory.ini`는 상위 디렉터리에 존재한다.

```text
~/dandeliondir/ansible/
├── ansible.cfg
├── inventory.ini
└── playbooks/
    └── common.yml
```

`playbooks` 디렉터리에서 실행하여 상위 디렉터리의 프로젝트 설정을 자동으로 읽지 못했기 때문에 Inventory 및 `managed` 그룹 관련 경고가 발생하였다.

YAML 문법 자체는 마지막에 다음이 출력되었으므로 정상이다.

```text
playbook: common.yml
```

### 올바른 문법 검사 위치

Ansible 기본 디렉터리로 이동하여 실행하였다.

```bash
cd ~/dandeliondir/ansible
ansible-playbook --syntax-check playbooks/common.yml
```

정상 결과:

```text
playbook: playbooks/common.yml
```

앞으로 Ansible 명령은 기본적으로 다음 위치에서 실행한다.

```text
/home/ubuntu/dandeliondir/ansible
```

---

## 14. 실제 실행 보류 사유

현재 다른 팀원이 각 노드에서 패키지 설치 작업을 진행 중이다.

동시에 APT 관련 작업을 실행하면 다음과 같은 잠금 충돌이 발생할 수 있다.

```text
Could not get lock /var/lib/dpkg/lock-frontend
```

따라서 현재는 다음 작업까지만 완료하였다.

| 항목 | 상태 |
|---|---|
| common.yml 작성 | 완료 |
| YAML 및 Playbook 문법 검사 | 완료 |
| Inventory 그룹 인식 확인 | 완료 |
| 실제 한 노드 시험 실행 | 보류 |
| 전체 managed 그룹 실행 | 보류 |
| 멱등성 재실행 검증 | 보류 |

---

## 15. 향후 실행 절차

### 15.1 한 노드 시험 실행

```bash
cd ~/dandeliondir/ansible
ansible-playbook playbooks/common.yml --limit web1-node
```

확인 기준:

```text
unreachable=0
failed=0
```

### 15.2 전체 노드 실행

```bash
ansible-playbook playbooks/common.yml
```

### 15.3 멱등성 확인

같은 Playbook을 다시 실행한다.

```bash
ansible-playbook playbooks/common.yml
```

이미 모든 패키지가 설치되어 있다면 다음과 같은 결과가 예상된다.

```text
changed=0
unreachable=0
failed=0
```

APT 캐시 상태에 따라 일부 Task는 `changed`로 표시될 수 있다.

---

## 16. 현재 디렉터리 구조

```text
dandeliondir/
└── ansible/
    ├── ansible.cfg
    ├── inventory.ini
    ├── site.yml
    └── playbooks/
        └── common.yml
```

이후 다음 파일을 순차적으로 작성한다.

```text
playbooks/
├── common.yml
├── docker.yml
├── database.yml
├── wordpress.yml
├── proxy.yml
└── backup.yml
```

---

## 17. 현재 작업 결과

| 점검 항목 | 결과 |
|---|---|
| Control Node Ansible 설치 | 성공 |
| SSH 개인키 설정 | 성공 |
| ansible.cfg 작성 및 인식 | 성공 |
| inventory.ini 작성 | 성공 |
| Inventory 그룹 구성 | 성공 |
| 관리 노드 Ansible Ping | 성공 |
| sudo 권한 상승 확인 | 성공 |
| site.yml 작성 | 성공 |
| common.yml 작성 | 성공 |
| common.yml 문법 검사 | 성공 |
| common.yml 실제 실행 | 보류 |

---

## 18. 다음 단계

다음 단계에서는 Web 노드에 Docker Engine과 Docker Compose Plugin을 설치하기 위한 `playbooks/docker.yml`을 작성한다.

현재 팀 결정에 따른 서비스 설치 방식:

```text
Web Node
→ Docker Engine 설치
→ Custom WordPress 컨테이너 구성

Proxy Node
→ Docker 컨테이너를 사용하지 않음
→ HAProxy 패키지를 직접 설치

DB Node
→ MariaDB를 직접 설치
```

따라서 `docker.yml`의 실행 대상은 Inventory의 `web` 그룹으로 지정한다.

```yaml
hosts: web
```
