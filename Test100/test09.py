#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
题目：暂停一秒输出。

程序分析：使用 time 模块的 sleep() 函数。
"""
from time import sleep
for i in range(10):
    sleep(1)
    print(i)

myDict = {1:'a', 2:'b', 3:'c', 4:'d'}
for key, value in dict.items(myDict):
    print(key, value)
    sleep(1)