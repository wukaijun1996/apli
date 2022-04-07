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
    print(url_for('static', filename='default.jpg'))

    # 查询所有的博客，把它渲染在首页上
    blogs = Blog.query.all()
    print(blogs)
    if session.get('username'):
        user = User.query.filter(User.username == session.get('username')).first()
        print(user.like_blogs)
        # 要拿到用户点过哪些博客 （列表） 传参  ， 在页面判断当前博客bid是否在列表中
        like_bids = [blog.bid for blog in user.like_blogs]
        return render_template('new_index.html',blogs=blogs,like_bids = like_bids)
    else:
        return render_template('new_index.html',blogs=blogs)


# 设置点赞路由
@blog_bp.route('/like/')
def like():
    print(request.args)
    if session.get("username"):
        # 获取点赞需要的数据
        user = User.query.filter(User.username == session.get('username')).first()
        # 获取博客的ID
        bid = int(request.args.get('bid'))
        blog = Blog.query.get(bid)  #根据bid获取当前博客对象
        like = Like(user.uid,bid)
        db.session.add(like)
        db.session.commit()

        # print(type(bid))
        print(f'当前{session.get("username")}用户点赞的博客 {user.like_blogs}')
        print(f'当前这篇博客的喜爱者有 {blog.like_users}')
        return redirect(url_for('blog.blogindex'))
    else:
        urlpath.current_url = url_for('blog.blogindex')
        # 跳转到登录页面
        return redirect(url_for('user.login'))

@blog_bp.route('/unlike/')
def unlike():
    # 获取点赞需要的数据
    user = User.query.filter(User.username == session.get('username')).first()
    # 获取博客的ID
    bid = int(request.args.get('bid'))
    blog = Blog.query.get(bid)  # 根据bid获取当前博客对象

    # 在like中查询这条记录
    like = Like.query.filter(Like.uid == user.uid,Like.bid == bid).first()
    db.session.delete(like)
    db.session.commit()
    print("删除点赞成功")
    return redirect(url_for('blog.blogindex'))


# 既接收点赞的请求 也接受取消点赞的请求
@blog_bp.route('/likeorunlike/')
def likeorunlike():

    if session.get('username'):
        # 获取操作的博客id
        bid = int(request.args.get('bid'))
        # 根据bid获取到博客对象
        blog = Blog.query.get(bid)
        # 获取用户信息
        user = User.query.filter(User.username == session.get('username')).first()
        # 区分用户要进行点赞还是进行取消
        flag = False
        for like_user in blog.like_users:
            if like_user.username == session.get('username'):
                flag = True
                break
        if flag is True:
            # 取消点赞
            like = Like.query.filter(Like.uid == user.uid,Like.bid == bid).first()
            db.session.delete(like)
            db.session.commit()
        else:
            # 进行点赞
            like = Like(user.uid,bid)
            db.session.add(like)
            db.session.commit()
        return redirect(url_for('blog.blogindex'))
    else:
        urlpath.current_url = url_for('blog.blogindex')
        return redirect(url_for('user.login'))




