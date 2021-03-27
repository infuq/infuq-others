#! /usr/bin/env python

'''
文件重命名
'''

import re
import os
import sys


def rename():
    files = os.listdir('./')
    for file in files:
        if not os.path.isfile(file):
            continue
        if os.path.splitext(file)[-1][1:] == 'flv':
            file_name = os.path.splitext(file)[0]
            file_name = re.match(r'^.*\(P\d+\.\s+(.*)\)$', file_name).group(1)
            os.rename(file, file_name + '.flv')


if __name__ == '__main__':
    rename()
