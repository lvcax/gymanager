from datetime import datetime

from flask import abort, request
from flask_restful import Resource, marshal_with

from gymanager.schemas import student_fields
from gymanager.controllers import student_controller
from gymanager.utils.validators import validate_fields


class CreateStudent(Resource):
    def post(self):
        data = request.json
        validation, msg = validate_fields(data, "student")

        if validation:
            data["birth_date"] = datetime.strptime(data.get("birth_date"), "%d/%m/%Y")

            response = student_controller.create(data)
            if response.get("msg") == "created":
                return response.get("data"), 201
            else:
                return abort(500, response.get("error"))
        else:
            return msg, 400

class RetrieveStudent(Resource):

    @marshal_with(fields=student_fields, envelope="student")
    def get(self, id):
        return {}, 200

class UpdateStudent(Resource):
    def put(self):
        return {}, 200

class DeleteStudent(Resource):
    def delete(self):
        return {}, 200

class ListStudents(Resource):

    @marshal_with(fields=student_fields, envelope="students")
    def get(self):
        data = student_controller.list()
        return data, 200
