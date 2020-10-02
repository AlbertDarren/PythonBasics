#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/2 20:54
# @Author  : Albert Darren
# @File    : 正则表达式练习-用户名密码限制.py
# @Software: PyCharm

"""
练习要求如下：
    1.用户名匹配
    -用户名只能包含数字，字母和下划线
    -不能以数字开头
    -长度在6到16位范围内
    2.密码匹配
    -不能包含!@#￥%^&*这些特殊符号
    -必须以字母开头
    -长度在6到12位范围内

"""
import re


def login(count=3):
    for count in range(count):  # 用户最大登陆次数限制
        print('欢迎登陆'.center(20, '*'))
        print("""
    输入用户名请注意：
    1.用户名只能包含数字，英文大小写字母和下划线
    2.不能以数字开头
    3.长度在6到16位范围内""")
        username = input('请输入用户名：')
        if check_username(username):
            print('用户名:{}不符合规范'.format(username))
            continue
        print("""
    输入密码请注意：
    1.不能包含!@#￥%^&*这些特殊符号
    2.必须以字母开头
    3.长度在6到12位范围内""")
        __password = input('请输入密码：')
        if check_password(__password):
            print('密码:{}不符合规范'.format(__password))
            continue
    else:
        print('对不起，已经达到最大登陆次数限制')


def check_password(password):
    """
    检验密码是否合法
    :param password: 待检验的密码
    :return: 返回判断结果
    """
    pattern = re.compile(r"[a-zA-Z][^!@#$^&*]{5,11}")
    result = pattern.fullmatch(password)
    return False if result else True


def check_username(user_name):
    """
    检验用户名是否合法
    :param user_name: 待检验的用户名
    :return: 返回判断结果
    """
    pattern = re.compile(r'^[a-zA-Z_]\w{5,15}$')
    result = pattern.match(user_name)
    return False if result else True


if __name__ == '__main__':
    login()
    # login(username, __password)
