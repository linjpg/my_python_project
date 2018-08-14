#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Python 练习实例1
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if(i != k) and (i != j) and (j != k):
#                 print i, j, k

# Python 练习实例2
# i = int(raw_input('净利润：'))
# arr = [1000000,600000,400000,200000,100000,0]
# rat = [0.01,0.015,0.03,0.05,0.075,0.1]
# r = 0
# for idx in range(0,6):
#     if i>arr[idx]:
#         r+=(i-arr[idx])*rat[idx]
#         print(r)
#         i = arr[idx]
# print r


# Python 练习实例4
# year = int(raw_input('year:\n'))
# month = int(raw_input('month:\n'))
# day = int(raw_input('day:\n'))
# months = (0,31,59,90,120,151,181,212,243,273,304,334)
# if 0<month<=12:
#     sum = months[month - 1]
# else:
#     print 'data error'
# sum += day
# leap = 0
# if(year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
#     leap = 1
# if (leap == 1) and month > 2:
#     sum +=1
#
# print 'it is the %dth day.' % sum

# Python 练习实例5
# l = []
# for i in range(3):
#     x = int(raw_input('integer:\n'))
#     l.append(x)
# l.sort()
# print l
# Python 练习实例6
# def fib(n):
#     a,b =1,1
#     for i in range(n-1):
#         print a
#         a,b = b,a+b
#     return a
# print fib(10)

# def fib(n):
#     if n==1 or n==2:
#         return 1
#     return fib(n-1)+fib(n-2)
# print fib(10)

# def Fib(n):
#     a, b = 0, 1
#     while n:
#         a, b, n = b, a + b, n - 1
#         print(a)
# Fib(7)

# Python 练习实例7
# a = [1,2,3]
# b = []
# b = a[:]
# print b
#
# list1 = [1,2,3]
# list2=[]
# list2.extend(list1)
# print list2

# Python 练习实例8
# for i in range(1, 10):
#     print
#     for j in range(1, i+1):
#         print "%d*%d=%d" % (i, j, i*j),

# Python 练习实例9
# import time
# myD = {1: 'a', 2: 'b'}
# for key,value in myD.items():
#     print key, value
#     time.sleep(1)

# Python 练习实例10
# print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
# time.sleep(1)
# print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

# Python 练习实例11
# f1 = 1
# f2 = 1
# for i in range(1,22):
#     print '%12ld %12ld' % (f1,f2),
#     if (i % 3) == 0:
#         print ''
#     f1 = f1 + f2
#     f2 = f1 + f2

# Python 练习实例12
# h = 0
# leap = 1
# from math import sqrt
# from sys import stdout
# for m in range(101,201):
#     k = int(sqrt(m+1))
#     for i in range(2,k+1):
#         if m % i == 0:
#             leap = 0
#             break
#     if leap == 1:
#         print '%-4d' % m
#         h += 1
#         if h % 10 == 0:
#             print ''
#     leap = 1
# print 'The total is %d' % h

for n in range(100,1000):
    i = n / 100
    j = n / 10 % 10
    k = n % 10
    if n == i ** 3 + j ** 3 + k ** 3:
        print n

def shui(n):
    i = n / 100
    j = n / 10 % 10
    k = n % 10
    if n == i ** 3 + j ** 3 + k ** 3:
        print n
    else:
        print("%d不是水仙数"%n)

print shui(200)