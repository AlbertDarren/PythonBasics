#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/28 09:45
# @Author  : Jack Deng
# @File    : 名片管理系统.py
# @Software: PyCharm
# with open(r'C:\Users\SiliconValley520\Desktop\名片管理系统.txt', 'a+', encoding='utf-8') as file_obj:
import sys

user_info = []


def login(login_count=3):
    answer='1'
    while login_count > 0 and answer == '1':
        login_count -= 1
        user_name = input('请输入您的姓名:')
        user_tel = input('请输入您的手机号(11位):')
        while  len(user_tel) != 11:
            user_tel = input('手机号位数有误,请重新输入您的手机号(11位):')
        user_qq = input('请输入您的QQ号:')
        for user_dict in user_info:
            if user_dict['name'] == user_name and user_dict['tel'] == user_tel and user_dict['qq'] == user_qq:
                print('登陆用户:{}成功，欢迎使用本系统'.format(user_name))
                break
        else:
            print('对不起，登录失败！用户不存在，您的输入信息有误。')
            if login_count>0:
                print('您还有{}次登录机会！'.format(login_count))
                answer = input("请选择数字1重新登录login或者回车直接退出exit:")
                if answer == '':
                    sys.exit()


if __name__ == '__main__':
    login()

# while 1:
#     print("""
#     ---------------------------------
#             名片管理系统 Version1.0
#     1.添加名片
#     2.删除名片
#     3.修改名片
#     4.查询名片
#     5.显示所有名片
#     6.退出系统
#     ---------------------------------
#     """)
#     option = eval(input('请选择数字1-6进行操作:'))
#     if option == 1:
#         user_dict = {}
#         user_name = input('请输入您的姓名:')
#         user_tel = input('请输入您的手机号(11位):')
#         if len(user_tel) != 11:
#             user_tel = input('手机号位数有误,请重新输入您的手机号:(11位)')
#         user_qq = input('请输入您的QQ号:')
#         user_dict['name'] = user_name
#         user_dict['tel'] = user_tel
#         user_dict['qq'] = user_qq
#         user_info.append(user_dict)
#         print(user_info)
#     elif option == 2:
#         pass
#     elif option == 3:
#         print(user_info)
#         user_index = int(input('请输入要修改的用户索引序号:'))
#         print('你要修改的信息如下:')
#
#     elif option == 4:
#         pass
#     elif option == 5:
#         pass
#     elif option == 6:
#         print('成功退出，感谢您的使用')
#         sys.exit()
#     else:
#         option = eval(input('对不起，您输入的数字有误！请重新输入:'))
