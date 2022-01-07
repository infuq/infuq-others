#! /usr/bin/env python

"""
读取Excel工具
"""
import re
from ReadExcelUtil import ReadExcelUtil


if __name__ == '__main__':

    if 1 < 0:
        file = r'D:\Repository\infuq-others\Python\resources\data_test.xls'
        file = re.sub(r"\\", '/', file) # \ -> /
        rows = ReadExcelUtil(file)
        for row,value in rows:
            # row = 行号
            # value = 行内容
            # value[n] = 具体列内容
            print(row, value, value[2])

    if -1 < 0:
        file = r'D:\Repository\infuq-others\Python\resources/data_test_2.xlsx'
        file = re.sub(r"\\", '/', file) # \ -> /
        rows = ReadExcelUtil(file)
        for row,value in rows:
            # row = 行号
            # value = 行内容
            # value[n] = 具体列内容
            print(row, value, value[2])


