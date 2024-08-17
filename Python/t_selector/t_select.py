#! /usr/bin/env python

"""
事件循环 + IO多路复用 + 回调
"""

import logging
import socket
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE


# 解码器 (参照Netty思路)
class DecoderHandler(object):

    def __init__(self):
        self.data = b''

    def decode(self, data):
        self.data = self.data + data
        if len(self.data) > 4:
            data = self.data[0:5].decode()
            print('接收数据:{}'.format(data))
            self.data = self.data[5:]


# 服务端
class Server(object):

    def __init__(self):
        self.address = ('127.0.0.1', 8080)
        self.selector = DefaultSelector()
        self.decoder = DecoderHandler()
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.server.bind(self.address)
        self.server.listen(50)
        self.server.setblocking(False)
        # 注册ACCEPT事件 和 回调函数
        self.selector.register(self.server.fileno(), EVENT_READ, (self.connected, self.server))
        self.loop()

    # 处理ACCEPT事件
    def connected(self, key, mask):
        client, addr = key.data[1].accept()  # client, addr = self.server.accept()
        print('接收客户端{}连接...'.format(addr))
        client.setblocking(False)
        # 注册读事件 和 回调函数
        # 只要读缓冲区中有数据那么就会触发读事件 即便一次性没有读取完数据 那么也会继续触发读事件  [水平触发]
        self.selector.register(client.fileno(), EVENT_READ,  (self.read, client))

    def read(self, key, mask):
        if mask & EVENT_READ:  # 读事件
            pass
        if mask & EVENT_WRITE:  # 写事件
            pass

        client = key.data[1]
        data = client.recv(1024)
        self.decoder.decode(data)
        self.send(key, '\r\nHello, World\r\n')

       

    def send(self, key, msg):
        client = key.data[1]
        # print('发送数据...')
        # 返回发送成功的字节数
        d = client.send(str(msg).encode())
        # print(d)

    # 事件循环
    def loop(self):
        while True:
            # print('执行select...')
            data = self.selector.select()  # timeout 单位秒
            for key, mask in data:
                callback = key.data[0]
                callback(key, mask)


if __name__ == '__main__':

    server = Server()
    server.start()
