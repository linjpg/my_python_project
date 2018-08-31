#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/8/31 14:32
# @Author  : linjunpeng
# @Site    : 
# @File    : index_handler.py
# @Software: PyCharm
# @Desc


import tornado

from tornado import options
options.OptionParser().define("port", default=8000, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ', friendly user!')

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()