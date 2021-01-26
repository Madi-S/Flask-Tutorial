import re
from app import db
from datetime import datetime
from random import randint

from flask_security import UserMixin, RoleMixin


post_tags = db.Table('post_tags',
    db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
 )


def generate_slug(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s).lower()[:50] + str(randint(1000, 9999))
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

    def __str__(self):
        return self.title



class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    slug = db.Column(db.String(150))

    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(*args, **kwargs)
        self.slug = generate_slug(self.name)

    def __repr__(self):
        return f'<Tag id: {self.id}, name: {self.name}>'

    def __str__(self):
        return self.name

# To connect tags manually:
# t1 = Tag.query.first()
# p1 = Post.query.first()
# p1.tags.append(t)


# For flask security

roles_users = db.Table('roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
    )

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(110), unique=True)
    password = db.Column(db.String(600))
    name = db.Column(db.String(100))
    active = db.Column(db.Boolean())

    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

    def __repr__(self):
        return f'<User id: {self.id}, name: {self.name}>'

    def __str__(self):
        return self.name

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))

    def __repr__(self):
        return f'<Role id: {self.id}, name: {self.name}>'

    def __str__(self):
        return self.name
