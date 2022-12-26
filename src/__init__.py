from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config["SECRET_KEY"] ="klf33ghjg321knvn"

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

db.init_app(app)

with app.app_context():
    db.create_all()


login_manager = LoginManager()
login_manager.init_app(app)


login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return models.UserModel.query.get(int(user_id))




from src.views import auth,lists,todos
from src import models
from src import forms
