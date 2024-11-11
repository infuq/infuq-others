#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
pip install elasticsearch
pip3 install elasticsearch==7.14.0

在 Kibana 中执行 PUT /<索引名称>
{
    ...
}
"""

import requests
from elasticsearch import Elasticsearch

host = '192.168.10.25'
port = 9200

def create_index(index, data):
    es = Elasticsearch([{'host': host, 'port': port}])
    res = es.indices.create(index=index, body=data)
    print('响应', res)


if __name__ == '__main__':

    data = {
        "settings": {
            "index.number_of_shards": 1,
            "index.number_of_replicas": 0
        },
        "mappings": {
            "properties": {
                "db": {
                    "type": "keyword",
                    "index": True
                },
                "environment": {
                    "type": "keyword",
                    "index": True
                },
                "op": {
                    "type": "keyword",
                    "index": True
                },
                "tableName": {
                    "type": "keyword",
                    "index": True
                },
                "data": {
                    "type": "object",
                    "properties": {
                        "before": {
                            "type": "text",
                            "analyzer": "ik_smart"
                        },
                        "after": {
                            "type": "text",
                            "analyzer": "ik_smart"
                        }
                    }
                },
                "createTime": {
                    "type": "keyword",
                    "index": True
                }
            }
        }
    }

    create_index('search_foo', data)


