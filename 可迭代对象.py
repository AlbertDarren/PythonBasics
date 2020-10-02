#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/26 11:06
# @Author  : Jack Deng
# @File    : 可迭代对象.py
# @Software: PyCharm
"""
系统有很多内置可迭代类对象，list/tuple/dict/set/filter/map/str/range
也可以自定义一个可迭代类对象，需要重写__iter__魔术方法
"""
from collections.abc import Iterable


class MyIter(object):
    def __init__(self, iter_count, iter_content):
        self.iter_count = iter_count
        self.iter_content = iter_content

    def __iter__(self):  # 只要重写__iter__方法就是可迭代对象
        return self

    def __next__(self):
        if self.iter_count > 0:
            self.iter_count -= 1
            return self.iter_content
        else:
            raise StopIteration


"""
for. . .in循环的本质就调用对象的__iter__方法，获取到这个方法的返回值
这个返回值需要是一个对象，然后再调用这个对象__next__方法
"""
for i in MyIter(10, 'hello'):
    print(i)
