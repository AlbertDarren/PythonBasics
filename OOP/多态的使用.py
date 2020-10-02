#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/19 09:39
# @Author  : Jack Deng
# @File    : 多态的使用.py
# @Software: PyCharm
"""
多态是基于继承，通过子类重写父类方法，达到不同子类对象调用
相同的父类方法，得到不同结果，提高代码灵活度
"""


class Dog(object):
    def __init__(self, name, code, dog_type):
        self.name = name
        self.code = code
        self.type = dog_type

    def work(self):
        print(self.name + '正在工作', '编号：{}'.format(self.code))


class PoliceDog(Dog):
    def work(self):
        print('{} {} 正在攻击坏人'.format(self.type, self.name))


class DrugDog(Dog):
    def work(self):
        print('{} {} 正在搜毒'.format(self.type, self.name))


class BlindDog(Dog):
    def work(self):
        print('{} {} 正在领路'.format(self.type, self.name))


class Person(object):
    def __init__(self, name, dog):
        self.name = name
        self.dog = dog

    def work_with_dog(self):
        self.dog.work()


police_dog = PoliceDog('猎影', 666, '警犬')
blind_dog = BlindDog('布鲁托', 20, '导盲犬')
drug_dog=DrugDog('烈焰',1314,'缉毒犬')
person1 = Person('王五',police_dog)
person1.work_with_dog()
person2 = Person('李四',blind_dog)
person2.work_with_dog()
person3 = Person('张三',drug_dog)
person3.work_with_dog()
