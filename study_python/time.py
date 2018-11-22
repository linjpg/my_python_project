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

#时间转成int
def get_time_stamp():
    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    data_secs = (ct - int(ct)) * 1000
    time_stamp = "%s.%03d" % (data_head, data_secs)
    print(time_stamp)
    stamp = ("".join(time_stamp.split()[0].split("-")) + "".join(time_stamp.split()[1].split(":"))).replace('.', '')
    print(stamp)

# 获取星期 0-6
def week():
    d = datetime.datetime.now() + datetime.timedelta(days=-2)
    print(d)
    d.weekday()
    print(d.weekday())

def nottype():
    a = 0
    if not a:
        print(a)

#定时任务
def interval_event(*args, **kw):
    start_time = (datetime.datetime.now() - datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H:00:00")
    end_time = (datetime.datetime.now() - datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H:59:59")
    # start_time = '2018-08-20 13:00:00'
    # end_time = '2018-08-20 13:59:59'
    # DEBUG_LOG('server|start_time=%s,end_time=%s'(start_time,end_time))
    # CopyTableManager().copy_item_data(start_time, end_time)
    #
    #
    # set_timeout(interval_event, 1000)
    # set_interval(interval_event, 1000 * 60 * 60)
def cha_time(h=14, m=41):
    now = datetime.datetime.now()
    # start_time = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d 00:00:00")
    #
    # end_time = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d 23:59:59")

    # if now>start_time:
    #     print("-----------")
    # if now<end_time:
    #     print("==========")
    # print(now)
    # print("=====", time.time())
    # print( type(time.time()))
    # ct = time.time()
    # local_time = time.localtime(ct)
    print(int(time.time()))
    time.sleep(2)
    print(int(time.time()))
    # DEBUG_LOG('start_time', int(time.time()))
    # DEBUG_LOG("server|time", now.hour, now.minute)
    # if now.hour == h and now.minute == m:
    #     start_time = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d 00:00:00")
    #     end_time = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d 23:59:59")
    #     print(start_time,end_time)


if __name__ == '__main__':
    cha_time()
