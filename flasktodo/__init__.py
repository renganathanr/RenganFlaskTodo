from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from flasktodo.main.routes import main
    app.register_blueprint(main)
    from flasktodo.titles.routes import titles
    app.register_blueprint(titles)
    from flasktodo.tasks.routes import tasks
    app.register_blueprint(tasks)

    return app

from flasktodo import models  