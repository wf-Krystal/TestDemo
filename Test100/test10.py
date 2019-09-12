#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
题目：暂停一秒输出，并格式化当前时间。

"""
import time, datetime

# print(time.strftime('%Y-%m-%d %H:%M:%S'), time.localtime(time.time()))
#
# time.sleep(1)
#
# print(time.strftime('%Y-%m-%d %H:%M:%S'), time.localtime(time.time()))


time.sleep(1)
Time = datetime.datetime.now()
print(Time.strftime('%Y-%m-%d %H:%M:%S'))