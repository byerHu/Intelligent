# coding:utf8
from . import home  # 从当前目录导入home蓝图
from flask import render_template, request, flash, redirect, url_for, session
from app.home.forms import RegisterForm, LoginForm, SearchForm
from app import app
from app.models import User, Law
from app import db, app
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy import and_


# 首页
@home.route("/")
def index():
    return render_template('home/index.html')


# 搜索页
@home.route('/search/', methods=['GET', 'POST'])
@login_required
def search():
    data = request.args.get('search_key')
    print(data)
    words = ['%' + data + '%']
    rule = and_(*[Law.key.like(w) for w in words])
    res = Law.query.filter(rule).first()
    if not res:
        return redirect(url_for('home.index'))
    else:
        return render_template('home/search.html', res=res)


# 条文详情页
@home.route('/provision/detail')
@login_required
def provision_detail():
    return render_template('home/provision_detail.html')


# 案件描述页
@home.route('/case/desc')
@login_required
def case_desc():
    return render_template('home/case_desc.html')


# 搜索明细
@home.route('/search/detail')
@login_required
def search_detail():
    return render_template('home/search_detail.html')


# 法律条文
@home.route('/legalprovision/')
@login_required
def legalprovision():
    return render_template('home/legalprovision.html')


# 注册页
@home.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        data = form.data
        # print(data)
        user = User.query.filter_by(username=data["username"]).first()
        if user:
            flash("用户名已经注册!", "err")
            return redirect(url_for('home.register'))
        user = User(
            username=data["username"],
            pwd=data["pwd"]
        )
        db.session.add(user)
        db.session.commit()
        flash("注册成功,请登录", "ok")
        return redirect(url_for('home.login'))
    return render_template('home/register.html', form=form)


# 登录页
@home.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        user = User.query.filter_by(username=data["username"]).first()
        if not user:
            flash("用户不存在！", "err1")
        elif data['pwd'] != user.pwd:
            flash("密码错误!", "err2")
        else:
            login_user(user)
            # 登录成功,保存会话
            session[user.username] = data['username']
            return redirect(url_for('home.index'))

    return render_template('home/login.html', form=form)


# 登出
@home.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash(u'您已退出登陆')
    return redirect(url_for('home.login'))


# 案件研判
@home.route('/case/judge')
@login_required
def case_judge():
    return render_template('home/case_judge.html')


# 判决文书
@home.route('/judgmentdoc/')
@login_required
def judgmentdoc():
    return render_template('home/judgmentdoc.html')
