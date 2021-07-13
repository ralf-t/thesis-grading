from flask import current_app
from flask_login import UserMixin
from sqlalchemy.dialects.mysql import INTEGER, BOOLEAN, BIGINT

from thesis_grading import db, login_manager

from datetime import datetime
import pytz
# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


'''
	syntax i followed for creating models w/ relationships
	one to many
	class Parent():
		...
		children = db.relationship()
		
	class Child():
		...
		parent_id = db.Column()
'''

class User(db.Model, UserMixin):
	id = db.Column(INTEGER(unsigned=True), primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	full_name = db.Column(db.String(64), nullable=False)
	email = db.Column(db.String(64), unique=True)
	password = db.Column(db.String(60), nullable=False)
	is_admin = db.Column(BOOLEAN(), default=False)
	date_registered = db.Column(db.DateTime, nullable=False, default=lambda:datetime.now(tz=pytz.timezone('Asia/Manila')))
	
	logs = db.relationship('Log', backref='user', lazy='dynamic', cascade="all, delete")

	def __repr__(self):
		return f"[{self.id}] {self.username} - {self.full_name}"

class Log(db.Model):
	id = db.Column(BIGINT(unsigned=True), primary_key=True)
	description = db.Column(db.String(60), nullable=False)
	date = db.Column(db.DateTime, nullable=False, default=lambda:datetime.now(tz=pytz.timezone('Asia/Manila')))

	user_id = db.Column(INTEGER(unsigned=True), db.ForeignKey('user.id'), nullable=False)

	def __repr__(self):
		return f"[{self.id}] {self.description} - {self.date}"
