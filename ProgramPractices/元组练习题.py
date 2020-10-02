#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/25 08:33
# @Author  : Jack Deng
# @File    : 元组练习题.py
# @Software: PyCharm
# 用三个元组表示三门学科的选课学生姓名(一个学生可以同时选多门课)
sing = ('李白','白居易','李清照','杜甫','王昌龄','王维','孟浩然','王安石')
dance =('李商隐','杜甫','李白','白居易','岑参','王昌龄')
rap = ('李清照','刘禹锡','岑参','王昌龄','苏轼','王维','李白')

# (1)求选课学生总共有多少人
# 使用集合set去重
total=set(sing+dance+rap)
print('选课学生总共有%d人' % len(total))

# (2)求只选了第一个学科的人的数量和对应的名字
first_subject=[student for student in sing if (student not in dance) and (student not in rap)]
print('只选了第一个学科的人的数量是：{} 对应的名字是{}'.format(len(first_subject), ','.join(first_subject)))


"""
(3)求只选了一门学科的学生的数量和对应的名字
(4）求只选了两门学科的学生的数量和对应的名字
(5)求选了三门学生的学生的数量和对应的名字
"""
# 获得一个学生姓名对应选课门数的字典
subject_dict=[(student,int(student in sing)+int(student in dance)+int(student in rap))for student in total]
# 请求用户输入
number=int(input('请输入想要获得的学生选课门数(1-3):'))
# 获得满足用户输入的学生名字列表
subject=[item[0] for item in subject_dict if item[1]==number]
print('只选了{}门学科的学生的数量是{},对应的名字是{}'.format(number, len(subject), ','.join(subject)))

