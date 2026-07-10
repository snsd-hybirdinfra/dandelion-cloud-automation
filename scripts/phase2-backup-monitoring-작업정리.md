# 통합

`bakcup-monitoring.sh`
```bash
#!/bin/bash

# data
sudo tar -cvzf "grafana_data_$(date +%Y%m%d_%H%M%S).tar.gz" /var/lib/grafana/

# config
sudo tar -cvzf "grafana_config_$(date +%Y%m%d_%H%M%S).tar.gz" /etc/grafana/
ubuntu@monitoring:~/dandeliondir/backup$ cat backup-monitoring.sh
#!/bin/bash

# grafana data
sudo tar -cvzf "/home/ubuntu/dandeliondir/grafana_data_$(date +%Y%m%d_%H%M%S).tar.gz" /var/lib/grafana/

# grafana config
sudo tar -cvzf "/home/ubuntu/dandeliondir/grafana_config_$(date +%Y%m%d_%H%M%S).tar.gz" /etc/grafana/

# promethus
sudo tar -cvzf "/home/ubuntu/dandeliondir/promethus_backup_$(date +%Y%m%d_%H%M%S).tar.gz" /home/ubuntu/dandeliondir/monitoring/prometheus-3.5.4.linux-amd64

# alertmanager
sudo tar -cvzf "/home/ubuntu/dandeliondir/alertmanager_backup_$(date +%Y%m%d_%H%M%S).tar.gz" /home/ubuntu/dandeliondir/monitoring/alertmanager-0.28.1.linux-amd64
```

# 개별

`backup-alertmanager.sh`
```bash
#!/bin/bash
sudo tar -cvzf "alertmanager_backup_$(date +%Y%m%d_%H%M%S).tar.gz" /home/ubuntu/dandeliondir/monitoring/alertmanager-0.28.1.linux-amd64
```
`backup-grafana.sh`
```bash
#!/bin/bash

# data
sudo tar -cvzf "grafana_data_$(date +%Y%m%d_%H%M%S).tar.gz" /var/lib/grafana/

# config
sudo tar -cvzf "grafana_config_$(date +%Y%m%d_%H%M%S).tar.gz" /etc/grafana/
```
`backup-promethus.sh`
```bash
#!/bin/bash
sudo tar -cvzf "promethus_backup_$(date +%Y%m%d_%H%M%S).tar.gz" /home/ubuntu/dandeliondir/monitoring/prometheus-3.5.4.linux-amd64
```