#! /usr/bin/env python
# -*- coding:utf-8 -*-

import time
import socket
import ssl


def download():
    host = 'gitee.com'
    port = 443
    sock = ssl.wrap_socket(socket.socket())
    sock.connect((host, port))
    request_url = 'GET /infuq/jdk1.8.0_202/raw/master/bin/jinfo HTTP/1.1\r\nHost: gitee.com\r\nConnection: close\r\n\r\n'

    sock.send(request_url.encode())
    rec = sock.recv(1024)
    response = b''
    while rec:
        response += rec
        start = 0
        index = 0
        if response[0:1] != b'\x7f':
            while start < response.__len__():
                if response[start:start+1] == b'\r' and response[start+1:start+2] == b'\n':
                    index = start + 2
                start = start + 1
            if index:
                response = response[index:]
        rec = sock.recv(1024)
        # print(rec)

    print('===')
    print(response)
    response = response[0:-7]
    with open('jinfo', 'wb+') as f:
        f.write(response)


if __name__ == '__main__':
    download()
