#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
题目：给你一字典a，如a={1:1,2:2,3:3}，输出字典a的key，以','链接，如‘1,2,3'
"""

a={1: 11, 2: 22, 3: 33}  #key：和valus间有一个空格
print(a.keys())
print(','.join([str(key) for key in a.keys()])) #匿名函数，等于for key in a.keys(): return str(key)

print(','.join(map(str, a.keys())))   #map函数   map(函数，列表)

