#!/usr/bin/python
# -*- coding: UTF-8 -*-

#案例1：判断一个数是否为素数

def is_prime(num):
    i = 1
    for i in range(2, num):
        if num % i == 0:
            #print(i)
            break
            #return False
    if i == num -1:
        print('素数')
    else:
        print("不是素数")

#案例2:输出100以内的素数；

def is_prime2(num):
    list = []
    j = 1
    for i in range(3, num):
        for j in range(2, i):
            if i % j == 0:
                break
        if j == i -1:
            list.append(i)
    return list

if __name__ == '__main__':
    num = int(input("请输入一个正整数："))
    is_prime(num)
    print("%s以内的素数有：" %num)
    print(is_prime2(num))