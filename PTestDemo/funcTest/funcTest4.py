#!/usr/bin/python
# -*- coding: UTF-8 -*-

#案例5：计算传入的列表的最大值、最小值和平均值，并以元组的方式返回；

import math
def numdel(li):
    list = []
    list.append(float(max(li)))
    list.append(float(min(li)))
    sum = 0
    for i in li:
        sum += float(i)
        aver = sum/len(li)
    list.append(aver)
    return tuple(list)
    print("-------list-------", list)

if __name__ == '__main__':
    list = input("please input a list,just contain number:",)  #input()函数输入的是字符串str，若要用算术时，需要类型转换
    li = list.split(',')
    print("tuple contain max_number,min_number and average_number:", numdel(li))

"""
python2.x与python3.x中关于input()函数的区别：
python2.x中有两种input
1.input()   input("1")输入的类型是number；input("hello word")输入的类型是字符串str  即用户输入的是什么类型就是什么类型
2.raw_input()    不论输入什么，都是字符串类型，比如raw_input("123") = ‘123’ 字符串类型
python3.x只有一个input，功能等同于raw_input() 都是字符串类型

"""