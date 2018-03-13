#!/usr/bin/env python
#-*-coding:utf-8-*-

from . import adminbapp
from flask import  render_template,redirect,url_for,flash,session,request
from admin.forms import LoginForm
from models import Admin,UserLog,User
from functools import wraps
from movie_project import db

#由于在注册app的时候给后台加了admin的后缀，所以这里默认的“/” 跳转到登录界面
# @adminbapp.route("/")
# def admin():
#     return render_template('admin/login.html')

def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if session.get('admin'):   #验证session
            return func(*args, **kwargs)
        else:
            return redirect(url_for('admin.login'))
    return decorated_function


@adminbapp.route('/login/',methods=['GET','POST'])
def login():
    forms = LoginForm()          #实例化
    if forms.validate_on_submit():       #提交的时候进行验证
        data = forms.data                #获取form数据信息
        admin = Admin.query.filter_by(name=data["account"]).first()
        # if admin == None:
        #     flash("账号不存在")
        #     return redirect(url_for('admin.login'))
        if admin != None and not admin.check_pwd(data["pwd"]): #这里的check_pwd函数在models 下Admin模型下定义
            flash("密码错误")
            return  redirect(url_for('admin.login'))
        session['admin'] = data['account']          #添加session
        #session['user_id'] = User.
        return redirect(request.args.get('next') or url_for('admin.index'))
    return render_template('admin/login.html',form=forms)

@adminbapp.route('/logout/')
def logout():
    session.pop('admin',None)                   #退出时删除session
    return redirect(url_for('admin.login'))

@adminbapp.route('/index/')
@login_required
def index():
    return render_template('admin/index.html')
#
@adminbapp.route('/pwd/')
@login_required
def pwd():
    return render_template('admin/pwd.html')

@adminbapp.route('/tag/add/')
@login_required
def tag_add():
    return render_template('admin/tag_add.html')

@adminbapp.route('/tag/list/')
@login_required
def tag_list():
    return render_template('admin/tag_list.html')

@adminbapp.route('/movie/add/')
@login_required
def movie_add():
    return render_template('admin/movie_add.html')

@adminbapp.route('/movie/list/')
@login_required
def movie_list():
    return render_template('admin/movie_list.html')

@adminbapp.route('/preview_add/')
@login_required
def preview_add():
    return render_template('admin/preview_add.html')

@adminbapp.route('/preview_list/')
@login_required
def preview_list():
    return render_template('admin/preview_list.html')

@adminbapp.route('/user_list/')
@login_required
def user_list():
    return render_template('admin/user_list.html')

@adminbapp.route('/user_view/')
@login_required
def user_view():
    return render_template('admin/user_view.html')


@adminbapp.route('/comment_list/')
@login_required
def comment_list():
    return render_template('admin/comment_list.html')

@adminbapp.route('/moviecol_list/')
@login_required
def moviecol_list():
    return render_template('admin/moviecol_list.html')

@adminbapp.route('/oplog_list/')
@login_required
def oplog_list():
    return render_template('admin/oplog_list.html')

@adminbapp.route('/adminloginlog_list/')
@login_required
def adminloginlog_list():
    return render_template('admin/adminloginlog_list.html')

@adminbapp.route('/userloginlog_list/<int:page>/',methods=['GET'])
@login_required
def userloginlog_list(page=None):
    if page is None:
        page = 1
    page_data = UserLog.query.filter_by(user_id = int(session['user_id'])).order_by(UserLog.addtime.desc()
                                                                                     .paginate(page=page,per_page=10))
    return render_template('admin/userloginlog_list.html',page_data = page_data)


@adminbapp.route('/auth_add/')
@login_required
def auth_add():
    return render_template('admin/auth_add.html')

@adminbapp.route('/auth_list/')
@login_required
def auth_list():
    return render_template('admin/auth_list.html')


@adminbapp.route('/role_add/')
@login_required
def role_add():
    return render_template('admin/role_add.html')

@adminbapp.route('/role_list/')
@login_required
def role_list():
    return render_template('admin/role_list.html')

@adminbapp.route('/admin_add/')
@login_required
def admin_add():
    return render_template('admin/admin_add.html')

@adminbapp.route('/admin_list/')
@login_required
def admin_list():
    return render_template('admin/admin_list.html')




