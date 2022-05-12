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
        content = ('张三', 25, '江苏', '310198276189023145')
        writebook.write(content)
        writebook.save()
            

