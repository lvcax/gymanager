from base64 import b64decode

from flask import abort, request
from flask_restful import Resource

from gymanager.controllers import user_controller


class RegisterUser(Resource):
    def post(self):
        body = request.json
        data = user_controller.register(body)

        if data.get("msg") == "created":
            return 201, data.get("data")
        else:
            return abort(data.get("status"), data.get("msg"))

class LoginUser(Resource):
    def get(self):
        if not request.headers.get("Authorization"):
            return {"msg": "invalid credentials"}, 400
        
        basic, code = request.headers.get("Authorization").split(" ")

        if not basic.lower() == "basic":
            return {"msg": "f no chat"}
        
        email, password = b64decode(code).decode("utf-8").split(":")
        result = user_controller.login(email, password)

        if "msg" in result.keys():
            return result, 400
        else:
            return result, 200


class UpdateUser(Resource):
    def put(self):
        ...

class DeleteUser(Resource):
    def delete(self):
        ...
