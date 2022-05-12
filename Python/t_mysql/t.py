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

    for i in range(100003, 200000):
        _id = i
        u_id = i + random.randint(2, 9)
        u_name = 'U' + str(i)
        u_year = random.randint(2021, 2030)
        u_address = random.choice(('chengdu', 'hangzhou', 'Nanjing', 'shanghai', 'Jinan'))
        param = (_id, u_id, u_name, u_year, u_address)
        sql = "insert into t values(%s, %s, %s, %s, %s)"
        cursor.execute(sql, param)
        conn.commit()

    conn.close()
    cursor.close()


if __name__ == '__main__':
    insert()
