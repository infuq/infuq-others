#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Req(object):
    # http://dubbo.apache.org/zh-cn/blog/dubbo-protocol.html
    magic = bytearray(2)
    flag = bytearray(1)
    status = bytearray(1)
    req_id = bytearray(8)
    body_len = bytearray(4)
    body = None  # body'length
    data = bytearray(16)

    def __init__(self):
        pass


if __name__ == '__main__':
    req = Req()
    print(req)
    magic = 0xdabb






