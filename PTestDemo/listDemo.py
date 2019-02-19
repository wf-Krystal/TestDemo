#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
products = ['Iphone8',6888],['MacPro',14800],['小米6',2499],['Coffee',31],['Book',80],['Nike Shoes',799]
shopcar =[]

while True:
    print('---------products---------')
    for index, p in enumerate(products):
        print('%s.%s %s' %(index, p[0], p[1]))
    choice = input('please input your numbers:')
    if choice.isdigit():
        choice = int(choice)
        shopcar.append(products[choice])
    elif choice == 'q':
        print('---------shopcar list----------')
        for index, p in enumerate(shopcar):
            print('%s.%s %s' %(index, p[0], p[1]))
        break
"""

products = [['Iphone8',6888],['MacPro',14800],['小米6',2499],['Coffee',31],['Book',80],['Nike Shoes',799]]
shopping_cart = []
run_flag = True
while run_flag:
    print ('-------------商品列表--------------')
    for index,i in enumerate(products):
        print ('%s.%s    %s'%(index,i[0],i[1]))
    choice = input('please input your numbers:')
    if choice.isdigit():
        choice = int(choice)
        shopping_cart.append(products[choice])
    elif choice == 'q':
        print ('-----------------您以购买如下商品------------')
        for index,i in enumerate(shopping_cart):
            print ('%s.%s    %s'%(index,i[0],i[1]))
        run_flag = False

