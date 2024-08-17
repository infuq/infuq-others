#! /usr/bin/env python
# -*- coding:utf-8 -*-


from socket import *
import pickle
import struct


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
        

    server = socket(AF_INET, SOCK_STREAM)
    server.bind(('127.0.0.1', 8081))
    server.listen(10)
    cli,addr = server.accept()


    head_len = struct.calcsize("I")
    # 读取head
    head = cli.recv(head_len)

    # head中存body的长度
    body_len = int(struct.unpack('I', head)[0])

    res = cli.recv(body_len)
    seria = pickle.loads(res)
    print(seria.addr)







