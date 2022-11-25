from flask_restful import Api

from gymanager.resources.docs import Docs
from gymanager.resources.student import ListStudents, CreateStudent, RetrieveStudent


def init_app(app):
    api = Api(app=app, prefix="/api/v1")
    api.add_resource(Docs, "/docs")
    api.add_resource(CreateStudent, "/students/create")
    api.add_resource(ListStudents, "/students/list")
    api.add_resource(RetrieveStudent, "/student/<id>")
