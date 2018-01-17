# -*- coding:utf-8 -*-
#date:  2017/10/17

# def count():
#     fs = []
#     for i in range(1,4):
#         def f():
#             return i*i
#         fs.append(f)
#     return fs
#
#
# f1= count()



# def lazy_sum(*args):
#     def sumss():
#         ax = 0
#         for i in args:
#             ax = ax + i
#         return ax
#     return sumss
#
# f = lazy_sum(1,3,5,7,9)
# print(f)
# print(f())


l=[1,2,3,4,6]
d=iter(l)
print(d)

#生成器都是迭代器，迭代器不一定是生成器

#迭代器？
#满足两个条件：1，有iter方法；2，有next方法

import time

print(help(time))
