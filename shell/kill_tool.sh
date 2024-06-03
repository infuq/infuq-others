
脚本内容如下
#!/usr/bin/bash

pid=`ps -ef | grep tools_prod | grep -v grep | awk '{print $2}'`

if [ $pid != "" ]; then
   echo "kill tools_prod " $pid
   kill -9 $pid
   rm -rf /root/work/tools_prod.jar
   rm -rf /root/work/tools_prod.log
fi


定时执行脚本
[root@iZbp185e7123y0mt0xsq74Z ~]# crontab -e
20 10 * * * sh /root/work/kill_tools.sh  > /root/work/kill_tools.log