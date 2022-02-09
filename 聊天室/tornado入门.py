#-*- codeing = utf-8 -*-
# @Time : 2022/2/9 21:42 
# @Author : wu
# @File : tornado入门.py 
# @Software: PyCharm


import tornado.web
import tornado.ioloop

class Index(tornado.web.RequestHandler):
    def get(self):
        self.write("hello,tornado")


def make_app():
    app = tornado.web.Application(
        handlers=[
            (r'/index/',Index)
        ]
    )
    return app

if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()


