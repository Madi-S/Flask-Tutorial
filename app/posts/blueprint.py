from flask import Blueprint
from flask import request
from flask import render_template

from models import Post, Tag
from app import app

from .forms import PostForm



posts = Blueprint('posts', __name__, template_folder='templates')
# the name 'posts' will be used in url_for function 
# For instance, posts.index or posts.post_detail



# Must be above than `index` because it will cosnider `create` as `q` parameter
# http://localhost:5000/blog/create
@posts.route('/create')
def create_post():
    form  = PostForm()
    return render_template('posts/create_post.html', form=form)



@app.route('/search')
def search():
    q = request.args.get('q')
    if q:
        posts = Post.query.filter(Post.title.contains(q) | Post.body.contains(q)).all()
    else:
        posts = Post.query.all()
    
    return render_template('posts/index.html', posts=posts)


@posts.route('/search')
def index():
    posts = Post.query.all()
    
    return render_template('posts/index.html', posts=posts)


# http://localhost:5000/blog/first-post
@posts.route('/<slug>')
def post_detail(slug):
    # post not POST request but blog text
    post = Post.query.filter(Post.slug==slug).first()
    tags = post.tags
    return render_template('posts/post_detail.html', post=post, tags=tags)


# slug for specific 'tags' -> e.g., http://localhost:5000/blog/tag/sports
@posts.route('/tag/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug==slug).first()
    posts = tag.posts #.all()
    return render_template('posts/tag_detail.html',tag=tag, posts=posts)


