#! /usr/bin/env python
# -*- coding:utf-8 -*-

from socket import *
import struct
import json



class Book(object):

    def __init__(self, addr, year):
        self.addr = addr
        self.year = year

    def addr(self):
        return self.addr

    def keys(self):
        return ['addr', 'year']

    def __getitem__(self, item):
        return getattr(self, item)


if __name__ == '__main__':
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(('127.0.0.1', 8082))

    book = Book('杭州', 2021)

    data = json.dumps(dict(book)) # data是字符串类型
    body = bytes(data, 'utf-8') # data是字节类型

    body_len = len(body)

    # head中存body的长度
    head = struct.pack('>I', body_len)

    client.sendall(head + body)





