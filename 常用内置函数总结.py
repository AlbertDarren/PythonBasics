#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/27 09:46
# @Author  : Jack Deng
# @File    : 常用内置函数总结.py
# @Software: PyCharm

# 数学相关函数：
# 1.sum求和
# print(sum([]))  # 返回开始值，默认是0
# print(sum([1, 2, 3]))  # 可迭代对象元素求和,6
# print(sum([1, 2, 3], 1))  # 可迭代对象元素求和结果加上开始值1,7
# 2.round四舍五入，
# print(round(372485.6415926))# 未指定保留到小数点后的精度，默认保留到个位，372486
# print(round(372485.6415926,ndigits=3))# 保留到小数点后3位，372485.642
# print(round(372485.6415926,ndigits=-2))# 保留到小数点前3位，372500.0
# 3.pow幂运算,pow(x,y)等价于x**y,pow(x,y,z)等价于x**y % z
# print(pow(2, 3))# 8
# print(pow(2, 3,3))# 2
# 4.进制转换，oct,bin,hex,int
# decimal_integer = 20
# print(oct(decimal_integer))# 0o24
# print(bin(decimal_integer))# 0b10100
# print(hex(decimal_integer))# 0x14
# print(int(str(decimal_integer), base=20))  # int可以将数值型字符串指定转换2-36进制,这里指定20进制解析,默认十进制输出，40
# 5.最大值max，最小值min,可以指定比较函数
# iterable_object1='beydhosglpqmx'
# print(max(iterable_object1, key=ord))# y
# iterable_object2=[4,7,-10,3.19,2**0.5]
# print(max(iterable_object2, key=abs))# -10
# iterable_object3={'linda','mary','joe','Alexander','jack','fairy','jordan'}
# print(min(iterable_object3, key=len))# joe
# 6.同时求商和余数divmod,Return the tuple (x//y, x%y)
# print(divmod(10, 3))# (3, 1)

# 查找一个object可以调用的函数
# print(dir([]))
"""
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__',
'__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__',
'__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__',
'__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__',
'__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse',
'sort']

"""
# 面向对象相关的函数
# 1.isinstance判断一个对象是不是一个类或者子类的实例,issubclass判断一个类是不是另一个类的子类或者是同一个类

# 获得内存地址id
# variable = 'hello'
# print(id(variable))  # 十六进制地址，1595215756592

# 输入输出相关函数input,print
# input(input('请输入数字：'))# 提示符是内层input接收的结果
# print((input('请输入打印内容：')))

# 查看帮助信息help
# help(print)
"""
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

"""

# 字符unicode编码与字符转换函数chr,ord
# print(chr(65))  # A
# print(ord('a'))  # 97

# 变量相关函数
# 获取全局变量globals,获取局部变量locals
# global_variable1 = '晴天'
#
#
# def global_variable2():
#     local_variable1 = [1, 2]
#     local_variable2 = 12
#
#
# print(globals())
# # {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__':
# # <_frozen_importlib_external.SourceFileLoader object at 0x00000172E47EED08>, '__spec__': None, '__annotations__': {
# # }, '__builtins__': <module 'builtins' (built-in)>, '__file__':
# # 'C:/Users/SiliconValley520/PycharmProjects/pythonProject/常用内置函数总结.py', '__cached__': None, 'global_variable1':
# # '晴天', 'global_variable2': <function global_variable2 at 0x00000172E48DD4C8>}
# print(locals())
# # {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__':
# # <_frozen_importlib_external.SourceFileLoader object at 0x00000172E47EED08>, '__spec__': None, '__annotations__': {
# # }, '__builtins__': <module 'builtins' (built-in)>, '__file__':
# # 'C:/Users/SiliconValley520/PycharmProjects/pythonProject/常用内置函数总结.py', '__cached__': None, 'global_variable1':
# # '晴天', 'global_variable2': <function global_variable2 at 0x00000172E48DD4C8>}
