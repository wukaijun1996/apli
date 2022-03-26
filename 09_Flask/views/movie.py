#-*- codeing = utf-8 -*-
# @Time : 2022/3/26 17:25 
# @Author : wu
# @File : movie.py 
# @Software: PyCharm
from flask import Blueprint

# name --蓝图的名字 定位蓝图用的
# import_name 创建蓝图所在的模块名
# url_prefix   这个板块路由的前缀
movie_bp = Blueprint('movie',__name__,url_prefix='/movie/')

@movie_bp.route('/')
def index():
    return '电影首页'

