#!/usr/bin/python
# -*- coding: UTF-8 -*-

# ---习题7：编写一个函数，接收传入的字符串，统计大写字母的个数、小写字母的个
#数、数字的个数、其它字符的个数，并以元组的方式返回这些数，然后调用该函数；

def char_count(li):
    list = []
    upper = 0
    lower = 0
    num = 0
    other = 0
    for i in range(len(li)):
        if li[i].isupper():   #大写字母判断
            upper += 1
        elif li[i].islower():   #小写字母判断
            lower += 1
        elif li[i].isnumeric():  #数字判断
            num += 1
        else:
            other += 1
    list.append(upper)
    list.append(lower)
    list.append(num)
    list.append(other)
    tup = tuple(list)
    return tup

if __name__ == '__main__':
    ll = input("please input some char(or a string):", )
    print("tuple contain count with upper char,lower char ,number and others:", char_count(ll))
