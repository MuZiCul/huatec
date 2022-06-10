from flask import Blueprint,render_template,redirect

system = Blueprint("system",__name__)

@system.route('/system')
def systemhome():
    return render_template('system/system.html')

@system.route('/s_user')
def s_user():
    return render_template('system/s_user.html')