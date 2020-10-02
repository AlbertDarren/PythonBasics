#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/23 08:36
# @Author  : Jack Deng
# @File    : 交换两变量值.py
# @Software: PyCharm

variable1=20
variable2=30
# 方法1.使用第三个变量
# c=variable1
# variable1=variable2
# variable2=c
# print(variable1)# 30
# print(variable2)# 20

# 方法2.使用运算符实现，只能是数字
# variable1=variable1+variable2
# variable2=variable1-variable2
# variable1=variable1-variable2
# print(variable1)# 30
# print(variable2)# 20

# 方法3.使用异或运算符
# variable1=variable1^variable2
# variable2=variable1^variable2
# variable1=variable1^variable2
# print(variable1)# 30
# print(variable2)# 20

# 方法4.Python特有的方法
# variable1,variable2=variable2,variable1
# print(variable1)# 30
# print(variable2)# 20

