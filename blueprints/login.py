from flask import Blueprint, g, render_template, request, session, flash, url_for, redirect
from blueprints.forms import LoginForm, RegisterForm
from decorators import login_required
from exts import db
from models import UserModel

login = Blueprint("login", __name__, url_prefix='/')


@login.route('/')
def home():
    return render_template('login/login.html')


@login.route("/login", methods=['POST', 'GET'])
def log_in():
    if hasattr(g, 'user'):
        return render_template('Home/index.html', username='1', password='1')
    if request.method == 'POST':
        form = LoginForm(request.form)
        if form.validate():
            username = form.username.data
            password = form.password.data
            user = UserModel.query.filter_by(username=username).first()
            if user:
                if not user.password == password:
                    flash('账号密码不正确！')
                    return render_template('login/login.html', data=form)
                session['userid'] = user.id
                return render_template('Home/index.html', username='1', password='1')
            else:
                flash('账户或密码格式有误，请检查！')
                return render_template('login/login.html', data=form)
        else:
            flash('账户或密码格式有误，请检查！')
            return render_template('login/login.html', data=form)
    else:
        return render_template('login/login.html')


@login.route("/register", methods=['POST', 'GET'])
def register():
    if hasattr(g, 'user'):
        return redirect(url_for('Home.indexhome'))
    if request.method == 'GET':
        return render_template('login/register.html')
    form = RegisterForm(request.form)
    if form.validate():
        username = form.username.data
        password = form.password.data
        rpassword = form.rpassword.data
        if password != rpassword:
            flash('两次密码输入不一致')
            return render_template('login/register.html', data=form)
        user = UserModel(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        flash('注册成功，三秒后跳转到登录页面！')
        return redirect(url_for('login.log_in'))
    else:
        for mes in form.errors:
            if mes:
                flash(form.errors[mes][1])
        return render_template('login/register.html', data=form)


@login.route('/logoff')
@login_required
def logoff():
    session.clear()
    flash("账号已退出")
    return render_template('login/login.html')


@login.route('/logout')
@login_required
def logout():
    user = UserModel.query.filter_by(id=g.user.id).first()
    if user:
        db.session.delete(user)
        db.session.commit()
    session.clear()
    flash("账号已注销")
    return render_template('login/login.html')
