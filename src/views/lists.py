from src import app,db
from flask import render_template,redirect
from src.forms import ListForm
from flask_login import login_required,current_user
from src.models import List


@app.route('/')
@login_required
def home():
    lists = List.query.filter_by(user=current_user).order_by(List.created_at).all()
    return render_template('home.html',lists=lists)

@app.route('/create-list',methods=["GET","POST"])
@login_required
def create_list():
    form = ListForm()
    if form.validate_on_submit():
        list_ = List(name=form.name.data,user=current_user)
        db.session.add(list_)
        db.session.commit()
        return redirect('/')

    return render_template('create_list.html',form=form)
@app.route('/delete/list/<id>')
@login_required
def delete_list(id):
    list_ = db.get_or_404(List,id)
    if list_.user == current_user:
        db.session.delete(list_)
        db.session.commit()
        return redirect('/')
    else:
        return "You don't have the rights to do this action"