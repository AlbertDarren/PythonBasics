#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/27 19:01
# @Author  : Jack Deng
# @File    : 装饰器.py
# @Software: PyCharm
# 应用：得到一段代码执行平均时间


def calc_time(fn):  # 第二步被装饰函数指向fn,即fn=demo
    """
    得到一个函数执行count次的平均时间
    :param fn: 函数
    :return: 函数执行平均时间
    """
    print('外部函数开始执行')

    def wrapper(max_value, count=100, digits=6, *args, **kwargs):
        import time
        start_time = time.time()
        for i in range(count):
            result = fn(max_value)
        end_time = time.time()
        return '函数{}执行{}次平均时间是：{}'.format(fn.__name__, count, round((end_time - start_time) / count, ndigits=digits))

    return wrapper  # 第三步返回wrapper给demo,即demo=wrapper


@calc_time  # 第一步执行cal_time
def demo(max_value):
    x = 0
    for i in range(max_value):
        x += i
    return x


print(demo.__name__)  # 相当于调用wrapper
print(demo(10000, count=200))
# 外部函数开始执行
# 函数demo执行200次平均时间是：0.000587
