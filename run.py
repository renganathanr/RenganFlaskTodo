from flasktodo import create_app, db
from flasktodo.models import User, Title, Task

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User,'Title': Title, 'Task': Task}