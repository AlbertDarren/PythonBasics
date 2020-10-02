#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/24 09:41
# @Author  : Jack Deng
# @File    : 深拷贝和浅拷贝.py
# @Software: PyCharm
import copy

fruits = ['apple', 'pear', 'orange', ['banana', 'grape', 'watermelon'], 'cherry', 'lemon']
# 1.赋值不是浅拷贝或者深拷贝，仅仅是一个指向
# new_fruits = fruits
# fruits[0]='pineapple'
# print(new_fruits)
"""
输出结果：['pineapple', 'pear', 'orange', ['banana', 'grape', 'watermelon'], 'cherry', 'lemon']
"""

# fruits[3][1]='blueberry'
# print(new_fruits)
"""
输出结果：['apple', 'pear', 'orange', ['banana', 'blueberry', 'watermelon'], 'cherry', 'lemon']
"""

# 2.浅拷贝,可以理解为只拷贝一层，深层的只做赋值指向，不拷贝
# fruits_shallow_copy1 = fruits.copy()
# fruits_shallow_copy2 = fruits[::]
# fruits_shallow_copy3 = copy.copy(fruits)

# fruits[0]='pineapple'
# print(fruits_shallow_copy1, fruits_shallow_copy2,fruits_shallow_copy3,sep='\n')
"""
输出结果：
['apple', 'pear', 'orange', ['banana', 'grape', 'watermelon'], 'cherry', 'lemon']
['apple', 'pear', 'orange', ['banana', 'grape', 'watermelon'], 'cherry', 'lemon']
['apple', 'pear', 'orange', ['banana', 'grape', 'watermelon'], 'cherry', 'lemon']
"""

# fruits[3][1]='blueberry'
# print(fruits_shallow_copy1, fruits_shallow_copy2,fruits_shallow_copy3,sep='\n')
"""
输出结果：
['apple', 'pear', 'orange', ['banana', 'blueberry', 'watermelon'], 'cherry', 'lemon']
['apple', 'pear', 'orange', ['banana', 'blueberry', 'watermelon'], 'cherry', 'lemon']
['apple', 'pear', 'orange', ['banana', 'blueberry', 'watermelon'], 'cherry', 'lemon']
"""
# 3.深拷贝，完全拷贝，深层的也拷贝
fruits_deepcopy = copy.deepcopy(fruits)
# fruits[0]='pineapple'
# print(fruits_deepcopy)
"""
['apple', 'pear', 'orange', ['banana', 'grape', 'watermelon'], 'cherry', 'lemon']
"""
fruits[3][1]='blueberry'
print(fruits_deepcopy)
"""
['apple', 'pear', 'orange', ['banana', 'grape', 'watermelon'], 'cherry', 'lemon']
"""