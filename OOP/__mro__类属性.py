#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/16 10:13
# @Author  : Jack Deng
# @File    : __mro__类属性.py
# @Software: PyCharm
class A:
    pass


class B:
    def foo(self):
        print('我是B类的foo方法')


class C(A):
    def foo(self):
        print('我是C类的foo方法')


class D(B):
    pass


class Final(D, C):
    pass


final = Final()
# 调用foo方法，输出：我是B类的foo方法，说明深度优先
final.foo()
# 查看类属性mro解析方法foo的顺序
print(Final.__mro__)
"""
(<class '__main__.Final'>, <class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
"""