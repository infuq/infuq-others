#! /usr/bin/env python

import dis
import inspect


def foo():
    yield "9527"
    yield "qwert"

def delegate():

    # 将foo压入C栈和Python栈
    yield from foo()

def main():
    d = delegate()

    # 将delegate压入C栈和Python栈
    print(next(d))

    # 执行到此处, foo和delegate都从C栈和Python栈出栈

    # 将delegate压入C栈和Python栈
    print(next(d))


if __name__ == '__main__':
    main()
