from flask import render_template, redirect, url_for
from flasktodo import app, db
from flasktodo.forms import TodoForm
from flasktodo.models import Title

@app.route('/', methods=['GET', 'POST'])
def home():
    form = TodoForm()
    if form.validate_on_submit():
        title = Title(content=form.content.data)
        db.session.add(title)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('home.html', form=form, titles=Title.query.all())