#! /usr/bin/env python
# -*- coding:utf-8 -*-

from socket import *
import pickle
import struct
import json



class Seria(object):

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

    seria = Seria('Hangzhou', 2021)

    # data = pickle.dumps(dict(seria))

    data = json.dumps(dict(seria))
    data = bytes(data, 'utf-8')

    body_len = len(data)

    # head中存body的长度
    # head = struct.pack('I', body_len)

    head = bytes(str(body_len), 'utf-8')
    client.sendall(head + data)
    # client.sendall(data)





