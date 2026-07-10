# 설치
```bash
sudo apt install python3-pip
apt install python3.12-venv
```
`requirements.txt`
```bash
fastapi
uvicorn
paramiko
```
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```


`app.py`
```python
from fastapi import FastAPI, Request
from recover import handle

app = FastAPI()

from fastapi import FastAPI, Body

app = FastAPI()

@app.post("/recover")
def recover(payload: dict = Body(...)):
    for alert in payload["alerts"]:
        handle(alert["labels"]["alertname"])

    return {"status": "ok"}
```

`recover.py`
```python
from ssh import recover_db, recover_web


def handle(alertname):

    if alertname == "WebContainerDown":
        recover_web()

    elif alertname == "WordPressDBMissing":
        recover_db()

    elif alertname == "WebContainerMemoryHigh":
        print("Scale Out")
```

`ssh.py`
```python
import subprocess

def recover_web():
    subprocess.Popen([
        'ssh',
        '-i',
        '/home/ubuntu/.ssh/dandelion.pem',
        '-o', 'StrictHostKeyChecking=no',
        '-o', 'UserKnownHostsFile=/dev/null',
        'ubuntu@web1',
        'cd /home/ubuntu/wordpress; docker stack deploy -c docker-compose.yml dandelion-wordpress'
    ])

def recover_db():
    cmd = 'mysql --defaults-extra-file=/home/ubuntu/dandeliondir/.my.cnf -e "CREATE DATABASE IF NOT EXISTS wordpress_db;"'
    result = subprocess.run(cmd, shell=True)
    print(result.returncode)
    print(result.stdout)
    print(result.stderr)
    cmd = "ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -i /home/ubuntu/.ssh/dandelion.pem ubuntu@backup 'cat $(ls -td /tmp/backup/* | head -n 1)/backup.sql' | mysql --defaults-extra-file=/home/ubuntu/dandeliondir/.my.cnf wordpress_db"
    result = subprocess.Popen(cmd, shell=True)
    print(result.returncode)
    print(result.stdout)
    print(result.stderr)
```