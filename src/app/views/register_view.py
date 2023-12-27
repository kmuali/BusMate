from app import app

from flask import redirect, render_template, request, url_for

from app.api.database import db
from app.models.driver import Driver
from app.models.passenger import Passenger


@app.route('/register')
def register_view():
    if request.cookies.get('id'):
        return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/register-submit', methods=['POST'])
def register_submit():
    is_passenger = request.form['ispassenger'] == 'true'
    card_cvv = request.form['cardcvv']
    card_number = request.form['cardnumber']
    card_month = request.form['cardmonth']
    card_year = request.form['cardyear']
    name = '{} {}'.format(request.form['firstname'], request.form['familyname'])
    password = request.form['password']
    phone = request.form['phone']
    if is_passenger:
        passenger = Passenger(name=name, password=password, phone=phone)
        db.session.add(passenger)
        db.session.commit()
    else:
        driver = Driver(name=name, password=password, phone=phone)
        db.session.add(driver)
        db.session.commit()
    return redirect(url_for('login_view'))
