#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/22 17:50
# @Author  : linjunpeng
# @Site    : 
# @File    : index_handler.py
# @Software: PyCharm
# @Desc
from tornado.httpserver import HTTPServer

import tornado.web
import tornado.ioloop
from tornado.ioloop import IOLoop


#定义处理类型
class IndexHandler(tornado.web.RequestHandler):
    #添加一个处理get请求方式的方法
    def get(self):
        #向响应中，添加数据
        self.write('好看的皮囊千篇一律，有趣的灵魂万里挑一。')

if __name__ == '__main__':
    #创建一个应用对象
    app = tornado.web.Application([(r'/',IndexHandler)])
    #绑定一个监听端口
    #app.listen(8888)
    #启动web程序，开始监听端口的连接
    #tornado.ioloop.IOLoop.current().start()
    http_server = HTTPServer(app)
    # 最原始的方式
    http_server.bind(8888)
    http_server.start(1)
    IOLoop.current().start()
