from flask import Flask,render_template
import pymysql
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
app = Flask(__name__)           #实例化flask
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://flask:flask@10.10.10.11:3306/flask_movie?charset=utf8"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = os.urandom(24)


app.debug = True
db = SQLAlchemy(app)

#导入蓝图对象(from 文件夹 import 定义的蓝图名称（本例在_init__中定义的）)
from admin import adminbapp as admin_blueprint
from home import homebapp as home_blueprint

#注册(对象名称（蓝图名称），url前缀)
app.register_blueprint(home_blueprint)          #前台首页不需要设置后缀
app.register_blueprint(admin_blueprint,url_prefix='/admin')         #后台登录设置一下前缀

@app.errorhandler(404)
def page_noe_found(error):
    return render_template('home/404.html'),404



# if __name__ == '__main__':
#     app.run()
