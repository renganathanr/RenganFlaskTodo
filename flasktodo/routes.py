from flasktodo import app

@app.route('/')
def home():
    return 'FlaskTodo app is in creation'