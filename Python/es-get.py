#! /usr/bin/env python
# -*- coding:utf-8 -*-

import socket

def request():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 9200))
    # 简单查询
    request_url = 'GET /book/type/2 HTTP/1.1\r\nHost: 127.0.0.1:9200\r\n\r\n'

    # 条件查询
    request_url = 'POST /book/_search HTTP/1.1\r\nHost: 127.0.0.1:9200\r\nContent-Type: application/json\r\nContent-Length: 227\r\n\r\n{"query":{"match":{"country":"唐朝"\}\},"from":1,"size":2,"sort":[{"date":{"order":"desc"\}\}]}\r\n'

    client.send(request_url.encode())
    response = client.recv(2048)
    print(response)



if __name__ == '__main__':
    request()
