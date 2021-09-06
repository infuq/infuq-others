import socket
import time

if __name__ == '__main__':

        client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        client.connect(('127.0.0.1', 8083))

        data = 'start...'
        
        for i in range(1, 10000):
                data = data + "gen data"

        client.send(data.encode('utf-8'))

    # time.sleep(600)
