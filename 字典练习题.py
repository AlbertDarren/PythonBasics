#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/24 20:28
# @Author  : Jack Deng
# @File    : 字典练习题.py
# @Software: PyCharm
# 声明一个列表,在列表中保存6个学生的信息(6个字典)
students = [
    {'name': '张三', 'age': 18, 'score': 98, 'tel': '1388888998', 'gender': 'female'},
    {'name': '李四', 'age': 28, 'score': 95, 'tel': '1388666666', 'gender': 'male'},
    {'name': '王五', 'age': 21, 'score': 97, 'tel': '1365588889', 'gender': 'unknown'},
    {'name': 'chris', 'age': 17, 'score': 58, 'tel': '13777775523', 'gender': 'male'},
    {'name': 'jack', 'age': 23, 'score': 52, 'tel': '13999999928', 'gender': 'female'},
    {'name': 'tony', 'age': 15, 'score': 98, 'tel': '1388888888', 'gender': 'unknown'},
    {'name': 'mary', 'age': 19, 'score': 93, 'tel': '1388885555', 'gender': 'unknown'}
]
# (1）统计不及格学生的个数
failed_student_count=0
# (3)统计未成年学生的个数
minor_student=0
max_value=students[0]['score']
for student in students:
    if student['score']<60:
        failed_student_count += 1
        # (2)打印不及格学生的名字和对应的成绩
        print('{}不及格,对应的成绩{}'.format(student['name'],student['score']))

    if student['age']<18:
        minor_student+=1

    # if student['tel'].endswith('8'):
    if student['tel'][-1]=='8':
        # (4)打印手机尾号是8的学生的名字
        print('%s手机尾号是8' % student['name'])
    if student['score']>max_value:
        max_value=student['score']
print('不及格学生的个数:{}个'.format(failed_student_count))
print('未成年学生的个数:{}个'.format(minor_student))
# (5)打印最高分和对应的学生的名字
for index, student in enumerate(students):
    if student['score']==max_value:
        print('{}同学是最高分{}'.format(student['name'],max_value))
# (6)删除性别不明的所有学生(这个地方有个坑),bug在于列表边遍历边删除会漏掉一些项
# way1:列表生成式
new_students=[student for student in students if student['gender']!='unknown']
print(new_students)
# way2:遍历浅拷贝的列表，在原始列表上删除数据
# for student in students[:]:
#     if student['gender']=='unknown':
#         students.remove(student)
# print(students)
# way3:
# i=0
# while i<len(students):
#     if students[i]['gender']=='unknown':
#         students.remove(students[i])
#         # i-=1
#         continue
#     i+=1
# print(students)

# (7)将列表按学生成绩从大到小排序(选做)


# print(students)