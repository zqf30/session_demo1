from flask import Flask, session
from models import Article
from exts import db
import config
import pymysql
import mysql.connector
pymysql.install_as_MySQLdb()


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

with app.app_context():
    db.create_all()

# 首页
@app.route('/')
def hello_world():
    session['username'] = 'zqf666'
    return 'Hello World!'



# 增加数据
@app.route('/add')
def addArticle():
    newArticle = Article(title='aaa', content='bbb')
    db.session.add(newArticle)
    db.session.commit()
    return "add successfully"

# 删除数据
@app.route('/del')
def delArticle():
    deArticle = Article.query.filter(Article.title == 'aaa').first()
    print(deArticle.title)
    db.session.delete(deArticle)
    db.session.commit()
    return "delete successfully"

# 改变数据
@app.route('/update')
def updtArticle():
    upArticle = Article.query.filter(Article.id == '1').first()
    print(upArticle.title)
    upArticle.title = 'new title'
    db.session.commit()
    return "update successfully"

# 查找数据
@app.route('/search')
def srchArticle():
    sArticle = Article.query.filter(Article.id == '1').first()
    print(sArticle.title)
    return "search successfully"

# 获取session
@app.route('/get')
def get():
    print(session.get('username'))
    session.clear()
    print(session.get('username'))
    return 'success'

# 设置session
@app.route('/session')
def sessionTest():
    session['username'] = 'zqf666'
    return 'session set successfully'

if __name__ == '__main__':
    app.run(host='127.0.0.1',
            port=8888,
            debug=True)
