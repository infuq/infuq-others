#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
pip install elasticsearch
pip3 install elasticsearch==7.14.0

在 Kibana 中执行 DELETE <索引名称>
"""

import requests
from elasticsearch import Elasticsearch

host = '192.168.10.25'
port = 9200

# 方式一
def delete_index(index):
    es = Elasticsearch([{'host': host, 'port': port}])
    res = es.indices.delete(index=index)
    print('响应', res)


# 方式二
def delete_index_2(index):
    url = f'http://{host}:{port}/{index}'
    print('请求地址', url)
    res = requests.delete(url)
    print('响应', res.text)


if __name__ == '__main__':
    # delete_index('search_foo')
    delete_index_2('search_foo')

