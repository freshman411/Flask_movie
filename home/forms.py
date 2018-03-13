#!/usr/bin/env python
#-*-coding:utf-8-*-

from flask_wtf import FlaskForm                 #FlaskForm 为表单基类
from wtforms import StringField,PasswordField,SubmitField,TextAreaField,FileField     #导入字符串字段，密码字段，提交字段
from wtforms.validators import DataRequired,ValidationError,Email,Regexp,EqualTo
from models import User

class RegistUser(FlaskForm):
    account = StringField(
        # 标签
        label="昵称",
        # 验证器
        validators=[
            DataRequired('请输入昵称')
        ],
        description="昵称",
        # 附加选项,会自动在前端判别
        render_kw={
            "class":"form-control",
            "placeholder":"请输入昵称",
            #"required":'required'               #表示输入框不能为空
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
            #"required": 'required'  # 表示输入框不能为空
        }
    )

    phone = StringField(
        label="手机",
        # 验证器
        validators=[
            DataRequired('请输入手机号码'),
            Regexp("1[3578]\d{9}", message="手机格式不正确")  # 用正则匹配手机号码规则
        ],
        description="手机",
        # 附加选项,会自动在前端判别
        render_kw={
            "class": "form-control",
            "placeholder": "请输入手机号码",
            #"required": 'required'  # 表示输入框不能为空
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
            #"required": 'required'  # 表示输入框不能为空
        }
    )

    repwd = PasswordField(
        # 标签
        label="确认密码",
        # 验证器
        validators=[
            DataRequired('确认密码'),
            EqualTo('pwd',message="两次密码输入不一致")
        ],
        description="确认密码",
        # 附加选项,会自动在前端判别
        render_kw={
            "class": "form-control",
            "placeholder": "确认密码",
            #"required": 'required'  # 表示输入框不能为空
        }
    )
    submit = SubmitField(
        label="注册",
        render_kw={
            "class": "btn btn-success btn-block",
        }
    )

    # 账号认证，自定义验证器
    def validate_name(self, filed):
        name = filed.data
        account = User.query.filter_by(name=name).count()
        if account == 1:
            raise ValidationError("昵称已经存在")

    def validate_email(self, filed):
        emails = filed.data
        account = User.query.filter_by(email=emails).count()
        if account == 1:
            raise ValidationError("邮箱已经注册")

    def validate_phone(self, filed):
        phones = filed.data
        account = User.query.filter_by(phone=phones).count()
        if account == 1:
            raise ValidationError("手机号已经注册")


class LoginForm(FlaskForm):
    account = StringField(
        # 标签
        label="昵称",
        # 验证器
        validators=[
            DataRequired('请输入昵称')
        ],
        description="昵称",
        # 附加选项,会自动在前端判别
        render_kw={
            "class": "form-control input-lg",
            "placeholder": "用户名/邮箱/手机号",
            #"required":'required'               #表示输入框不能为空
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
            "class": "form-control input-lg",
            "placeholder": "密码",
            #"required": 'required'  # 表示输入框不能为空
        }
    )

    submit = SubmitField(
        label="登录",
        render_kw={
            "class": "btn btn-lg btn-success btn-block",
        }
    )

    # def validate_name(self, filed):
    #     name = filed.data
    #     email = filed.data
    #     phone = filed.data
    #     username = User.query.filter_by(name=name).count()
    #
    #     if username == 0 :
    #         raise ValidationError("账户不存在")

class UserForm(FlaskForm):
    name = StringField(
        # 标签
        label="昵称",
        # 验证器
        validators=[
            DataRequired('请输入昵称')
        ],
        description="昵称",

        render_kw={
            "class": "form-control",
            "placeholder": "昵称",

        }
    )
    email = StringField(
        # 标签
        label="邮箱",
        # 验证器
        validators=[
            DataRequired('请输入邮箱'),
            Email("邮箱")
        ],
        description="昵称",

        render_kw={
            "class": "form-control",
            "placeholder": "邮箱",

        }
    )

    phone = StringField(
        # 标签
        label="手机",
        # 验证器
        validators=[
            DataRequired('请输入手机'),
            Regexp("1[3,5,7,8]\d{9}",message="手机格式不正确")
        ],
        description="手机",

        render_kw={
            "class": "form-control",
            "placeholder": "手机",

        }
    )

    face = FileField(

        label="头像",
        # 验证器
        validators=[
            DataRequired('上传头像')
        ],
        description="昵称",


    )

    des = TextAreaField(
        # 标签
        label="简介",
        # 验证器
        validators=[
            DataRequired('请输入简介')
        ],
        description="简介",

        render_kw={
            "class": "form-control",
            "rows":10

        }
    )
    submit = SubmitField(
        label="保存修改",
        render_kw={
            "class": "btn btn-success",
        }
    )
