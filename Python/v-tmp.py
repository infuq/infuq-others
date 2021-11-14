#! /usr/bin/env python
# -*- coding:utf-8 -*-


from socket import *

if __name__ == '__main__':

    
    import shutil
    import os
    
    shutil.rmtree("d:/!CloudShell")

    ip=gethostbyname(gethostname())
    
    server = socket(AF_INET, SOCK_STREAM)
    server.bind((ip, 8081))
    server.listen(10)
    

    while False:
        try:
            cli,addr = server.accept()
            # res = cli.recv(1024)
            # cli.send(res)
        except Exception as x:
            pass






