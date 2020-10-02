#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/31 08:16
# @Author  : Jack Deng
# @File    : 使用第三方模块.py
# @Software: PyCharm
import sys

# python在查找模块时的路径是sys.path
print(sys.path)
"""
['C:\\Users\\SiliconValley520\\PycharmProjects\\pythonProject', 
'C:\\Users\\SiliconValley520\\PycharmProjects\\pythonProject', 
'C:\\Users\\SiliconValley520\\anaconda3\\python37.zip', 
'C:\\Users\\SiliconValley520\\anaconda3\\DLLs', 
'C:\\Users\\SiliconValley520\\anaconda3\\lib', 
'C:\\Users\\SiliconValley520\\anaconda3', 
'C:\\Users\\SiliconValley520\\anaconda3\\lib\\site-packages', 
'C:\\Users\\SiliconValley520\\anaconda3\\lib\\site-packages\\win32', 
'C:\\Users\\SiliconValley520\\anaconda3\\lib\\site-packages\\win32\\lib', 
'C:\\Users\\SiliconValley520\\anaconda3\\lib\\site-packages\\Pythonwin'] 
"""
# 使用pip工具进行Python包管理
"""
一，常用的命令
1.pip install <package_name>，下载并安装第三方模块
2.pip uninstall <package_name>，卸载第三方模块
3.pip list ，列出当前环境已经安装的第三方模块名字和版本号
4.pip freeze，列出当前环境已经安装的第三方模块名字和版本号
5.pip freeze > 相对路径或者绝对路径+requirements.txt
    个人电脑上将当前环境已经安装的第三方模块名字和版本号重定向输出到指定文件requirements.txt
6.pip install -r 相对路径或者绝对路径+requirements.txt
    在服务器上面读取文件里面模块名和版本号并安装
二，镜像源下载
1.临时修改，只修改这一个包的下载路径
    pip install <package_name> -i <url> 从指定地址下载包
2.常用的国内镜像地址:
    阿里云 https://mirrors.aliyun.com/pypi/simple/
    中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
    豆瓣(douban) https://pypi.douban.com/simple/
    清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
    中国科学技术大学 https://pypi.mirrors.ustc.edu.cn/simple/
3.永久修改
    除了临时修改pip的下载源以外，我们还能永久改变pip的默认下载路径。
    在当前用户目录下创建一个pip的文件夹，然后再在文件夹里创建pip.ini文件并输入一下内容:
    [global]
    index-url=https://pypi.douban.com/simple
    [install]
    trusted-host=pypi.douban.com
三，使用Pycharm管理第三方包
    集成图形化第三方包管理：File | Settings | Project: pythonProject | Python Interpreter
"""
