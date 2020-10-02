#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/18 09:33
# @Author  : Jack Deng
# @File    : 离散数学实验一.py
# @Software: PyCharm
# 实验1
def experiment1(loop_count=4):
    truth_value = [0, 1]
    while loop_count > 0:
        # 请求用户输入
        p_value = eval(input('请输入命题p的真值(1或者0):'))
        q_value = eval(input('请输入命题q的真值(1或者0):'))
        if p_value not in truth_value or q_value not in truth_value:
            print('您的输入不合法，请重新输入')
        else:
            print('逻辑运算结果'.center(20, '-'))
            print('p{}q的真值为:{}'.format(chr(ord('\u2227')), p_value & q_value))
            print('p{}q的真值为:{}'.format(chr(ord('\u2228')), p_value | q_value))
            print('p{}q的真值为:{}'.format('^', p_value ^ q_value))
            print('p{}q的真值为:{}'.format(chr(ord('\u2192')), int(not p_value or q_value)))
            print('p等价于q的真值为:{}'.format(int(p_value == q_value)))
            print('-' * 20)
        loop_count -= 1


def experiment2():
    """
    输出命题公式:(p∨q)→r的真值表，主析取范式，主合取范式
    """
    truth_value = [0, 1]
    # 主析取范式
    dnf = []
    # 主合取范式
    cnf = []
    # 打印表头
    print('真值表'.center(20, '-'))
    print(' {} {} {} | {:^7} | {}'.format('p', 'q', 'r', '(p \u2228 q)', '(p \u2228 q) \u2192 r'))
    for p in truth_value:
        for q in truth_value:
            for r in truth_value:
                print(' {} {} {} | {:^7} | {:^12}'.format(p, q, r, (p | q), int(not (p | q) or r)))
                decimal_index = int(str(p) + str(q) + str(r), 2)
                if not (p | q) or r:
                    dnf.append('m' + str(decimal_index))
                else:
                    cnf.append('M' + str(decimal_index))
    print('主合取范式：' + '\u2227'.join(cnf))
    print('主析取范式：' + '\u2228'.join(dnf))


def experiment3(start: int, stop: int):
    # 存放满足要求的整数
    num_set = []
    # 取出寻找范围内的每一个正整数
    for number in range(start, stop + 1):
        min_num = 1
        max_num = int(pow(number, 1 / 3))
        # 取出第一个数
        count = 0
        for first_num in range(min_num, max_num + 1):
            # 取出第二个数
            for second_num in range(min_num, max_num):
                if number == pow(first_num, 3) + pow(second_num, 3):
                    # print('{}={}^3+{}^3'.format(number, first_num, second_num))

                    count += 1
                    if count == 2:
                        num_set.append(number)

    return num_set


def double_cube_int():
    """
    数据结构用得好
    """
    t = {}
    i = 1
    j = 1
    for i in range(1, 30):
        for j in range(i+1, 30):
            temp_num = pow(i, 3) + pow(j, 3)
            if temp_num not in t:
                t[temp_num] = [[i, j]]
            else:
                t[temp_num].append([i, j])
    for key in t.keys():
        if len(t[key]) > 1:
            print('---------\n' + str(key))
            for p in t[key]:
                print('=' + str(p[0]) + '^3 + ' + str(p[1]) + '^3')


if __name__ == '__main__':
    # double_cube_int()
    # 执行效率：35.3 ms ± 8.63 ms per loop (mean ± std. dev. of 7 runs, 10 loops each)
    print(experiment3(10, 1000))
    #  执行结果：[559, 855]
    #  执行效率：55.9 ms ± 2.23 ms per loop((mean ± std. dev. of 7 runs, 10 loops each)
    # experiment2()
