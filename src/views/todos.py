from src import app,db
from flask import redirect,render_template,request
from src.models import List,Todo
from flask_login import current_user,login_required


@app.route('/list/<id>',methods=["GET","POST"])
@login_required
def todolist(id):
    list_ = db.get_or_404(List,id)

    if request.method == "POST":
        content = request.form["content"]
        todo= Todo(content=content,list=list_)
        db.session.add(todo)
        db.session.commit()
        return redirect(f'/list/{id}')
    
    return render_template('list.html',list=list_)



@app.route('/list/delete/<id>',methods=["GET","POST"])
@login_required
def delete_todo(id):
    todo = db.get_or_404(Todo,id)
    if todo.list.user == current_user:
        db.session.delete(todo)
        db.session.commit()
        return redirect(f'/list/{todo.list.id}')
    else:
        return "You don't have the rights to do this action"

@app.route('/list/complete/<id>',methods=["GET","POST"])
@login_required
def complete_todo(id):
    todo = db.get_or_404(Todo,id)
    if todo.list.user == current_user:
        todo.completed = not todo.completed
        db.session.commit()
        return redirect(f'/list/{todo.list.id}')
    else:
        return "You don't have the rights to do this action"