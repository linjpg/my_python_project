#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/22 18:05
# @Author  : linjunpeng
# @Site    : 
# @File    : index_handler2.py
# @Software: PyCharm
# @Desc

from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer


class IndexHandler(RequestHandler):

    def get(self):
        # 获取get方式传递的参数
        username = self.get_query_argument("username")
        usernames = self.get_query_arguments("username")

        print (username)
        print (usernames)

    def post(self):
        # 获取post方式传递的参数
        username = self.get_body_argument("aa")
        usernames = self.get_body_arguments("aa")

        print (username)
        print (usernames)

if __name__ == "__main__":
    app = Application([(r"/",IndexHandler)])

    app.listen(8000)

    IOLoop.current().start()
