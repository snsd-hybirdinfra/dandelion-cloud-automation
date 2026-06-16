<!-- STATUS: COMPLETE -->

# Ansible Automation

## 1. 문서 목적

본 문서는 Team Dandelion 프로젝트의 Ansible 자동화 기준을 정의한다.

본 프로젝트는 OpenStack 기반 Ubuntu 인스턴스 위에서 Control Node가 Ansible을 실행하고, Proxy Node, Web Node, DB Node, Backup / Validation Node를 역할별로 구성한다.

Phase 1에서는 Docker 설치, MariaDB 설치 및 구성, Custom WordPress 배포, HAProxy HTTP Reverse Proxy 배포를 자동화한다.

---

## 2. Phase 기반 자동화 전략

본 프로젝트는 Phase 기반 구현 로드맵을 사용한다.

~~~text
Phase 1: 필수 구성 및 기본 검증 단계
Phase 2: 운영 확장 및 검증 고도화 단계
Phase 3: 도전 확장 단계
Out of Scope: 제외 범위
~~~

Ansible 자동화 범위는 다음과 같이 구분한다.

| Phase | Automation Scope |
|---|---|
| Phase 1 | Docker 설치, DB Node MariaDB 설치 및 구성, Web Node WordPress 배포, Proxy Node HAProxy HTTP Reverse Proxy 배포 |
| Phase 2 | HTTPS, Cinder backup mount 지원, monitoring stack, backup/restore playbook화, roles 구조 분리 |
| Phase 3 | Web Node 2 추가, HAProxy backend 확장, roundrobin Load Balancing 검증 |

---

## 3. Ansible 실행 구조

## 3.1 Control Node 역할

Control Node는 Ansible 실행 서버이다.

~~~text
Control Node
├── ansible.cfg
├── inventory.ini
├── site.yml
└── playbooks or roles
~~~

Control Node는 SSH를 통해 각 노드에 접속하고, 역할별로 필요한 패키지와 컨테이너 구성을 적용한다.

---

## 3.2 Managed Node 역할

| Node | Ansible Role |
|---|---|
| Proxy Node | HAProxy HTTP Reverse Proxy 배포 |
| Web Node | Custom WordPress 컨테이너 배포 |
| DB Node | MariaDB 서비스 배포 |
| Backup / Validation Node | health_check.sh, backup.sh, restore 검증 지원 |

---

## 4. 권장 디렉터리 구조

Phase 1에서는 단일 `site.yml` 기반으로 시작한다.

~~~text
ansible/
├── ansible.cfg
├── inventory.ini
└── site.yml
~~~

Phase 2에서 시간이 남으면 roles 구조로 개선할 수 있다.

~~~text
ansible/
├── ansible.cfg
├── inventory.ini
├── site.yml
├── playbooks/
│   ├── backup.yml
│   └── validate.yml
└── roles/
    ├── docker/
    ├── proxy/
    ├── wordpress/
    ├── mariadb/
    ├── backup/
    └── monitoring/
~~~

Phase 1에서는 단일 `site.yml` 성공을 우선한다.

---

## 5. ansible.cfg 기준

예시 `ansible/ansible.cfg`:

~~~ini
[defaults]
inventory = inventory.ini
host_key_checking = False
remote_user = ubuntu
private_key_file = ~/.ssh/dandelion-key.pem
retry_files_enabled = False

[ssh_connection]
pipelining = True
~~~

실제 key 경로와 사용자명은 실습 환경에 맞게 수정한다.

---

## 6. inventory.ini 기준

예시 `ansible/inventory.ini`:

~~~ini
[control]
control-node ansible_host=CONTROL_NODE_IP

[proxy]
proxy-node ansible_host=PROXY_NODE_IP

[web]
web-node ansible_host=WEB_NODE_IP

[db]
db-node ansible_host=DB_NODE_IP

[backup]
backup-node ansible_host=BACKUP_NODE_IP

[managed:children]
proxy
web
db
backup

[all:vars]
ansible_user=ubuntu
ansible_ssh_private_key_file=~/.ssh/dandelion-key.pem
~~~

Phase 3에서 Web Node 2를 추가할 경우 다음과 같이 확장한다.

~~~ini
[web]
web-node-1 ansible_host=WEB_NODE_1_IP
web-node-2 ansible_host=WEB_NODE_2_IP
~~~

---

## 7. Phase 1 site.yml 자동화 범위

Phase 1의 `site.yml`은 다음 순서로 구성한다.

~~~text
1. 공통 패키지 설치
2. Docker 설치
3. Docker Compose 사용 가능 여부 확인
4. DB Node에 MariaDB 직접 설치
5. Web Node에 Custom WordPress 배포
6. Proxy Node에 HAProxy HTTP Reverse Proxy 배포
7. Backup / Validation Node에 health_check.sh, backup.sh 배치
8. 기본 검증 명령 실행 또는 안내
~~~

---

## 8. Phase 1 Playbook 예시 구조

예시 `ansible/site.yml` 흐름:

~~~yaml
- name: Install Docker on managed nodes
  hosts: proxy:web:db
  become: true
  tasks:
    - name: Update apt cache
      apt:
        update_cache: true

    - name: Install required packages
      apt:
        name:
          - docker.io
          - docker-compose-plugin
        state: present

    - name: Enable docker service
      service:
        name: docker
        state: started
        enabled: true

- name: Deploy MariaDB on DB Node
  hosts: db
  become: true
  tasks:
    - name: Create DB compose directory
      file:
        path: /opt/dandelion/db
        state: directory
        mode: "0755"

    - name: Copy DB compose file
      copy:
        src: ../docker/compose/db/docker-compose.yml
        dest: /opt/dandelion/db/docker-compose.yml

    - name: Start MariaDB
      command: docker compose up -d
      args:
        chdir: /opt/dandelion/db

- name: Deploy WordPress on Web Node
  hosts: web
  become: true
  tasks:
    - name: Create WordPress compose directory
      file:
        path: /opt/dandelion/web
        state: directory
        mode: "0755"

    - name: Copy WordPress compose files
      copy:
        src: ../docker/
        dest: /opt/dandelion/docker/

    - name: Start WordPress
      command: docker compose up -d
      args:
        chdir: /opt/dandelion/docker/compose/web

- name: Deploy HAProxy on Proxy Node
  hosts: proxy
  become: true
  tasks:
    - name: Create proxy compose directory
      file:
        path: /opt/dandelion/proxy
        state: directory
        mode: "0755"

    - name: Copy HAProxy compose files
      copy:
        src: ../docker/proxy/
        dest: /opt/dandelion/proxy/

    - name: Start HAProxy
      command: docker compose up -d
      args:
        chdir: /opt/dandelion/proxy
~~~

위 예시는 구조 설명용이며, 실제 경로와 변수는 repository 구조에 맞게 조정한다.

---

## 9. 변수 관리 기준

Phase 1에서는 복잡한 변수 구조보다 명확한 inventory와 compose 파일을 우선한다.

권장 변수:

| Variable | Description |
|---|---|
| DB_NODE_PRIVATE_IP | DB Node 내부 IP |
| WEB_NODE_PRIVATE_IP | Web Node 내부 IP |
| PROXY_NODE_PRIVATE_IP | Proxy Node 내부 IP |
| WORDPRESS_DB_NAME | WordPress DB 이름 |
| WORDPRESS_DB_USER | WordPress DB 사용자 |
| WORDPRESS_DB_PASSWORD | WordPress DB 비밀번호 |
| MYSQL_ROOT_PASSWORD | MariaDB root 비밀번호 |

비밀번호는 발표자료나 공개 문서에 실제 값 그대로 노출하지 않는다.

---

## 10. Ansible 실행 명령어

Ansible 설정 확인:

~~~bash
cd ansible
ansible --version
ansible-inventory --list
~~~

Ping 테스트:

~~~bash
ansible all -m ping
~~~

Playbook 문법 확인:

~~~bash
ansible-playbook site.yml --syntax-check
~~~

Playbook 실행:

~~~bash
ansible-playbook site.yml
~~~

특정 그룹만 확인:

~~~bash
ansible proxy -m ping
ansible web -m ping
ansible db -m ping
ansible backup -m ping
~~~

---

## 11. Phase 1 검증 기준

| 검증 항목 | 명령어 | 성공 기준 |
|---|---|---|
| Inventory 확인 | ansible-inventory --list | proxy / web / db / backup 그룹 표시 |
| SSH 연결 | ansible all -m ping | 모든 managed node SUCCESS |
| Docker 설치 | ansible managed -a "docker --version" | Docker version 출력 |
| Compose 확인 | ansible managed -a "docker compose version" | Docker Compose version 출력 |
| Proxy 컨테이너 | ansible proxy -a "docker ps" | dandelion-haproxy running |
| Web 컨테이너 | ansible web -a "docker ps" | dandelion-wordpress running |
| DB 컨테이너 | ansible db -a "docker ps" | mariadb service active |
| HTTP 접속 | curl -I http://PROXY_NODE_IP | HTTP 응답 확인 |
| DB 포트 | ansible web -a "nc -zv DB_NODE_IP 3306" | DB 연결 성공 |

---

## 12. Backup / Validation Node 자동화 기준

Phase 1에서는 Backup / Validation Node에 health_check.sh와 backup.sh를 배치하고 수동 또는 반자동으로 실행한다.

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

Phase 1에서 필수로 확인할 항목:

| 항목 | 기준 |
|---|---|
| health_check.sh | Proxy / Web / DB 상태 확인 |
| backup.sh | mysqldump 기반 MariaDB dump 및 WordPress files archive 생성 |
| restore.md | 복구 절차 문서화 및 검증 |

---

## 13. Phase 2 자동화 개선

Phase 2에서는 다음 자동화 개선을 시도할 수 있다.

| 항목 | 설명 |
|---|---|
| backup.yml | backup.sh 실행을 Ansible Playbook으로 관리 |
| validate.yml | health check와 결과 검증을 Playbook으로 관리 |
| roles/docker | Docker 설치 역할 분리 |
| roles/proxy | HAProxy 구성 역할 분리 |
| roles/wordpress | WordPress 구성 역할 분리 |
| roles/mariadb | MariaDB 구성 역할 분리 |
| roles/backup | 백업 스크립트 배치 및 실행 역할 분리 |
| roles/monitoring | Prometheus/Grafana 구성 역할 분리 |

Phase 2는 Phase 1이 안정적으로 완료된 이후 진행한다.

---

## 14. Phase 3 자동화 확장

Phase 3에서는 Web Node 2를 추가하고 HAProxy backend를 2개로 확장할 수 있다.

~~~text
[web]
web-node-1
web-node-2
~~~

HAProxy backend 예시:

~~~text
backend wordpress_backend
    balance roundrobin
    option httpchk GET /
    server web1 WEB_NODE_1_PRIVATE_IP:80 check
    server web2 WEB_NODE_2_PRIVATE_IP:80 check
~~~

Phase 3 검증 항목:

| 항목 | 기준 |
|---|---|
| Web Node 2 Ansible ping | SUCCESS |
| Web Node 2 WordPress 배포 | 컨테이너 running |
| HAProxy backend 2개 | web1 / web2 등록 |
| Round Robin | Web-1 / Web-2 응답 분산 |
| 공통 DB | 두 Web Node가 동일 DB Node 연결 |
| 장애 테스트 | Web-1 중지 시 Web-2 응답 |

---

## 15. 제외 범위

다음 항목은 Ansible 자동화 범위에서 제외한다.

~~~text
OpenStack 전체 자동 구축
Kolla-Ansible 기반 OpenStack 재구축
OpenStack LBaaS / Octavia 자동화
DB Replication 자동화
DB Clustering 자동화
Kubernetes 배포 자동화
Docker Swarm 배포 자동화
WordPress files 자동 동기화
운영 수준 CI/CD 배포 자동화
~~~

OpenStack CLI + Ansible End-to-End 자동화는 Phase 3 후순위 추가 도전으로만 검토한다.

---

## 16. 필수 캡처 기준

| 영역 | 캡처 항목 |
|---|---|
| Ansible | ansible --version |
| Inventory | ansible-inventory --list |
| Ping | ansible all -m ping |
| Syntax | ansible-playbook site.yml --syntax-check |
| Playbook | ansible-playbook site.yml 실행 결과 |
| Proxy | HAProxy 컨테이너 상태 |
| Web | WordPress 컨테이너 상태 |
| DB | MariaDB 서비스 상태 |
| HTTP | Proxy Node 경유 WordPress 접속 결과 |
| DB 연결 | Web Node에서 DB Node 3306 연결 결과 |
| Backup | backup.sh 실행 결과 |

---

## 17. 핵심 자동화 메시지

~~~text
본 프로젝트의 Ansible 자동화는 단순 패키지 설치가 아니라,
Control Node에서 Proxy Node, Web Node, DB Node, Backup / Validation Node를 역할별로 제어하는 구조이다.

Phase 1에서는 Docker 설치, MariaDB 설치 및 구성, Custom WordPress 배포, HAProxy HTTP Reverse Proxy 배포를 자동화한다.

Phase 2에서는 backup/restore playbook화와 roles 구조 분리를 통해 자동화 품질을 개선한다.

Phase 3에서는 Web Node 2대와 HAProxy Load Balancing을 자동화 확장 대상으로 검토한다.
~~~

<<<<<<< HEAD
<!-- AUTO_IMAGES_START -->
## 자동 반영 이미지

아래 이미지는 screenshots/ 폴더에 파일이 업로드되면 자동으로 표시된다.

### Ansible Version

../screenshots/ansible/ansible-version.png 이미지가 아직 업로드되지 않았다.

### Inventory Configuration

../screenshots/ansible/inventory.png 이미지가 아직 업로드되지 않았다.

### Ping Test Result

../screenshots/ansible/ping-test.png 이미지가 아직 업로드되지 않았다.

### Playbook Execution Result

../screenshots/ansible/playbook-result.png 이미지가 아직 업로드되지 않았다.

### WordPress/MariaDB Deployment Result

../screenshots/ansible/wordpress-deploy-result.png 이미지가 아직 업로드되지 않았다.
<!-- AUTO_IMAGES_END -->
=======
>>>>>>> 6912a81 (Correct MariaDB architecture to host installed service)
