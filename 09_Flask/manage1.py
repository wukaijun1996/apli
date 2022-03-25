#-*- codeing = utf-8 -*-
# @Time : 2022/3/25 21:55 
# @Author : wu
# @File : mansge1.py 
# @Software: PyCharm
import random

from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy  #关系映射工具

app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
# 跟数据库之间建立联系
# 数据库系统+连接池：//登录数据库系统的用户名：密码@主机地址：端口号/数据库的名字
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/book_1'

manager = Manager(app)

# 创建关系映射的工具
db = SQLAlchemy(app)

class Teacher(db.Model):
    # 声明对应的字段 ---映射表中的字段


    tid = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(100),nullable=False)
    salary = db.Column(db.Float)

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

names = ['赵老师','钱老师','孙老师','李老师','周老师','吴老师',]

@app.route('/')
def add_teacher():
    name= random.choice(names)
    # 创建一个老师对象
    t = Teacher(name,10000)
    # 添加数据
    db.session.add(t)
    # 把数据提交到数据库
    db.session.commit()

    return '添加成功'



if __name__ == '__main__':

    db.create_all()    #把模型 ---映射的表在数据库中创建出来

    manager.run()







