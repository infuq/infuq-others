#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Future(object):
    def __init__(self):
        pass

    def __iter__(self):
        print('1')
        yield self
        print("2")
        return "will"


class Caller(object):
    def __init__(self, f):
        self._future = f

    def call(self):
        ret = yield from self._future
        print(ret)
        ret = yield from self._future
        print(ret)
        return ret


if __name__ == '__main__':
    future = Future()
    caller = Caller(future)
    g = caller.call()
    for _ in g:
        pass


