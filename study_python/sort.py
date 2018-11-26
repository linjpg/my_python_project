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

import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
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

def hget_test():
    r = redis.Redis(host='127.0.0.1', port=6379, db=0)

    # keya = 'a'
    # keyb = 'b'
    #
    # r.hset("all",keya,"1")
    # r.hset("all",keyb,"2")
    # data = r.hgetall("all")
    # print(data)
    # print(len(data))
    period_record = {}
    period_record['activity_name'] = '中国'
    r.set("aa",'重中之重')
    print(r.get('aa'))

def test():
    user_count = 0
    user_list = [54036,54036]
    uid = 54036
    user_count_list =[]
    for u in user_list:
        if u:
            if int(u) == int(uid):
                user_count_list.append(u)
    print(len(user_count_list))

def is_None(data):
    if  data!=0 or data == 'None' or data is None:
        return True
    else:
        return False

def redis_expire():
    r = redis.Redis(host='127.0.0.1', port=6379, db=0)
    ret = r.set("aa", 1)
    print(ret)
    r.expire('aa', 10)
def get_data(aa):
    r = redis.Redis(host='127.0.0.1', port=6379, db=0)
    print(r.get(aa))
    list = ['a','b']
    r.hset('a','b',list)
    r.hset('a','c',1)
    k = r.hgetall('a')
    print(k)

def get_rez():
    r = redis.Redis(host='127.0.0.1', port=6379, db=0)
    r.zadd("page_size",10,"baidu")
    print(r.zcard("a"))

if __name__ == '__main__':
    # lottery_update_white(1111, 1)
    #redis_expire()
    get_rez()