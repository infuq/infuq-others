#! /usr/bin/env python

"""
线程通信
"""

import queue
import threading
from queue import Queue
import time
import random


class Get(threading.Thread):

    def __init__(self, name, queue):
        super().__init__(name=name)
        self.queue = queue

    def run(self):
        while True:
            item = self.queue.get()
            print('取出 %s' % (item))


class Put(threading.Thread):

    def __init__(self, name, queue):
        super().__init__(name=name)
        self.queue = queue
        self.count = 20

    def run(self):
        while self.count > 0:
            time.sleep(2)
            self.queue.put(random.randint(1,10))
            self.count = self.count - 1


if __name__ == '__main__':
    queue = Queue(maxsize=1000)
    thread1 = Get(name='Get线程', queue=queue)
    thread2 = Put(name='Put线程', queue=queue)

    thread1.start()
    thread2.start()








