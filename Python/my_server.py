#! /usr/bin/env python

import socket


def start():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 8080))
    server.listen(50)
    while True:
        client, addr = server.accept()
        print(addr)


if __name__ == '__main__':
    start()
