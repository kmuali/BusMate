from flask import render_template, request
from app import app
from app.models.passenger import Passenger

@app.route('/driver')
def passenger_view():
    passenger = Passenger.query.filter_by(id=request.cookies.get('id')).first()
    return render_template('passenger.html', name=passenger.name)
