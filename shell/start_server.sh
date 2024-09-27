#!/usr/bin/bash

# Redis
echo "start redis ..."
docker start 0f4069afbbe9 >/dev/null 2>&1
sleep 5

# ES
echo "start elasticsearch ..."
docker start f86222989c65 >/dev/null 2>&1
sleep 20

# Kibana
echo "start kibana ..."
docker start b97bb77112a3 >/dev/null 2>&1
sleep 20

echo "start app ..."
java -Dspring.profiles.active=prod -jar /root/tools/app.jar > /root/tools/app.log &
sleep 30

# InfluxDB
echo "start influxdb ..."
/root/tools/influxdb/influxdb2-2.7.8/usr/bin/influxd > /root/tools/influxdb/influxdb2-2.7.8/usr/bin/influx.log &

