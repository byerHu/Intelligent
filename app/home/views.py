# coding:utf8
from . import home  # 从当前目录导入home蓝图
from flask import render_template, request, flash, redirect, url_for, session
from app.home.forms import RegisterForm, LoginForm, SearchForm
from app import app
from app.models import User, Law, Case, Cases
from app import db, app
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy import and_
import json
import os


# 首页
@home.route("/")
def index():
    return render_template('home/index.html')


# 搜索页
@home.route('/search/', methods=['GET', 'POST'])
@login_required
def search():
    data = request.args.get('search_key')
    words = ['%' + data + '%']
    rule = and_(*[Law.keywords.like(w) for w in words])
    res_1 = Law.query.filter(rule).first()
    if res_1:
        res_2 = Law.query.filter_by(id=res_1.similarity_1).first()
        res_3 = Law.query.filter_by(id=res_1.similarity_2).first()
        res = []
        res.append(res_1)
        res.append(res_2)
        res.append(res_3)
        return render_template('home/search.html', res=res)
    else:
        return redirect(url_for('home.index'))


# 条文详情页
@home.route('/provision/detail/<id>')
@login_required
def provision_detail(id):
    res_1 = Law.query.filter_by(id=id).first()
    if res_1:
        res_2 = Law.query.filter_by(id=res_1.similarity_1).first()
        res_3 = Law.query.filter_by(id=res_1.similarity_2).first()
        res = []
        res.append(res_1)
        res.append(res_2)
        res.append(res_3)
    return render_template('home/provision_detail.html', res=res)


mydata = ""

fname = os.getcwd() + "/app/templates/home/data.json"


# 文件上传页
@home.route('/upload')
@login_required
def upload():
    data = request.args.get('text')
    print(data)
    case = Case.query.filter_by(fact=data).first()
    js = {}
    js["criminals"] = case.criminals
    js["death_penalty"] = case.death_penalty
    js["imprisonment"] = case.imprisonment
    js["life_imprisonment"] = case.life_imprisonment
    js["punish_of_money"] = case.punish_of_money
    js["accusation"] = case.accusation
    js["relevant_articles"] = case.relevant_articles
    res = []
    res.append(js)
    a = {}
    a['site'] = res
    mydata = json.dumps(a, ensure_ascii=False).encode("utf8")
    with open(fname, 'wb') as f:
        f.write(mydata)
        f.close()
    return render_template('home/case_judge.html')


@home.route('/data/')
def data():
    return render_template('home/data.json')


# 案件描述页
@home.route('/case/desc/<id>')
@login_required
def case_desc(id):
    case = Cases.query.filter_by(id=id).first()
    return render_template('home/case_desc.html',case=case)


# 搜索明细
@home.route('/search/detail/<res>')
@login_required
def search_detail(res):
    res_1 = Law.query.filter_by(id=res).first()
    if res_1:
        res_2 = Law.query.filter_by(id=res_1.similarity_1).first()
        res_3 = Law.query.filter_by(id=res_1.similarity_2).first()
        res = []
        res.append(res_1)
        res.append(res_2)
        res.append(res_3)
    return render_template('home/search_detail.html', res=res)


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
@home.route('/case/judge', methods=['GET', 'POST'])
@login_required
def case_judge():
    return render_template('home/case_judge.html')


# 判决文书
@home.route('/judgmentdoc/')
@login_required
def judgmentdoc():
    return render_template('home/judgmentdoc.html')


# 文书明细
@home.route('/wenshu/detail/')
@login_required
def wenshu_search_detail():
    cases = Cases.query.limit(10)
    return render_template('home/wenshu_search_detail.html', cases=cases)
