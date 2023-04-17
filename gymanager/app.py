from flask import Flask

from gymanager.extensions import conf
from gymanager.extensions import cors
from gymanager.extensions import database
from gymanager.extensions import migrator
from gymanager import routes

def create_app():
    app = Flask(__name__)

    conf.init_app(app)
    database.init_app(app)
    migrator.init_app(app, database.db)
    cors.init_app(app)
    routes.init_app(app)

    @app.shell_context_processor
    def context_processor():
        from gymanager.models import User

        return dict(app=app, db=database.db, User=User)

    return app
