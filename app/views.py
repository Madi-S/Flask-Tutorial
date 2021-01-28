from app import app
from flask import redirect
from flask import url_for
from flask import render_template


@app.route('/')
def home():
    return redirect(url_for('posts.index'))


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', error=e), 404