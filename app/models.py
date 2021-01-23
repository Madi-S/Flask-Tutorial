import re
from app import db
from datetime import datetime



def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)
    # return s.replace(' ','-')

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.slug = self.generate_slug(self.slug)


    def generate_slug(self):
        if self.title:
            return slugify(self.title) # generating slug (unique url part)


    def __repr__(self):
        return f'<Post id: {self.id}, title: {self.title}'
