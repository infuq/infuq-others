#!/usr/bin/bash

pid=`ps -ef | grep influxd | grep -v grep | awk '{print $2}'`
if [ $pid != "" ]; then
   echo "stop influxd ..."
   kill -9 $pid >/dev/null 2>&1
   rm -rf /root/tools/influxdb/influxdb2-2.7.8/usr/bin/influx.log
fi
sleep 3

echo "stop kibana ..."
docker stop b97bb77112a3 >/dev/null 2>&1

echo "stop elasticsearch ..."
docker stop f86222989c65 >/dev/null 2>&1

