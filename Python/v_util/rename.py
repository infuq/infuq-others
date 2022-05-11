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
    files = os.listdir('D:/Repository/infuq-others/')
    for file in files:
        if not os.path.isfile(file):
            continue
        if os.path.splitext(file)[-1][1:] == 'flv':
            file_name = os.path.splitext(file)[0]

            file_name_1 = re.match(r'^.*[(](P.*?)[)]?$', file_name).group(1)        

            new_file_name = file_name_1
            print(new_file_name)
            os.rename(file, new_file_name + '.flv')


if __name__ == '__main__':
    batch_rename()