#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/19 10:17
# @Author  : Jack Deng
# @File    : 打开文件.py
# @Software: PyCharm

# python使用内置函数open打开并操作一个指定文件
# 在Windows操作系统里面打开文件默认使用gbk编码格式打开，open函数打开文件最好指定编码格式
# 1.使用相对路径打开
# file_obj = open('操作文件', encoding='utf8')
# import os
#
# print(os.sep)  # 获得操作系统里面文件夹中间使用的分隔符，这里使用的是Windows操作系统，使用 \ 反斜杠分隔符
"""
在python的字符串里面，\ 反斜杠表示转义，所以会造成报错
"""

"""
一，路径书写的三种方式：
    1.'//'
    2.r'\'
    3.'/'(推荐使用这种方式兼容性好)
二，路径类型
    1.相对路径(推荐使用)
    2.绝对路径
"""
file_obj1 = open(r'/pythonProject/Data/FileOperation/操作文件', encoding='utf8')
file_obj2 = open('/pythonProject/Data/FileOperation/操作文件', encoding='utf8')
file_obj3 = open('/pythonProject/Data/FileOperation/操作文件', encoding='utf8')
print(file_obj1.readline(1))
print(file_obj2.readline(2))
print(file_obj2.readline(3))

file_obj1.close()
file_obj2.close()
file_obj3.close()
