#!/usr/bin/env python
#-*-coding:utf-8-*-


import datetime
from movie_project import db

#用户
class User(db.Model):
    __tablename__ ="user"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable=False,unique=True)  #unique代表不能重复，唯一的
    pwd = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(64),nullable=False,unique=True)
    phone = db.Column(db.String(11),nullable=False,unique=True)
    info = db.Column(db.Text)
    face = db.Column(db.String(100))         #头像
    addtime = db.Column(db.DateTime,index=True,default=datetime.datetime.now)
    uuid = db.Column(db.String(255))

    userlogs = db.relationship('UserLog',backref='user') #外键关系关联
    comments = db.relationship('Comment',backref='user')
    movicols = db.relationship('Moviecol', backref='user')

    def __repr__(self): #定义返回的类型
        return '<user %r>' % self.name

    def check_pwd(self,pwd):
        from werkzeug.security import check_password_hash
        return  check_password_hash(self.pwd,pwd)


#登录日志
class UserLog(db.Model):
    __tablename__ = 'userlog'
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    ip = db.Column(db.String(30))
    addtime = db.Column(db.DateTime,index=True,default=datetime.datetime.now)

    def __repr__(self):
        return  '<userlog %r>' % self.id


#标签数据模型

class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),unique=True)
    addtime = db.Column(db.DateTime,index=True,default=datetime.datetime.now)
    movies = db.relationship('Movie',backref='tag')
    def __repr__(self):
        return '<tag %r>' % self.name


#电影模型

class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(20),unique=True)
    url = db.Column(db.String(255),unique=True)     #地址
    info = db.Column(db.Text)                       #简介
    logo = db.Column(db.String(255),unique=True)    #封面
    star = db.Column(db.SmallInteger)                #星级
    playnum = db.Column(db.BigInteger)                  #播放量
    commentnum = db.Column(db.BigInteger)               #评论量
    tag_id = db.Column(db.Integer,db.ForeignKey('tag.id'))
    area = db.Column(db.String(255))                #上映地区
    replease_time = db.Column(db.Date)              #上映时间
    length  = db.Column(db.String(100))
    addtime = db.Column(db.DateTime,index=True,default=datetime.datetime.now)

    comments = db.relationship('Comment',backref='movie')
    moviecols = db.relationship('Moviecol', backref='movie')

    def __repr__(self):
        return '<movie %r>' %  self.title


class Preview(db.Model):
    __tablename__ = 'preview'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unique=True)
    logo = db.Column(db.String(255), unique=True)
    addtime = db.Column(db.DateTime, index=True, default=datetime.datetime.now)
    def __repr__(self):
        return '<preview %r>' %  self.title


#评论

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    movie_id = db.Column(db.Integer,db.ForeignKey('movie.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    addtime = db.Column(db.DateTime,index=True,default=datetime.datetime.now)
    def __repr__(self):
        return '<content %r>' %  self.content

#电影收藏

class Moviecol(db.Model):
    __tablename__ = 'moviecol'
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    addtime = db.Column(db.DateTime, index=True, default=datetime.datetime.now)

    def __repr__(self):
        return '<Moviecol %r>' %  self.id


#权限及角色数据模型

class Auth(db.Model):
    __tablename__ = 'auth'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20),unique=True) #权限名称
    url = db.Column(db.String(255),unique=True)
    addtime = db.Column(db.DateTime, index=True, default=datetime.datetime.now)

    def __repr__(self):
        return '<auth %r>' %  self.name


#角色模型
class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)  # 权限名称
    auths = db.Column(db.String(600))
    addtime = db.Column(db.DateTime, index=True, default=datetime.datetime.now)

    def __repr__(self):
        return '<Role %r>' %  self.name


#管理员数据模型
class Admin(db.Model):
    __tablename= 'admin'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)  # unique代表不能重复，唯一的
    pwd = db.Column(db.String(100), nullable=False)
    is_super = db.Column(db.SmallInteger)  #是否为超级管理员
    role_id = db.Column(db.Integer,db.ForeignKey('role.id'))
    addtime = db.Column(db.DateTime, index=True, default=datetime.datetime.now)

    adminlogs = db.relationship('Adminlog',backref='admin')
    adminoption = db.relationship('Oplogs', backref='admin')

    def __repr__(self):
        return '<Admin %r>' % self.name

    def check_pwd(self,pwd):
        from werkzeug.security import check_password_hash
        return  check_password_hash(self.pwd,pwd)
#管理员登录日志

class Adminlog(db.Model):
    __tablename__ = 'adminlog'
    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    ip = db.Column(db.String(30))
    addtime = db.Column(db.DateTime, index=True, default=datetime.datetime.now)

    def __repr__(self):
        return '<Admin %r>' % self.name

#操作日志

class Oplogs(db.Model):
    __tablename__ = 'oplogs'
    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    ip = db.Column(db.String(30))
    reason = db.Column(db.String(600))  #操作原因
    addtime = db.Column(db.DateTime, index=True, default=datetime.datetime.now)

    def __repr__(self):
        return '<oplog %r>' % self.id


if __name__ == '__main__':
    db.create_all()
    # from werkzeug.security import generate_password_hash
    # role = Role(
    #     name="超级管理员",
    #     auths = ''
    # )
    # admin = Admin(
    #     name="test",
    #     pwd=generate_password_hash("test"),
    #     is_super=0,
    #     role_id=1
    # )
    # db.session.add(role)
    # db.session.add(admin)
    # db.session.commit()