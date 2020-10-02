#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/3 20:22
# @Author  : Jack Deng
# @File    : self语句使用.py
# @Software: PyCharm

# 定义一个学生类，默认继承最终父类object
class Student(object):
    # 直接在类里面定义一个槽属性，是一个元组，用来规定对象可以存在的属性，限制动态属性可以添加的属性
    __slots__ = ('name', 'age', 'height')

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


# 分析此处代码执行情况
# 1.调用__new__(cls, *args, **kwargs)，申请一个内存空间
# 2.invoke __init__方法传入参数，让self指向申请好的内存空间
# 3.实例对象也指向同一个申请的内存空间
student1 = Student('jack', 21)
print(student1.age)

# 直接访问对象没有的属性会报错：AttributeError: 'Student' object has no attribute 'height'
# print(student1.height)
"""
python的动态属性
可以使用赋值运算符给一个属性赋值
student1.age = 30  # 如果对象有该属性则修改这个属性
print(student1.age)
student1.height = 170  # 如果对象没有该属性则添加这个属性并赋值
print(student1.height)
"""
