#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
pip install elasticsearch
pip3 install elasticsearch==7.14.0
"""

from elasticsearch import Elasticsearch

host = '192.168.10.25'
port = 9200

def delete_doc():
    es = Elasticsearch([{'host': host, 'port': port}])

    index = 'example_1_index'

    res = es.delete(index=index, id='GVJ_NpIBkE0jtAWMBp3F')
    print('响应', res)



if __name__ == '__main__':

    delete_doc()



