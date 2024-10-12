#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
pip install elasticsearch
pip3 install elasticsearch==7.14.0

在 Kibana 中执行 GET _cat/health
"""

import requests
from elasticsearch import Elasticsearch

host = '192.168.10.25'
port = 9200

def cat(uri):
    # url = 'http://%s:%s/%s' % (host, port, uri)
    url = f'http://{host}:{port}/{uri}'
    res = requests.get(url)
    print(res.text)

    
    
if __name__ == '__main__':

    # cat('_all/_search?pretty')
    # cat('_search?pretty')
    # cat('_cluster/health?pretty')
    # cat('_cluster/health?level=indices&pretty')

    # 查看单节点的shard分配整体情况
    # cat('_cat/allocation')
    # 查看各shard的详细情况
    # cat('_cat/shards')
    # 查看指定分片的详细情况
    # cat('_cat/shards/{index}')
    # 查看master节点信息
    # cat('_cat/master')
    # 查看所有节点信息
    # cat('_cat/nodes')
    # cat('_nodes/stats?pretty')
    # 查看集群中所有index的详细信息
    cat('_cat/indices')
    # 查看集群中指定index的详细信息
    # cat('_cat/indices/{index}')
    # 查看各index的segment详细信息,包括segment名, 所属shard, 内存(磁盘)占用大小, 是否刷盘
    # cat('_cat/segments')
    # 查看指定index的segment详细信息
    # cat('_cat/segments/{index}')
    # 查看当前集群的doc数量
    # cat('_cat/count')
    # 查看指定索引的doc数量
    # cat('_cat/count/{index}')
    # 查看集群内每个shard的recovery过程.调整replica
    # cat('_cat/recovery')
    # 查看指定索引shard的recovery过程
    # cat('_cat/recovery/{index}')
    # 查看集群健康状态
    # cat('_cat/health')
    # 查看当前集群的pending task
    # cat('_cat/pending_tasks')
    # 查看集群中所有alias信息,路由配置等
    # cat('_cat/aliases')
    # 查看指定索引的alias信息
    # cat('_cat/aliases/{alias}')
    # 查看集群各节点内部不同类型的threadpool的统计信息
    # cat('_cat/thread_pool')
    # cat('_cat/thread_pool/write?v&h=node_name,name,active,rejected,completed')
    # 查看集群各个节点上的plugin信息
    # cat('_cat/plugins')
    # 查看当前集群各个节点的fielddata内存使用情况
    # cat('_cat/fielddata')
    # 查看指定field的内存使用情况,里面传field属性对应的值
    # cat('_cat/fielddata/{fields}')
    # 查看单节点的自定义属性
    # cat('_cat/nodeattrs')
    # 输出集群中注册快照存储库
    # cat('_cat/repositories')
    # 输出当前正在存在的模板信息
    # cat('_cat/templates')
    
