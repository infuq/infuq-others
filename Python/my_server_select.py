#! /usr/bin/env python

import socket
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE


class Server(object):

    def __init__(self):
        self.address = ('127.0.0.1', 8080)
        self.selector = DefaultSelector()
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.server.bind(self.address)
        self.server.listen(50)
        self.server.setblocking(False)
        # 注册ACCEPT事件
        self.selector.register(self.server.fileno(), EVENT_READ, self.connected)
        self.loop()

    def connected(self, key):
        client, addr = self.server.accept()
        print(addr)

    def loop(self):
        while True:
            print('执行select...')
            data = self.selector.select()
            for key, mask in data:
                key.data(key)


if __name__ == '__main__':

    server = Server()
    server.start()
