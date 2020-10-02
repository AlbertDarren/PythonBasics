#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/13 20:00
# @Author  : Jack Deng
# @File    : 私有属性.py
# @Software: PyCharm
class Student:

    def __init__(self, name: str, age: int, id: int):
        self.name = name
        self.age = age
        self.__id = id  # 以两个下划线开头的属性是私有属性，类体外部无法直接访问和修改

    def get_id(self):
        return self.__id

    def set_id(self, money):
        self.__id = money

    def __property(self): # 以两个下划线开始的函数是私有函数，只能在类体调用
        return '私有函数'


student = Student(name='zhangsan', age=18, id=511024)
# print(student.__id) # 这里运行报错

# 使用私有属性或者函数的方法
# 1.使用 对象名._类名__私有属性(函数)名 获取
# print(student._Student__id)
# print(student._Student__property())

# 2.定义set和get方法获取
# print(student.get_id())
# student.set_id(720)
# print(student.get_id())

# 3.使用property获取
