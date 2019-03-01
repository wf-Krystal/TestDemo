#!/usr/bin/python
# -*- coding: UTF-8 -*-

#一个字符串list，每个元素都是一个ip，求出现次数最多的ip

list=['10.199.88.161','10.199.88.162','10.199.88.163','10.199.88.163','10.199.88.163']
dict={}
li=[]
for i in list:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1
for i in dict.keys():
    if dict[i] == max(dict.values()):
        print("出现次数最多的ip是：", i)
