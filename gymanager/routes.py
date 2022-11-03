from flask_restful import Api

from gymanager.resources.docs import Docs


def init_app(app):
    api = Api(app=app, prefix="/api/v1")
    api.add_resource(Docs, "/docs")
