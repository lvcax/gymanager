from flask import Flask

from gymanager import models
from gymanager import routes
from gymanager.extensions import conf
from gymanager.extensions import cors
from gymanager.extensions import database
from gymanager.extensions import jwt
from gymanager.extensions import mailer


def create_app():
    app = Flask(__name__)

    conf.init_app(app)
    database.init_app(app)
    cors.init_app(app)
    jwt.init_app(app)
    mailer.init_app(app)
    routes.init_app(app)

    @app.shell_context_processor
    def context_processor():
        return dict(app=app, db=database.db, Customer=models.Customer)

    return app
