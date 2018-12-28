#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 14:26
# @Author  : linjunpeng
# @Site    : 
# @File    : random_test.py
# @Software: PyCharm
# @Desc



# coding:utf-8
import random
import bisect

list = ['A', 'B', 'C', 'D']
weight = [5, 2, 2, 1]
def weight_choice1(list, weight):
    """
    :param list: 待选取序列
    :param weight: list对应的权重序列
    :return:选取的值
    """
    new_list = []
    for i, val in enumerate(list):
        # print(i)
        # print(val)
        # print(weight[i])
        # print(val * weight[i])
        # print(5*'A')
        # print(type(val * weight[i]))
        new_list.extend(val * weight[i])
    #print(new_list)
    return random.choice(new_list)


def weight_choice2(weight):
    """
    :param weight: list对应的权重序列
    :return:选取的值在原列表里的索引
    """
    print(weight)
    t = random.randint(0, sum(weight) - 1)
    print('=======t',t)
    for i, val in enumerate(weight):
        print(t)
        t -= val
        print(t,i)
        if t < 0:
            return i

def weight_choice(weight):
    """
    :param weight: list对应的权重序列
    :return:选取的值在原列表里的索引
    """
    weight_sum = []
    sum = 0
    for a in weight:
        sum += a
        weight_sum.append(sum)
    t = random.randint(0, sum - 1)
    return bisect.bisect_right(weight_sum, t)


if __name__ == "__main__":
    #print(weight_choice1(list,weight))
    print(list[weight_choice(weight)])



