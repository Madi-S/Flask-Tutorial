from flask import Flask, redirect, url_for, request

from flask_sqlalchemy import SQLAlchemy

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView

from flask_security import SQLAlchemyUserDatastore, Security, current_user

from config import Configuration


app = Flask(__name__)
app.config.from_object(Configuration)


db = SQLAlchemy(app)


# For DB migration:
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


# For admin page:
from models import Post, Tag, User, Role

class AdminMixin:
    def is_accessible(self):
        return current_user.has_role('Admin')
    
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next=request.url))


class AdminView(AdminMixin, ModelView):
    pass


class HomeAdminView(AdminMixin, AdminIndexView):
    pass



admin = Admin(app, 'FlaskBlog', url='/blog', index_view=HomeAdminView(name='Home'))
admin.add_view(AdminView(Post, db.session))
admin.add_view(AdminView(Tag, db.session))


# For security:

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

# Endow user `admin` role:
# user = user_datastore.add_user(name='Madi', ...)
# role = user_datastore.add_role(name='Admin', ...)
# db.session.commit()
# user_datastore.add_role_to_user(user, role)
# db.session.commit()