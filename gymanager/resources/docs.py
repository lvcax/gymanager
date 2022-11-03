from flask import make_response, render_template
from flask_restful import Resource


class Docs(Resource):
    def get(self):
        headers = {"Content-Type": "text/html"}
        return make_response(
            render_template("swaggerui.html"),
            200,
            headers
        )