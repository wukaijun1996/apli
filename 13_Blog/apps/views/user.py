#-*- codeing = utf-8 -*-
# @Time : 2022/3/27 23:07 
# @Author : wu
# @File : user.py 
# @Software: PyCharm

from flask import Blueprint,request,render_template
from apps.models.blogmodels import User
from exts import db

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

        return render_template('login.html')

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

















