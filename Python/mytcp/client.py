import socket

ADDRESS = ('172.23.7.103', 2181)


def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.bind(('10.31.23.101', 11560))
    client.connect(ADDRESS)

    while True:
        msg = input("> ").strip()

        # 防止发送空字节
        if not msg:
            continue

        client.send(msg.encode("utf-8"))
        if msg == "quit":
            break
        
        '''
        recv_data = client.recv(1024).decode("utf-8")
        print(f'Client recv : {recv_data}')
        '''

    client.close()


if __name__ == '__main__':
    connect()
