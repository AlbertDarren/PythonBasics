#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/2 19:35
# @Author  : Albert Darren
# @File    : Match类.py
# @Software: PyCharm
"""
match,search,finditer方法返回结果都是Match类型的对象
"""
import re

pattern=r'(?P<first_match>A.*B)(?P<second_match>.*3)(?P<third_match>.*C)'
string='gyuAwebhftByavgtfyty3weCbffm'
matches = re.search(pattern, string)  # 默认匹配都是贪婪模式，即匹配尽可能长的字符串
"""
这里正则表达式有4个分组,起名以后可以同时使用下标和键访问匹配的字符串
第1组：(?P<first_match>A.*B)(?P<second_match>.*3)(?P<third_match>.*C)
第2组：(?P<first_match>A.*B)
第3组：                     (?P<second_match>.*3)
第4组：                                          (?P<third_match>.*C)

"""

"""
group表示正则表达式的分组，可以传递整型参数n，表示第n组
1.正则表达式里面使用()表示分组
2.如果没有分组，默认只有一组
3.分组下标从0开始
"""
# for i in range(4):
#     print('第{}组匹配到字符串是{}'.format(i+1,matches.group(i)))  # 获取到匹配的第i组字符串
"""
groups返回匹配的几组字符串形成的元组:('AwebhftB', 'yavgtfyty3', 'weC')
"""
# print(matches.groups())
"""
使用?P<name>给分组起名以后可以使用groupdict方法获得一个字典
{'first_match': 'AwebhftB', 'second_match': 'yavgtfyty3', 'third_match': 'weC'}
"""
# 使用键进行访问
print(matches.group('second_match'))