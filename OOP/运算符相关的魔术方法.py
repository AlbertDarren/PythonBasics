#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/7 14:11
# @Author  : Jack Deng
# @File    : 运算符相关的魔术方法.py
# @Software: PyCharm
class Student:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __eq__(self, other):  # 重写这个方法，实现满足要求的判断
        return self.name == other.name and self.age == other.age

    def __ne__(self, other):  # 使用!=关系运算符，本质上是调用not equal魔术方法或者equal取反
        return self.age != other.age

    def __gt__(self, other):  # 使用>关系运算符，本质上调用该方法greater than
        return self.age > other.age

    def __ge__(self, other):  # 使用>=关系运算符，本质上调用该方法greater than or equal
        return self.age >= other.age

    def __lt__(self, other):  # 使用<关系运算符，本质上调用该方法less than
        return self.age < other.age

    def __le__(self, other):  # 使用<=关系运算符，本质上调用该方法less than or equal
        return self.age <= other.age


student1 = Student('张三', 20)
student2 = Student('李四', 30)
# # is 身份运算符，判断内存地址是否相同，返回True or False
# # 因为每次实例化一个对象都要先调用__new__方法，申请内存空间，所以下面比较结果是False
# print(student1 is student2)
# # == 关系运算符，本质上是调用对象的__eq__方法，相当于student1.__eq(student2)，默认比较内存地址，所以下面比较结果是False
# # 重写这个方法以后结果就是True
# print(student1 == student2)

# 创建两个内容相同的列表，其实内存地址不相同
# list1 = [1, 2, 3]
# list2 = [1, 2, 3]
# print(list1.__eq__(list2),list1==list2)

# 创建两个内容相同的字符串，内存地址相同
# str1='h'
# str2='h'
# print(id(str1), id(str2))
# print(str1.__eq__(str2),str1==str2,str1 is str2) # True True True
