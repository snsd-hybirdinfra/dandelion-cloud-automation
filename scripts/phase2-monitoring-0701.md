# Prometheus 기반 자동 복구 시스템 구축 작업 내역

## 작업 목표

Prometheus와 Alertmanager를 이용하여 웹 서버 및 데이터베이스 서버의 이상 상태를 감지하고, FastAPI 기반 복구 서버(Webhook)를 통해 자동 복구 명령을 실행하는 환경을 구축한다.

---

# 1. Prometheus 설정

## Alertmanager 연동

`prometheus.yml`

```yaml
alerting:
  alertmanagers:
    - static_configs:
        - targets:
            - localhost:9093
```

### 목적

* Prometheus에서 발생한 Alert를 Alertmanager로 전달
* Alertmanager가 Webhook을 통해 복구 서버에 요청 전송

> Docker 환경이 아닌 systemd 서비스 환경에서는 `alertmanager:9093` 대신 `localhost:9093`를 사용하였다.

---

## Rule 파일 등록

```yaml
rule_files:
  - alarm_rules.yml
```

별도의 Rule 파일에서 장애 감지 규칙을 관리하도록 구성하였다.

---

## Exporter 등록

다음 대상들을 Prometheus의 모니터링 대상으로 등록하였다.

* Prometheus
* Node Exporter (Web)
* Node Exporter (DB)
* Node Exporter (Backup)
* Node Exporter (Proxy)
* Node Exporter (Control)
* cAdvisor
* MySQL Exporter
* Blackbox Exporter

각 Target에는 다음과 같이 별칭(Label)을 추가하였다.

```yaml
labels:
  alias: web
```

이를 통해 Alert 발생 시 사람이 읽기 쉬운 이름을 사용할 수 있도록 하였다.

---

# 2. Alert Rule 작성

`alarm_rules.yml`

다음 장애를 감지하도록 Rule을 작성하였다.

## WebContainerDown

웹 컨테이너가 중지된 경우 감지한다.

```yaml
alert: WebContainerDown
```

---

## WordPressDBMissing

WordPress 데이터베이스가 존재하지 않는 경우 감지한다.

```yaml
alert: WordPressDBMissing
```

`absent()` 함수를 이용하여 데이터베이스 존재 여부를 확인하도록 구성하였다.

---

## WebContainerMemoryHigh

웹 컨테이너 메모리 사용률이 80% 이상인 경우 감지한다.

```yaml
alert: WebContainerMemoryHigh
```

---

Alert 이름(`alertname`)은 이후 FastAPI에서 복구 작업을 분기하는 기준으로 사용한다.

---

# 3. Alertmanager 설정

`alertmanager.yml`

Receiver는 하나만 사용하도록 단순화하였다.

```yaml
receivers:
  - name: recovery
    webhook_configs:
      - url: http://localhost:5000/recover
```

Routing 역시 하나의 Receiver만 사용한다.

```yaml
route:
  receiver: recovery
```

복구 종류는 Alert 이름으로 구분하도록 설계하였다.

---

# 4. FastAPI 복구 서버 구축

Alertmanager의 Webhook 요청을 수신하기 위한 FastAPI 프로젝트를 생성하였다.

프로젝트 구조

```text
recovery-server/
├── app.py
├── requirements.txt
├── services/
│   ├── recover.py
│   └── ssh.py
└── venv/
```

필요 패키지

```
fastapi
uvicorn
paramiko
```

---

# 5. FastAPI 서비스 등록

systemd 서비스를 이용하여 FastAPI를 항상 실행되도록 구성하였다.

서비스 이름

```
recovery.service
```

실행 명령

```
uvicorn app:app --host 0.0.0.0 --port 5000
```

부팅 시 자동 실행되도록 등록하였다.

```
sudo systemctl enable recovery
```

---

# 6. 자동 복구 방식 설계

전체 흐름은 다음과 같다.

```
Exporter

        │

        ▼

Prometheus

        │

        ▼

Alert Rule

        │

        ▼

Alertmanager

        │

Webhook

        ▼

FastAPI

        │

alertname 확인

        │

        ▼

SSH 명령 실행

        │

        ▼

Web / DB / Backup 서버 복구
```

---

# 7. 복구 방식

복구 서버는 Alertmanager로부터 Alert를 수신한 후 `alertname` 값을 확인하여 작업을 분기한다.

예시

* WebContainerDown

  * 웹 컨테이너 재시작
  * 필요 시 백업 서버로 교체

* WordPressDBMissing

  * Backup 서버의 최신 SQL 백업을 이용하여 DB 복구

* WebContainerMemoryHigh

  * Scale-Out 또는 관리자 알림 수행

Alertmanager에서 여러 Receiver를 사용하는 대신, FastAPI에서 `alertname` 기준으로 복구 작업을 분기하도록 설계하였다.

---

# 8. 트러블슈팅

---

## Python 가상환경 문제

Ubuntu 24.04의 PEP 668 정책으로 인해 시스템 Python에 직접 패키지를 설치할 수 없었다.

원인

* `/usr/bin/python3`
* `/usr/bin/pip`

를 사용하고 있었기 때문이었다.

가상환경을 생성하고 해당 환경의 Python 및 pip를 사용하도록 수정하였다.

---