# from flask import Flask, url_for
# from markupsafe import escape
# from flask import render_template
# from flask_sqlalchemy import SQLAlchemy
# import os

# app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path,'data.db') # 数据库文件的路径
# name = 'Monty_Lee'
# movies = [
#     {'title': 'My Neighbor Totoro', 'year': '1988'},
#     {'title': 'Dead Poets Society', 'year': '1989'},
#     {'title': 'A Perfect World', 'year': '1993'},
#     {'title': 'Leon', 'year': '1994'},
#     {'title': 'Mahjong', 'year': '1996'},
#     {'title': 'Swallowtail Butterfly', 'year': '1996'},
#     {'title': 'King of Comedy', 'year': '1999'},
#     {'title': 'Devils on the Doorstep', 'year': '1999'},
#     {'title': 'WALL-E', 'year': '2008'},
#     {'title': 'The Pork of Music', 'year': '2012'},
# ]
# db = SQLAlchemy(app)

# @app.route('/') # URL 规则
# def index():
#     return render_template('index.html',name=name,movies=movies)

# sudo lsof -i:5000  ## 此条指令用于查询端口正在被那些进程占据
# sudo kill -9 PID ## 此条指令可将上述查出来占用的端口给删除掉，其中，PID根据上述查询出来的结果而定


import os
import sys
import click

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控
db = SQLAlchemy(app)  # 初始化扩展，传入程序实例 app

class User(db.Model):  # 表名将会是 user（自动生成，小写处理）
    id = db.Column(db.Integer, primary_key=True)  # 主键
    name = db.Column(db.String(20))  # 名字

class Movie(db.Model):  # 表名将会是 movie
    id = db.Column(db.Integer, primary_key=True)  # 主键
    title = db.Column(db.String(60))  # 电影标题
    year = db.Column(db.String(4))  # 电影年份

'''
如果你改动了模型类，想重新生成表模式，那么需要先使用 db.drop_all() 删除表，然后重新创建：
>>> db.drop_all()
>>> db.create_all()
'''

@app.cli.command()  # 注册为命令
@click.option('--drop', is_flag=True, help='Create after drop.')  # 设置选项
def initdb(drop):
    """Initialize the database."""
    if drop:
        db.drop_all()
    db.create_all()
    click.echo('Initialized database.')  # 输出提示信息

@app.route('/')
def index():
    user = User.query.first()
    movies = Movie.query.all()
    return render_template('index.html', name='Monty _Lee', movies=movies)

@app.cli.command()
def forge():
    """ Generate fake data. """
    name = 'Monty Lee'
    movies = [
        {'title': 'My Neighbor Totoro', 'year': '1988'},
        {'title': 'Dead Poets Society', 'year': '1989'},
        {'title': 'A Perfect World', 'year': '1993'},
        {'title': 'Leon', 'year': '1994'},
        {'title': 'Mahjong', 'year': '1996'},
        {'title': 'Swallowtail Butterfly', 'year': '1996'},
        {'title': 'King of Comedy', 'year': '1999'},
        {'title': 'Devils on the Doorstep', 'year': '1999'},
        {'title': 'WALL-E', 'year': '2008'},
        {'title': 'The Pork of Music', 'year': '2012'},
    ]

    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m['title'], year=m['year'])
        db.session.add(movie)

    db.session.commit()
    click.echo('Done.')