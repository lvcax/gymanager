from flask_restful import Api

from gymanager.resources.auth.login import Login


def init_app(app):
    api = Api(app, prefix="/api")

    api.add_resource(Login, "/auth/login")
