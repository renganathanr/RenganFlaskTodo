from flask import render_template, redirect, url_for, request
from flasktodo import app, db
from flasktodo.forms import TodoForm
from flasktodo.models import Title

@app.route('/')
def home():
    titles = Title.query.all()
    form = TodoForm()
    return render_template('home.html', form=form, titles=titles)

@app.route('/<name>/add', methods=['GET', 'POST'])
def add_content(name):
    form = TodoForm()
    if form.validate_on_submit():
        if name == 'title':
            title = Title(content=form.content.data)
            db.session.add(title)
            db.session.commit()
        return redirect(url_for('home'))

@app.route('/<int:id>/delete')
def delete_content(id):
    title_to_delete = Title.query.get_or_404(id)
    db.session.delete(title_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/<int:id>/update', methods=['GET', 'POST'])
def update_content(id):
    title_to_update = Title.query.get_or_404(id)
    form = TodoForm()
    if form.validate_on_submit():
        title_to_update.content = form.content.data
        db.session.commit()
        return redirect(url_for('home'))
    elif request.method == 'GET':
        form.content.data = title_to_update.content
    return render_template('update_content.html', form=form)