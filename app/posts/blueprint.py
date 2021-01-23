from flask import Blueprint
from flask import render_template
from models import Post


posts = Blueprint('posts', __name__, template_folder='templates')
# the name 'posts' will be used in url_for function

@posts.route('/')
def index():
    posts = Post.query.all()
    return render_template('posts/index.html', posts=posts)