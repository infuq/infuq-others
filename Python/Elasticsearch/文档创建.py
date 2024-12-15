#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
pip install elasticsearch
pip3 install elasticsearch==7.14.0
"""

from elasticsearch import Elasticsearch

host = '192.168.10.25'
port = 9200

def create_doc(index):
    es = Elasticsearch([{'host': host, 'port': port}])
    doc = {'title': 'Python Elasticsearch Guide', 'content': 'This is a beginner\'s guide...'}
    res = es.index(index=index, body=doc)
    print('响应', res)


if __name__ == '__main__':

    index = 'search_foo'
    create_doc()

