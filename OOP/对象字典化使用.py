#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/12 12:59
# @Author  : Jack Deng
# @File    : 对象字典化使用.py
# @Software: PyCharm
class Person:
    """
    This is a customize class
    """

    def __init__(self, name: str, age: int, height: float):
        self.name = name
        self.age = age
        self.height = height

    def __setitem__(self, key, value):
        """
        1.self.key=value,会给对象增加一个属性并且赋值value
        2.self[key]=value,会出现超出递归深度的错误
        """
        self.__dict__[key] = value

    def __getitem__(self, item):
        return self.__dict__[item]

    def run(self):
        """
        自定义跑步方法
        """
        print(f'{self.name}正在跑步')


person1 = Person('Mary', 19, 1.75)
person2 = Person('Tom', 29, 1.90)
# 不能直接把对象当成字典使用,会报错，需要重写相关方法
# TypeError: 'Person' object does not support item assignment
# 解决：[]语法会自动调用对象的__setitem__魔术方法，可以重写该方法
# 1.__setitem__
# print(person1.name)  # 修改之前person1的name属性值为Mary
# person1['name'] = 'Jason'
# print(person1.name)  # 修改之后person1的name属性值Jason
#
# print(person2.age)  # 修改之前person2的age属性值为29
# person2['age'] = 32
# print(person2.age)  # 修改之后person2的age属性值32
# 2.__getitem__
# print(person1['name'])  # Mary
# print(person2['age'])  # 29
