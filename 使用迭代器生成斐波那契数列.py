#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/27 17:16
# @Author  : Jack Deng
# @File    : 使用迭代器生成斐波那契数列.py
# @Software: PyCharm
class Fibonacci(object):
    def __init__(self, n):
        """
        初始化对象的属性
        :param n: Fibonacci数列的前n项
        """
        self.n = n
        self.number1 = self.number2 = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count <= self.n:
            temp = self.number1
            self.number1, self.number2 = self.number2, self.number1 + self.number2
            return temp
        else:
            raise StopIteration


for num in Fibonacci(30000):
    print(num)
