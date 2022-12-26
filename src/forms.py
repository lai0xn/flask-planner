from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Length,DataRequired,EqualTo,Email,ValidationError
from src.models import UserModel
from flask_login import login_user
from src import bcrypt


class RegistrationForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email(),Length(min=12,max=24)])
    password = PasswordField('Password',validators=[DataRequired()])
    password2 = PasswordField('Password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Signup')

    def validate_email(self,email):
        user = UserModel.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('User with this email already exists')
        







class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email(),Length(min=12,max=24)])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Signup')

   

    def validate_password(self,password):
        
        user = UserModel.query.filter_by(email=self.email.data).first()
        if not user:
            raise ValidationError('Cannot login with the provided credentials')
        if bcrypt.check_password_hash(user.password,password.data):
            login_user(user)
        else:
            raise ValidationError('Cannot login with the provided credentials')
    
class ListForm(FlaskForm):
    name = StringField('Name',validators=[DataRequired(),Length(min=5,max=24)])