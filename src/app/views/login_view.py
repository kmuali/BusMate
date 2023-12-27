from app import app

from flask import json, jsonify, make_response, redirect, render_template, request, url_for

from app.api.database import db
from app.models.driver import Driver
from app.models.passenger import Passenger


@app.route('/login')
def login_view():
    if request.cookies.get('id'):
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/login-submit', methods=['POST'])
def login_submit():
    is_passenger = request.form['ispassenger'] == 'true'
    password = request.form['password']
    phone = request.form['phone']
    if is_passenger:
        passenger = Passenger.query.filter_by(phone=phone, password=password).first()
        if passenger:
            response = redirect(url_for('index'))
            response.set_cookie('is_passenger', '1')
            response.set_cookie('id', f'{passenger.id}')
            return response
    else:
        driver = Driver.query.filter_by(phone=phone, password=password).first()
        if driver:
            response = redirect(url_for('index'))
            response.set_cookie('is_passenger', '0')
            response.set_cookie('id', f'{driver.id}')
            return response
    return redirect(url_for('login_view'))
