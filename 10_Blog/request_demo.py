#-*- codeing = utf-8 -*-
# @Time : 2022/3/26 22:43 
# @Author : wu
# @File : request_demo.py 
# @Software: PyCharm

from flask import Flask,render_template,request   #  request 接受客户端发送请求时的请求对象
from flask_script import Manager
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
# 给跨站请求伪造保护 设置一个令牌
app.config['SECRET_KEY'] = 'vw242cvdsdc242cv2cv2ffwd22111fhn67'

manager = Manager(app)
# 创建对象保护app
CSRFProtect(app)


@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login/',methods=['POST','get'])
def login():
    # 客户端每次发送一个请求 在服务端有一个对应的请求对象接受这个请求 request
    print(f'请求方式{request.method}')
    print(f'获取get请求传递过来的信息{request.args}')  # 一个字典类型的数据  字段为键  数据为值
    print(f'获取post请求传递过来的数据{request.form}')
    return '1'

if __name__ == '__main__':
    manager.run()






