from flask import render_template, Blueprint
from flasktodo.models import Title
from flasktodo.main.forms import TodoForm

main = Blueprint('main', __name__)

@main.route('/')
def home():
    titles = Title.query.all()
    form = TodoForm()
    return render_template('home.html', form=form, titles=titles)