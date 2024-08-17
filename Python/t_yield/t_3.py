#! /usr/bin/env python

import dis
import inspect

"""
https://www.yuque.com/infuq/others/dbxoeg#vmwxO
"""


def foo():
    yield "9527"
    yield "qwert"

def delegate():

    print('栈', inspect.stack())

    """
    字节码
    LOAD_GLOBAL              0 (foo)     加载全局变量foo, 将其压入栈顶
    CALL_FUNCTION            0           调用栈顶的函数, 此处为foo函数,传入0个参数
    GET_YIELD_FROM_ITER                  从栈顶获取迭代器对象,并返回迭代器对象
    LOAD_CONST               0 (None)    加载常量值None, 将其压入栈顶
    YIELD_FROM
    POP_TOP                              弹出栈顶的值
    """
    yield from foo()


def main():
    d = delegate()

    print(next(d))

    print(next(d))


if __name__ == '__main__':
    main()
