# coding:utf8
from . import home  # 从当前目录导入home蓝图
from flask import render_template


@home.route("/")
def index():
    return render_template('home/index.html')


@home.route('/legalprovision/')
def legalprovision():
    return render_template('home/legalprovision.html')


@home.route('/register/')
def register():
    return render_template('home/register.html')


@home.route('/login/')
def login():
    return render_template('home/login.html')


@home.route('/list/')
def list():
    return render_template('home/list.html')


@home.route('/judgmentdoc/')
def judgmentdoc():
    return render_template('home/judgmentdoc.html')
