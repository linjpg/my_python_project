#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/9/20 17:05
# @Author  : linjunpeng
# @Site    : 
# @File    : time.py
# @Software: PyCharm
# @Desc


import time


def get_time_stamp():
    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    data_secs = (ct - int(ct)) * 1000
    time_stamp = "%s.%03d" % (data_head, data_secs)
    print(time_stamp)
    stamp = ("".join(time_stamp.split()[0].split("-")) + "".join(time_stamp.split()[1].split(":"))).replace('.', '')
    print(stamp)


if __name__ == '__main__':
    get_time_stamp()
