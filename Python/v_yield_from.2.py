#! /usr/bin/env python


class Student(object):
    def __init__(self):
        pass

    def __iter__(self):
        print('x')
        yield 1
        next(self)
        print('y')
        yield 2

    def __next__(self):
        print('n')


def caller():
    print('1')
    stu = Student()
    # 可迭代对象
    yield from stu


if __name__ == '__main__':
    caller = caller()
    caller.send(None)
    print(caller.send(5))

