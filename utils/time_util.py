#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime
import time

class TimeUtil(object):
    # 时间转成字符串
    def datetime_str(self,date_time):
        return date_time.strftime("%Y-%m-%d %H:%M:%S")

    # 获取格式化时间
    def get_data_time(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 获取到秒的时间戳
    def get_second_time(self):
        return int(time.time())

