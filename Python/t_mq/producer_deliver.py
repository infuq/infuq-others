#!/usr/bin/env python
# coding=utf8

"""
pip install mq_http_sdk
pip install aliyun-python-sdk-core
pip install aliyun-python-sdk-ecs
pip install aliyun-python-sdk-ons
"""

import sys
from mq_http_sdk.mq_exception import MQExceptionBase
from mq_http_sdk.mq_producer import *
from mq_http_sdk.mq_client import *
import time
import base64
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException



# 文档 https://help.aliyun.com/document_detail/255822.html
#     https://help.aliyun.com/document_detail/29549.html


# 发送延时消息
def send():

    # 测试环境配置
    host = ""
    instance_id = ""
    access_id = ""
    access_key = ""

    # 延时主题
    topic_name = ""

    # 消息内容
    message_body = '{"payAmount":1,"payBillNo":"4200001025202104291320435588"}'
    message_tag = "" # 消息标签
    message_key = ''

    # 初始化 client
    mq_client = MQClient(host=host, access_id=access_id, access_key=access_key)
    producer = mq_client.get_producer(instance_id, topic_name)


    msg_count = 4

    try:
        for i in range(msg_count):
                msg = TopicMessage(message_body, message_tag)
                msg.put_property("a", "i")
                msg.set_message_key("MessageKey" + str(i))

                # 延时时间 最大可设置延迟40天投递
                msg.set_start_deliver_time(int(round(time.time() * 1000)) + 10 * 1000)
                
                re_msg = producer.publish_message(msg)
                print("Publish Timer Message Succeed. MessageID:%s, BodyMD5:%s" % (re_msg.message_id, re_msg.message_body_md5))
                
                time.sleep(1)
    except MQExceptionBase as e:
        if e.type == "TopicNotExist":
            print("Topic not exist, please create it.")
            sys.exit(1)
        print("Publish Message Fail. Exception:%s" % e)



if __name__ == '__main__':
    send()


