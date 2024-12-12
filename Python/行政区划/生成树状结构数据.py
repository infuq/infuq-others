#! /usr/bin/env python
# -*- coding:utf-8 -*-

import re

import pymysql
import requests
from lxml import etree


def conn_mysql():
    conn = pymysql.connect(host="rm-bp18623422m8o2n7x1o.mysql.rds.aliyuncs.com", port=3306, user="root", passwd="v12306#DB", db="db1")
    return conn


def tree():
    year = 2022
    conn = conn_mysql()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 查询省份
    sql = "SELECT * FROM db1.area where year = %s and level = 1 ORDER BY short_code"
    cursor.execute(sql, (year,))
    all_province = cursor.fetchall()

    tree_data =[]

    for province in all_province:
        province_node = {
            "value": province["code"],
            "label": province["short_name"],
        }

        # 查询省的孩子节点 = 地级市
        sql = "SELECT * FROM db1.area where year = %s AND parent_id = %s ORDER BY short_code"
        cursor.execute(sql, (year, province['id']))
        all_city = cursor.fetchall()
        if all_city is not None and len(all_city) > 0:
            province_node_children = []
            for city in all_city:
                city_node = {
                    "value": city["code"],
                    "label": city["short_name"],
                }

                # 查询地级市的孩子节点 = 区域
                sql = "SELECT * FROM db1.area where year = %s AND parent_id = %s ORDER BY short_code"
                cursor.execute(sql, (year, city['id']))
                all_region = cursor.fetchall()
                if all_region is not None and len(all_region) > 0:
                    city_node_children = []
                    for region in all_region:
                        region_node = {
                            "value": region["code"],
                            "label": region["short_name"],
                        }
                        city_node_children.append(region_node)
                    city_node['children'] = city_node_children

                province_node_children.append(city_node)

            province_node['children'] = province_node_children

        tree_data.append(province_node)

    print(tree_data)

if __name__ == '__main__':
    tree()




