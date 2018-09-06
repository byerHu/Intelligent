from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired


# 搜索表单页面
class SearchForm(FlaskForm):
    '''搜索表单页面'''
    # 搜索框
    search_input = StringField(
        label='搜索关键词',
        validators=[
            DataRequired("请输入要搜索的内容!")
        ],
        description="搜索",
        render_kw={
            "class": "search-input",
            "style": "width:50%;height: 50px;text-align: center;",
            "placeholder": "请输入您要搜索的内容..."
        }
    )
    # 提交
    submit = SubmitField(
        label='搜索',
        render_kw={
            "class": "search-btn",
            "style": "width:10%;height: 50px;",
            "value": "搜索"
        }
    )


# 注册表单页面
class RegisterForm(FlaskForm):
    '''用户注册表单'''
    # 账号
    username = StringField(
        label='用户名',  # 标签
        validators=[
            DataRequired("请输入账号！")
        ],
        description="用户名",
        render_kw={
            "id": "username",
            "class": "form-control",
            "placeholder": "请输入用户名",
            "maxlength": "20"
        }
    )

    # 密码
    pwd = PasswordField(
        label="密码",
        validators=[
            DataRequired('请输入密码！')
        ],
        description="密码",
        render_kw={
            "id": "password",
            "class": "form-control",
            "placeholder": "请输入密码",
            "maxlength": "20"
        }
    )
    # 提交
    submit = SubmitField(
        label='注册',
        render_kw={
            "class": "form-control btn btn-primary",
            "id": "submit",
            "value": "立即注册"
        }
    )


# 登录表单页面
class LoginForm(FlaskForm):
    '''用户登录表单'''
    # 账号
    username = StringField(
        label='用户名',  # 标签
        validators=[
            DataRequired("请输入账号！")
        ],
        description="用户名",
        render_kw={
            "class": "form-control",
            "id": "inputEmail3",
            "placeholder": "username"
        }
    )

    # 密码
    pwd = PasswordField(
        label="密码",
        validators=[
            DataRequired('请输入密码！')
        ],
        description="密码",
        render_kw={
            "class": "form-control",
            "id": "inputPassword3",
            "placeholder": "Password"
        }
    )
    # 提交
    submit = SubmitField(
        label='注册',
        render_kw={
            "class": "btn btn-default",
            "value": "登录"
        }
    )
