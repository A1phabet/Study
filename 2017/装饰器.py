# -*- coding:utf-8 -*-
#date:  2017/12/7

def log(func):
    def wrapper(*args,**kkw):
        print('call %s():' % func.__name__)
        return func(*args,**kkw)
    return wrapper

@log
def now():
    print('chz')

print(now())