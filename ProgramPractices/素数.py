#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/21 18:48
# @Author  : Jack Deng
# @File    : 素数.py
# @Software: PyCharm
"""
背景：素数，也叫质数，指的是只能被1和本身整除的的自然数
    1既不是素数也不是合数
任务：找出给定范围内的所有质数
"""
start = int(input("请输入范围开始的自然数:"))
stop = int(input("请输入范围结束的自然数:"))
if start == 1:  # 单独考虑开始值为1的情况
    print("1既不是素数也不是合数")
    start += 1
for i in range(start, stop + 1):  # 遍历给定范围的所有自然数

    for j in range(2, int(i ** 0.5) + 1):
        # 遍历所有可能整除的数,注意一定要加1才可以取到最后一个数，
        # 比如 16**0.5=4，不加1取不到4
        if i % j == 0:  # 只要存在一个可以整除的数就终止内层循环
            # print(i, "是一个合数")
            break
    else:
        print(i, "是一个质数")
