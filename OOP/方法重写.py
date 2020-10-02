#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/18 08:29
# @Author  : Jack Deng
# @File    : 方法重写.py
# @Software: PyCharm
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def sleep(self):
        return f'{self.name}正在睡觉'


class Student(Person):
    # 重写Person的__init__方法,子类在父类实现的基础上，添加了自己的新实现
    def __init__(self, name: str, age: int, id_num: int):
        # Person.__init__(self,name,age)
        """
        调用父类方法的两种方式
        1.父类名.方法名(self,参数列表) e.g Person.__init__(self,name,age)
        2.推荐使用这一种，使用super关键字
          super().方法名(父类被重写方法参数列表) e.g super().__init__(name, age)
          super(类名，self).方法名(父类被重写方法参数列表) e.g super(Student, self).__init__(name, age)
        """
        super(Student, self).__init__(name, age)
        self.id_num = id_num

    def sleep(self):
        return super().sleep() + f'学号是:{self.id_num}'


person = Person(name='jack', age=22)
"""
is equivalent to the statements below
person = object.__new__(Person)
person.__init__('jack', 22)  # is equivalent to Person.__init__(person,'jack',22)
"""
print(person.sleep())
print(Person.sleep(person))
"""
调用对象方法有两种方式
1.对象名.方法名(实参列表)
2.类名.方法名(对象名，实参列表)
"""
