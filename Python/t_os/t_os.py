#!/usr/bin/env python3

import os

if __name__ == '__main__':
    print(os.getcwd())
    print(os.listdir('.'))

    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            print(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))
