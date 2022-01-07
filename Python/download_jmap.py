#! /usr/bin/env python
# -*- coding:utf-8 -*-

import time
import socket
import ssl


def download():
    host = 'gitee.com'
    port = 443
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    sock = context.wrap_socket(socket.socket())
    sock.connect((host, port))
    request_url = 'GET /infuq/infuq-file/raw/master/jmap.exe HTTP/1.1\r\nHost: gitee.com\r\nConnection: close\r\n\r\n'

    sock.send(request_url.encode())
    rec = sock.recv(8192)
    # print(rec)
    response = rec[-1077:0]
    # with open('jinfo', 'wb+') as f:
        # f.write(response)


if __name__ == '__main__':
    download()
