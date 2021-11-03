#! /usr/bin/env python
# -*- coding: utf-8 -*-
 
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

        # node = zkc.get_children('/dubbo')
        # print(node)

        # node = zkc.get("/dubbo/com.infuq.facade.QueryUserInfoFacade")
        # print(node)

        # node = zkc.get_children("/dubbo/com.infuq.facade.QueryUserInfoFacade/")
        # print(node)

        node = zkc.get_children("/dubbo/com.infuq.facade.QueryUserInfoFacade/providers/")
        print(node)
        for v in node:
            print(parse.unquote(v))



        # zkc.close()
        zkc.stop()
    except Exception as err:
        print(err)
 
 
if __name__ == "__main__":
    try:
        main()
    finally:
        sys.exit()
