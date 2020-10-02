#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/24 19:25
# @Author  : Jack Deng
# @File    : stdin_stdout_stderr.py
# @Software: PyCharm
import sys

"""
3个属性都是文件流对象
stdin:标准输入
stdout:标准输出
stderr:标准错误输出
"""
stdin = sys.stdin  # input函数就是读取sys.stdin里的数据
stdout = open('../Data/指定输出文件.txt', 'w', encoding='utf8')
sys.stderr = open('../Data/stderr.txt', 'w', encoding='utf8')
# while 1:
#     content = stdin.readline().rstrip('\n')  # content==读到的内容尾部追加了一个\n,可以使用rstrip去掉
#     if content == '':
#         print('输入结束')
#         break
#     print(content)
while 1:
    content = stdin.readline().rstrip('\n')
    if content == '':
        print('输入结束')
        break
    print(content, file=stdout)
print(1/0)