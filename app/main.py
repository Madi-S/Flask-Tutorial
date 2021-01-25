from app import app, db
from posts.blueprint import posts
from fill_db import fill_posts


if __name__ == '__main__':
    # fill_posts()
    app.register_blueprint(posts, url_prefix='/blog')
    app.run()