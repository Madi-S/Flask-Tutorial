from app import app
from models import Post
from flask import render_template


# {'/':'index', '/blog': 'index'}
@app.route('/')
def index():
    my_name = 'Madi'
    return render_template('index.html', title=Post.query.all())

