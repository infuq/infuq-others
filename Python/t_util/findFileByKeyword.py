#! /usr/bin/env python3
# -*- encoding:utf-8 -*-

'''
查找指定目录中, 文件中包含指定关键字的文件
例如: findFileByKeyword.py  /root/d/tmp  2021         查找/tmp目录中包含2021关键字的文件

'''


import os
import sys


class MatchFile:
    def __init__(self, path, keyword):
        self.enable_suffix=True
        self.suffix = ('.txt', '.java', '.py')
        self.path = path
        self.keyword = keyword

    def __find_files(self):
        for root, dirs, files in os.walk(r'%s' % self.path):
            for name in files:
                yield os.path.join(root, name)


    def find_files(self):
        for file in self.__find_files():
            if self.enable_suffix and file.endswith(self.suffix):
                with open(file, 'r') as f:
                    for line in f.readlines():
                        if self.keyword in line:
                            print(file)
                            break
            if not self.enable_suffix:
                with open(file, 'r') as f:
                    for line in f.readlines():
                        if self.keyword in line:
                            print(file)
                            break



if __name__ == '__main__':

    if len(sys.argv) < 3:
        print('参数不满足...\n格式: find 目录 文件中的关键字')
        sys.exit(-1)

    cur_path = sys.argv[1]
    keyword = sys.argv[2]

    matcher = MatchFile(cur_path, keyword)
    matcher.find_files()


