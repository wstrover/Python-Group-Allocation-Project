from enum import unique
from sqlalchemy.orm import backref
from project import db, login_manager, bcrypt
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False)
    hashed_password = db.Column(db.String, nullable=False)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, password):
        self.hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.hashed_password, password)

    def __repr__(self):
        return '<User %r>' % self.id


class Choices(db.Model, UserMixin):
    # don't need a username validator as I just made a valid check in routes.py(probably can be improved)
    username = db.Column(db.String, primary_key=True)
    first_choice = db.Column(db.String, nullable=False)
    second_choice = db.Column(db.String, nullable=False)
    third_choice = db.Column(db.String, nullable=False)

class Grouping(db.Model, UserMixin):
    # same as in choices I can just check if the username is in the db
    username = db.Column(db.String, primary_key=True)
    group = db.Column(db.String, nullable=False)