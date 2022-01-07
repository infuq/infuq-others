#! /usr/bin/env python

import xlwt
import datetime


class WriteXlsUtil(object):

    def __init__(self, file_name='File'):
        self.suffix = '.xls'
        self.workbook = xlwt.Workbook()
        self.sheet = self.workbook.add_sheet("Sheet")
        self.file_name = file_name
        self.empty = True  # 标记是否真的写入了内容
        self.row = -1

    # 写入单元格内容
    def write(self, content):
        self.empty = False
        self.row += 1
        for index in range(len(content)):
            cnt = str(content[index])
            if cnt.isdigit():
                self.sheet.write(self.row, index, cnt.zfill(len(cnt)))
            else:
                self.sheet.write(self.row, index, content[index])

    # 保存文件
    def save(self):
        if not self.empty:
            self.workbook.save("./" + self.file_name + "-" + datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S') + self.suffix)
