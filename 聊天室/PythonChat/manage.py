#-*- codeing = utf-8 -*-
# @Time : 2022/2/9 21:58 
# @Author : wu
# @File : manage.py 
# @Software: PyCharm

import tornado.web
import tornado.ioloop
import tornado.websocket

class Login(tornado.web.RequestHandler):
    def get(self):
        self.render('login.html')
    def post(self):
        #接收前端浏览器提交过来的用户名和 密码
        uname = self.get_argument('username')
        ps = self.get_argument('password')
        # print(uname,ps)
        if uname in ["zhangsan","lisi","wangwu"] and ps == "123456":
            print("登录成功")
            #设置cookie 保存登录状态
            self.set_cookie('uname',uname,expires_days=7)
            #跳转到聊天室页面
            self.redirect('/chat/')
            # self.redirect("http://baidu.com")
        else:
            self.write('登录失败：用户名或密码错误')


class Chat(tornado.web.RequestHandler):
    def get(self):
        #获取当前登录的用户名
        uname = self.get_cookie('uname')
        self.render('chatroom.html',uname=uname)

#聊天室中转站：websocket
class Chatroom(tornado.websocket.WebSocketHandler):

    #在线用户
    online_users = []

    #连接：当有新用户连接我时，会自动调用
    def open(self, *args: str, **kwargs):
        uname = self.get_cookie('uname')
        print("有用户连接我了{}".format(uname))
        # 有用户加入聊天室时，加入到online_users中
        self.online_users.append(self)

    #接收消息：接收前端浏览器发过来的消息
    def on_message(self, message):
        print("接收前端浏览器发过来的消息",message)
        # 获取当前用户名
        uname = self.get_cookie('uname')
        #群发给每个在线用户
        for user in self.online_users:
            user.write_message(f'[{uname}]:{message}')

    #关闭：有用户退出聊天室会自动调用
    def on_close(self):
        print('有用户已经退出聊天室')
        self.online_users.remove(self)



def make_app():
    app = tornado.web.Application(
        handlers= [
            (r'/login/',Login), #登录页面的路由
            (r'/chat/', Chat), #聊天室页面的路由
            (r'/chatroom/',Chatroom)
        ]
    )
    return app

if __name__ == '__main__':
    app = make_app()
    app.listen(8886)
    tornado.ioloop.IOLoop.current().start()




