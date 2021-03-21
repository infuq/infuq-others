#! /usr/bin/env python

'''
进程通信 管道
'''

import multiprocessing


def send(conn, data):
    conn.send([data])


def recv(con):
    print(con.recv())


def main():
    pipe_send, pipe_recv = multiprocessing.Pipe()
    process_send = multiprocessing.Process(target=send, args=(pipe_send, '数据'))
    process_recv = multiprocessing.Process(target=recv, args=(pipe_recv,))
    process_send.start()
    process_recv.start()


if __name__ == '__main__':
    main()

