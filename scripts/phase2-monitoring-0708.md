# 모니터링 노드 프로메테우스 & 그라파나 & 알람매니저 설치

## 프로메테우스

### 설치 파일 다운로드
wget https://github.com/prometheus/prometheus/releases/download/v3.5.4/prometheus-3.5.4.linux-amd64.tar.gz
tar xzvf prometheus-3.5.4.linux-amd64.tar.gz

### 서비스 등록 준비
`/etc/systemd/system/prometheus.service`
```
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
### 서비스 등록
sudo systemctl daemon-reload
sudo systemctl enable promethus
sudo systemctl start promethus


## 알람매니저

### 설치 파일 다운로드
wget https://github.com/prometheus/alertmanager/releases/download/v0.28.1/alertmanager-0.28.1.linux-amd64.tar.gz

### 서비스 등록 준비
`/etc/systemd/system/alertmanager.service`
```
[Unit]
Description=Prometheus Alertmanager
Wants=network-online.target
After=network-online.target

[Service]
User=root
Group=root
Type=simple
WorkingDirectory=/home/ubuntu/dandeliondir/monitoring/alertmanager-0.28.1.linux-amd64

ExecStart=/home/ubuntu/dandeliondir/monitoring/alertmanager-0.28.1.linux-amd64/alertmanager \
  --config.file=/home/ubuntu/dandeliondir/monitoring/alertmanager-0.28.1.linux-amd64/alertmanager.yml \
  --storage.path=/home/ubuntu/dandeliondir/monitoring/alertmanager-0.28.1.linux-amd64/data

Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

### 서비스 등록
sudo systemctl daemon-reload
sudo systemctl enable alertmanager
sudo systemctl start alertmanager


## 그라파나

### 서비스 설치

- 저장소 업데이트
sudo apt update -y && sudo apt upgrade -y
- 필요한 패키지 설치
sudo apt install -y apt-transport-https software-properties-common wget
- 그라파나 gpg 키 추가
sudo mkdir -p /etc/apt/keyrings/
wget -q -O - https://apt.grafana.com/gpg.key | gpg --dearmor | sudo tee /etc/apt/keyrings/grafana.gpg > /dev/null
- 그라파나 apt 저장소 추가
echo "deb [signed-by=/etc/apt/keyrings/grafana.gpg] https://apt.grafana.com stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list
sudo apt update
- 그라파나 설치
sudo apt install grafana
- 서비스 시작
sudo systemctl start grafana-server
sudo systemctl enable grafana-server
- 방화벽 작업
sudo ufw enable 
sudo ufw allow ssh
sudo ufw allow 3000/tcp

# 웹 노드 node exporter & cAdvisor & blackbox exporter 설치


## node exporter 설치

### 설치 파일 다운로드

wget https://github.com/prometheus/node_exporter/releases/download/v1.7.0/node_exporter-1.7.0.linux-amd64.tar.gz
tar xzvf node_exporter-1.7.0.linux-amd64.tar.gz


### 서비스 등록 준비
`/etc/systemd/system/node_exporter.service`
```
[Unit]
Description=Node Exporter
Wants=network-online.target
After=network-online.target

[Service]
User=root
Group=root
Type=simple
ExecStart=/home/ubuntu/monitoring/node_exporter-1.7.0.linux-amd64/node_exporter --collector.systemd --collector.systemd.unit-include="docker.service"

[Install]
WantedBy=multi-user.target
```
### 서비스 등록
sudo systemctl daemon-reload
sudo systemctl enable node_exporter
sudo systemctl start node_exporter


## cAdvisor 가동

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


## blackbox exporter 설치

### 설치 파일 다운로드

wget https://github.com/prometheus/blackbox_exporter/releases/download/v0.18.0/blackbox_exporter-0.18.0.linux-amd64.tar.gz
tar xzvf blackbox_exporter-0.18.0.linux-amd64.tar.gz

### 서비스 등록 준비
`/etc/systemd/system/blackbox_exporter.service
```
[Unit]
Description=Blackbox Exporter
After=network.target

[Service]
User=root
Group=root
ExecStart=/home/ubuntu/monitoring/blackbox_exporter-0.18.0.linux-amd64/blackbox_exporter --config.file=/home/ubuntu/monitoring/blackbox_exporter-0.18.0.linux-amd64/blackbox.yml

Restart=always

[Install]
```

### 서비스 등록

sudo systemctl daemon-reload
sudo systemctl enable blackbox_exporter
sudo systemctl start blackbox_exporter

# db 노드


## node exporter 설치

### 설치 파일 다운로드

wget https://github.com/prometheus/node_exporter/releases/download/v1.7.0/node_exporter-1.7.0.linux-amd64.tar.gz
tar xzvf node_exporter-1.7.0.linux-amd64.tar.gz


### 서비스 등록 준비
`/etc/systemd/system/node_exporter.service`
```
[Unit]
Description=Node Exporter
Wants=network-online.target
After=network-online.target

[Service]
User=root
Group=root
Type=simple
ExecStart=/home/ubuntu/monitoring/node_exporter-1.7.0.linux-amd64/node_exporter --collector.systemd --collector.systemd.unit-include="mysqld.service"

[Install]
WantedBy=multi-user.target
```
### 서비스 등록
sudo systemctl daemon-reload
sudo systemctl enable node_exporter
sudo systemctl start node_exporter

## mysql exporter 설치

### 설치 파일 다운로드
wget https://github.com/prometheus/mysqld_exporter/releases/download/v0.16.0/mysqld_exporter-0.16.0.linux-amd64.tar.gz
tar xzvf mysqld_exporter-0.16.0.linux-amd64.tar.gz

### 서비스 등록 준비
`/etc/systemd/system/mysqld_exporter.service`
```
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
        --config.my-cnf=/home/ubuntu/monitoring/mysqld_exporter-0.16.0.linux-amd64/.my.cnf \
        --collect.engine_tokudb_status \
        --collect.global_status \
        --collect.global_variables \
        --collect.info_schema.clientstats \
        --collect.info_schema.innodb_metrics \
        --collect.info_schema.innodb_tablespaces \
        --collect.info_schema.innodb_cmp \
        --collect.info_schema.innodb_cmpmem \
        --collect.info_schema.processlist \
        --collect.info_schema.processlist.min_time=0 \
        --collect.info_schema.query_response_time \
        --collect.info_schema.replica_host \
        --collect.info_schema.tables \
        --collect.info_schema.tables.databases="*" \
        --collect.info_schema.tablestats \
        --collect.info_schema.schemastats \
        --collect.info_schema.userstats \
        --collect.mysql.user \
        --collect.perf_schema.eventsstatements \
        --collect.perf_schema.eventsstatements.digest_text_limit=120 \
        --collect.perf_schema.eventsstatements.limit=250 \
        --collect.perf_schema.eventsstatements.timelimit=86400 \
        --collect.perf_schema.eventsstatementssum \
        --collect.perf_schema.eventswaits \
        --collect.perf_schema.file_events \
        --collect.perf_schema.file_instances \
        --collect.perf_schema.file_instances.remove_prefix=false \
        --collect.perf_schema.indexiowaits \
        --collect.perf_schema.memory_events \
        --collect.perf_schema.memory_events.remove_prefix=false \
        --collect.perf_schema.tableiowaits \
        --collect.perf_schema.tablelocks \
        --collect.perf_schema.replication_group_members \
        --collect.perf_schema.replication_group_member_stats \
        --collect.perf_schema.replication_applier_status_by_worker \
        --collect.slave_status \
        --collect.slave_hosts \
        --collect.heartbeat \
        --collect.heartbeat.database=true \
        --collect.heartbeat.table=true \
        --collect.heartbeat.utc

[Install]
WantedBy=multi-user.target
```
### 서비스 등록
sudo systemctl daemon-reload
sudo systemctl enable mysqld_exporter
sudo systemctl start mysqld_exporter

# 공통


## node exporter 설치

### 설치 파일 다운로드

wget https://github.com/prometheus/node_exporter/releases/download/v1.7.0/node_exporter-1.7.0.linux-amd64.tar.gz
tar xzvf node_exporter-1.7.0.linux-amd64.tar.gz


### 서비스 등록 준비
`/etc/systemd/system/node_exporter.service`
```
[Unit]
Description=Node Exporter
Wants=network-online.target
After=network-online.target

[Service]
User=root
Group=root
Type=simple
ExecStart=/home/ubuntu/monitoring/node_exporter-1.7.0.linux-amd64/node_exporter --collector.systemd

[Install]
WantedBy=multi-user.target
```
### 서비스 등록
sudo systemctl daemon-reload
sudo systemctl enable node_exporter
sudo systemctl start node_exporter



# promethus 설정
`/dandeliondir/monitoring/prometheus-3.5.4.linux-amd64/promethus.yml`
```
# my global config
global:
  scrape_interval: 15s # Set the scrape interval to every 15 seconds. Default is every 1 minute.
  evaluation_interval: 30s # Evaluate rules every 15 seconds. The default is every 1 minute.
  # scrape_timeout is set to the global default (10s).

# Alertmanager configuration
alerting:
  alertmanagers:
    - static_configs:
        - targets:
           - localhost:9093

# Load rules once and periodically evaluate them according to the global 'evaluation_interval'.
rule_files:
  - alert_rules.yml
  # - "first_rules.yml"
  # - "second_rules.yml"

# A scrape configuration containing exactly one endpoint to scrape:
# Here it's Prometheus itself.
scrape_configs:
  # The job name is added as a label `job=<job_name>` to any timeseries scraped from this config.
  - job_name: "prometheus"

    # metrics_path defaults to '/metrics'
    # scheme defaults to 'http'.
    scrape_interval: 5s
    static_configs:
      - targets: ["localhost:9090"]
       # The label name is added as a label `label_name=<label_value>` to any timeseries scraped from this config.
        labels:
          app: "prometheus"

  - job_name: 'docker-web-node-containers'
    scrape_interval: 5s
    static_configs:
      - targets: ['web1:8080']
        labels:
          alias: web

  - job_name: 'web-blackbox'
    metrics_path: /probe
    params:
      module: [http_2xx]

    static_configs:
      - targets: ['web1:9115']
        labels:
          alias: web

    relabel_configs:
      - source_labels: [__address__]
        target_label: __param_target

      - source_labels: [__param_target]
        target_label: instance

      - target_label: __address__
        replacement: blackbox-exporter:9115

  - job_name: 'web-node'
    static_configs:
      - targets: ['web1:9100']
        labels:
          alias: web

  - job_name: 'db-node'
    static_configs:
      - targets: ['db_primary:9100']
        labels:
          alias: db

  - job_name: 'db-server'
    scrape_interval: 5s
    static_configs:
      - targets: ['db_primary:9104']
        labels:
          alias: db

  - job_name: 'db-replica-node'
    static_configs:
      - targets: ['db_replica:9100']
        labels:
          alias: db

  - job_name: 'db-replica-server'
    scrape_interval: 5s
    static_configs:
      - targets: ['db_replica:9104']
        labels:
          alias: db


  - job_name: 'proxy-node'
    static_configs:
      - targets: ['proxy:9100']
        labels:
          alias: proxy
  - job_name: 'control-node'
    static_configs:
      - targets: ['control:9100']
        labels:
          alias: control

  - job_name: 'backup-node'
    static_configs:
      - targets: ['backup:9100']
        labels:
          alias: backup

```

`/home/ubuntu/dandeliondir/monitoring/prometheus-3.5.4.linux-amd64/alert_rules.yml`
```
groups:
  - name: web_and_db_auto_recovery
    rules:
      - alert: WebContainerDown
        expr: absent(container_last_seen{job="docker-web-node-containers", container_label_com_docker_stack_namespace="dandelion-wp"})
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: " wordpress container 비정상 감지"
          description: "web 서버의 wordpress  컨테이너가 다운되었습니다. 백업 교체가 필요합니다."

      - alert: WordPressDBMissing
        expr: absent(mysql_info_schema_table_rows{job="db-server", schema="wordpress_db"})
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "WordPress DB 누락 감지"
          description: "db 노드에 wordpress_db가 없습니다. 백업으로 교체 요청합니다."

      - alert: WordPressDBMissing-replica
        expr: absent(mysql_info_schema_table_rows{job="db-replica-server", schema="wordpress_db"})
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "WordPress DB 누락 감지"
          description: "db replica 노드에 wordpress_db가 없습니다. 백업으로 교체 요청합니다."


      - alert: WebContainerMemoryHigh
        expr: (container_memory_working_set_bytes{container_label_com_docker_compose_service=~"dandelion_wordpress.*"} / container_spec_memory_limit_bytes{container_label_com_docker_compose_service=~"dandelion_wordpress.*"}) * 100 >= 80
        for: 1m
        labels:
          severity: warning
        annotations:
          summary: "wordpress container  메모리 과부하 (80% 이상)"
          description: "현재 wordpress  컨테이너의 메모리 사용량이 80%를 초과하여 스케일 아웃이 필요합니다."
```

## alertmanager 설정
`/home/ubuntu/dandeliondir/monitoring/alertmanager-0.28.1.linux-amd64/alertmanager.yml`
```
global:
  smtp_smarthost: 'smtp.gmail.com:587'
  smtp_from: 'some2tell@gmail.com'
  smtp_auth_username: 'some2tell@gmail.com'
  smtp_auth_password: 'ktpu epae aucm mnux'
  resolve_timeout: 5m

route:
  receiver: 'email-notifications'
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 3h

receivers:
  - name: 'email-notifications'
    email_configs:
      - to: 'some2tell@gmail.com'
        send_resolved: true
```

# grafana 설정
`/etc/grafana/provisioning/datasources/prometheus.yaml`
```
apiVersion: 1

datasources:
  - name: prometheus
    type: prometheus
    access: proxy
    url: http://localhost:9090  # 프로메테우스가 있는 IP와 포트
    isDefault: true
    editable: false
```
`/etc/grafana/provisioning/datasources/alertmanager.yaml`
```
apiVersion: 2


datasources:
  - name: alertmanager
    type: alertmanager
    access: proxy
    url: http://localhost:9093
    isDefault: false
    editable: false
    jsonData:
      implementation: prometheus
      httpMethod: GET
```