#!/usr/bin/env python
# -*- coding:utf-8 -*-
import redis


class RedisConfig(object):
    def get_redis():
       return redis.Redis(host='127.0.0.1', port=6379, db=0)

