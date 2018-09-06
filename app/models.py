# coding:utf8
from datetime import datetime

from app import db

from flask_login import UserMixin
from app import login_manager


@login_manager.user_loader
def get_user(ident):
    return User.query.get(int(ident))


# 用户数据模型
class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    username = db.Column(db.String(100), unique=True)  # 昵称
    pwd = db.Column(db.String(100))  # 密码


# 法律条文数据模型
class Law(db.Model):
    __tablename__ =  "law"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    catalog = db.Column(db.String(100), unique=True)  # 目录
    classes = db.Column(db.String(100))  # 类别
    key = db.Column(db.String(100)) # 关键词
    time = db.Column(db.DateTime, index=True, default=datetime.now)  # 颁布时间
    addr = db.Column(db.String(100))
    content = db.Column(db.Text)
'''
if __name__ == "__main__":
    db.create_all() # 创建所有的数据表
'''
