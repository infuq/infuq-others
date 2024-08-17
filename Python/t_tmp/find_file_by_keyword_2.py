#! /usr/bin/env python

'''
查找指定目录下包含指定关键字的文件
'''

import re
import os
import sys

# 返回指定目录下的文件 & 递归
def dir_recursion(root, suffix):
    for root, dirs, files in os.walk(root, topdown=True):
        for file in files:
            if suffix and not file.endswith(suffix):
                continue
            yield os.path.join(root, file)
        for dir in dirs:
            # 递归
            dir_recursion(os.path.join(root, dir), suffix)


def find_file_by_keyword(directory, keyword, suffix=None):
    for file in dir_recursion(directory, suffix):
        try:
            with open(file, mode='r', encoding='utf8') as f:
                # 逐行读取
                for line in f:
                    matcher = re.match(r'^.*%s.*$' % keyword, line)
                    if matcher:
                        print(file)
                        break
        except:
            pass

if __name__ == '__main__':
    
    directory = 'D:/Repository/infuq-others/Python/'
    keyword = '8\.8\.8\.8'
    suffix = '.py'
    # 查找指定目录下指定后缀文件包含指定关键字的文件
    find_file_by_keyword(directory, keyword, suffix)
    # 查找指定目录下包含指定关键字的文件
    # find_file_by_keyword(directory, keyword)

  