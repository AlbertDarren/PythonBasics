#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/25 13:15
# @Author  : Jack Deng
# @File    : 异常处理.py
# @Software: PyCharm
"""
异常处理：用来处理程序运行过程中出现的异常
    语法格式
    try:
        code block
    except ZeroDivisionError:
        code block
    except FileNotFoundError:
        code block
    except:
        code block
    ...
    else:
        code block
    finally:
        code block
"""
try:
    file=open('ddd.txt', 'r')
    print(file.read())
    print(1 / 0)
    dict1 = {'name': 'jack', 'age': 22}
    print(dict1['height'])
    pass
except ZeroDivisionError:
    print('division by zero')
except FileNotFoundError:
    print('No such file or directory')
except Exception as e:
    print(e)
else:
    print('运行没有异常')
finally:
    print('异常处理结束')