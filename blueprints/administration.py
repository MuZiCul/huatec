from flask import Blueprint, render_template, redirect

administration = Blueprint("administration", __name__)


@administration.route('/administration')
def administrationhome():
    return render_template('administration/administration.html')


@administration.route('/a_entry')
def a_entry():
    return render_template('administration/a_entry.html')


@administration.route('/a_fire')
def a_fire():
    return render_template('administration/a_fire.html')
