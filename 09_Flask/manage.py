#-*- codeing = utf-8 -*-
# @Time : 2022/3/22 22:50 
# @Author : wu
# @File : manage.py 
# @Software: PyCharm

#渲染模板 render_template
# 反向解析url_for
# 重定向 redirect
from flask import Flask,render_template,url_for,redirect
from flask_script import Manager #管理项目启动

app = Flask(__name__)
# print(app.config)
app.config['ENV'] = 'development' #设置成开发环境
app.config['DEBUG'] = True #设置处于调试阶段

manager = Manager(app)

#设置路由+视图函数
@app.route('/') #设置路由规则
def hello():
    return "hello flask"

@app.route('/index/',endpoint='other')
def index():
    print(url_for('other'))

    stus = [
        {'name':'张三','age':'21','score':'79',},
        {'name': '李四', 'age': '18', 'score': '59', },
        {'name': '王五', 'age': '21', 'score': '91', },
        {'name': '吴六', 'age': '22', 'score': '75', },
    ]


    return render_template('index.html',username = "王德发",students = stus)

@app.route('/main/',methods=['post','get'])
def main():
    return redirect(url_for('other'))




# print(__name__)

if __name__ == '__main__':
    manager.run()

