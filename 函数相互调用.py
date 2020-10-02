#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/25 21:21
# @Author  : Jack Deng
# @File    : 函数相互调用.py
# @Software: PyCharm

# 定义一个求阶乘的函数，e.g.输入3，得到3！
def factorial(number: int):
    product = 1
    for i in range(1, number + 1):
        product *= i
    return product


# 调用函数factorial
print('5的阶乘为{}'.format(factorial(5)))


# 定义一个求阶乘之和的函数,e.g. 输入3，得到 1！+2！+3！的结果
def factorial_sum(number: int):
    product = 0
    for i in range(1, number + 1):
        product += factorial(i)
    return product


# 调用函数factorial_sum
print('1-5的阶乘之和为{}'.format(factorial_sum(5)))
