#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/22 22:09
# @Author  : Jack Deng
# @File    : csv文件读写.py
# @Software: PyCharm
import csv

with open('../Data/info.csv', 'a', encoding='utf8', newline='') as w_file:
    csv_writer = csv.writer(w_file)
    csv_writer.writerows(
        [[],
         ['Jack', 30, 'male', 'BeiJin'],
         ['Long', 45, 'male', 'TianJin']
         ]
    )
    csv_writer.writerow(['July', 17, 'female', 'Berlin'])
    csv_writer.writerow(['joice', 19, 'female', 'ChenDu'])
with open('../Data/info.csv', 'rt', encoding='utf8') as r_file:
    csv_reader = csv.reader(r_file)
    for row in csv_reader:
        print(row)