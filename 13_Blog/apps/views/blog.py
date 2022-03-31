#-*- codeing = utf-8 -*-
# @Time : 2022/3/31 20:59 
# @Author : wu
# @File : blog.py 
# @Software: PyCharm

from flask import Blueprint,request,session,redirect,url_for,render_template
import urlpath
from apps.models.blogmodels import User,Blog,Like
from exts import db

blog_bp = Blueprint('blog',__name__,url_prefix='/blog')

# 发表博客
@blog_bp.route('/publish/',methods = ['GET','POST'])
def publish():
    if request.method == 'GET':
        # 使用session存储登录状态 这个状态有值
        if session.get('username'):
            return render_template('publish.html')

        else:
            # 到登录
            urlpath.current_url = url_for('blog.publish')
            return redirect(url_for('user.login'))
    else:
        print(request.form)
        # 获取发表博客的用户
        user = User.query.filter(User.username == session.get('username')).first()

        title = request.form.get('title')
        content = request.form.get('content')
        # 创建博客对象
        blog = Blog(title,content,user.uid)

        db.session.add(blog)
        db.session.commit()

        return redirect(url_for('index'))


# 首页内容展示
@blog_bp.route('/index/')
def blogindex():

    # 查询所有的博客，把它渲染在首页上
    blogs = Blog.query.all()
    print(blogs)

    return render_template('index.html',blogs=blogs)








