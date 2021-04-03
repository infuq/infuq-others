#! /usr/bin/env python3.7
# -*- encoding:utf-8 -*-

import socket

if __name__ == '__main__':

    host = '118.31.52.232'
    port = 443

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setblocking(False)
    try:
        client.connect((host, port))
    except BlockingIOError as err:
        pass

    while True:
        try:
            ret = client.send('GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n'.format('/', host).encode('utf-8'))
            break
        except OSError as err:
            pass

    data = b''
    while True:
        try:
            d = client.recv(1024)
        except BlockingIOError as err:
            print(err)
            continue
        if d:
            data += d
        else:
            break

    data = data.decode('utf-8')
    html = data.split('\r\n\r\n')[1]
    client.close()
