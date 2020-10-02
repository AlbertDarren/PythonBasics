#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/26 18:20
# @Author  : Jack Deng
# @File    : sort方法高级使用.py
# @Software: PyCharm
# 声明一个列表,在列表中保存6个学生的信息(6个字典)
students = [
    {'name': '张三', 'age': 18, 'score': 98, 'tel': '1388888998', 'gender': 'female'},
    {'name': '李四', 'age': 28, 'score': 95, 'tel': '1388666666', 'gender': 'male'},
    {'name': '王五', 'age': 21, 'score': 97, 'tel': '1365588889', 'gender': 'unknown'},
    {'name': 'chris', 'age': 17, 'score': 58, 'tel': '13777775523', 'gender': 'male'},
    {'name': 'jack', 'age': 23, 'score': 52, 'tel': '13999999928', 'gender': 'female'},
    {'name': 'tony', 'age': 15, 'score': 98, 'tel': '1388888888', 'gender': 'unknown'},
    {'name': 'mary', 'age': 19, 'score': 93, 'tel': '1388885555', 'gender': 'unknown'}
]
# 将列表按学生成绩从大到小排序
# 使用匿名函数接收遍历列表的参数(字典)，根据字典的指定键进行比较从而排序
students.sort(key=lambda element:element['score'])
# *students，将students拆包为单个元素逐个打印换行输出
print(*students,sep='\n')