from app import app
from flask import render_template


# {'/':'index', '/blog': 'index'}
@app.route('/')
def index():
    return render_template('index.html')

