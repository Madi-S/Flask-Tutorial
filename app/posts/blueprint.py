from flask import Blueprint
from flask import render_template
from models import Post


posts = Blueprint('posts', __name__, template_folder='templates')
# the name 'posts' will be used in url_for function 
# For instance, posts.index or posts.post_detail


@posts.route('/')
def index():
    posts = Post.query.all()
    return render_template('posts/index.html', posts=posts)


# https://localhost:5000/blog/first-post
@posts.route('/<slug>')
def post_detail(slug):
    # post not POST request but blog text
    post = Post.query.filter(Post.slug==slug).first()   
    return render_template('posts/post_detail.html', post=post)