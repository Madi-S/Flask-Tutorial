import re
from app import db
from datetime import datetime
from random import randint



post_tags = db.Table('post_tags',
    db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
 )





def generate_slug(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s).lower() + str(randint(1000, 9999))
    # return s.replace(' ','-')


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300))
    slug = db.Column(db.String(300), unique=True)
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.slug = generate_slug(self.title)

    tags = db.relationship('Tag', secondary=post_tags, backref=db.backref('posts', lazy='dynamic'))

    def __repr__(self):
        return f'<Post id: {self.id}, title: {self.title}>'



class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    slug = db.Column(db.String(150))

    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(*args, **kwargs)
        self.slug = generate_slug(self.name)

    def __repr__(self):
        return f'<Tag id: {self.id}, name: {self.name}>'

# t = Tag.query.first()
# p1 = Post.query.filter(Post.id==1).first()
# p1.tags.append(t)