#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
pip install elasticsearch
pip3 install elasticsearch==7.14.0
"""

from elasticsearch import Elasticsearch

host = '192.168.10.25'
port = 9200

def create_index():
    es = Elasticsearch([{'host': host, 'port': port}])

    index = 'example_1_index'

    res = es.indices.create(index=index)
    print('响应', res)


def create_doc():
    es = Elasticsearch([{'host': host, 'port': port}])

    index = 'example_1_index'

    doc = {'title': 'Python Elasticsearch Guide', 'content': 'This is a beginner\'s guide...'}
    res = es.index(index=index, body=doc)
    print('响应', res)


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


def update_doc():
    es = Elasticsearch([{'host': host, 'port': port}])

    index = 'example_1_index'

    res = es.update(index=index, id='GVJ_NpIBkE0jtAWMBp3F', body={'doc': {'title': 'Updated Title'}})
    print('响应', res)


def delete_doc():
    es = Elasticsearch([{'host': host, 'port': port}])

    index = 'example_1_index'

    res = es.delete(index=index, id='GVJ_NpIBkE0jtAWMBp3F')
    print('响应', res)



if __name__ == '__main__':
    search()
    # create_doc()
    # update_doc()
    # delete_doc()





















