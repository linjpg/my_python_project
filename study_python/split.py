#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/20 17:05
# @Author  : linjunpeng
# @Site    : 
# @File    : time.py
# @Software: PyCharm
# @Desc
import datetime
import time
import random
def split():
    rade = '100%'
    rate = int(rade.split('%')[:1][0])
    print(type(rate))
    print(rate)

def rand():
    rand = random.randint(0, 100)
    print(type(rand))
    print(rand)

def yu():
    # count = 0
    # max_count = 5
    # redis_count = count % max_count
    # print(redis_count)
    #
    # for i in range(3):
    #     print(i)
    #
    # str = 'CR1.3.73_Android'
    # str = str.split('_')[0][2:]
    # print(str)


    random_round =[{u'rate': u'10%', u'id': 1, u'round': 1}, {u'rate': u'20%', u'id': 2, u'round': 2}, {u'rate': u'50%', u'id': 3, u'round': 3}, {u'rate': u'80%', u'id': 4, u'round': 4}, {u'rate': u'100%', u'id': 5, u'round': 5}],random_item=[{u'item_id': 1001, u'item_name': u'\u91d1\u5e01', u'rate': u'20%', u'id': 1, u'item_count': 100}, {u'item_id': 1005, u'item_name': u'\u5e78\u8fd0\u7b26', u'rate': u'20%', u'id': 2, u'item_count': 10}, {u'item_id': 1002, u'item_name': u'\u829d\u58eb\u8c46', u'rate': u'50%', u'id': 3, u'item_count': 10}, {u'item_id': 1501, u'item_name': u'1\u5143\u5fae\u4fe1\u7ea2\u5305', u'rate': u'10%', u'id': 4, u'item_count': 1}]
    # for i in range(len(list)):
    #     b = list[i]
    #     print(b['a'])
    play_time = 0
    round = None
    for i in range(len(random_round)-1):
        print(i)
        round_one = random_round[i]['a']
        round_two = random_round[i + 1]['a']
        if round_one>=play_time:
            round = random_round[i]
            break

        if round_one <= play_time and play_time < round_two:
            round = random_round[i]
            break
    print(len(random_round))
    if round is None:
        round = random_round[len(random_round)-1]
    print(round)

    for i in range(2):
        print(i)

if __name__ == '__main__':
    yu()
