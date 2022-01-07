#! /usr/bin/env python

'''
查找当前目录下包含关键字的文件
'''

import re
import os
import sys

# 返回指定目录下的文件
def dir(root, suffix):
    files = os.listdir(root)
    for file in files:
        if not os.path.isfile(os.path.join(root, file)):
            continue
        if suffix and os.path.splitext(file)[-1][1:] != suffix[1:]: # 如果指定了文件后缀则校验, 否则不校验
            continue
        yield os.path.join(root, file)


def find_file_by_keyword(directory, keyword, suffix=None):
    for file in dir(directory, suffix):
        with open(file, mode='r', encoding='utf8') as f:
            # 逐行读取
            for line in f:
                matcher = re.match(r'^.*%s.*$' % keyword, line)
                if matcher:
                    print(file)
                    break

if __name__ == '__main__':
    
    
    directory = 'D:/Repository/infuq-others/Python/v_tmp/'
    keyword = '8.8.8.8'
    suffix = '.py'
    # 查找指定目录下指定后缀文件包含指定关键字的文件
    find_file_by_keyword(directory, keyword, suffix)
    # 查找指定目录下包含指定关键字的文件
    find_file_by_keyword(directory, keyword)

    # for root, dirs, files in os.walk("v_tmp/", topdown=True):
    #     for file in files:
    #         if file.endswith('.txt'):
    #             print('这是一个txt文件')
    #         print(os.path.join(root, file))
    #     for dir in dirs:
    #         print(os.path.join(root, dir))    