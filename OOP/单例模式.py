#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/16 08:15
# @Author  : Jack Deng
# @File    : 单例模式.py
# @Software: PyCharm


class Singleton:
    __instance = None  # 私有类属性，只能在本类中使用
    __is_first = True
    __count = 0  # 创建一个私有类属性，统计创建对象的数目，防止在类对象以外修改

    def __new__(cls, *args, **kwargs):
        cls.__count += 1
        if cls.__instance is None:
            # 使用object.__new__申请内存，创建对象，并把对象的类型设置为cls
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, name: str, age: int):
        # 判断是否是第一次创建对象，
        if self.__is_first:  # 由于第一次对象创建以后没有属性__is_first，所以此处__is_first为类属性
            self.name = name
            self.age = age
            self.__is_first = False  # self新建一个属性__is_first，指向False，第二次以后就不会再覆盖原先对象的属性

    @classmethod
    def get_count(cls):
        return cls.__count


# 使用类创建对象时，先调用__new__方法申请内存，然后调用__init__方法为对象分配属性
# 重写new方法可以实现单例模式,也就是在本文件全局只有一个对象，第一次以后创建对象都只会覆盖原先对象的属性，内存地址不变
singleton1 = Singleton(age=18, name='linda')
singleton2 = Singleton(age=20, name='jerry')
print(singleton1 is singleton2, id(singleton1), id(singleton2))
print(singleton1.age, singleton2.age)
print(Singleton.get_count())