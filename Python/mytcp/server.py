
# from socket import *
import socket

ADDRESS = ('127.0.0.1', 8081)

def start():
    # 实例化一个socket对象
    # AF_INET表示使用IP协议
    # SOCK_STREAM表示使用TCP协议
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server.bind(ADDRESS)
    server.listen(5)
    print('Server start success...')
    client, addr = server.accept()
    print(f'Server accept client\'addr {addr}')

    while True:
        buf = client.recv(1024)

        # 如果读取的数据是空bytes, 表示对方关闭了连接
        if not buf:
            client.close()
            break

        # 读取的数据是bytes类型, 需要解码成字符串
        print('Server recv : ' + buf.decode('utf-8'))


if __name__ == '__main__':
    start()

