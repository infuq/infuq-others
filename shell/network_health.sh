#!/bin/bash

# 探测网络是否健康

index=1;
while true;
do
    ping www.infuq.com -c 1 > /dev/null
    echo $index "network..."
    index=$((index+1))
done;