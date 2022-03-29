#-*- codeing = utf-8 -*-
# @Time : 2022/3/27 23:07 
# @Author : wu
# @File : user.py 
# @Software: PyCharm

from flask import Blueprint,request,render_template
from apps.models.blogmodels import User

user_bp = Blueprint('user',__name__,url_prefix='/user')

@user_bp.route('/register/',methods = ['GET','POST'])
def register():
    if request.method == "GET":
        # 只获取注册页面
        return render_template('register.html')
    else:
        #获取post提交的数据
        print(f'{request.form}')
        return '注册成功'

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

    return 'ok'

















