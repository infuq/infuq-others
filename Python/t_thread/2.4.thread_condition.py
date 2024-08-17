#! /usr/bin/env python

"""
条件变量
"""

import time
import threading
from threading import Condition


class AThread(threading.Thread):

    def __init__(self, cond):
        super().__init__(name="线程A")
        self.cond = cond

    def run(self):
        with self.cond:
            print("{}: 君住长江头".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{}: 日日思君不见君".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{}: 此水几时休".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{}: 只愿君心似我心".format(self.name))
            self.cond.notify()


class BThread(threading.Thread):

    def __init__(self, cond):
        super().__init__(name="线程B")
        self.cond = cond

    def run(self):
        with self.cond:
            self.cond.wait()
            print("{}: 我住长江尾".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{}: 共饮长江水".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{}: 此恨何时已".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{}: 定不负相思意".format(self.name))

if __name__ == '__main__':
    cond = Condition()
    
    BThread(cond).start()
    time.sleep(1)
    AThread(cond).start()
    
