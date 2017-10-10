# -*- coding:utf-8 -*-
#date:  2017/9/30

'''输入用户名和密码，如果连续错误3次就退出'''

user_1 = "jingjie"
pwd = '123.com'

time = 0




while time < 3:
    username = input("Username:")
    password = input("Password:")
    if username == user_1 and password == pwd:
        print("Welcome {} logiin." .format(user_1))
        break
    else:
        print("Invalid Username or Password.")

        time +=1

else:
    print('AAA')