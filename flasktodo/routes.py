from flask import render_template
from flasktodo import app

@app.route('/')
def home():
    return render_template('home.html')