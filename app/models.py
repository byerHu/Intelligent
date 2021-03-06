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
    __tablename__ = "law2"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) # 编号
    category = db.Column(db.String(100), unique=True)  # 类别
    catalog = db.Column(db.String(100)) # 目录
    keywords = db.Column(db.String(100)) # 关键词
    content = db.Column(db.Text) # 内容
    enactment = db.Column(db.String(100)) # 颁布单位
    number_reference = db.Column(db.String(100)) # 参考号
    date_promulgation = db.Column(db.DateTime, index=True, default=datetime.now)
    date_execution = db.Column(db.DateTime, index=True, default=datetime.now)
    timeliness = db.Column(db.String(100))
    level = db.Column(db.String(100))
    similarity_1 = db.Column(db.Integer)
    degree_1 = db.Column(db.String(100))
    similarity_2 = db.Column(db.Integer)
    degree_2 = db.Column(db.String(100))

# 案件模型
class Case(db.Model):
    __tablename__ = "cail_0518"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) # 编号
    criminals = db.Column(db.String(100), unique=True)  # 类别
    death_penalty = db.Column(db.String(255))
    imprisonment = db.Column(db.String(255))
    life_imprisonment = db.Column(db.String(255))
    punish_of_money = db.Column(db.Integer)
    accusation = db.Column(db.String(255))
    relevant_articles = db.Column(db.String(255))
    fact = db.Column(db.Text)

# case案件
class Cases(db.Model):
    __tablename__ = "case"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号
    title = db.Column(db.String(100), unique=True)
    content = db.Column(db.Text)
    hotword1 = db.Column(db.Text)
    hotword2 = db.Column(db.Text)
    name = db.Column(db.String(255))
    time = db.Column(db.String(255))
    header = db.Column(db.Text)
    infact = db.Column(db.Text)
    according_to = db.Column(db.Text)
    judicial_decision = db.Column(db.Text)
    tails = db.Column(db.Text)
    law_1 = db.Column(db.String(255))
    law_2 = db.Column(db.String(255))
'''
if __name__ == "__main__":
    db.create_all() # 创建所有的数据表
'''
