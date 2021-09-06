
# from socket import *
import socket

ADDRESS = ('127.0.0.1', 8083)

def start():

    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    server.bind(ADDRESS)
    print('Server start success...')
    
    while True:
        buf = server.recvfrom(1024)
        print(buf)

if __name__ == '__main__':
    start()

