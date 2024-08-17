#! /usr/bin/env python

"""
通过Lock实现线程同步
可重入
"""

import threading
from threading import RLock

count = 0


class Add(threading.Thread):
    def __init__(self, name, lock):
        super().__init__(name=name)
        self.lock = lock

    def run(self):
        global count
        for _ in range(1000000):
            self.lock.acquire()
            count += 1
            self.lock.release()


class Desc(threading.Thread):
    def __init__(self, name, lock):
        super().__init__(name=name)
        self.lock = lock

    def run(self):
        global count
        for _ in range(1000000):
            # 加锁 可重入
            self.lock.acquire()
            self.lock.acquire()
            count -= 1
            # 释放锁 加锁几次则释放锁几次
            self.lock.release()
            self.lock.release()


if __name__ == '__main__':
    lock = RLock()
    thread1 = Add(name='加线程', lock=lock)
    thread2 = Desc(name='减线程', lock=lock)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("count = %d\n" % (count))


