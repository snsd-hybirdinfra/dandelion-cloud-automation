#!/bin/bash

echo "===== Hostname ====="
hostname

echo "===== Uptime ====="
uptime

echo "===== Memory ====="
free -h

echo "===== Disk ====="
df -h

echo "===== IP Address ====="
ip addr

echo "===== Listening Ports ====="
ss -tulnp

echo "===== Docker Status ====="
systemctl is-active docker

echo "===== Running Containers ====="
docker ps

echo "===== HTTP Check ====="
curl -I http://localhost
