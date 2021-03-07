# /usr/env/python

from ReadExcelUtil import ReadExcelUtil


if __name__ == '__main__':

    util = ReadExcelUtil('D:/Repository/others/python/1.xlsx')
    for row,value in util:
        print(row, value)

    util = ReadExcelUtil('D:/Repository/others/python/2.xls')
    for row,value in util:
        print(row, value)        
