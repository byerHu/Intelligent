# coding:utf8
from flask import Flask

app = Flask(__name__)
app.debug = True

from app.home import home as home_blueprint  # 导入home蓝图对象
from app.admin import admin as admin_blueprint  # 导入admin蓝图对象

app.register_blueprint(home_blueprint)  # 注册home蓝图
app.register_blueprint(admin_blueprint, url_prefix="/admin")  # 注册admin蓝图对象
