from flask import render_template, redirect, url_for, request, Blueprint
from flasktodo import db
from flasktodo.models import Title
from flasktodo.main.forms import TodoForm

titles = Blueprint('titles', __name__)

@titles.route('/title/add', methods=['GET', 'POST'])
def add_title():
    form = TodoForm()
    if form.validate_on_submit():
        title = Title(content=form.content.data)
        db.session.add(title)
        db.session.commit()
        return redirect(url_for('main.home'))

@titles.route('/title/<int:id>/delete')
def delete_title(id):
    title = Title.query.get_or_404(id)
    tasks = title.tasks.all()
    for task in tasks:
        db.session.delete(task)
    db.session.delete(title)
    db.session.commit()
    return redirect(url_for('main.home'))

@titles.route('/title/<int:id>/update', methods=['GET', 'POST'])
def update_title(id):
    title = Title.query.get_or_404(id)
    form = TodoForm()
    if form.validate_on_submit():
        title.content = form.content.data
        db.session.commit()
        return redirect(url_for('main.home'))
    elif request.method == 'GET':
        form.content.data = title.content
    return render_template('update_content.html', form=form, title='Update Title')
