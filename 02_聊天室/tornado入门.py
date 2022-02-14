#-*- codeing = utf-8 -*-
# @Time : 2022/2/9 21:42 
# @Author : wu
# @File : tornado入门.py 
# @Software: PyCharm


import tornado.web
import tornado.ioloop


#类   视图
class Index(tornado.web.RequestHandler):
    #当浏览器使用get请求时，这个函数就会自动调用
    def get(self):
        #向浏览器页面返回内容
        self.write("hello,tornado")


def make_app():
    #创建一个tornado应用对象
    app = tornado.web.Application(
        #路由：网址和类的对应
        handlers=[
            (r'/index/',Index)
        ]
    )
    return app

if __name__ == '__main__':
    app = make_app()
    app.listen(8888)  #设置端口，监听端口
    #启动tornado
    tornado.ioloop.IOLoop.current().start()


