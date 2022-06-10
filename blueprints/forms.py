import wtforms
from wtforms.validators import length

from models import UserModel


class LoginForm(wtforms.Form):
    username = wtforms.StringField(validators=[length(min=1, max=254)])
    password = wtforms.StringField(validators=[length(min=1, max=20)])

    def validate_username(self, field):
        data = field.data
        if len(data) < 1:
            raise wtforms.ValidationError('用户名不能为空！')

    def validate_password(self, field):
        data = field.data
        if len(data) < 1:
            raise wtforms.ValidationError('密码不能为空！')


class RegisterForm(wtforms.Form):
    username = wtforms.StringField(validators=[length(min=1, max=5)])
    password = wtforms.StringField(validators=[length(min=1, max=20)])
    rpassword = wtforms.StringField(validators=[length(min=1, max=20)])

    def validate_username(self, field):
        data = field.data
        if len(data) < 1:
            raise wtforms.ValidationError('用户名不能为空！')
        user_model_username = UserModel.query.filter_by(username=data).first()
        if user_model_username:
            raise wtforms.ValidationError('用户名已被使用！')

    def validate_password(self, field):
        data = field.data
        if len(data) < 1:
            raise wtforms.ValidationError('密码不能为空！')

