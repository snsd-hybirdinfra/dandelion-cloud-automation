<!-- STATUS: TEMPLATE -->
# TEMP: 팀원 실제 작업 결과 반영 필요

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

## 7. Screenshots

### 7.1 Ansible Version

이미지 파일 위치:

~~~text
screenshots/ansible/ansible-version.png
~~~

### 7.2 Inventory Configuration

이미지 파일 위치:

~~~text
screenshots/ansible/inventory.png
~~~

### 7.3 Ping Test Result

이미지 파일 위치:

~~~text
screenshots/ansible/ping-test.png
~~~

### 7.4 Playbook Execution Result

이미지 파일 위치:

~~~text
screenshots/ansible/playbook-result.png
~~~

### 7.5 Nginx Deployment Result

이미지 파일 위치:

~~~text
screenshots/ansible/nginx-deploy-result.png
~~~

## 8. 담당자 제출 체크리스트

| 항목 | 완료 여부 |
|---|---|
| Ansible 버전 캡처 | TBD |
| inventory.ini 작성 | TBD |
| ansible.cfg 작성 | TBD |
| site.yml 작성 | TBD |
| ansible all -m ping 성공 캡처 | TBD |
| ansible-playbook 실행 성공 캡처 | TBD |

## 7. Screenshots

### 7.1 Ansible Version

이미지 파일 위치:

~~~text
screenshots/ansible/ansible-version.png
~~~

### 7.2 Inventory Configuration

이미지 파일 위치:

~~~text
screenshots/ansible/inventory.png
~~~

### 7.3 Ping Test Result

이미지 파일 위치:

~~~text
screenshots/ansible/ping-test.png
~~~

### 7.4 Playbook Execution Result

이미지 파일 위치:

~~~text
screenshots/ansible/playbook-result.png
~~~

### 7.5 Nginx Deployment Result

이미지 파일 위치:

~~~text
screenshots/ansible/nginx-deploy-result.png
~~~

## 8. 담당자 제출 체크리스트

| 항목 | 완료 여부 |
|---|---|
| Ansible 버전 캡처 | TBD |
| inventory.ini 작성 | TBD |
| ansible.cfg 작성 | TBD |
| site.yml 작성 | TBD |
| ansible all -m ping 성공 캡처 | TBD |
| ansible-playbook 실행 성공 캡처 | TBD |

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

### Nginx Deployment Result

../screenshots/ansible/nginx-deploy-result.png 이미지가 아직 업로드되지 않았다.
<!-- AUTO_IMAGES_END -->
