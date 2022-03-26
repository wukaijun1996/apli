#-*- codeing = utf-8 -*-
# @Time : 2022/3/26 17:25 
# @Author : wu
# @File : music.py 
# @Software: PyCharm
from flask import Blueprint

# name --蓝图的名字 定位蓝图用的
# import_name 创建蓝图所在的模块名
# url_prefix   这个板块路由的前缀
music_bp = Blueprint('music',__name__,url_prefix='/music/')

@music_bp.route('/')
def index():
    return '音乐首页'