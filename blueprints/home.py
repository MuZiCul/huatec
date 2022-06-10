from flask import Blueprint, render_template
home = Blueprint("home", __name__, url_prefix='')


@home.route('/home')
def indexhome():
    return render_template('Home/index.html')


@home.route('/shouye', methods=['GET', 'POST'])
def shouye():
    return render_template('Home/home.html')


@home.route('/user')
def user():
    return render_template('user/user.html')


@home.route('/u_selftion')
def u_selftion():
    sno = "1910602142"
    name = "刘世敏"
    sex = "女"
    faculty = "人工智能学院"
    sclass = "计科一班"
    return render_template('user/u_selftion.html',
                           my_sno=sno,
                           my_name=name,
                           my_sex=sex,
                           my_faculty=faculty,
                           my_scalss=sclass)


@home.route('/u_liuyan')
def u_liuyan():
    return render_template('user/u-liuyan.html')


@home.route('/u_checking')
def u_checking():
    return render_template('user/u_checking.html')


@home.route('/u_conference')
def u_conference():
    return render_template('user/u_conference.html')


@home.route('/u_weekly')
def u_weekly():
    name = "刘世敏"
    return render_template('user/u_weekly.html',
                           my_name=name)


@home.route('/u_password')
def u_password():
    return render_template('user/u_password.html')
