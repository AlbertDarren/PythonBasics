#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/12 12:29
# @Author  : Jack Deng
# @File    : 内置属性.py
# @Software: PyCharm
class Person:
    """
    This is a customize class
    """
    def __init__(self, name: str, age: int, height: float):
        self.name = name
        self.age = age
        self.height = height

    def run(self):
        """
        自定义跑步方法
        """
        print(f'{self.name}正在跑步')


person = Person('Mary', 19, 1.75)
# dir内置方法，返回对象的所有属性(方法也可以理解为属性，对应一个函数)
# print(dir(person))  # 双下划线开头结尾的属性是内置属性
"""
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', 
'__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', 
'__subclasshook__', '__weakref__', 'age', 'height', 'name', 'run'] 
"""
# print(person.__class__)  # 返回对象的类型,<class '__main__.Person'>

# print(person.__dict__)  # 返回对象属性和对应值形成的字典, {'name': 'Mary', 'age': 19, 'height': 1.75}

# __doc__属性返回,类,对象或者其属性的注释文档
# print(person.__doc__)
# print(Person.__doc__)
# print(person.run.__doc__)
print(range.__doc__)
"""
range(stop) -> range object
range(start, stop[, step]) -> range object

Return an object that produces a sequence of integers from start (inclusive)
to stop (exclusive) by step.  range(i, j) produces i, i+1, i+2, ..., j-1.
start defaults to 0, and stop is omitted!  range(4) produces 0, 1, 2, 3.
These are exactly the valid indices for a list of 4 elements.
When step is given, it specifies the increment (or decrement).
"""