from flask import Blueprint,render_template,redirect

resource = Blueprint("resource",__name__)

@resource.route('/resource')
def resourcehome():
    return render_template('resource/resource.html')

@resource.route('/r_study')
def r_study():
    return render_template('resource/r_study.html')

@resource.route('/r_project')
def r_project():
    return render_template('resource/r_project.html')