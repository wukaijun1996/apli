#-*- codeing = utf-8 -*-
# @Time : 2022/3/27 23:07 
# @Author : wu
# @File : user.py 
# @Software: PyCharm

from flask import Blueprint,request,render_template

user_bp = Blueprint('user',__name__,url_prefix='/user')

@user_bp.route('/register/',methods = ['GET','POST'])
def register():
    if request.method == "GET":
        # 只获取注册页面
        return render_template('register.html')













