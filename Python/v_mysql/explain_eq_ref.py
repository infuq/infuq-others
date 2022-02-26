#! /usr/bin/env python

"""
pip install pymysql
"""

"""
文章地址
https://infuq.github.io/MySQL_EXPLAIN.html#eq_ref
"""

import pymysql
import random


def insert():
    conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="9527", db="db0")
    cursor = conn.cursor()

    for i in range(13, 2000):

        u_name = 'U' + str(i)
        u_year = 'chengdu'
        param = (i, u_name, u_year)
        sql = "insert into t7 values(%s, %s, %s)"
        cursor.execute(sql, param)
        conn.commit()

    conn.close()
    cursor.close()


if __name__ == '__main__':
    insert()
