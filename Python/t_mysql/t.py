#! /usr/bin/env python

"""
pip install pymysql
"""

"""
文章地址
https://www.infuq.com/manual/db/MySQL_EXPLAIN.html
"""

import pymysql
import random


def insert():
    conn = pymysql.connect(host="172.31.3.199", port=3306, user="root", passwd="9527", db="db1")
    cursor = conn.cursor()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor) # 得到的数据会以{'字段':数据}形式输出


    for i in range(1, 1900000):
        _id = i
        u_id = i + random.randint(2, 9)
        order_id = i + random.randint(12, 19)
        u_name = 'U' + str(i)
        # status = random.choice(('chengdu', 'hangzhou', 'Nanjing', 'shanghai', 'Jinan'))
        if i % 3000 == 0:
            status = random.choice((1,))
        else:
            status = random.choice((3,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3))
        param = (_id, u_id, u_name, order_id, status, 0)
        sql = "insert into t_order_2(id,user_id,user_name,order_id,order_status,is_deleted) values(%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, param)
        conn.commit()

    conn.close()
    cursor.close()



if __name__ == '__main__':
    insert()
