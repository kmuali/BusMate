from app import app

from flask import render_template


@app.route('/register')
def register_view():
    return render_template('register.html')
