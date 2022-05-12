#! /usr/bin/env python
# -*- coding:utf-8 -*-

from socket import *
import pickle
import struct
import time



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

    data = pickle.dumps(seria)
    body_len = len(data)

    # head中存body的长度
    head = struct.pack('I', body_len)


    client.sendall(head + data)
    # client.sendall(data)





