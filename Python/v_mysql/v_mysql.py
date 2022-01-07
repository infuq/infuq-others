#! /usr/bin/env python

'''
pip install pymysql
'''


import pymysql
import random


def insert():
    conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="9527", db="test_2" )
    cursor=conn.cursor()

    for i in range(1,500000):
        
        user_id = random.randint(1, 500000)
        order_id = random.randint(1, 500000)
        order_status = random.randint(1, 3)
        param = (user_id, order_id, order_status)
        sql="insert into t_order(user_id, order_id, order_status, create_time) values(%s, %s, %s, now())"
        cursor.execute(sql, param)
        conn.commit()

    conn.close()
    cursor.close()


def insert2():
    conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="9527", db="test_2" )
    cursor=conn.cursor()

    for i in range(1,300000):
        
        order_id = random.randint(1, 500000)
        product_name = random.choice(('A', 'B', 'C', 'E', 'F'))
        param = (order_id, product_name)
        sql="insert into t_order_detail(order_id, product_name, create_time) values(%s, %s, now())"
        cursor.execute(sql, param)
        conn.commit()

    conn.close()
    cursor.close()


if __name__ == '__main__':
    insert2()