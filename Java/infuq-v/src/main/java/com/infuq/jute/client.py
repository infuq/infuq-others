#! /usr/bin/env python

import socket


if __name__ == '__main__':
    with open('D:/Repository/infuq-others/Java/jute.txt', 'r') as f:
        data = f.read()
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1',8081))
    client.send(data)
    client.close()

    exit()



