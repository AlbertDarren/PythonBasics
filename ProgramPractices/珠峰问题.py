#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/21 21:47
# @Author  : Jack Deng
# @File    : 珠峰问题.py
# @Software: PyCharm
"""
问题：现在有一张0.08mm厚的纸张，请问对折多少次可以达到珠峰高度8844.13m
"""
height = 0.08 / 1000  # 统一单位为米
count = 0  # 初始化次数为0
while 1:
    height *= 2
    count += 1
    if height >= 8844.13:
        break
print(f"一张0.08mm厚的纸张，对折{count}次可以达到珠峰高度8844.13m")
