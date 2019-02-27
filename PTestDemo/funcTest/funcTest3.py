#!/usr/bin/python
# -*- coding: UTF-8 -*-
#案例4:已知三角形的三个坐标，求求三角形周长
"""
输入3个点的坐标，根据坐标来求三角形的周长

"""
import math
def lenths(x1, y1, x2, y2):
    L = math.sqrt((x2-x1)**2+(y2-y1)**2)
    return L

def isTriangle(x1, y1, x2, y2, x3, y3):
    flag=((x1-x2)*(y3-y2)-(x3-x2)*(y1-y2))!=0
    return flag

def main():
    print('输入三个点的坐标：')
    x1,y1=eval(input('x1,y1='))   #eval()函数作用：可以把list,tuple,dict和string相互转化。
    x2,y2=eval(input('x2,y2='))
    x3,y3=eval(input('x3,y3='))
    if(isTriangle(x1,y1,x2,y2,x3,y3)):
        perim = lenths(x1,y1,x2,y2)+lenths(x1,y1,x3,y3)+lenths(x2,y2,x3,y3)
        print('the primeter is',perim)
    else:
        print('this is not triangle')

main()
