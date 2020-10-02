#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/30 20:00
# @Author  : Jack Deng
# @File    : hashlib和hmac模块.py
# @Software: PyCharm
import hashlib, hmac

# 这两个模块都是用来信息加密的
# message digest 5 and security hash algorithm
# hashlib模块主要支持两个算法 MD5和sha(sha后面的数字代表加密后的二进制数字长度)
# 加密方式：
# 单向加密，比如 MD5和sha 只有加密过程，没有解密过程，
# 对称加密，
# 非对称加密RSA

"""
加密过程：
生成一个对象
指定一种编码将加密内容转换为二进制
调用对象的hexdigest方法
"""
# md5 = hashlib.md5()
# md5.update('hello'.encode('gbk'))
# print(md5.hexdigest())  # 5d41402abc4b2a76b9719d911017c592
# md5.update('hello'.encode('big5'))
# print(md5.hexdigest())  # 23b431acfeb41e15d466d75de822307c
# md5.update('hello'.encode('ascii'))
# print(md5.hexdigest())  # 99fb31087791f6317ad7c6da1433f172
# sha1 = hashlib.sha1('hello'.encode('utf8'))
# print(sha1.hexdigest())  # aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d
# sha224 = hashlib.sha224('hello'.encode('utf8'))
# print(sha224.hexdigest())  # ea09ae9cc6768c50fcee903ed054556e5bfc8347907f12598aa24193
# sha256 = hashlib.sha256('hello'.encode('utf8'))
# print(sha256.hexdigest())  # 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
# sha384 = hashlib.sha384('hello'.encode('utf8'))
# print(sha384.hexdigest())
# # 59e1748777448c69de6b800d7a33bbfb9ff1b463e44354c3553bcdb9c666fa90125a3c79f90397bdf5f6a13de828684f
# hamc可以指定秘钥加密
hmac_obj = hmac.new('hello'.encode('utf8'), 'me'.encode('gbk'))
# 获得加密后的结果
print(hmac_obj.hexdigest())  # 3bed7d43331e43c01f04c7c7c44f081d
