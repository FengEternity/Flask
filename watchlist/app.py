from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/') # URL 规则
def hello():
    return '<h1><center>Hello Monty_Lee!</center></h1><center><img src="http://helloflask.com/totoro.gif"></center>'

@app.route('/user/<name>')
def user_page(name):
    return '<h1>Hello, %s!</h1>' % escape(name)

@app.route('/test')
def test_url_for():
    print(url_for('test'))
    print(url_for('user_page', name='Monty_Lee'))
    print(url_for('user_page', name='Peter'))
    print(url_for('test_url_for'))
    print(url_for('test_url_for', num=2))
    return 'Test page'

# sudo lsof -i:5000  ##此条指令用于查询端口正在被那些进程占据
# sudo kill PID ## 此条指令可将上述查出来占用的端口给删除掉，其中，PID根据上述查询出来的结果而定
