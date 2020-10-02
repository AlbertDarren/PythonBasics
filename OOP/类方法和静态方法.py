#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/14 08:45
# @Author  : Jack Deng
# @File    : 类方法和静态方法.py
# @Software: PyCharm
class Person:
    country = 'China'

    def __init__(self, name: str, age: int, weight: float) -> None:
        super().__init__()
        self.name = name
        self.age = age
        self.__weight = weight  # 私有属性

    def eat(self, food):  # 这是一个对象方法，保存在类对象里，但是每个对象都绑定一个不同的eat方法
        print('{}正在吃{}'.format(self.name, food))

    @staticmethod
    def static_method():  # 如果一个方法里面没有使用任何实例对象的属性，建议定义为static方法
        print('hello')

    @classmethod
    def class_method(cls):  # 如果一个方法只用到了类属性，可以定义为类方法,cls指的是类对象，不需要手动传参
        return cls.country


person1 = Person('张三', 20, 144.5)
person2 = Person('李四', 32, 178.5)
"""
对象方法，保存在类对象里，但是每个对象都绑定一个不同的eat方法
"""
# print(person1.eat is person2.eat)  # False
# print(person1.eat == person2.eat)  # False
# print(person1.eat)  # <bound method Person.eat of <__main__.Person object at 0x0000023263D41508>>
# print(person2.eat)  # <bound method Person.eat of <__main__.Person object at 0x0000023263F71E48>>
# print(Person.eat)  # <function Person.eat at 0x00000232650523A8>
"""
静态方法保存在类对象里，实例对象和类对象相同,类方法不同
"""
# print(Person.static_method is person1.static_method)  # True
# print(Person.static_method == person1.static_method)  # True
print(Person.class_method is person1.class_method)  # False
print(Person.class_method == person1.class_method)  # True
print(Person.class_method)  # <bound method Person.class_method of <class '__main__.Person'>>
print(person1.class_method)  # <bound method Person.class_method of <class '__main__.Person'>>

"""
普通方法（对象方法）调用：
"""
# 1.直接使用实例对象调用方法不需要手动传参，会自动将对象名传递给self形参：对象名.方法名(实参列表)
# person1.eat('苹果')  # 张三正在吃苹果
# person2.eat('樱桃')  # 李四正在吃樱桃
# # 2.使用类对象调用时需要手动指定self: 类名.方法名(对象名，实参列表)
# Person.eat(person1, 'apple')  # 张三正在吃apple
# Person.eat(person2, 'cherry')  # 李四正在吃cherry
"""
静态方法调用方式:对象名或者类名.静态方法名(实参列表)
"""
# person1.static_method()
# Person.static_method()
"""
类方法调用方式:对象名或者类名.类方法名(实参列表)
"""
# print(Person.class_method())
# print(person1.class_method())
