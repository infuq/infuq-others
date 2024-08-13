#! /usr/bin/env python
# -*- coding: utf-8 -*-
 
"""
pip install kazoo
"""

import sys
from kazoo.client import KazooClient
from urllib import parse


def main():
    try:
        host = "zk.infuq.com"
        port = "2181"
        timeout = 100
        zkc = KazooClient(hosts=host + ':' + port, timeout=timeout)
        zkc.start()

        print('[ zk状态 ]->{}'.format(zkc.state))

        # node = zkc.get_children('/')
        # node = zkc.get_children('/dubbo')
        # print(node)

        # 提供Dubbo接口数量
        i = 0
        node = zkc.get_children('/dubbo')
        for v in node:
            if 'keyword' in v:
                i = i + 1            
                print(v)
        print("提供Dubbo接口数量:[%d]" % (i))



        service_name = 'com.infuq.facade.QueryUserInfoFacade'

        # node = zkc.get("/dubbo/{}/".format(service_name))
        # node = zkc.get_children("/dubbo/{}".format(service_name))
        # print(node)

        
        # 提供者信息
        providers = zkc.get_children('/dubbo/{}/providers'.format(service_name))
        for _provider in providers:
            provider = parse.unquote(_provider)
            print('[ 提供者 ]->{}'.format(provider))
            # 获取提供者IP和端口
            ip = provider.split("/")[2].split(':')[0]
            print('[ 提供者IP ]->{}'.format(ip))
            port = provider.split("/")[2].split(':')[1]
            print('[ 提供者端口 ]->{}'.format(port))

        # 消费者信息
        consumers = zkc.get_children('/dubbo/{}/consumers'.format(service_name))
        with open('1.txt', 'a') as f:
            for _consumer in consumers:
                consumer = parse.unquote(_consumer)
                # print('[ 消费者 ]->{}'.format(consumer))
                f.write(consumer)
                f.write('\n')
                # 获取消费者IP
                # ip = consumer.split("/")[2].split(':')[0]
                # print('[ 消费者IP ]->{}'.format(ip))



        # zkc.close()
        zkc.stop()
    except Exception as err:
        print(err)


def i():
    host = "121.43.180.176"
    port = "2181"
    timeout = 100
    zkc = KazooClient(hosts=host + ':' + port, timeout=timeout)
    zkc.start()

    print('[ zk状态 ]->{}'.format(zkc.state))

    node = zkc.get_children('/')
    print(node)

 
if __name__ == "__main__":
    try:
        # main()
        i()
    finally:
        sys.exit()




