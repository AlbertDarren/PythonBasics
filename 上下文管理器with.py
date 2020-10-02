#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/25 18:40
# @Author  : Jack Deng
# @File    : 上下文管理器with.py
# @Software: PyCharm
"""
with关键字，称为上下文管理器，很多需要手动关闭的连接，
比如 文件连接，socket连接，数据库连接都能使用with关键字自动关闭连接
with关键字后面的对象，需要实现__enter__()和__exit__()魔法方法
当执行进入with代码块时，会自动调用__enter__()方法
当with代码块执行结束，会自动调用__exit__()方法
"""


class Demo(object):
    def __enter__(self):
        print('enter方法被调用了')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit方法被调用了')


def create_obj():
    x = Demo()
    return x


with create_obj() as obj: # as 后面是变量名
    # 变量obj不是create_obj()函数的返回值，而是obj=create_obj().__enter__()
    print(obj)
