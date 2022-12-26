from flask import render_template, Blueprint,redirect
from src.forms import RegistrationForm,LoginForm
from src import app ,bcrypt
from src.models import UserModel
from flask_login import login_required,logout_user,current_user
from src import db
@app.route('/login',methods=['GET',"POST"])
def login():
    if current_user.is_authenticated:
        return redirect('/')
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/')
    return render_template('login.html',form=form)


@app.route('/signup',methods=['GET',"POST"])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        hased_password = bcrypt.generate_password_hash(form.password.data)
        user = UserModel(email=form.email.data,password=hased_password)
        db.session.add(user)
        db.session.commit()
        return redirect('/login')
        

    return render_template('signup.html',form=form)


@app.route('/logout')
@login_required

def logout():
    logout_user()
    return redirect('/login')

