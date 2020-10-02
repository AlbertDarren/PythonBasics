#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/25 20:46
# @Author  : Jack Deng
# @File    : function_define.py
# @Software: PyCharm

# define a function named add,which has two positional parameters,namely num1,num 2
def add(number1: int, number2: int):  # specify the expected data type ,only suggestions ,not compulsory
    """
    Return the sum  of num1，num2
    :param number1: the first number
    :param number2: the second number
    :return: the sum
    """
    return number1 + number2


# now,invoke the above defined function add,assign two arguments
result = add(1, 2)
print('结果是%s'%result)

# access the Docstring by builtin_function help
help(add)
"""
Help on function add in module __main__:

add(number1: int, number2: int)
    Return the sum  of num1，num2
    :param number1: the first number
    :param number2: the second number
    :return: the sum
"""
