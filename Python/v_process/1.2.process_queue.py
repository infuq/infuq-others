#! /usr/bin/env python

"""
进程通信 Queue

这里使用的multiprocessing中的Queue, 不能用于进程池中的进程通信
如果需要让进程池中的进程使用Queue通信, 那么必须使用Manager().Queue()

常见Queue
from queue import Queue
from multiprocessing import Queue
from multiprocessing import Manager


"""

import time
from multiprocessing import Process, Queue, Manager


def produce(queue):
    queue.put('A')
    time.sleep(2)


def consume(queue):
    time.sleep(2)
    data = queue.get()
    print(data)


if __name__ == '__main__':
    queue = Queue(10)
    # queue = Manager().Queue(10)  # 用于进程池中的进程通信
    producer = Process(target=produce, args=(queue,))
    consumer = Process(target=consume, args=(queue,))
    producer.start()
    consumer.start()

    time.sleep(6)
