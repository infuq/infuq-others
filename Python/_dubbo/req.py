#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Req(object):
    
    def __init__(self):
        # http://dubbo.apache.org/zh-cn/blog/dubbo-protocol.html
        self.magic = bytearray(2)
        self.flag = bytearray(1)
        self.status = bytearray(1)
        self.req_id = bytearray(8)
        self.body_len = bytearray(4)
        self.body = None  # body'length
        self.data = bytearray(16)


if __name__ == '__main__':
    req = Req()
    print(req)
    magic = 0xdabb






