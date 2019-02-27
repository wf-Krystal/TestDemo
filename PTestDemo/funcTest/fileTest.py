#!/usr/bin/python
# -*- coding: UTF-8 -*-

with open('user.txt', 'r') as f:
    for line in f:
        user_list = line.strip().split("|")
        print(user_list)

