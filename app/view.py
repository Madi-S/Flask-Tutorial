from app import app
from flask import render_template


# {'/':'index', '/blog': 'index'}
@app.route('/')
def index():
    my_name = 'Madi'
    return render_template('index.html', name=my_name)

