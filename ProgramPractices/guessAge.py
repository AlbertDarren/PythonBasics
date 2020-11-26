# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time        : 2020/10/12 17:15
@Author      : Albert Darren
@Contact     : 2563491540@qq.com
@File        : guessAge.py
@Version     : Version 1.0.0
@Description : TODO
@Created By  : PyCharm
"""
from random import randint

"""
流程控制题，猜年龄游戏，有三次机会猜，三次后，若没有猜对，则输入是否想继续，如是y/Y则继续，否则就结束游戏。
猜年龄范围控制在20-30之间。
"""


def guess_age(count: int = 3, start_age: int = 20, end_age: int = 30):
    """
    猜年龄的程序
    :param count: 用户可以猜测的次数
    :param start_age: 猜测年龄的开始值
    :param end_age:猜测年龄的结束值
    :return:
    """
    initial_age = randint(start_age, end_age)
    print('系统已经生成随机年龄')
    for i in range(count):
        user_age = eval(input('请输入您猜的年龄，范围20-30岁：'))
        if user_age == initial_age:
            print('恭喜您，猜对了！')
            break
        else:
            print('对不起，您猜错了！')
    else:
        print('请问您是否想继续游戏？')
        answer = input('请输入y/Y继续，否则结束游戏:')
        if answer.lower() != "y":
            return
        guess_age()


if __name__ == '__main__':
    guess_age()
