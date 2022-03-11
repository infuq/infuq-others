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



# 文档 https://help.aliyun.com/document_detail/255821.html


# 消费消息
def consume():

    # 测试环境配置
    host = ""
    instance_id = ""
    access_id = ""
    access_key = ""

    # 虽然这里发送HTTP请求, 但是这里使用的是TCP协议下的GID
    group_id = ""

    # 如果是延时消息, 这里填写延时主题
    topic_name = ""
    message_tag = "" # 消息标签


    # 初始化 client
    mq_client = MQClient(host=host, access_id=access_id, access_key=access_key)    
    consumer = mq_client.get_consumer(instance_id, topic_name, group_id)
    wait_seconds = 3
    batch = 3
    while True:
        try:
            recv_msgs = consumer.consume_message_orderly(batch, wait_seconds)
            # recv_msgs = consumer.consume_message(batch, wait_seconds)
            for msg in recv_msgs:
                """
                print("\tMessageId: %s, \n\tMessageBodyMD5: %s, \n\tNextConsumeTime: %s, \n\tConsumedTimes: %s, \n\tPublishTime: %s \n\tBody: %s \
                        \n\tReceiptHandle: %s \
                        \n\tProperties: %s, \n\tShardingKey: %s\n" % \
                    (msg.message_id, msg.message_body_md5,
                    msg.next_consume_time, msg.consumed_times,
                    msg.publish_time, msg.message_body,
                    msg.receipt_handle, msg.properties, msg.get_sharding_key()))
                """
                consumer.ack_message(msg.receipt_handle.split())
                print(("========>Ack %s Message Succeed." % (msg.message_id)))
                
        except MQExceptionBase as e:
            if e.type == "MessageNotExist":
                # print(("No new message! RequestId: %s" % e.req_id))                
                # continue
                # break
                time.sleep(5)
                continue

            print(("Consume Message Fail! Exception:%s\n" % e))
            time.sleep(2)
            continue

        # ACK
        """
        try:
            receipt_handle_list = [msg.receipt_handle for msg in recv_msgs]
            consumer.ack_message(receipt_handle_list)
            print(("========>Ak %s Message Succeed.\n\n" % len(receipt_handle_list)))
        except MQExceptionBase as e:
            print(("\nAk Message Fail! Exception:%s" % e))
            if e.sub_errors:
                for sub_error in e.sub_errors:
                    print(("\tErrorHandle:%s,ErrorCode:%s,ErrorMsg:%s" % \
                        (sub_error["ReceiptHandle"], sub_error["ErrorCode"], sub_error["ErrorMessage"])))

        """


if __name__ == '__main__':
    consume()



