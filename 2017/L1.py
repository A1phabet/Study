

# -*- coding:utf-8 -*-
'''打印九九乘法表'''


for m in range(1,10):
    for n in range(1,m+1):
        print('{}*{}={}'.format(m,n,m*n),end = ' ')
    print()

