#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/21 09:39
# @Author  : Jack Deng
# @File    : 位运算示例.py
# @Software: PyCharm
"""
位运算：
运算符号     中文名称
&            按位与
|            按位或
^           按位异或
~           按位取反
<<          左移运算
>>          右移运算
"""
# 要求：将一个RGB值0xfeac78里面的red,green,blue值通过位运算提取，并使用十进制输出
# 说明：RGB采用十六进制表示颜色值
RGB = eval(input("请输入十六进制RGB值:"))  # RGB = 0xfeac78
red = RGB >> 16
green = RGB & 0xff00
blue = RGB & 0xff
print("红色值:{}\n绿色值:{}\n蓝色值:{}\n".format(red, green, blue))
"""
运行结果：
请输入十六进制RGB值:0xfeac78
红色值:254
绿色值:44032
蓝色值:120
"""
