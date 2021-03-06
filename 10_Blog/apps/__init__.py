#-*- codeing = utf-8 -*-
# @Time : 2022/3/26 21:13 
# @Author : wu
# @File : __init__.py 
# @Software: PyCharm

from flask import Flask
from exts import db


def create_app():
    app = Flask(__name__,template_folder='../templates',static_folder='../static')
    app.config.from_pyfile('../settings.py')
    db.init_app(app)
    return app