#-*- codeing = utf-8 -*-
# @Time : 2022/3/26 20:52 
# @Author : wu
# @File : manage.py 
# @Software: PyCharm
from flask import render_template
from flask_script import Manager
from apps import create_app
from flask_migrate import Migrate,MigrateCommand
from exts import db

app = create_app()

manager = Manager(app)

# 设置数据库迁移相关信息
migrate = Migrate(app,db)
# 将迁移操作使用指令的形式 交给manager
manager.add_command("database",MigrateCommand)


@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    manager.run()