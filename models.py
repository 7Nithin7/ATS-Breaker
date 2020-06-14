from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user

db = SQLAlchemy()
login_manager = LoginManager()


class User(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True)
    fname = db.Column(db.String)
    lname = db.Column(db.String)
    password = db.Column(db.String)
    authenticated = db.Column(db.Boolean, default=False)

    

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
