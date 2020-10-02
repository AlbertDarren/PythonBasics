#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/20 08:58
# @Author  : Jack Deng
# @File    : inheritance_exercise.py
# @Software: PyCharm
"""
练习要求：
    建立一个汽车类Auto
    包括轮胎个数，汽车颜色，车身重量，速度等属性，并通过不同的构造方法创建实例。
    至少要求汽车能够加速,减速,停车。
    再定义一个小汽车类CarAuto继承Auto并添加空调、CD属性
    并且重新实现方法覆盖加速、减速的方法
"""


class Auto(object):
    def __init__(self, name: str, color: str, weight: float, speed: float, wheel_count=4):
        self.name = name
        self.wheel_count = wheel_count
        self.color = color
        self.weight = weight
        self.speed = speed

    def speed_up(self, speed):
        self.speed += speed
        return """
        车型：{},
        颜色:{},
        自重:{}T,
        车轮数:{}个,
        当前速度是:{}km/h""".format(self.name, self.color, self.weight, self.wheel_count, self.speed)

    def speed_down(self, speed):
        if self.speed >= speed:
            self.speed -= speed
            return """
        车型：{},
        颜色:{},
        自重:{}T,
        车轮数:{}个,
        当前速度是:{}km/h""".format(self.name, self.color, self.weight, self.wheel_count, self.speed)
        else:
            return '当前速度小于0，不合法'

    def stop(self):
        self.speed = 0
        return '车型：{},已经停车，当前速度是:{}'.format(self.name, self.speed)


class CarAuto(Auto):
    def __init__(self, name: str, color: str, weight: float, speed: float, air_conditioner, navigator, wheel_count=4):
        super().__init__(name, color, weight, speed, wheel_count)
        self.navigator = navigator
        self.air_conditioner = air_conditioner

    def speed_up(self, speed):
        return '空调品牌:{},导航系统是:{}'.format(self.air_conditioner, self.navigator) + super().speed_up(speed)

    def speed_down(self, speed):
        return '空调品牌:{},导航系统是:{}'.format(self.air_conditioner, self.navigator) + super().speed_down(speed)


auto1 = Auto(name='奔驰', color='Blue', weight=1.6, speed=100)
auto2 = Auto(name='本田', color='Red', weight=1.0, speed=30, wheel_count=3)
print(auto1.speed_down(20))
print(auto1.speed_up(20))
print(auto1.stop())
print(auto2.speed_down(20))
print(auto2.speed_up(20))
print(auto2.stop())
car_auto1 = CarAuto(name='大众', color='white', weight=7.0, speed=70, air_conditioner='美的', navigator='GPS')
car_auto2 = CarAuto(name='兰博基尼', color='yellow', weight=6.5, speed=300, air_conditioner='格力', navigator='北斗')
print(car_auto1.speed_up(20))
print(car_auto1.speed_down(40))
print(car_auto2.speed_up(100))
print(car_auto2.speed_down(200))
