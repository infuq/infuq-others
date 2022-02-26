#! /usr/bin/env python

"""
pip install pymysql
"""

"""
CREATE TABLE `t_order` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `order_id` int DEFAULT NULL,
  `order_status` tinyint DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

CREATE TABLE `t_order_detail` (
  `id` int NOT NULL AUTO_INCREMENT,
  `order_id` int DEFAULT NULL,
  `product_name` varchar(100) DEFAULT NULL,
  `create_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
"""

import pymysql
import random


def insert_order():
    conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="9527", db="db0")
    cursor = conn.cursor()

    for i in range(1, 10000):
        
        user_id = random.randint(1, 500000)
        order_id = random.randint(1, 500000)
        order_status = random.randint(1, 3)
        param = (user_id, order_id, order_status)
        sql = "insert into t_order(user_id, order_id, order_status, create_time) values(%s, %s, %s, now())"
        cursor.execute(sql, param)
        conn.commit()

    conn.close()
    cursor.close()


def insert_order_detail():
    conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="9527", db="db0")
    cursor = conn.cursor()

    for i in range(1,300000):
        
        order_id = random.randint(1, 500000)
        product_name = random.choice(('A', 'B', 'C', 'E', 'F'))
        param = (order_id, product_name)
        sql = "insert into t_order_detail(order_id, product_name, create_time) values(%s, %s, now())"
        cursor.execute(sql, param)
        conn.commit()

    conn.close()
    cursor.close()


if __name__ == '__main__':
    insert_order_detail()
