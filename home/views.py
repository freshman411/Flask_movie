#!/usr/bin/env python
#-*-coding:utf-8-*-

from . import homebapp
from flask import render_template,redirect,url_for,request,flash,session,send_from_directory
from models import User,UserLog
from .forms import RegistUser,LoginForm,UserForm
from werkzeug.security import generate_password_hash
from movie_project import db,app
import uuid,os
from functools import wraps
from werkzeug.utils import secure_filename

def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if session.get('user'):   #验证session
            return func(*args, **kwargs)
        else:
            return redirect(url_for('home.login',next=request.url))
    return decorated_function


@homebapp.route("/")
def index():
    return render_template('home/index.html')

@homebapp.route("/animation/")
def animation():
    return render_template('home/animation.html')

@homebapp.route("/login/",methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        user = User.query.filter_by(name=data['account']).first()

        # email = User.query.filter(email=data['account']).first()
        # phone = User.query.filter(phone=data['account']).first()
        if user is None:
            flash("账号不存在",'err')
            return redirect(url_for('home.login'))
        else:
            if not user.check_pwd(data['pwd']):
                print (data['pwd'])
                flash("密码不正确",'err')
                return redirect(url_for('home.login'))
            flash("登录成功",'ok')
            session['user_id'] = user.id
            session['user'] = user.name
            userlog = UserLog(
                user_id = user.id,
                ip=request.remote_addr
            )
            db.session.add(userlog)
            db.session.commit()
            return redirect(url_for('home.user'))

    return render_template('home/login.html',form=form)

            #检验密码

        #return render_template("home/login.html",form=form)

@homebapp.route("/logout/")
def logout():
    session.pop('user',None)
    session.pop('user_id',None)
    return redirect(url_for('home.login'))

@homebapp.route("/register/",methods=['GET','POST'])
def register():
    form = RegistUser() #实例化form

    if form.validate_on_submit():
        data = form.data
        user = User(
            name=data['account'],
            email=data['email'],
            phone = data['phone'],
            pwd=generate_password_hash(data['pwd']),
            uuid = uuid.uuid4().hex
        )
        db.session.add(user)
        db.session.commit()
        flash("注册成功",'ok')
    return render_template("home/register.html",form=form)

@homebapp.route('/user/',methods=['GET','POST'])
@login_required
def user():
    form = UserForm()
    user = User.query.get(int(session['user_id']))
    form.face.validators = []
    if request.method == 'GET':
        form.name.data = user.name
        form.email.data = user.email
        form.phone.data = user.phone
        form.des.data = user.info
    if form.validate_on_submit():
        data = form.data
    return render_template('home/user.html',form = form,user=user)

@homebapp.route('/pwd/')
def pwd():
    return render_template('home/pwd.html')

@homebapp.route('/comments/')
def comments():
    return render_template('home/comments.html')

@homebapp.route('/loginlog/')
def loginlog():
    return render_template("home/loginlog.html")

@homebapp.route('/moviecol/')
def moviecol():
    return render_template("home/moviecol.html")


@homebapp.route('/search/')
def search():
    return render_template("home/search.html")

@homebapp.route('/play/')
def play():
    return render_template("home/play.html")


