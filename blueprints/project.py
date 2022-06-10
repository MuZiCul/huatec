from flask import Blueprint, render_template, request, jsonify

from exts import db
from models import basicModel

project = Blueprint("project", __name__)


@project.route('/project')
def projecthome():
    return render_template('project/project.html')


@project.route('/p_basic', methods=['POST', 'GET'])
def p_basic():
    data = basicModel.query.all()
    return render_template('project/p_basic.html', data=data)


@project.route('/search_basic', methods=['POST', 'GET'])
def search_basic():
    basicdata = []
    basicId = request.form.get('basicId')
    basicName = request.form.get('basicName')
    if basicId:
        basic = basicModel.query.filter_by(id=basicId).all()
        if basicName:
            for i in basic:
                if i.name == basicName:
                    basicdata.append(i)
        else:
            for i in basic:
                basicdata.append(i)
    elif basicName:
        basic = basicModel.query.filter_by(name=basicName).all()
        if basicId:
            for i in basic:
                if i.id == basicId:
                    basicdata.append(i)
        else:
            for i in basic:
                basicdata.append(i)
    dit = {}
    for index, b in enumerate(basicdata):
        dic = {'id': b.id, 'name': b.name, 'school': b.school, 'phone': b.phone, 'email': b.email, 'zip': b.zip,
               'address': b.address}
        dit[index] = dic
    return dit


@project.route('/add_basic', methods=['POST', 'GET'])
def add_basic():
    id_ = request.form.get('id')
    name = request.form.get('name')
    school = request.form.get('school')
    email = request.form.get('email')
    phone = request.form.get('phone')
    zip_ = request.form.get('zip')
    address = request.form.get('address')
    basic = basicModel(id=id_, name=name, school=school, email=email, zip=zip_, phone=phone, address=address)
    db.session.add(basic)
    db.session.commit()
    return jsonify({'code': 200})


@project.route('/p_major')
def p_major():
    data = basicModel.query.all()
    return render_template('project/p_major.html', data=data)


@project.route('/p_people')
def p_people():
    return render_template('project/p_people.html')


@project.route('/p_student')
def p_student():
    return render_template('project/p_student.html')


@project.route('/p_asset')
def p_asset():
    return render_template('project/p_asset.html')


@project.route('/p_information')
def p_information():
    return render_template('project/p_information.html')


@project.route('/p_training')
def p_training():
    return render_template('project/p_training.html')
