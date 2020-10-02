#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/25 15:56
# @Author  : Jack Deng
# @File    : exercise1.py
# @Software: PyCharm
"""
定义一个点类pointer
属性是横向坐标×与纵向坐标y
定义一个圆类circle
属性有圆心点cp 与半径radius
方法有∶
    1.求圆的面积
    2。求圆的周长
    3.求指定点与圆的关系
提示:关系有三种【圆内 圆外  圆上】
    涉及到的数学公式∶指定点与圆心点之间的距离与圆的半径进行比较
"""
from math import pi, sqrt, pow


class Pointer(object):
    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def coordinate(self):
        return self.x_coordinate, self.y_coordinate


class Circle(object):
    def __init__(self, cp: Pointer, radius):
        self.radius = radius
        self.cp = cp

    def get_area(self):
        return pi * self.radius ** 2

    def get_perimeter(self):
        return pi * self.radius * 2

    def relationship(self, dot: Pointer):
        """
        返回指定点和圆的位置关系
        :param dot:指定点
        :return:位置关系,有三种--圆内  圆外  圆上
        """
        distance = sqrt(
            pow((dot.x_coordinate - self.cp.x_coordinate), 2) + pow((dot.y_coordinate - self.cp.y_coordinate), 2))
        if distance < self.radius:
            result = '内'
        elif distance == self.radius:
            result = '上'
        else:
            result = '外'
        return '点{}在半径为:{},圆心为:{}的圆{}'.format(dot.coordinate(), self.radius, self.cp.coordinate(),result)


cp = Pointer(x_coordinate=3, y_coordinate=5)
circle = Circle(cp, 3)
print('圆面积是:{},圆周长是:{}'.format(circle.get_area(), circle.get_perimeter()))
point1 = Pointer(x_coordinate=1, y_coordinate=2)
print(circle.relationship(point1))
point2 = Pointer(x_coordinate=2, y_coordinate=4)
print(circle.relationship(point2))
point3 = Pointer(x_coordinate=0, y_coordinate=5)
print(circle.relationship(point3))
