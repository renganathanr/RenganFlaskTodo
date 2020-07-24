from flask import render_template, redirect, url_for, request
from flasktodo import app, db
from flasktodo.forms import TodoForm
from flasktodo.models import Title, Task

@app.route('/')
def home():
    titles = Title.query.all()
    form = TodoForm()
    return render_template('home.html', form=form, titles=titles)

@app.route('/title/add', methods=['GET', 'POST'])
def add_title():
    form = TodoForm()
    if form.validate_on_submit():
        title = Title(content=form.content.data)
        db.session.add(title)
        db.session.commit()
        return redirect(url_for('home'))

@app.route('/title/<int:id>/delete')
def delete_title(id):
    title = Title.query.get_or_404(id)
    db.session.delete(title)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/title/<int:id>/update', methods=['GET', 'POST'])
def update_title(id):
    title = Title.query.get_or_404(id)
    form = TodoForm()
    if form.validate_on_submit():
        title.content = form.content.data
        db.session.commit()
        return redirect(url_for('home'))
    elif request.method == 'GET':
        form.content.data = title.content
    return render_template('update_content.html', form=form)

@app.route('/title/<int:id>/tasks', methods=['GET', 'POST'])
def tasks(id):
    title_to_add_tasks = Title.query.get(id)
    tasks = title_to_add_tasks.tasks.all()
    form = TodoForm()
    if form.validate_on_submit():
        task = Task(content=form.content.data, title=title_to_add_tasks)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('tasks', id=title_to_add_tasks.id))
    return render_template('tasks.html', form=form, tasks=tasks)

@app.route('/task/<int:id>/delete')
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('tasks', id=task.title_id))

@app.route('/task/<int:id>/update', methods=['GET', 'POST'])
def update_task(id):
    task = Task.query.get_or_404(id)
    form = TodoForm()
    if form.validate_on_submit():
        task.content = form.content.data
        db.session.commit()
        return redirect(url_for('tasks', id=task.title_id))
    elif request.method == 'GET':
        form.content.data = task.content
    return render_template('update_content.html', task=task, form=form)