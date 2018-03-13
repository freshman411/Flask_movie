#!/usr/bin/env python
#-*-coding:utf-8-*-

#导入模块
from flask_wtf import FlaskForm                 #FlaskForm 为表单基类
from wtforms import StringField,PasswordField,SubmitField     #导入字符串字段，密码字段，提交字段
from wtforms.validators import DataRequired,ValidationError,Email
from models import Admin

#定义登录表单
class LoginForm(FlaskForm):
    account = StringField(
        # 标签
        label="用户名",
        # 验证器
        validators=[
            DataRequired('请输入用户名')
        ],
        description="用户名",
        # 附加选项,会自动在前端判别
        render_kw={
            "class":"form-control",
            "placeholder":"请输入用户名",
            "required":'required'               #表示输入框不能为空
        }
    )

    email = StringField(
        label="邮箱",
        # 验证器
        validators=[
            DataRequired('请输入邮箱'),
            Email('邮箱格式不正确')
        ],
        description="邮箱",
        # 附加选项,会自动在前端判别
        render_kw={
            "class": "form-control",
            "placeholder": "请输入邮箱!",
            "required": 'required'  # 表示输入框不能为空
        }
    )

    phone = StringField(
        label="手机",
        # 验证器
        validators=[
            DataRequired('请输入手机号'),
            Email('邮箱格式不正确')
        ],
        description="手机",
        # 附加选项,会自动在前端判别
        render_kw={
            "class": "form-control",
            "placeholder": "请输入手机好嘛",
            "required": 'required'  # 表示输入框不能为空
        }
    )

    pwd = PasswordField(
        # 标签
        label="密码",
        # 验证器
        validators=[
            DataRequired('请输入密码')
        ],
        description="密码",
        # 附加选项,会自动在前端判别
        render_kw={
            "class": "form-control",
            "placeholder": "请输入密码!",
            "required": 'required'  # 表示输入框不能为空
        }
    )


    submit = SubmitField(
        label="登录",
        render_kw={
            "class": "btn btn-primary btn-block btn-flat",
        }
    )

#账号认证，自定义验证器
    # def validata_account(self,filed):
    #     account = filed.data
    #     admin = Admin.query.filter_by(name=account).count()
    #     if admin == 0:
    #         raise ValidationError("账号不存在")
