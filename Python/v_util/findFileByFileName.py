#! /usr/bin/env python3
# -*- encoding:utf-8 -*-

'''
查找指定目录中, 文件名包含指定关键字的文件
例如: findFileByFileName.py  /root/d/tmp  2021         查找/tmp目录中文件名包含2021的文件

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
            if not os.path.isfile(file):
                continue

            if self.enable_suffix and file.endswith(self.suffix):
                # 例如file_name=server.py
                file_name = os.path.basename(file)
                if self.keyword in file_name:
                    print(file)
            
            if not self.enable_suffix:
                file_name = os.path.splitext(file)[0]
                if self.keyword in file_name:
                    print(file)



if __name__ == '__main__':

    if len(sys.argv) < 3:
        print('参数不满足...\n格式: find 目录 文件名的关键字')
        sys.exit(-1)

    cur_path = sys.argv[1]
    keyword = sys.argv[2]

    matcher = MatchFile(cur_path, keyword)
    matcher.find_files()


