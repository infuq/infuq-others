#!/usr/bin/env python
# coding=utf8

'''
pip install aliyun-python-sdk-core
pip install aliyun-python-sdk-ecs
pip install aliyun-python-sdk-ons
'''

import base64
import json
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkons.request.v20190214.OnsMessageGetByMsgIdRequest import OnsMessageGetByMsgIdRequest


# 文档 https://help.aliyun.com/document_detail/141780.html
# https://api.aliyun.com/?spm=5176.smartservice_service_robot_chat_new.0.0.37843cdaaWBcgI#/?product=Ons&version=2019-02-14&api=OnsMessageGetByMsgId&params={}&tab=DEMO&lang=PYTHON


def get_message_by_msg_id():

    access_id=""
    access_key=""
    instance_id = ""
    region = "cn-shanghai"

    topic_name = ""
    message_id = ""
    

    client = AcsClient(access_id, access_key, region)
    request = OnsMessageGetByMsgIdRequest()
    request.set_accept_format('json')
    request.set_Topic(topic_name)
    request.set_InstanceId(instance_id)
    request.set_MsgId(message_id)

    response = client.do_action_with_exception(request)
    json_data = str(response, encoding='utf-8')
    message_obj = json.loads(json_data)
    message_body = message_obj['Data']['Body']

    message = str(base64.b64decode(message_body), encoding='utf-8')
    print(message)


if __name__ == '__main__':
    get_message_by_msg_id()
    