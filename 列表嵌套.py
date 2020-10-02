#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/23 21:17
# @Author  : Jack Deng
# @File    : 列表嵌套.py
# @Software: PyCharm

# 背景：一个学校，有三个办公室，现在有10位老师等待工位分配，请编写程序，完成随机分配
# 导入随机数模块
import random

# 创建老师名字的列表
teachers = ["Tony", "Jack", 'Mary', 'Linda', 'Lucy', 'John', 'Trump', 'Jason', 'Turing', 'Amanda']

# 创建办公室的列表
offices = [[], [], []]
# 遍历每一个老师名字
for teacher in teachers:

    # 随机生成办公室索引，添加老师
    offices[random.randint(0, len(offices) - 1)].append(teacher)

# 注意：每一次运行结果都不一样，下面不做运行演示，仅给出一种情况
print(offices)
"""
[['John', 'Trump', 'Turing', 'Amanda'], ['Tony', 'Jack', 'Mary', 'Jason'], ['Linda', 'Lucy']]
"""