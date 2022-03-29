#-*- codeing = utf-8 -*-
# @Time : 2022/3/26 21:28 
# @Author : wu
# @File : blogmodels.py 
# @Software: PyCharm

from exts import db

class User(db.Model):
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(20),nullable=False)
    phone = db.Column(db.String(11), unique=True)
    def __init__(self,username,password,phone):
        self.username = username
        self.password = password
        self.phone = phone









