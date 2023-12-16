from app import app

from flask import render_template

from datetime import datetime

@app.route('/')
def index():
    return render_template('index.html', datetime=datetime.now())
