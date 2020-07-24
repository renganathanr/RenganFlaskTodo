from flasktodo import create_app, db
from flasktodo.models import Title, Task

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Title': Title, 'Task': Task}