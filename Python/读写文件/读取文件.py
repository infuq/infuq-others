#! /usr/bin/env python3.7
# -*- coding: UTF-8 -*-


with open('./info.txt','r') as f:
	info = f.read()
	print(info)

with open('./info.txt','r') as f:
	info = f.read(3)
	print(info)	
	info = f.read(3)
	print(info)

with open('./info.txt','r') as f:
	for line in f.readlines():
		print(line.strip())
		
# 读取二进制文件
f = open('./info.jpg','rb')


f = open('./info.txt','r',encoding='GBK')
