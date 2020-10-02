#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/23 15:34
# @Author  : Jack Deng
# @File    : bubble_sort_optimization.py
# @Software: PyCharm
raw_list = [2, 1, 3, 8, 5, 12, 9, 7, 6, 4]
"""
没有优化前，比较次数为(len(raw_list) - 1)**2,即81次
优化：
1.每次排序多交换的次数，优化后45次
   执行：346 µs ± 4.54 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
2.已排好序减少后续排序，优化后63次
   执行：The slowest run took 4.39 times longer than the fastest. 
        This could mean that an intermediate result is being cached.
        1 ms ± 614 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
3.同时优化后次数为,42次
    执行：382 µs ± 57.9 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
"""
j = 0
count = 0
while j < len(raw_list) - 1:
    i = 0
    flag = True  # 假设本次排序没有发生一次交换
    while i < len(raw_list) - 1-j :  # 减少每次排序多交换的次数
        count += 1  # 计数，每次比较加1
        if raw_list[i] > raw_list[i + 1]:
            flag = False  # 只要发生一次排序说明假设不成立
            raw_list[i], raw_list[i + 1] = raw_list[i + 1], raw_list[i]
        i += 1
    if flag:
        break
    j += 1
print(raw_list)
print("一共比较了%d次" % count)
