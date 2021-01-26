from flask import Blueprint
from flask import request
from flask import redirect
from flask import url_for
from flask import render_template

from flask_security import login_required

from models import Post, Tag
from app import db, app

from .forms import PostForm



posts = Blueprint('posts', __name__, template_folder='templates')
# the name 'posts' will be used in url_for function 
# For instance, posts.index or posts.post_detail



# Must be above than `index` because it will cosnider `create` as `q` parameter
# http://localhost:5000/blog/create
@posts.route('/create', methods=['POST','GET'])
@login_required
def create_post():
    form = PostForm(meta={'csrf': False})

    if request.method == 'POST':
        if form.validate_on_submit():
            title = request.form.get('title')
            body = request.form.get('body')

            try:
                post = Post(title=title, body=body)
                db.session.add(post)
                db.session.commit()
            except Exception as e:
                print('Error:', e)           

            return redirect(url_for('posts.index'))
        else:
            print('Form did not pass validation')

    return render_template('posts/create_post.html', form=form)



@posts.route('/')
def index():
    page = request.args.get('page')
    q = request.args.get('q','')

    if q:
        posts = Post.query.filter(Post.title.contains(q) | Post.body.contains(q))
    else:
        posts = Post.query.order_by(Post.created.desc())

    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    pages = posts.paginate(page=page, per_page=5)

    return render_template('posts/index.html', pages=pages, q=q)


# http://localhost:5000/blog/first-post
@posts.route('/<slug>')
def post_detail(slug):
    # post not POST request but blog text
    post = Post.query.filter(Post.slug==slug).first()
    try:
        tags = post.tags
    except AttributeError:
        tags = []

    return render_template('posts/post_detail.html', post=post, tags=tags)


# slug for specific 'tags' -> e.g., http://localhost:5000/blog/tag/sports
@posts.route('/tag/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug==slug).first()
    posts = tag.posts 

    return render_template('posts/tag_detail.html',tag=tag, posts=posts)




@posts.route('/<slug>/edit', methods=['POST', 'GET'])
@login_required
def edit_post(slug):
    post = Post.query.filter(Post.slug==slug).first()

    if request.method == 'POST':
        form = PostForm(formdata=request.form, obj=post)
        form.populate_obj(post)
        db.session.commit()

        return redirect(url_for('posts.post_detail', slug=post.slug))

    form = PostForm(obj=post)
    return render_template('posts/edit_post.html', form=form, post=post)



@app.route('/')
def home():
    return redirect(url_for('posts.index'))