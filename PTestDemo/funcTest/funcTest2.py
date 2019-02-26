#!/usr/bin/python
# -*- coding: UTF-8 -*-
#案例3：判断三边能否构成三角形；

def triangle(a, b, c):
    if a+b>c and a+c>b and b+c>a:
        print("%d %d %d 3个数能组成三角形" %(a, b, c))
        if a==b==c:
            print("等边三角形")
        elif a==b or b==c or a==c:
            print("等腰三角形")
        elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
            print("直角三角形")
        else:
            print("普通三角形")
    else:
        print("不能组成三角形")
if __name__ == '__main__':
    print("--------请输入三个正整数-------")
    a = int(input("first number:"))
    b = int(input("second number:"))
    c = int(input("third number:"))
    triangle(a, b, c)