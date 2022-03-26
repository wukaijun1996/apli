#-*- codeing = utf-8 -*-
# @Time : 2022/3/26 0:22 
# @Author : wu
# @File : manage3.py 
# @Software: PyCharm
from flask import Flask,render_template,redirect,url_for
from flask_script import Manager

# 导入小分支
from views.movie import movie_bp
from views.music import music_bp

app = Flask(__name__)
app.config['ENV'] = 'developmeng'
app.config['DEBUG'] = True

# 合并小分支到主项目下
app.register_blueprint(music_bp)
app.register_blueprint(movie_bp)


manager = Manager(app)

@app.route('/')
def index():
    return render_template('start.html')

@app.route('/hello/')
def hello():
    return redirect(url_for('index'))

if __name__ == '__main__' :
    manager.run()


