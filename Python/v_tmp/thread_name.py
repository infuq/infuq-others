#! /usr/bin/env python
# -*- coding:utf8 -*-

import threading


class MyThread(threading.Thread):

    def __init__(self, name):
        # python2情况
        super(MyThread, self).__init__(name=name)

    def run(self):
        print("{} is running... tid={}".format(self.name, 3))


if __name__ == '__main__':
    thread = MyThread("v-thread_name")
    thread.start()
