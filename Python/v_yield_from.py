#! /usr/bin/env python

def child():
    i = 1
    while i < 4:
        n = yield i
        print('child =>', n)
        if i == 3:
            return 100
        i += 1


def parent():
    val = yield from child()
    print(val)
    n = yield 101
    print('parent =>', n)
    yield 202


if __name__ == '__main__':

    t = parent()
    t.send(None)
    j = 0
    while j < 4:
        j += 1
        try:
            t.send(j)
        except StopIteration:
            print('抛出异常')
            break


