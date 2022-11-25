from datetime import datetime

from flask import abort, request
from flask_restful import Resource

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
    def get(self, id):
        student = student_controller.retrieve(id)
        if student.get("msg") == "ok":
            return student.get("data"), 200
        else:
            return abort(400, student.get("msg"))

class UpdateStudent(Resource):
    def put(self):
        return {}, 200

class DeleteStudent(Resource):
    def delete(self):
        return {}, 200

class ListStudents(Resource):
    def get(self):
        data = student_controller.get_all()
        if data.get("msg") == "ok":
            return data.get("data"), 200
        else:
            return abort(500, data.get("msg"))
