# -*- coding: utf-8 -*-
from pip._vendor import requests


def hello(name):
    strHello = 'Hello, '+name
    return strHello;

print (hello("你好"))


url = 'http://www.cnblogs.com/qun542110741/p/9184629.html'

response = requests.get(url)   #请求数据
response.encode = 'utf-8'
print(response.text)

print(' '.join([' '.join(['%s*%s=%-2s'%(y,x,x*y)for y in range(1,x+1)]) for x in range(1,10)]))