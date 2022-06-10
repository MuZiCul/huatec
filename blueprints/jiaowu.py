from flask import Blueprint,render_template,redirect

jiaowu = Blueprint("jiaowu",__name__)

@jiaowu.route('/jiaowu')
def jiaowuhome():
    return render_template('jiaowu/jiaowu.html')

@jiaowu.route('/j_evaluation')
def j_evaluation():
    return render_template('jiaowu/j_evaluation.html')

@jiaowu.route('/j_exam')
def j_exam():
    return render_template('jiaowu/j_exam.html')

@jiaowu.route('/j_score')
def j_score():
    return render_template('jiaowu/j_score.html')
