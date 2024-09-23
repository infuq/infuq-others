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
        host = "192.168.10.9"
        port = "2181"
        timeout = 100
        zkc = KazooClient(hosts=host + ':' + port, timeout=timeout)
        zkc.start()

        print('[ zk状态 ] -> {}\n'.format(zkc.state))

        # node = zkc.get_children('/')
        node = zkc.get_children('/dubbo/')
        print(node,'\n')


        service_name = 'com.infuq.facade.UserFacade'

        # node = zkc.get("/dubbo/{}/".format(service_name))
        # node = zkc.get_children("/dubbo/{}".format(service_name))
        # print(node)

        
        # 提供者信息
        providers = zkc.get_children('/dubbo/{}/providers'.format(service_name))
        for _provider in providers:
            provider = parse.unquote(_provider)
            print('[ 提供者 ] -> {}'.format(provider))

            ip = provider.split("/")[2].split(':')[0]
            print('[ 提供者IP ] -> {}'.format(ip))
            port = provider.split("/")[2].split(':')[1]
            print('[ 提供者端口 ] -> {}\n'.format(port))

        print('\n')

        # 消费者信息
        consumers = zkc.get_children('/dubbo/{}/consumers'.format(service_name))
        for _consumer in consumers:
            consumer = parse.unquote(_consumer)
            print('[ 消费者 ] -> {}'.format(consumer))

            ip = consumer.split("/")[2].split(':')[0]
            print('[ 消费者IP ] -> {}\n'.format(ip))
            



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
        main()
        # i()
    finally:
        sys.exit()




