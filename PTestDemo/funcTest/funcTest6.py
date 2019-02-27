#!/usr/bin/python
# -*- coding: UTF-8 -*-
#案例8：实现登录与注册

def login(username, password):
    """
    function: login
    :param username: 用户输入的用户名
    :param password: 用户输入的密码
    :return: True，登录成功；False，登录失败
    """
    # f = open('user.txt', 'r')
    # for line in f:
    #     user_list = line.strip().split("|")
    #     if user_list[0] == username and user_list[1] == password:
    #         return True
    #     return False
    with open('user.txt', 'r') as f:
        data = f.readlines()     #readline与readlines要区别
        for line in data:
            user_list = line.strip().split("|")
            #print(user_list)
            if user_list[0] == username and user_list[1] == password:
                return True
            else:
                return False

def register(username, password):
    """
    function: register
    :param username: 用户名
    :param passeord: 密码
    :return: 默认返回None
    """
    # f = open('user.txt', 'a')
    # temp = "\n"+username+"|"+password
    # f.write(temp)
    # f.close()
    with open('user.txt','a') as file:
        temp = "\n"+username+"|"+password
        file.write(temp)

def main():
    t = input("1.登录；2.注册\n")
    if t == "1":
        user = input("请输入用户名：")
        pwd = input("请输入密码：")
        r = login(user, pwd)

        if r:
            print("登录成功")
        else:
            print("登录失败")
    elif t == "2":
        user = input("请输入用户名：")
        pwd = input("请输入密码：")
        register(user, pwd)
    else:
        print("输入错误，请重新输入：1.登录；2.注册")
main()