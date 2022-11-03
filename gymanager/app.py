from flask import Flask

from gymanager import routes
from gymanager.extensions import config, cors, db
from gymanager.models import Student


def create_app():
    app = Flask(__name__)

    config.init_app(app)
    db.init_app(app)
    cors.init_app(app)
    routes.init_app(app)

    @app.shell_context_processor
    def make_shell_context():
        return dict(db=db, Student=Student)

    return app
