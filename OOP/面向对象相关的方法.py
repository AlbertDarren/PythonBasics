#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/17 09:55
# @Author  : Jack Deng
# @File    : 面向对象相关的方法.py
# @Software: PyCharm
class Animal(object):
    pass


class Living:
    pass


class Person(Animal, Living):
    pass


obj1 = Animal()
obj2 = Person()
"""
    isinstance,判断一个对象是否是指定类或者其子类创建的实例对象
    Return whether an object is an instance of a class or of a subclass thereof.

    A tuple, as in ``isinstance(x, (A, B, ...))``, may be given as the target to
    check against. This is equivalent to ``isinstance(x, A) or isinstance(x, B)
    or ...`` etc.
"""
print(isinstance(obj1, Animal))
print(isinstance(obj2, Animal))
print(isinstance(obj2, Living))
print(isinstance(obj2, (Animal,Living)))
"""
    issubclass,判断一个类是否是指定类的子类或者本类
    Return whether 'cls' is a derived from another class or is the same class.

    A tuple, as in ``issubclass(x, (A, B, ...))``, may be given as the target to
    check against. This is equivalent to ``issubclass(x, A) or issubclass(x, B)
    or ...`` etc.
"""
print(issubclass(Person, Animal))
print(issubclass(Person, Living))
print(issubclass(Person, (Animal,Living)))