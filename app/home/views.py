# coding:utf8
from . import home  # 从当前目录导入home蓝图
from flask import render_template


# 首页
@home.route("/")
def index():
    return render_template('home/index.html')


# 搜索页
@home.route('/search/')
def search():
    return render_template('home/search.html')


# 条文详情页
@home.route('/provision/detail')
def provision_detail():
    return render_template('home/provision_detail.html')


# 案件描述页
@home.route('/case/desc')
def case_desc():
    return render_template('home/case_desc.html')


# 法律条文
@home.route('/legalprovision/')
def legalprovision():
    return render_template('home/legalprovision.html')


# 注册页
@home.route('/register/')
def register():
    return render_template('home/register.html')


# 登录页
@home.route('/login/')
def login():
    return render_template('home/login.html')


# 案件研判
@home.route('/case/judge')
def case_judge():
    return render_template('home/case_judge.html')


# 判决文书
@home.route('/judgmentdoc/')
def judgmentdoc():
    return render_template('home/judgmentdoc.html')
