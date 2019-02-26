#!/usr/bin/python
# -*- coding: UTF-8 -*-

info = {
    'stu1101': "zhangsan",
    'stu1102': "wangwu",
    'stu1103': "lisi"
}

b = {
    'stu1101': "wangsui",
    1: 3,
    2: 5
}

c = dict.fromkeys([6, 7, 8])  #初始化一个字典,初始化keys

print(info.values())  #输出字典中的值
print('-------分隔线-------')
print(b.keys())   #输出字典中的key
print('-------分隔线-------')
info.setdefault('stu1101', 'abc')   #如果key存在，不改变任何值；如果key不存在，则创建key并赋值
info.update(b)  #合并字典，并且更新对应的key的值
print(info)
print('--------分隔线------')
print(c)
print('--------分隔线------')
#字典循环
#example1 推荐方法
for i in info:
    print(i, info[i])
print('--------分隔线------')
#example2 不推荐使用，先要把字典转成列表，如果数据量大，效率大大降低
for k, v in info.items():
    print(k, v)