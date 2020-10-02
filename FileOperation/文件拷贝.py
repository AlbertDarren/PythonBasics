#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/21 14:54
# @Author  : Jack Deng
# @File    : 文件拷贝.py
# @Software: PyCharm
import os


def copy_file(src_path, dst_path):
    if os.path.isfile(src_path):  # 判断源文件路径是否存在

        with open(src_path, 'rb') as src_file:

            with open(dst_path, 'wb') as dst_file:
                while 1:
                    container = src_file.read(1024)
                    dst_file.write(container)
                    if not container:
                        break

    else:
        print('对不起，您输入的源文件路径不存在')


# 1.使用相对路径
# copy_file('../../../Desktop/演讲赛题.mp4','../../../Videos/演讲赛题.mp4' )
# 2.使用绝对路径
# copy_file('C:/Users/SiliconValley520/Desktop/演讲赛题.mp4','C:/Users/SiliconValley520/Videos/演讲赛题.mp4' )
