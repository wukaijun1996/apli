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
    # 这个用户发表了哪些博客
    # 这些博客的类型
    #backref = ‘属性名’
    # 属性名隐式添加在博客类型中  获取到发表博客的用户信息
    blogs = db.relationship('Blog',backref='user')

    like_blogs = db.relationship('Blog',secondary = 'like')

    def __init__(self,username,password,phone):
        self.username = username
        self.password = password
        self.phone = phone


# 博客模型
class Blog(db.Model):
    bid = db.Column(db.Integer,primary_key=True,autoincrement=True)
    # 博客标题
    title = db.Column(db.String(100),nullable=False)
    # 缩略内容
    thum_content = db.Column(db.Text,nullable=False)
    # 完整内容
    content = db.Column(db.Text,nullable=False)
    # 谁发表的  -- 外键  联系两张表
    # db.ForeignKey('user.uid') 关联的是哪张表的哪个字段  将这两张表联系起来
    uid = db.Column(db.Integer,db.ForeignKey('user.uid'))



    like_users = db.relationship('User',secondary = 'like')

    def __init__(self,title,content,uid):
        self.title = title
        self.thum_content= content[:100] + '......'if len(content) > 100 else content
        self.content = content
        self.uid = uid

# 点赞 联系的是用户点赞了博客  博客被哪些用户点赞了
class Like(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    # 用户id 联系的是用户表中id
    uid = db.Column(db.Integer, db.ForeignKey('user.uid'))
    # 博客id 联系的是博客表中id
    bid = db.Column(db.Integer, db.ForeignKey('blog.bid'))

    def __init__(self,uid,bid):
        self.uid = uid
        self.bid = bid



