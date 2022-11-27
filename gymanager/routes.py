from flask_restful import Api

from gymanager.resources.docs import Docs
from gymanager.resources.student import (
    ListStudents,
    CreateStudent,
    RetrieveStudent,
    UpdateStudent,
    DeleteStudent
)
from gymanager.resources.user import RegisterUser, LoginUser, ForgetPasswordUser


def init_app(app):
    api = Api(app=app, prefix="/api/v1")
    api.add_resource(Docs, "/docs")
    api.add_resource(ListStudents, "/students/list")
    api.add_resource(CreateStudent, "/students/create")
    api.add_resource(RetrieveStudent, "/student/<id>")
    api.add_resource(UpdateStudent, "/student/<id>/update")
    api.add_resource(DeleteStudent, "/student/<id>/delete")
    api.add_resource(RegisterUser, "/user/register")
    api.add_resource(LoginUser, "/user/auth/login")
    api.add_resource(ForgetPasswordUser, "/user/auth/forget-password")
