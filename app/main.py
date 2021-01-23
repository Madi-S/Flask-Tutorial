import view
from app import app, db
from posts.blueprint import posts


if __name__ == '__main__':
    app.register_blueprint(posts, url_prefix='/blog')
    app.run()