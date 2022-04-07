#-*- codeing = utf-8 -*-
# @Time : 2022/3/27 23:07 
# @Author : wu
# @File : user.py 
# @Software: PyCharm

from flask import Blueprint, request, render_template, redirect, url_for, session
from apps.models.blogmodels import User
from exts import db
import urlpath

user_bp = Blueprint('user',__name__,url_prefix='/user')

@user_bp.route('/register/',methods = ['GET','POST'])
def register():
    if request.method == "GET":
        # 只获取注册页面
        return render_template('register.html')
    else:
        #获取post提交的数据
        print(f'{request.form}')
        name= request.form.get('username')
        psw = request.form.get('psw')
        phone = request.form.get('phone')
        # 创建对象
        user = User(name,psw,phone)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('user.login'))

# 检验用户名是否存在
@user_bp.route('/checkname/',methods=['POST'])
def check_name():
    print(request.form)
    username = request.form.get('username')
    # 在数据库中查询
    data = User.query.filter(User.username == username).first()
    print(data)
    if data:
        return {'code': 2000,'msg': '用户名已存在'}
    else:
        return {'code': 2001,'msg': '用户名不存在'}


# 检验手机号是否被注册
@user_bp.route('/checkphone/',methods=['POST'])
def check_phone():
    print(request.form)
    phone= request.form.get('phone')
    # 在数据库中查询
    data = User.query.filter(User.phone == phone).first()
    print(data)
    if data:
        return {'code': 2000,'msg': '手机号已被注册'}
    else:
        return {'code': 2001,'msg': '手机号可用'}

@user_bp.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html', message = '')
    else:
        print(request.form)
        # 提取数据 根据数据查询
        username = request.form.get('username')
        password = request.form.get('psw')
        user = User.query.filter(User.username == username,User.password == password).first()
        print(user)
        if user:
            # 保存用户的信息  证明是哪个用户登录的
            session['username'] = username  #存储用户名
            print(session)

            return redirect(urlpath.current_url)
        else:
            return render_template('login.html',message = "登录失败")

@user_bp.route('/exit/')
def exit():
    # 移除存储的用户登录的状态
    session.pop('username')
    print(session)
    return redirect(url_for('index'))

@user_bp.route('/updateicon/',methods=['GET','POST'])
def updateicon():
    if request.method == 'GET':
        return render_template('updateicon.html')
    else:
        # 接收数据
        print(request.form)
        # 接收图片数据
        print(request.files)  #ImmutableMultiDict([('icon', <FileStorage: 'notepad++.exe' ('application/x-msdownload')>)])

        # 把文件存储到本地
        icon = request.files.get('icon')

        # print(basepath)

        return '修改成功'













