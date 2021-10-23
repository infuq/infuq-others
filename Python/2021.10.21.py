#! /usr/bin/env python

class MyIter(object):

    def __init__(self):
        self.index = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        return self.index


if __name__ == '__main__':
    my_iter = MyIter()

    print(next(my_iter))
    print(next(my_iter))
    print(next(my_iter))
