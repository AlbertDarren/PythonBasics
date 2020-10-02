#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/25 21:19
# @Author  : Jack Deng
# @File    : 自定义异常.py
# @Software: PyCharm
"""
写一个自定义异常类继承Exception,并且重新两个魔术方法__init__和__str__，在需要抛出异常的位置使用raise关键字抛出异常
"""


class LengthError(Exception):
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def __str__(self):
        return '用户名长度必须在{}和{}之间'.format(self.min_length, self.max_length)


user_name = input('请输入用户名，注意长度必须在6-12之间:')
min_value = 6
max_value = 12
if min_value <= len(user_name) <= max_value:
    print('用户名正确')

else:
    raise LengthError(min_value, max_value)
