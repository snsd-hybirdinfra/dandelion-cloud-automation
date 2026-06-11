# Restore Test Guide

## 1. Test File Create

~~~bash
sudo mkdir -p /var/www/html
echo "Team Dandelion Backup Test" | sudo tee /var/www/html/index.html
~~~

## 2. Backup Execute

~~~bash
sudo chmod +x backup.sh
sudo ./backup.sh
ls -lh /backup
~~~

## 3. Failure Simulation

~~~bash
sudo rm -f /var/www/html/index.html
ls -l /var/www/html
~~~

## 4. Restore Execute

~~~bash
sudo tar -xzf /backup/백업파일명.tar.gz -C /
~~~

## 5. Restore Validation

~~~bash
cat /var/www/html/index.html
curl http://localhost
~~~
