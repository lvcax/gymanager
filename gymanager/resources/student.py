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
            if "ok" in response.keys():
                return response.get("data"), 201
            else:
                return abort(500, response.get("error"))
        else:
            return msg, 400

class RetrieveStudent(Resource):
    def get(self):
        return {}, 200

class UpdateStudent(Resource):
    def put(self):
        return {}, 200

class DeleteStudent(Resource):
    def delete(self):
        return {}, 200

class ListStudents(Resource):
    def get(self):
        return {"oi": "tudo bem?"}, 200
