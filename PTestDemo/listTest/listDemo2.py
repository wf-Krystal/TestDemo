#!/usr/bin/python
# -*- coding: UTF-8 -*-

#num = int(input("请输入一个正整数（3 <= n < 1000）:"))
num = input("请输入一个正整数(3 ≤ n < 1000)：")
if num.isdigit():
    num = int(num)
    li = []    #找出num内的所有质数，并保存在li列表中
    for j in range(2, num):
        for i in range(2, num):
            i = 2
            if j % i != 0:
                i += 1
                li.append(j)
            break
    # 找出符合条件质数，输出总对数
    p = []
    count = 0
    for m in li:  # m遍历列表li
        for n in li[li.index(m):]:  # n只遍历在列表li中的m及其后的质数
            if n + m == num:
                t = (m, n)
                count += 1
    print(count)
else:
    print("您的输入不合法！")


