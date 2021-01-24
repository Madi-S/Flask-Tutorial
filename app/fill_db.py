from app import db
from models import Post
from posts_generator import get_posts


def fill_posts(limit=20,q=None):
    posts = get_posts(limit, q)
    ps = [Post(title=post.get('title'),body=post.get('body')) for post in posts]
    db.session.add_all(ps)
    db.session.commit()
    return True

