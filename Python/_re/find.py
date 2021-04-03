#! /usr/bin/env python3.7
# -*- coding:utf-8 -*-

import re

# 闲谈式讲课风格
# 个人站点: https://www.infuq.com/
# 个人公众号: Netty历险记

if __name__ == '__main__':
    '''
    前提: 对正则有一定基础
    目的: 获取字符串中的abc(包括连续).   abc abcabc abcabcabc ...
    期望结果: abcabcabc abc
    '''

    data = 'abcabcabcxyz123abc'

    ret = re.findall(r'(abc)+', data)
    print(ret)
    ret = re.findall(r'(?:abc)+', data)
    print(ret)



    '''
    目的: 获取字符串中的数字和python关键字
    '''
    #
    # data = 'python-123xyz-python-google-456-mysql-python-git-789-oracle-python-tomcat'
    #
    # ret = re.findall(r'(\d+).*?(python)+', data)
    # print(ret)

    # pattern = re.compile(r'(\d+).*?(python)+')
    # ret = pattern.findall(data)
    # print(ret)

