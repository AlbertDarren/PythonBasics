#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/24 18:28
# @Author  : Jack Deng
# @File    : 向内存中写入数据.py
# @Software: PyCharm
"""
需要使用两个类StringIO, BytesIO
"""
from io import StringIO, BytesIO

# StringIO
# 写法1
# 创建字符串流对象
str_stream = StringIO()
# 向内存写入字符串数据
str_stream.write('Hello World!')
str_stream.write('I\'m Python!')
# print函数的file参数需要一个文件流对象，默认是sys.stdout，这里指定为str_stream
print('a general purpose programming language', file=str_stream)
# 从内存中取出数据
print(str_stream.getvalue())
str_stream.close()

# 写法2
# 创建字符串流对象
with StringIO() as stream:
    # 向内存写入字符串数据
    stream.write('Hello World!')
    stream.write('I\'m Python!')
    # print函数的file参数需要一个文件流对象，默认是sys.stdout，这里指定为str_stream
    print('a general purpose programming language', file=stream)
    # 从内存中取出数据
    print(stream.getvalue())

#  BytesIO
# 写法1
# 创建字节流对象
bytes_stream = BytesIO()
# 向内存写入字节数据
bytes_stream.write('愿得一人心'.encode('utf8'))  # 一个中文字符对应 3 bytes,30个16进制位
# 从内存中取出数据
print(bytes_stream.getvalue())
bytes_stream.close()

# 写法2
# 创建字节流对象
with BytesIO() as stream:
    # 向内存写入字节数据
    stream.write('愿得一人心'.encode('utf8'))  # 一个中文字符对应 3 bytes,30个16进制位
    # 从内存中取出数据
    print(stream.getvalue())