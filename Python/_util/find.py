#! /usr/bin/env python3
# -*- encoding:utf-8 -*-

import os
import sys


class MatchFile:
    def __init__(self, path, keyword):
        self.suffix = ('.txt', '.java', '.py')
        self.path = path
        self.keyword = keyword

    def __find_files(self):
        for root, dirs, files in os.walk(r'%s' % self.path):
            for name in files:
                yield os.path.join(root, name)

    def find_files(self):
        for file in self.__find_files():
            if file.endswith(self.suffix):
                with open(file, 'r') as f:
                    data = f.read()
                    if self.keyword in data:
                        print(file)


if __name__ == '__main__':

    if len(sys.argv) < 3:
        print('参数不满足...\n格式: find 文件名 关键字')
        sys.exit(-1)

    cur_path = sys.argv[1]
    keyword = sys.argv[2]

    matcher = MatchFile(cur_path, keyword)
    matcher.find_files()
