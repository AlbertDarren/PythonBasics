#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/26 19:27
# @Author  : Jack Deng
# @File    : 常用的内置类和函数.py
# @Software: PyCharm

# 1.filter内置类,第一个参数是函数 or None，第二个是iterable
from functools import reduce

students = [
    {'name': '张三', 'age': 18, 'score': 98, 'tel': '1388888998', 'gender': 'female'},
    {'name': '李四', 'age': 28, 'score': 95, 'tel': '1388666666', 'gender': 'male'},
    {'name': '王五', 'age': 21, 'score': 97, 'tel': '1365588889', 'gender': 'unknown'},
    {'name': 'chris', 'age': 17, 'score': 58, 'tel': '13777775523', 'gender': 'male'},
    {'name': 'jack', 'age': 23, 'score': 52, 'tel': '13999999928', 'gender': 'female'},
    {'name': 'tony', 'age': 15, 'score': 98, 'tel': '1388888888', 'gender': 'unknown'},
    {'name': 'mary', 'age': 19, 'score': 93, 'tel': '1388885555', 'gender': 'unknown'}
]
# 将students删除未成年的学生
print(list(filter(lambda element: element['age'] > 18, students)))


list1=[2,5,7,9,1,0,20,17]
# 2.map内置类
print(list(map(lambda element: element + 2, list1)))
print(list1)
# 计算所有学生年龄之和
print(reduce(lambda x, y: x + y['age'], students, 0))
