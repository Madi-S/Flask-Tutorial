from app import db
from models import Post
from posts_generator import get_posts


def fill_posts(limit=20,q=None):
    posts = get_posts(limit, q)
    for post in posts:
        p = Post(title=post.get('title'),body=post.get('body'))
        db.session.add(p)
        print(f'{p} was added to db')
    db.session.commit()

