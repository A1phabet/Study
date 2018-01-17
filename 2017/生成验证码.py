# -*- coding:utf-8 -*-
#date:  2017/10/23


import random

# def v_code():
#     code=''
#     for i in range(10):
#         if i==random.randint(0,9):
#             add=random.randrange(10)
#         else:
#             add=chr(random.randrange(65,91))
#
#         code+=str(add)
#
#     print(code)
#
#
# v_code()


#---------------------------------------------------------------------------------

def v_code():
    code=''
    for i in range(5):
        add=random.choice([random.randrange(10),chr(random.randrange(65,91))])

        code+=str(add)

    print(code)

v_code()

