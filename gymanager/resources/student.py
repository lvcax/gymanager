from datetime import datetime

from flask import abort, request
from flask_restful import Resource

from gymanager.controllers import student_controller
from gymanager.utils.validators import validate_fields


class CreateStudent(Resource):
    def post(self):
        body = request.json
        validation, msg = validate_fields(body, "student")

        if validation:
            data = student_controller.create(body)
            if data.get("msg") == "created":
                return data.get("data"), 201
            else:
                return abort(500, data.get("error"))
        else:
            return msg, 400

class RetrieveStudent(Resource):
    def get(self, id):
        data = student_controller.retrieve(id)
        if data.get("msg") == "ok":
            return data.get("data"), 200
        else:
            return abort(400, data.get("msg"))

class UpdateStudent(Resource):
    def put(self, id):
        body = request.json
        data = student_controller.update(body, id)

        if data.get("msg") == "ok":
            return data.get("data"), 200
        else:
            return abort(500, data.get("msg"))

class DeleteStudent(Resource):
    def delete(self, id):
        data = student_controller.delete(id)
        if data.get("msg") == "deleted":
            return data.get("msg"), 204
        else:
            return abort(500, data.get("msg"))

class ListStudents(Resource):
    def get(self):
        data = student_controller.get_all()
        if data.get("msg") == "ok":
            return data.get("data"), 200
        else:
            return abort(500, data.get("msg"))
