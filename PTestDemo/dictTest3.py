#!/usr/bin/python
# -*- coding: UTF-8 -*-

dict = dict()
while True:
    print("""
    ###########用户管理系统###########
    #          1.注册新用户          #
    #          2.用户登录            #
    #          3.用户注销            #
    #          4.显示用户信息         #
    #          5.退出系统            #
    #################################
    """)
    s = int(input("请选择："))
    if s == 1:
        username = input("用户名：")
        password = input("密码：")
        if username in dict:
            print("该用户名已经存在")
        else:
            gender = input("性别（0为女，1为男）：")
            email = input("邮箱：")
            age = input("年龄：")
            dict[username] = [password, gender, email, age]
    elif s == 2:
        trycount = 0
        while trycount < 3:
            inname = input("用户名：")
            inpassword = input("密码：")
            if inname in dict and inpassword == dict.get(inname)[0]:
                print("登录成功")
                break
            else:
                print("登录失败")
                trycount += 1
        else:
            print("连续登录失败超过3次")
    elif s == 3:
        inname = input("用户名：")
        inpassword = input("密码：")
        if inname in dict and inpassword == dict.get(inname)[0]:
            dict.pop(inname)
        else:
            print("您输入的用户名或密码错误，请重试！")
    elif s == 4:
        username = input("用户名：")
        password = input("密码：")
        if username in dict and password == dict.get(username)[0]:
            print(dict.get(username))
        else:
            print("您输入的用户名或密码错误，请重试！")
    else:
        exit()
