#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
pip install elasticsearch
pip3 install elasticsearch==7.14.0
"""

import json
from elasticsearch import Elasticsearch

host = '192.168.10.25'
port = 9200


def search(index, data):
    es = Elasticsearch([{'host': host, 'port': port}])
    res = es.search(index=index, body=data)
    print('响应', res)
    print(json.dumps(res, indent=2, ensure_ascii=False))

if __name__ == '__main__':

    index = 'search_foo'
    data = {
        'query': {
            'match': {
                'title': 'Python'
            }
        }
    }


    search(index, data)

