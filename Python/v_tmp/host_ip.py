#! /usr/bin/env python

import socket

"""
查询本机ip地址    
"""

def host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


def host_ip_2():
    import socket
    hostname=socket.gethostname()
    print(hostname)
    ip=socket.gethostbyname(hostname)
    return ip

if __name__ == '__main__':
    print(host_ip_2())
