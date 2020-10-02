#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/26 18:32
# @Author  : Jack Deng
# @File    : 函数多返回值.py
# @Software: PyCharm

# 定义一个两个返回值的函数
def div_mod(number1: int, number2: int):
    """
    返回；两个整数的商和余数
    :param number1: 第一个整数
    :param number2: 第二个整数
    :return: 商，余数
    """
    return number1 // number2, number1 % number2


print(div_mod(14, 3))