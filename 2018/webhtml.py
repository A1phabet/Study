# -*- coding:utf-8 -*-
#date:  2018/1/16

import ssl
import socket



#socket.AF_INET 表示是ipv4协议
#socket.SOCK_STREM 表示TCP协议
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#https 需要import ssl
#s = ssl.wrap_socket(socket.socket(socket.AF_INET,socket.SOCK_STREAM))
host = 'www.qq.com'
port = 80

#用connect函数连上主机，参数是一人tuple
s.connect((host,port))
#获得本机ip和port
ip, port = s.getsockname()
print("'本地ip和port':{} {}".format(ip,port))

http_request = 'GET / HTTP/1.1\r\nhost:{}\r\n\r\n'.format(host)

request = http_request.encode('utf-8')
print('请求:',request)
s.send(request)

response = s.recv(1919)

print('响应',response)
print('响应的str格式',response.decode('utf-8'))



