#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/22 09:00
# @Author  : Jack Deng
# @File    : 字符串常见的操作.py
# @Software: PyCharm
# 1.查找函数，find,index,rfind,rindex
# string = "hEllo woRld"
# print(string.find("l"))  # 2
# print(string.rfind("l"))  # 9
# print(string.index("l"))  # 2
# print(string.rindex("l"))  # 9
# 2.大小写相关函数,upper,lower.capitalize,title
# new_string1 = string.upper()
# print(new_string1)  # HELLO WORLD
# new_string2 = string.lower()
# print(new_string2)  # hello world
# new_string3 = string.capitalize()
# print(new_string3)  # Hello world
# new_string4 = string.title()
# print(new_string4)  # Hello World
# 3.字符集编码函数，encode,decode
chinese_string="你好世界"
byte=chinese_string.encode("utf8")
print(byte)
# b'\xe4\xbd\xa0\xe5\xa5\xbd\xe4\xb8\x96\xe7\x95\x8c'
print(byte.decode("gbk"))
# 浣犲ソ涓栫晫

