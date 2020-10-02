#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/21 21:32
# @Author  : Jack Deng
# @File    : 百马百担.py
# @Software: PyCharm
"""
百马百担问题：
假设，1匹大马担3担,1匹大马担2担,2匹小马担1担
如果100匹马担100，请问大马，中马，小马分别多少匹？
"""
# 穷举法
# 大马数量可能的范围
for bigHorse in range(0, 100 // 3 + 1):

    # 中马数量可能的范围
    for middleHorse in range(0, 100 // 2 + 1):
        # 小马数量
        smallHorse = (100 - bigHorse - middleHorse)
        if bigHorse * 3 + middleHorse * 2 + smallHorse * 0.5 == 100:
            print("大马:{}匹\n中马:{}匹\n小马:{}匹\n".format(bigHorse, middleHorse, smallHorse))
