#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
pip install elasticsearch
pip3 install elasticsearch==7.14.0
"""

from elasticsearch import Elasticsearch

host = '192.168.10.25'
port = 9200


def search():
    es = Elasticsearch([{'host': host, 'port': port}])

    index = 'example_1_index'
    body = {
        'query': {
            'match': {
                'title': 'Python'
            }
        }
    }

    res = es.search(index=index, body=body)
    print('响应', res)

if __name__ == '__main__':
    search()

