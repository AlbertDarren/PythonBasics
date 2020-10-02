#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/23 18:08
# @Author  : Jack Deng
# @File    : 求列表最大数及下标.py
# @Software: PyCharm

raw_list = [4, 7, 1, 9, 3, 0, 8]
# way1:使用builtin函数sorted,或者列表排序函数sort
# 浅拷贝一份列表数据
# list1=raw_list.copy()

# in an ascending order,默认升序排序
# list0.sort()
# print("列表最大数是:%d,下标是%d"%(list0[-1],list1.index(list0[-1])))

# in an descending order,改为降序排序
# list0.sort(reverse=True)
# print("列表最大数是:%d,下标是%d"%(list0[0],list1.index(list0[0])))

# way2:for...in enumerate循环,假设列表第一个最大，依次比较然后更新最大值和下标
# max_value=raw_list[0]
# max_index=0
# for index,item in enumerate(raw_list):
#     if item>max_value:
#         max_value = item
#         max_index = index
# print("列表最大数是:%d,下标是%d"%(max_value,max_index))

# way3:while循环，假设列表第一个最大，依次比较然后更新最大值和下标
# max_value = raw_list[0]# 假设第一个是最大值
# max_index = 0 # 假设第一个是最大值下标
# i = 0  # i变量控制循环结束
# while i < len(raw_list):
#     if raw_list[i] > max_value:
#         max_value = raw_list[i]
#         max_index = i
#     i += 1
#
# print("列表最大数是:%d,下标是%d" % (max_value, max_index))

