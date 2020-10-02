#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/24 21:01
# @Author  : Jack Deng
# @File    : json的使用.py
# @Software: PyCharm
import json

"""
1.json模块:
    .将对象转换成为字符串，不管是在哪种操作系统，哪种编程语言里，字符串都是可识别的。
    .json就是用来在不同平台间传递数据的。
    .并不是所有的对象都可以直接转换成为一个字符串，下标列出了Python对象与json字符串的对应关
    系。
    Python      JSON
    dict        object
    list,tuple  array
    str         string
    int,float   number
    True        true
    False       false
    None        null
    .如果是一个自定义对象，默认无法装换成为json字符串，需要手动指定JSONEncoder.
    .如果是将一个json字符串重新转换成为对象，这个对象里的方法就无法使用了。
2.json里序列化，将数据持久有两个方法:
    dumps:将数据转换成为json字符串，不会将数据保存到文件里。
    dump(转储):将数据转换成为json字符串的同时写入到指定文件。
3.json反序列化也有两个方法:
    loads:将json字符串加载成为python里的数据
    load:读取一个文件，把文件里的json字符串加载成为python里的数据
"""
list1 = ['hello', 'world', 1, 3.14, True, "String"]
json_data1 = json.dumps(list1)
# data = {'name': 'jack', 'age': 12, 'height': {'value': 1.78, 'unit': 'm'}}
with open('../Data/序列化和反序列化.txt', 'w', encoding='utf8') as file:
    file.write(json_data1)
    # json.dump(data, file)

with open('../Data/序列化和反序列化.txt', 'r', encoding='utf8') as file:
    print(json.load(file))
obj = json.loads(json_data1)
print(type(obj), obj[-1], obj, sep='\n')


class MyEncode(json.JSONEncoder):
    def default(self, o):
        # return {"name":o.name, "age" :o.age}
        return o.__dict__


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + '正在吃东西')


p1 = Person('zhangsan', 18)
# 自定义对象想要转换成为json字符串，需要给这个自定义对象指定JSONEncoder
result = json.dumps(p1, cls=MyEncode)
print(result)  # {"name": "zhangsan","age": 18}
# 调用1oads方法将对象加载成为一个对象以后，得到的结果是一个字典
p = json.loads(result)
print(type(p))
