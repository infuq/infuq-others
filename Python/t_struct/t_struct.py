#! /usr/bin/env python

import struct

# 定长数据
data = struct.pack("2I3sI", 12, 22, b"xyz", 98)
decode = struct.unpack("2I3sI", data)
# print(decode)







# 变长字符串
str = "12345679abcdef这q"
# bs = bytes(str, 'utf-8')  # 转成字节
bs = str.encode('utf-8')  # 转成字节 maybe

# [4个字节存长度][数据]
data = struct.pack( "I%ds" % (len(bs),),    len(bs),          bs             )

size = struct.calcsize("I")# 计算一个整型的长度
(data_len,), data = struct.unpack("I", data[:size]),          data[size:]
print(data_len)
print(data.decode('utf-8'))






