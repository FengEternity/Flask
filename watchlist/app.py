from flask import Flask, url_for
from markupsafe import escape
from flask import render_template

app = Flask(__name__)

name = 'Monty_Lee'
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

@app.route('/') # URL 规则
def index():
    return render_template('index.html',name=name,movies=movies)

# sudo lsof -i:5000  ## 此条指令用于查询端口正在被那些进程占据
# sudo kill -9 PID ## 此条指令可将上述查出来占用的端口给删除掉，其中，PID根据上述查询出来的结果而定
