#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
pip install elasticsearch
pip3 install elasticsearch==7.14.0
"""

from elasticsearch import Elasticsearch

host = '192.168.10.25'
port = 9200


def update_doc():
    es = Elasticsearch([{'host': host, 'port': port}])

    index = 'example_1_index'

    res = es.update(index=index, id='GVJ_NpIBkE0jtAWMBp3F', body={'doc': {'title': 'Updated Title'}})
    print('响应', res)


if __name__ == '__main__':

    update_doc()



