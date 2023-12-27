from app import app

from flask import redirect, render_template, request, url_for

from datetime import datetime

@app.route('/')
def index():
    is_passenger = request.cookies.get('is_passenger')
    id = request.cookies.get('id')
    if not id:
        return render_template('index.html', datetime=datetime.now())
    if is_passenger:
        return redirect(url_for('passenger_view'))
    return redirect(url_for('driver_view'))

@app.route('/logout')
def logout():
    response = redirect(url_for('index'))
    response.delete_cookie('is_passenger')
    response.delete_cookie('id')
    return response
