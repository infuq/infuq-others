#! /usr/bin/env python
# -*- coding:utf-8 -*-

import re

import pymysql
import requests
from lxml import etree


# 仅数字
def is_only_digits(code):
    return re.fullmatch(r'\d+', code) is not None

# 省份
def is_province(code):
    return re.fullmatch(r'^\d{2}0000$', code) is not None

# 地级市
def is_city(code):
    return re.fullmatch(r'^\d{4}00$', code) is not None

# 直辖市: 北京市 天津市 上海市
def is_direct_province(province):
    return province == '11' or province == '12' or province == '31'

# 自治区: 内蒙古自治区 广西壮族自治区 西藏自治区 宁夏回族自治区 新疆维吾尔自治区
def is_self_direct_province(province):
    return province == '15' or province == '45' or province == '54' or province == '64' or province == '65'


def conn_mysql():
    conn = pymysql.connect(host="rm-bp18623422m8o2n7x1o.mysql.rds.aliyuncs.com", port=3306, user="root", passwd="v12306#DB", db="db1")
    return conn


def query(url):
    response = requests.get(url)
    response.encoding = 'utf-8'

    html_tree = etree.HTML(response.text)
    all_tr = html_tree.xpath('//table/tr')
    # 所有tr
    for tr in all_tr:
        # 单个tr下所有td的文本
        pair = tr.xpath('td/text()')

        if pair is None:
            continue
        if len(pair) != 2:
            continue

        code = pair[0]
        name = pair[1]

        if code is not None:
            code = code.rstrip()
        if name is not None:
            name = name.rstrip()

        if not is_only_digits(code):
            continue

        # 依次判断行政区划代码属于`省->地级市->区`哪一个
        if is_province(code):
            yield code, name, 1
        elif is_city(code):
            yield code, name, 2
        else:
            yield code, name, 3


def handle(url):
    conn = conn_mysql()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 遍历行政区划
    for data in query(url):
        code = data[0]
        name = data[1]
        level = data[2]

        # 省
        if level == 1:
            pass
            # handle_province(code, name, cursor, conn)
        # 地级市
        elif level == 2:
            pass
            # handle_city(code, name, cursor, conn)
        # 区
        elif level == 3:
            # pass
            handle_region(code, name, cursor, conn)


# 例如河北省 130000
def handle_province(code, name, cursor, conn):
    level = 1
    parent_id = -1

    short_code = code[0:2]
    province = code[0:2]

    if is_direct_province(province):  # 直辖市
        desc = "直辖市"

        sql = "INSERT INTO area(short_code,code,short_name,name,level,year,parent_id,description) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, (short_code, code, name, name, level, year, parent_id, desc))
        conn.commit()
    elif is_self_direct_province(province):
        desc = "自治区"

        sql = "INSERT INTO area(short_code,code,short_name,name,level,year,parent_id,description) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, (short_code, code, name, name, level, year, parent_id, desc))
        conn.commit()
    else:
        desc = "省"

        sql = "INSERT INTO area(short_code,code,short_name,name,level,year,parent_id,description) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, (short_code, code, name, name, level, year, parent_id, desc))
        conn.commit()


# 例如石家庄市 130100
def handle_city(code, name, cursor, conn):

    level = 2

    province = code[0:2]
    # 查询省份
    sql = "SELECT * FROM area WHERE short_code = %s AND year = %s"
    cursor.execute(sql, (province,year))
    all_data = cursor.fetchall()
    # 省份主键
    province_id = all_data[0]['id']
    province_name = all_data[0]['name']

    sql = "INSERT INTO area(short_code,code,short_name,name,level,year,parent_id) values(%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(sql, (code[0:4], code, name, province_name + "/" + name, level, year, province_id))
    conn.commit()


# 例如长安区 130102
def handle_region(code, name, cursor, conn):
    level = 3

    province = code[0:2]
    city = code[0:4]

    # 区挂靠直辖市
    if is_direct_province(province): # 直辖市
        # 查询直辖市
        sql = "SELECT * FROM area WHERE short_code = %s AND year = %s"
        cursor.execute(sql, (province,year))
        all_data = cursor.fetchall()
        # 直辖市主键
        province_id = all_data[0]['id']
        province_name = all_data[0]['name']

        sql = "INSERT INTO area(short_code,code,short_name,name,level,year,parent_id,description) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, (code, code, name, province_name + "/" + name, level, year, province_id, "直辖市管辖"))
        conn.commit()

    else:
        # 查询地级市
        sql = "SELECT * FROM area WHERE short_code = %s AND year = %s"
        cursor.execute(sql, (city,year))
        all_data = cursor.fetchall()

        # 未查询到地级市, 少数情况, 区挂靠省
        if all_data is None or len(all_data) < 1:
            # 查询省份
            sql = "SELECT * FROM area WHERE short_code = %s AND year = %s"
            cursor.execute(sql, (province,year))
            all_data = cursor.fetchall()
            # 省份主键
            province_id = all_data[0]['id']
            province_name = all_data[0]['name']

            sql = "INSERT INTO area(short_code,code,short_name,name,level,year,parent_id,description) values(%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, (code, code, name, province_name + "/" + name, level, year, province_id, "区挂靠省"))
            conn.commit()

        # 多数情况, 区挂靠地级市
        else:
            # 地级市主键
            city_id = all_data[0]['id']
            city_name = all_data[0]['name']

            sql = "INSERT INTO area(short_code,code,short_name,name,level,year,parent_id) values(%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, (code, code, name, city_name + "/" + name, level, year, city_id))
            conn.commit()



if __name__ == '__main__':
    year = 2002
    url = 'https://www.mca.gov.cn/mzsj/tjbz/a/201713/201708220927.html'
    handle(url)

