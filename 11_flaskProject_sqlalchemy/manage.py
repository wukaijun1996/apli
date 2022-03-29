from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import MigrateCommand,Migrate



app = Flask(__name__)
app.config['ENV'] = 'developmeng'
app.config['DEBUG'] = True
SQLALCHEMY_DATASBASE_URI = 'mysql + pymysql://root:123456@127.0.0.1:3306/book_2'

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
        self.username = name
        self.password = age
        self.phone = score


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    manager.run()
