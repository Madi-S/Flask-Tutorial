import re
from app import db
from datetime import datetime



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.slug = self.generate_slug(self.title)

    @staticmethod
    def generate_slug(s):
        if s:
            pattern = r'[^\w+]'
            return re.sub(pattern, '-', s).lower()
            # return s.replace(' ','-')


    def __repr__(self):
        return f'<Post id: {self.id}, title: {self.title}>'
