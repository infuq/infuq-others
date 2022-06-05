#! /usr/bin/env python
# -*- coding:utf8 -*-

import shutil


if __name__ == '__main__':
    # shutil.rmtree("C:/Program Files/1111")

    a = 10
    j = 9
    q = a if 1 < a < 20 else 8
    print(q)
    print(a)

    arr = ['I', 'love', 'python']
    print(*arr, sep=",") # I,love,python
    k = ','.join(arr) # I,love,python
    



