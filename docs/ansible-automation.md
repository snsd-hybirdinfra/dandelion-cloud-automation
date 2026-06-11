# Ansible Automation

## 1. Control Node Environment

| 항목 | 내용 |
|---|---|
| Ansible Version | TBD |
| Python Version | TBD |
| Inventory File | ansible/inventory.ini |
| Playbook File | ansible/site.yml |

## 2. Ansible Project Structure

~~~text
ansible/
├── ansible.cfg
├── inventory.ini
└── site.yml
~~~

## 3. Connection Test

~~~bash
ansible all -m ping
~~~

Expected Result:

~~~text
pong
~~~

## 4. Playbook Execution

~~~bash
ansible-playbook site.yml
~~~

## 5. Automation Scope

| 작업 | 자동화 여부 |
|---|---|
| apt cache update | Yes |
| basic package install | Yes |
| Docker install | Yes |
| Docker service start | Yes |
| Nginx container deploy | Yes |

## 6. Evidence

- ansible --version 캡처
- inventory.ini 캡처
- ansible.cfg 캡처
- site.yml 캡처
- ansible all -m ping 성공 캡처
- ansible-playbook 실행 성공 캡처
