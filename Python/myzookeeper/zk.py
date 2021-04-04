#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import sys
from kazoo.client import KazooClient


def main():
    try:
        host = "127.0.0.1"
        port = "2181"
        timeout = 100
        zkc = KazooClient(hosts=host + ':' + port, timeout=timeout)
        zkc.start()

        node = zkc.get_children('/dubbo')
        print(node)

        node = zkc.get("/")
        print(node)

        # zkc.close()
        zkc.stop()
    except Exception as err:
        print(err)
 
 
if __name__ == "__main__":
    try:
        main()
    finally:
        sys.exit()
