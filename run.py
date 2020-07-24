from flasktodo import app, db
from flasktodo.models import Title, Task

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Title': Title, 'Task': Task}