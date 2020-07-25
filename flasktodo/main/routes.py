from flask import render_template, redirect, url_for, Blueprint
from flask_login import current_user
from flasktodo.main.forms import TodoForm

main = Blueprint('main', __name__)

@main.route('/')
def home():
    if current_user.is_authenticated:
        return redirect(url_for('titles.titles_list'))
    return render_template('home.html')