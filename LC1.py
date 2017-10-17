# -*- coding:utf-8 -*-
#date:  2017/10/17

def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs


f1= count()
f1()



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