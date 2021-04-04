#! /usr/bin/env python

"""
进程通信 Queue
"""

import time
from multiprocessing import Process, Queue


def produce(queue):
    queue.put('A')
    time.sleep(2)


def consume(queue):
    time.sleep(2)
    data = queue.get()
    print(data)


if __name__ == '__main__':
    queue = Queue(10)
    producer = Process(target=produce, args=(queue,))
    consumer = Process(target=consume, args=(queue,))
    producer.start()
    consumer.start()

    time.sleep(6)
