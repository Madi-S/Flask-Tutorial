from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from flask_security import SQLAlchemyUserDatastore, Security

from config import Configuration


app = Flask(__name__)
app.config.from_object(Configuration)


db = SQLAlchemy(app)


# For DB migration:
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


# For admin page:
from models import Post, Tag
admin = Admin(app)
admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(Tag, db.session))


# For security:
from models import User, Role
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)