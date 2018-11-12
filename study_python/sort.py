#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/12 17:10
# @Author  : linjunpeng
# @Site    : 
# @File    : sort.py
# @Software: PyCharm
# @Desc
import json

import redis

from utils.redis import RedisConfig


def inti_shop_tab():
    r = redis.Redis(host='127.0.0.1', port=6379, db=0)
    # r.set('hello','world')
    tab_list = []
    dict1 = {"id": "1", "name": "道具兑换", "sort": 1}
    dict2 = {"id": "2", "name": "家用电器", "sort": 2}
    dict3 = {"id": "3", "name": "材米油盐", "sort": 3}
    tab_list.append(dict1)
    tab_list.append(dict2)
    tab_list.append(dict3)
    tab_list = sorted(tab_list, key=lambda x: x['sort'])
    print(tab_list)
    r.hmset('ckey',dict1)
    print(r.hgetall('ckey'))
    # import redis
    # r = redis.Redis(host='127.0.0.1',port=6379,db=0)
    # r.set('hello','world')
    #print(redis.get('hello'))


def lottery_update_white(uid, status):
    r = redis.Redis(host='127.0.0.1', port=6379, db=0)
    white_key = 'lx_key'
    data = r.get(white_key)
    # 1添加
    list = []
    if data:
        list = json.loads(data)
        # list = data
    if int(status) == 1:
        if uid not in list:
            list.append(uid)
    else:
        # 删除
        if list:
            list.remove(uid)
    r.set(white_key, list)


if __name__ == '__main__':
    lottery_update_white(1111, 1)