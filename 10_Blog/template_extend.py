#-*- codeing = utf-8 -*-
# @Time : 2022/3/26 22:43
# @Author : wu
# @File : request_demo.py
# @Software: PyCharm

from flask import Flask,render_template,request   #  request 接受客户端发送请求时的请求对象
from flask_script import Manager


app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True


manager = Manager(app)



@app.route('/')
def index():
    return render_template('sub.html')


if __name__ == '__main__':
    manager.run()






