#! /usr/bin/env python


import pymysql
import random
import time


def t():
    conn = pymysql.connect(host="172.21.126.201", port=3306, user="root", passwd="9527", db="db0")
    cursor = conn.cursor()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor) # 得到的数据会以{'字段':数据}形式输出



    sql = "SELECT * FROM t_1"
    cursor.execute(sql)
    res = cursor.fetchall()
    print(res)

    time.sleep(240)

    conn.close()
    cursor.close()



if __name__ == '__main__':
    t()
