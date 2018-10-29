#!/usr/bin/env python
# -*- coding:utf-8 -*-

import datetime
import time

class TimeUtil(object):
    # 时间转成字符串
    def datetime_str(self,date_time):
        return date_time.strftime("%Y-%m-%d %H:%M:%S")