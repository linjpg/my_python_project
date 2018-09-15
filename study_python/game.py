#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/31 14:32
# @Author  : linjunpeng
# @Site    :
# @File    : index_handler.py
# @Software: PyCharm
# @Desc

n = 5
def MiTest2(n):
    result=[]
    for i in range(n):
        result = result[-1:] + result[:-1]
        result = [(n-i)] + result
    print(result)

def test():
    a=[1,2,3,4]
    print(a[-1:])
    print(a[:-1])

MiTest2(15)
test()