from flask import Blueprint,render_template,redirect

affair = Blueprint("affair",__name__)

@affair.route('/affair')
def affairhome():
    return render_template('affair/affair.html')

@affair.route('/a_conference')
def a_conference():
    return render_template('affair/a_conference.html')

@affair.route('/a_huiwu')
def a_huiwu():
    return render_template('affair/a_huiwu.html')