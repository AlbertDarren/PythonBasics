#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/27 15:10
# @Author  : Jack Deng
# @File    : 高阶函数及应用.py
# @Software: PyCharm

"""
# 1.一个函数接收另一个函数作为参数，此处不讲

# 2.一个函数返回另一个函数
def outer1():
    print('我是外层函数outer1')

    def inner1():
        print('我是内层函数inner1')
        return 'inner1执行结束'

    return inner1


# 调用内层函数
print(outer1()())
# 我是外层函数outer1
# 我是内层函数inner1
# inner1执行结束
# 3.一个函数内部定义另一个函数
def outer2():
    print('我是外层函数outer2')

    def inner2():
        print('我是内层函数inner2')
"""
# 应用：得到一段代码执行平均时间
import time


def calc_time(fn, count=100, digits=6):
    """
    得到一个函数执行count次的平均时间
    :param fn: 函数
    :param count: 执行次数,默认100次
    :param digits: 执行时间保留小数点后位数，默认6位
    :return: 函数执行平均时间
    """
    start_time = time.time()
    for i in range(count):
        fn()
    end_time = time.time()
    return '函数{}执行{}次平均时间是：{}'.format(fn.__name__,count, round((end_time - start_time) / count, ndigits=digits))


def demo():
    x = 0
    for i in range(10000):
        x += i
    return x


print(calc_time(demo,200))
# 函数demo执行200次平均时间是：0.000671
