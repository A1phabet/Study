# -*- coding:utf-8 -*-
#date:  2017/10/11

import copy
a = [1,2,3,4,['a', 'b']]

b = a
c = copy.copy(a)    #浅拷贝
d = copy.deepcopy(a)    #深拷贝


a.append(5)
a[4].append('c')

print(a)
print(b)
print(c)
print(d)
