import socket
import time

if __name__ == '__main__':

        client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        client.connect(('127.0.0.1', 8083))

        for i in range(1, 1502):
                data = data + "v"

        client.send(data.encode('utf-8'))

    # time.sleep(600)
