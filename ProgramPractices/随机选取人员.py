# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time        : 2020/10/18 12:43
@Author      : Albert Darren
@Contact     : 2563491540@qq.com
@File        : 随机选取人员.py
@Version     : Version 1.0.0
@Description : TODO
@Created By  : PyCharm
"""
from random import choice

# 最开始全班所有同学的学号列表
origin_student = list(range(2019223753, 2019223792))
"""
转专业结束以后
"""
# 转走了2019223755,2019223760,2019223769,2019223778
student_out = [2019223755, 2019223760, 2019223769, 2019223778, 2019223785]
# 转入了2019220644,2019223261
student_in = [2019220644, 2019223261]
# 现在的学号表
modify_student = [student for student in origin_student if student not in student_out]
modify_student.extend(student_in)
print("现在的所有学号，如下：")
for index, value in enumerate(modify_student, start=1):
    print(value, end=" ")
    if index % 6 == 0:
        print()

# 最新排除随机选择的同学列表
exclude_list = [
    2019223777,
    2019223758,
    2019223771, ]

# 最终得到的列表
# modify_student = [student for student in modify_student if student not in exclude_list]
modify_student = [student for student in exclude_list]


# 再随机生成count位同学些辩论赛征集题目,默认为3
def rand_choose(student_list, count=3):
    student_result = set()
    while len(student_result) < count:
        student_result.add(choice(student_list))
    return count, student_result


if __name__ == '__main__':
    print("随机生成的{}位同学学号是:{}".format(rand_choose(modify_student)[0], rand_choose(modify_student)[1]))
