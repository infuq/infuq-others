#! /usr/bin/env python

import dis
import inspect

"""
https://www.yuque.com/infuq/others/dbxoeg#eayJa
https://docs.python.org/2/library/dis.html
"""


def foo():
    print('上一个', inspect.currentframe().f_back)
    print('当前', inspect.currentframe())
    print('栈', inspect.stack())

    """
    字节码
    LOAD_CONST               4 ('generator')         压入栈顶
    YIELD_VALUE                                      Pops TOS and yields it from a generator.
    POP_TOP                                          弹出栈顶的值
    """
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
