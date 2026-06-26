# 작업 일지 (Monitoring 구축)

## 작업 목표

Prometheus 기반 모니터링 환경을 구축하고 각 노드 및 컨테이너의 메트릭을 수집할 수 있도록 Exporter를 설치 및 구성하였다.

---

# 1. Prometheus 설치 및 실행

## 작업 순서

1. Prometheus 다운로드
2. 압축 해제
3. `prometheus.yml` 설정 수정
4. systemd 서비스 등록
5. 서비스 실행 및 확인

### systemd 서비스 파일

`/etc/systemd/system/prometheus.service`

```ini
[Unit]
Description=Prometheus Monitoring System
Wants=network-online.target
After=network-online.target

[Service]
User=root
Group=root
Type=simple
WorkingDirectory=/home/ubuntu/dandeliondir/monitoring/prometheus-3.5.4.linux-amd64

ExecStart=/home/ubuntu/dandeliondir/monitoring/prometheus-3.5.4.linux-amd64/prometheus \
  --config.file=/home/ubuntu/dandeliondir/monitoring/prometheus-3.5.4.linux-amd64/prometheus.yml \
  --storage.tsdb.path=/home/ubuntu/dandeliondir/monitoring/prometheus-3.5.4.linux-amd64/data \
  --storage.tsdb.retention.time=15d

[Install]
WantedBy=multi-user.target
```

### prometheus.yml

```yaml
alerting:
  alertmanagers:
    - static_configs:
        - targets:

rule_files:

scrape_configs:
  - job_name: "prometheus"
    scrape_interval: 5s
    static_configs:
      - targets: ["localhost:9090"]
        labels:
          app: "prometheus"

  - job_name: "docker-web-node-containers"
    static_configs:
      - targets:
          - web1:9100
          - web2:9100
          - web1:8080
          - web2:8080

  - job_name: "docker-db-node-containers"
    static_configs:
      - targets:
          - db:9100
          - db:9104

  - job_name: "docker-proxy-node-containers"
    static_configs:
      - targets:
          - proxy:9100

  - job_name: "docker-control-node-containers"
    static_configs:
      - targets:
          - control:9100

  - job_name: "docker-backup-node-containers"
    static_configs:
      - targets:
          - backup:9100
```

---

# 2. Node Exporter 설치 및 실행

각 서버의 CPU, Memory, Disk, Network 등의 시스템 메트릭 수집을 위해 Node Exporter를 설치하였다.

## 설치

```bash
mkdir -p ~/monitoring
cd ~/monitoring

wget https://github.com/prometheus/node_exporter/releases/download/v1.7.0/node_exporter-1.7.0.linux-amd64.tar.gz
tar xzvf node_exporter-1.7.0.linux-amd64.tar.gz
```

## systemd 서비스 등록

`/etc/systemd/system/node_exporter.service`

```ini
[Unit]
Description=Node Exporter
Wants=network-online.target
After=network-online.target

[Service]
User=root
Group=root
Type=simple
ExecStart=/home/ubuntu/monitoring/node_exporter-1.7.0.linux-amd64/node_exporter \
  --collector.systemd \
  --collector.systemd.unit-include="haproxy.service"

[Install]
WantedBy=multi-user.target
```

## 서비스 실행

```bash
sudo systemctl daemon-reload
sudo systemctl enable node_exporter
sudo systemctl start node_exporter
```

---

# 3. cAdvisor 컨테이너 실행

Docker 컨테이너의 CPU, Memory, Filesystem 등의 메트릭 수집을 위해 cAdvisor를 실행하였다.

```bash
docker run \
  --volume=/:/rootfs:ro \
  --volume=/var/run:/var/run:ro \
  --volume=/sys:/sys:ro \
  --volume=/var/lib/docker/:/var/lib/docker:ro \
  --volume=/dev/disk/:/dev/disk:ro \
  --publish=8080:8080 \
  --detach=true \
  --name=cadvisor \
  --privileged \
  --device=/dev/kmsg \
  --restart=always \
  gcr.io/cadvisor/cadvisor:v0.49.1
```

---

# 4. MySQL Exporter 설치 및 실행

DB 서버의 MySQL 메트릭 수집을 위해 mysqld_exporter를 설치하였다.

## 다운로드

```bash
wget https://github.com/prometheus/mysqld_exporter/releases/download/v0.16.0/mysqld_exporter-0.16.0.linux-amd64.tar.gz

tar -xvf mysqld_exporter-0.16.0.linux-amd64.tar.gz
cd mysqld_exporter-0.16.0.linux-amd64
```

## 인증 파일 생성

```bash
cat << EOF > .my.cnf
[client]
user=wp_monitor
password=test123
EOF

chmod 600 .my.cnf
```

## systemd 서비스 등록

`/etc/systemd/system/mysqld_exporter.service`

```ini
[Unit]
Description=MySQLd Exporter
Wants=network-online.target
After=network-online.target

[Service]
User=root
Group=root
Type=simple
WorkingDirectory=/home/ubuntu/monitoring/mysqld_exporter-0.16.0.linux-amd64

ExecStart=/home/ubuntu/monitoring/mysqld_exporter-0.16.0.linux-amd64/mysqld_exporter \
  --config.my-cnf=/home/ubuntu/monitoring/mysqld_exporter-0.16.0.linux-amd64/.my.cnf

[Install]
WantedBy=multi-user.target
```

## 서비스 실행

```bash
sudo systemctl daemon-reload

sudo systemctl start mysqld_exporter
sudo systemctl enable mysqld_exporter

sudo systemctl status mysqld_exporter
```

---

# 5. 동작 확인

Prometheus API를 이용하여 Exporter들이 정상적으로 수집되는지 확인하였다.

```bash
curl -G 'http://localhost:9090/api/v1/query' \
--data-urlencode 'query=up' | jq
```

정상 동작 시 각 Exporter(Node Exporter, cAdvisor, mysqld_exporter, Prometheus)의 `up` 값이 `1`로 조회된다.

---

# 작업 결과

* Prometheus 설치 및 서비스 등록 완료
* Node Exporter를 각 노드에 설치 및 실행 완료
* cAdvisor 컨테이너 실행 완료
* MySQL Exporter 설치 및 DB 모니터링 구성 완료
* Prometheus에서 모든 Exporter의 메트릭 수집 및 `up` 상태 확인 완료
