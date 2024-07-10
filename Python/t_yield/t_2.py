#! /usr/bin/env python

import dis
import inspect


def foo():
    print('上一个', inspect.currentframe().f_back)
    print('当前', inspect.currentframe())
    print('栈', inspect.stack())
    yield "generator"

def bar():
    print('-function-')

def main():
    f = foo()
    print(f)
    print(next(f))
    print(bar)


if __name__ == '__main__':
    main()
