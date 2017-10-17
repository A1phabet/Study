# -*- coding:utf-8 -*-
#date:  10/2/2017

'''购物车买东西'''


money=input('Please input your salary:')#输入有多少钱
shopping_car = []   #购物车里的商品
product_list = [
    ('Mac',9000),
    ('Kindle', 800),
    ('Tesla', 900000),
    ('Python Book', 105),
    ('Bike', 2000)
]   #商品列表




if money.isdigit():
    money = int(money)  #输入的是否是数字，是就int成数字
    while True:
        for i,v in enumerate(product_list,1):       #列表打印出来
            print(i,v)
        choice = input('What do you wang to buy:')

        if choice.isdigit():    #输入选择
            choice = int(choice)
            if choice > 0 and choice <= len(product_list ):#判断选择
                item = product_list[choice-1]
                if item[1] < money:
                    money = money - item[1]
                    shopping_car.append(item)
                else:
                    print('money is not enough')
                    break
                print('Your want to buy',item)
            else:
                print('item is not exist.')
        elif choice == 'q':
            print('-----You have buy below thins.-----')
            for i in shopping_car:
                print(i)
            print('You have ' ,money)
            break
        else:
            print('invalid input.')




