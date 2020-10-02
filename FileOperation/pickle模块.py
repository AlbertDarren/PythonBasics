#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/25 09:13
# @Author  : Jack Deng
# @File    : pickle模块.py
# @Software: PyCharm
"""
python里存入数据只支持存人字符串和二进制
json:将Python里的数据(str/list/tuple/dict/int/float/booL/None)等转换成为对应的json字符串
pickLe(泡菜):将Python里任意的对象转换成为二进制
序列化   dumps:将python数据转换成为二进制
        dump:将Python数据转换成为二进制，同时保存到指定文件
反序列化 loads:将二进制加载成为Python数据
        Load:读取文件，并将文件的二进制内容加载成为Python数据
"""
import pickle

list1 = ['hello', 'world', 1, 3.14, True, "String"]
bin_list1 = pickle.dumps(list1)
with open('../Data/pickle数据.txt', 'wb') as w_stream:
    w_stream.write(bin_list1)
with open('../Data/pickle数据.txt', 'rb') as r_stream:
    bin_content = r_stream.read()
    print(pickle.loads(bin_content))


class Dog(object):
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def eat(self):
        print(self.name + '正在吃东西')


d = Dog('大黄', '白色')
# 将对象以二进制形式保存到文件里
pickle.dump(d, open('../Data/dog.txt', 'wb'))
# 将文件的二进制内容加载成为Python数据
dd = pickle.load(open('../Data/dog.txt', 'rb'))
dd.eat()
print(dd.name, dd.color)
