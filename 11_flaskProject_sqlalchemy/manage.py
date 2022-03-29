from flask import Flask,request
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import MigrateCommand,Migrate
from sqlalchemy import and_,or_,desc

app = Flask(__name__)
app.config['ENV'] = 'developmeng'
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/book_2'

manager = Manager(app)

db = SQLAlchemy(app)

migrate = Migrate(app,db)
manager.add_command('database',MigrateCommand)

class Student(db.Model):
    sid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer)
    score = db.Column(db.Float)

    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/add/')
def add():
    name = input('输入姓名：')
    age = int(input('输入年龄'))
    score = float(input('输入成绩'))

    stu = Student(name,age,score)
    # 添加到对象关系映射数据库
    db.session.add(stu)
    # 提交同步到真实数据库
    db.session.commit()
    return '添加成功'

@app.route('/search/')
def search():
    # 查询所有
    stus = Student.query.all()
    print(stus)
    # 查询要求的有多少行
    lines = Student.query.count()
    print(lines)
    # 获取满足要求的第一个对象
    stu = Student.query.first()
    print(stu)
    # 添加筛选条件filter
    stus = Student.query.filter(Student.score > 80).all()
    print(stus)

    stu = Student.query.filter(Student.score > 80).first()
    print(stu)
    # 获取姓李学生的个数
    count = Student.query.filter(Student.name.startswith('李')).count()
    print(count)
    # 获取包含李字学生信息
    stus = Student.query.filter(Student.name.contains('李')).all()
    print(stus)
    # 查询成绩在70-100之间的信息
    stus = Student.query.filter(Student.score >= 70,Student.score <= 100).all()
    print(stus)
    # and_（条件1，条件2） 并且的关系
    stus = Student.query.filter(and_(Student.score >= 70,Student.score <= 100)).all()
    print(stus)
    stus = Student.query.filter(or_(Student.score <= 70,Student.score >= 100)).all()
    print(stus)


    # 排序  把满足条件的学生按照成绩升序排序
    stus = Student.query.order_by(Student.score).all()
    print(stus)
    # 排序  把满足条件的学生按照成绩降序排序
    stus = Student.query.order_by(desc(Student.score)).all()
    print(stus)

    # 判断成员  查看学号是 1 3 4 5 的学生信息
    stus = Student.query.filter(Student.sid.in_([1,3,4,5])).all()
    print(stus)

    # 根据主键获取对象
    stu = Student.query.get(4)
    print(stu)

    return '查询成功'


# 修改
@app.route('/update/')
def update():
    return "修改成功"







if __name__ == '__main__':


    manager.run()
