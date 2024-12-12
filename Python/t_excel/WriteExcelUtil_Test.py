#! /usr/bin/env python

"""
写入Excel工具
"""

import re
from WriteXlsxUtil import WriteXlsxUtil
from WriteXlsUtil import WriteXlsUtil


if __name__ == '__main__':

    if -1 < 0:
        writebook = WriteXlsUtil()
        content = ('李四', 25, '浙江', 310198276189023145)
        writebook.write(content)
        content = ('王五', 32, '成都', '31019827618902314X')
        writebook.write(content)
        writebook.save()
            

    if 1 < 0:
        writebook = WriteXlsxUtil()
        writebook.column_width('A', 30)
        writebook.column_width('B', 30)
        writebook.column_width('C', 15)
        writebook.column_width('D', 30)
        
        content = ('张三', 25, '江苏', {'value': '310198276189023145', 'color': 'FF0000'})
        writebook.write(content)
        writebook.save()
            

