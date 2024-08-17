#! /usr/bin/env python

"""
进程通信 管道

1. 管道只能适用于两个进程, 而Queue可以适用多个进程
2. 管道性能高于Queue

"""

import multiprocessing


def send(pipe, data):
    pipe.send([data])


def recv(pipe):
    print(pipe.recv())


def main():
    pipe_send, pipe_recv = multiprocessing.Pipe()
    process_send = multiprocessing.Process(target=send, args=(pipe_send, '数据'))
    process_recv = multiprocessing.Process(target=recv, args=(pipe_recv,))
    process_send.start()
    process_recv.start()


if __name__ == '__main__':
    main()

