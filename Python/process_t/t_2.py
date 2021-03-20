#! /usr/bin/env python

'''
创建进程 (面向对象)
'''

import multiprocessing

class MyProcess(multiprocessing.Process):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("PID={}, Name={}".format(multiprocessing.current_process().pid, multiprocessing.current_process().name))


if __name__ == '__main__':

    for i in range(3):
        process = MyProcess('My_%s' % (i))
        process.start()

