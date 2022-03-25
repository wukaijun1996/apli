#-*- codeing = utf-8 -*-
# @Time : 2022/3/25 23:15 
# @Author : wu
# @File : manage2.py 
# @Software: PyCharm

from flask import Flask
from flask_script import Manager  #以指令的形式启动项目 或者迁移数据库
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate,MigrateCommand

# Migrate  迁移类
# MigrateCommand 为迁移数据库设置一个字段表示数据库


app = Flask(__name__)
app.config['ENV'] = 'developmeng'
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/book_1'

# 创建 一个关系映射的工具
db = SQLAlchemy(app)  #连接数据库

manager = Manager(app)

# 创建一个迁移对象
migrate = Migrate(app,db)
# 为数据库迁移设置指令
# 在管理对象中添加一个MigrateCommand 这种类型的 指令名  通过这个指令名 完成对数据库的操作
manager.add_command('database',MigrateCommand)




class Dept(db.Model):
    dno = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(100))
    addr = db.Column(db.String(100))

    def __init__(self,name,addr):
        self.name = name
        self.addr = addr






if __name__ == '__main__':


    manager.run()



