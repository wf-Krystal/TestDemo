#!/usr/bin/python
# -*- coding: UTF-8 -*-

#字典复制
#d = {} 与d.clear()
#example1与2唯一不同的是在对字典d的清空处理上，1将d关联到一个新的空字典上，这种方式对字典dd是没有影响的，所以在字典d被置空后，字典dd里面的值仍旧没有变化。
# 但是在2中clear方法清空字典d中的内容，clear是一个原地操作的方法，使得d中的内容全部被置空，这样dd所指向的空间也被置空
"""
example1：
d={}
dd=d
d['one']=1
d['two']=2
print dd
d={}
print d
print dd
运算结果：

{'two': 2, 'one': 1}
{}
{'two': 2, 'one': 1}

example2:
d={}
dd=d
d['one']=1
d['two']=2
print dd
d.clear()
print d
print dd
运算结果：

{'two': 2, 'one': 1}
{}
{}
"""

#dict copy函数
x = {'one': 1, 'two': 2, 'three': 3, 'test': ['a', 'b', 'c']}
print(u'初始字典x---------')
print(x)

print(u'复制后的字典y---------')
y = x.copy()
print(y)

y['three'] = 33
print(u'修改y中的值后的y,x字典-------')
print(y)
print(x)

y['test'].remove('b')
print(u'删除y中的值后的y，x字典-------')
print(y)
print(x)
