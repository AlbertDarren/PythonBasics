#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/16 09:45
# @Author  : Jack Deng
# @File    : python语言继承特点.py
# @Software: PyCharm
"""
面向对象三大特征：封装，继承，多态
"""


class A:  # 如果不写父类，python3以后默认继承object类
    @staticmethod
    def a():
        print('我是A类的a方法')


class B(object):
    @staticmethod
    def b():
        print('我是B类的b方法')

    @staticmethod
    def a():
        print('我是B类的a方法')


# python支持多继承
class C(A, B):  # 让C类继承A类和B类
    @staticmethod
    def c():
        print('我是C类的c方法')


c_object = C()
# 多继承里面，如果多个父类有同名方法，有一个类属性__mro__,方法解析顺序可以查看方法调用顺序
print(C.__mro__)  # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
c_object.a()  # 调用父类A的方法a
c_object.b()  # 调用父类B的方法b
