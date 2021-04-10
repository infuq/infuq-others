#! /usr/bin/env python

import os
import re
import sys

"""
文件重命名
"""

import re
import os
import sys


def batch_rename():
    files = os.listdir('./')
    for file in files:
        if not os.path.isfile(file):
            continue
        if os.path.splitext(file)[-1][1:] == 'mp4':
            file_name = os.path.splitext(file)[0]
            file_name_1 = re.match(r'^.*【(.*)】\s*(.*)\)$', file_name).group(1)
            file_name_2 = re.match(r'^.*【(.*)】\s*(.*)\)$', file_name).group(2)
            file_name = file_name_1 + '-' + file_name_2
            # print(file,  file_name)
            os.rename(file, file_name + '.mp4')


if __name__ == '__main__':
    batch_rename()

