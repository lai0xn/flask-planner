from flask_sqlalchemy import SQLAlchemy
from src import app
from flask_login import UserMixin
from datetime import datetime
from src import db




class UserModel(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(200),nullable=False)
    password = db.Column(db.String(200),nullable=False)
    created_at = db.Column(db.DateTime,default=datetime.utcnow) 
    lists = db.relationship('List',backref='user')
    def __repr__(self) -> str:
        return f'{self.email}'



class List(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200),nullable=False)
    created_at = db.Column(db.DateTime,default=datetime.utcnow) 
  
    todos = db.relationship('Todo',backref='list')

    user_id = db.Column(db.Integer,db.ForeignKey('user_model.id'),nullable=False)
    def __repr__(self) -> str:
        return f'{self.id} {self.name}'

    def get_tasks_number(self):
        count = 0
        for todo in self.todos:
            count +=1
        return count

class Todo(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.String(200),nullable=False)
    completed = db.Column(db.Boolean(200),nullable=False,default=False)
    created_at = db.Column(db.DateTime,default=datetime.utcnow) 
    list_id = db.Column(db.Integer,db.ForeignKey('list.id'),nullable=False)
    def __repr__(self) -> str:
        return f'{self.id} {self.content}'
