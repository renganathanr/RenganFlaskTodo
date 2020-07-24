from flask import render_template, redirect, url_for, request, Blueprint
from flasktodo import db
from flasktodo.models import Title, Task
from flasktodo.main.forms import TodoForm

tasks = Blueprint('tasks', __name__)

@tasks.route('/title/<int:id>/tasks', methods=['GET', 'POST'])
def tasks_list(id):
    title_to_add_tasks = Title.query.get_or_404(id)
    tasks = title_to_add_tasks.tasks.all()
    form = TodoForm()
    if form.validate_on_submit():
        task = Task(content=form.content.data, title=title_to_add_tasks)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('tasks.tasks_list', id=title_to_add_tasks.id))
    return render_template('tasks.html', form=form, tasks=tasks)

@tasks.route('/task/<int:id>/delete')
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('tasks.tasks_list', id=task.title_id))

@tasks.route('/task/<int:id>/update', methods=['GET', 'POST'])
def update_task(id):
    task = Task.query.get_or_404(id)
    form = TodoForm()
    if form.validate_on_submit():
        task.content = form.content.data
        db.session.commit()
        return redirect(url_for('tasks.tasks_list', id=task.title_id))
    elif request.method == 'GET':
        form.content.data = task.content
    return render_template('update_content.html', task=task, form=form)