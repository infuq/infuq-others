#! /usr/bin/env python
# coding=utf8

'''
pip install mq_http_sdk
'''

import sys
import time
from mq_http_sdk.mq_exception import MQExceptionBase
from mq_http_sdk.mq_producer import *
from mq_http_sdk.mq_client import *


# 文档 https://help.aliyun.com/document_detail/141780.html

def send():

    # 初始化client
    mq_client = MQClient(
        host="", # 例如公网HTTP http://1841829814603902.mqrest.cn-yinchuan.aliyuncs.com
        access_id="",
        access_key=""
        )

    topic_name = "<TOPIC名称>"
    instance_id = "" # 实例ID

    producer = mq_client.get_producer(instance_id, topic_name)
    
    # 循环发布多条消息
    msg_count = 1

    try:
        for i in range(msg_count):
        
            msg = TopicMessage(
                # 消息内容
                '{"year":1993,"address":"yinchuan"}', 
                # 消息标签
                "<TAG>"
                )
            # 设置属性
            msg.put_property("self_key", "self_value")
            # 设置KEY
            msg.set_message_key("DH82691028")
            re_msg = producer.publish_message(msg)
            print("Publish Message Succeed. MessageID:%s, BodyMD5:%s" % (re_msg.message_id, re_msg.message_body_md5))

            time.sleep(1)
    except MQExceptionBase as e:
        if e.type == "TopicNotExist":
            print("Topic not exist, please create it.")
            sys.exit(1)
        print("Publish Message Fail. Exception:%s" % e)


if __name__ == '__main__':
    send()
    