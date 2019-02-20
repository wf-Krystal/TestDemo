#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
案例2：购买商品
要求用户输入总资产，例如：2000
显示商品列表，让用户根据序号选择商品，加入购物车
购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。
附加：可充值、某商品移除购物车

"""
"""
def shopping():
    goods = [
        {'name': '电脑', 'price': 1999},
        {'name': '鼠标', 'price': 10},
        {'name': '游艇', 'price': 20},
        {'name': '花', 'price': 998}
    ]
    #用户输入总资产
    total_money = int(input("请输入您的总资产："))
    print('''
                 我们有以下商品供您选择：  
                序号======>名称======>价格
                 1  ======>电脑======>1999
                 2  ======>鼠标======>10
                 3  ======>游艇======>20
                 4  ======>花======>998

           ''')
    tag = True
    while tag:
        # 显示商品列表，让用户根据序号选择商品，加入购物车(dic)
        dic = {}
        tag2 = True
        while tag2:
            choice_num = int(input("请输入商品所对应的序号：  \n如需充值请输入 5"))
            if choice_num == 1:
                print("您选择的商品为电脑，价格为1999元")
                dic['1'] = 1999
                print('\n')
                remaining_money = total_money - dic[str[choice_num]]
                print('账户余额：', remaining_money)
                ex = input("如需进行支付请输入 quit，输入任意键进行购买")
                if ex == 'quit':
                    tag2 == False
                continue
            elif choice_num == 2:
                print("您选择的商品为鼠标，价格为10元")
                dic["2"] = 10
                print("\n")
                remaining_money = total_money - dic[str(choice_num)]
                print("账户余额： ", remaining_money)
                ex = input("如需进行支付请输入 quit，输入任意键进行购买")
                if ex == "quit":
                    tag2 = False
                continue
            elif choice_num == 3:
                print("您选择的商品为游艇，价格为20元")
                dic["3"] = 20
                print("\n")
                remaining_money = total_money - dic[str(choice_num)]
                print("账户余额： ", remaining_money)
                ex = input("如需进行支付请输入 quit，输入任意键进行购买")
                if ex == "quit":
                    tag2 = False
                continue
            elif choice_num == 4:
                print("您选择的商品为花，价格为998元")
                dic["4"] = 998
                print("\n")
                remaining_money = total_money - dic[str(choice_num)]
                print("账户余额： ", remaining_money)
                ex = input("如需进行支付请输入 quit")
                if ex == "quit":
                    tag2 = False
                continue
            elif choice_num == 5:
                money = int(input("你要充值多少钱：  "))
                total_money += money
                remaining_money = total_money
                print("账户余额： ", remaining_money)
                ex = input("如需进行支付请输入 quit,输入mai键进行购买")
                if ex == "quit" or "mai":
                    tag2 = False
                continue
        cut_hand = int(input("请输入 3 进行购买：  \n输入6进行删除购物车"))
        if cut_hand == 3:
            if total_money >= dic[str(choice_num)]:
                print('购买成功')
            else:
                print('余额不足，无法购买，请充值')

        if cut_hand ==6:
            for i in dic:
                print(i, dic[i])
            del_num = int(input("请输出您要删除的物品对应的序号： "))
            del dic[str[del_num]]

if __name__ == '__main__':
    shopping()

"""

def work4():
    goods = [
        {"name": "电脑", "price": 1999},
        {"name": "鼠标", "price": 10},
        {"name": "游艇", "price": 20},
        {"name": "美女", "price": 998},
    ]
    # 要求用户输入总资产
    total_money = int(input("小子你有多少钱啊：  "))
    print('''
            我们有以下商品供您选择：  
            序号======>名称======>价格
            1  ======>电脑======>1999
            2  ======>鼠标======>10
            3  ======>游艇======>20
            4  ======>美女======>998

        ''' )

    tag = True
    while tag:

        # 显示商品列表，让用户根据序号选择商品，加入购物车(dic)
        dic = {}
        tag1 = True
        while tag1:
            choose_number = int(input("请输入商品所对应的序号：  \n如需充值请输入 5"))
            n = choose_number
            if n == 1:
                print("您选择的商品为电脑，价格为1999元")
                dic["1"] = 1999
                print("\n")
                balance = total_money-dic[str(n)]
                print("账户余额： ", balance)
                ex = input("如需进行支付请输入 quit，输入键进行购买")
                if ex == "quit":
                    tag1 = False

                continue

            elif n == 2:
                print("您选择的商品为鼠标，价格为10元")
                dic["2"] = 10
                print("\n")
                balance = total_money-dic[str(n)]
                print("账户余额： ", balance)
                ex = input("如需进行支付请输入 quit，输入任意键进行购买")
                if ex == "quit":
                    tag1 = False
                continue
            elif n == 3:
                print("您选择的商品为游艇，价格为20元")
                dic["3"] = 20
                print("\n")
                balance = total_money-dic[str(n)]
                print("账户余额： ", balance)
                ex = input("如需进行支付请输入 quit，输入任意键进行购买")
                if ex == "quit":
                    tag1 = False
                continue
            elif n == 4:
                print("您选择的商品为美女，价格为998元")
                dic["4"] = 998
                print("\n")
                balance = total_money-dic[str(n)]
                print("账户余额： ", balance)
                ex = input("如需进行支付请输入 quit")
                if ex == "quit":
                    tag1 = False
                continue
            elif n == 5:
                money = int(input("你要充值多少钱：  "))
                total_money += money
                balance = total_money
                print("账户余额： ", balance)
                ex = input("如需进行支付请输入 quit,输入mai键进行购买")
                if ex == "quit" or "mai":
                    tag1 = False
                continue
        cut_hand = int(input("请输入 3 进行购买：  \n输入6进行删除购物车"))
        if cut_hand == 3:
            if total_money >= dic[str(n)]:
                print("购买成功")
            else:
                print("you are a low b,please choose other cheap thing")

        if cut_hand == 6:
            for i in dic:
                print(i, dic[i])
            del_number = int(input("请输出您要删除的物品对应的序号： "))
            del dic[str(del_number)]

if __name__ == '__main__':
     work4()