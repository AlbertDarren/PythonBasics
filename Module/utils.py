#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/1 10:16
# @Author  : Jack Deng
# @File    : utils.py
# @Software: PyCharm

__all__ = ['e', 'pi', 'add', 'multiply', 'power']  # 限制*导入的内容


class Calculator(object):
    # 定义常用的数学常数值
    pi = 3.141592653589793
    e = 2.718281828459045

    @staticmethod
    def add(*args):
        my_sum = 0
        for arg in args:
            my_sum += arg
        return my_sum

    @staticmethod
    def multiply(*args):
        my_sum = 1
        for arg in args:
            my_sum *= arg
        return my_sum

    @staticmethod
    def power(base_num, index_num):
        return pow(base_num, index_num)


# 给所有类对象属性起一个别名，这样就可以直接通过模块访问
pi = Calculator.pi
e = Calculator.e
add = Calculator.add
multiply = Calculator.multiply
power = Calculator.power
