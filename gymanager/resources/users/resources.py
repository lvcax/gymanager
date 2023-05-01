import secrets
from base64 import b64decode
from datetime import timedelta

from flask import request
from flask_jwt_extended import create_access_token
from flask_restful import Resource, reqparse

from gymanager.models import User
from gymanager.extensions.database import db
from gymanager.services.mail import send_mail

from werkzeug.security import generate_password_hash, check_password_hash


class RegisterUser(Resource):
    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument("email", required=True, help="required")
        parser.add_argument("password", required=True, help="required")
        args = parser.parse_args()

        user_exisits = User.query.filter_by(email=args.email).first()
        if user_exisits:
            return {"error": "email already in use"}, 400
        
        user = User()
        user.email = args.email
        user.password = generate_password_hash(args.password, salt_length=10)

        db.session.add(user)

        try:
            db.session.commit()
            return {"msg": "user created successfully"}, 201
        except Exception as e:
            db.session.rollback()
            return {"error": "not possible to create user"}, 500


class LoginUser(Resource):
    def get(self):
        if not request.headers.get("Authorization"):
            return {"error": "Authorization not found"}, 400
        
        basic, code = request.headers["Authorization"].split(" ")
        if not basic.lower() == "basic":
            return {"error": "badly formatted authorization"}, 400
        
        email, password = b64decode(code).decode().split(":")

        user = User.query.filter_by(email=email).first()
        if not user:
            return {"error": "wrong email"}
        
        if not check_password_hash(user.password, password):
            return {"error": "wrong password"}
        
        token = create_access_token(
            identity={"id": user.id},
            expires_delta=timedelta(minutes=5)
        )

        return {"access_token": token}


class ForgetPassword(Resource):
    def post(self):
        parser = reqparse.RequestParser(trim=True)
        parser.add_argument("email", required=True, help="required field")
        args = parser.parse_args()

        user = User.query.filter_by(email=args.email).first()
        if not user:
            return {"error": "user not found"}, 400
        
        password_temp = secrets.token_hex(8)
        user.password = generate_password_hash(password_temp)
        
        db.session.add(user)

        try:
            db.session.commit()
            send_mail(
                subject="recuperação da conta",
                to=user.email,
                template="forget-password",
                password_temp=password_temp
            )

            return {"msg": "email sended successfully"}, 201
        except Exception as e:
            db.session.rollback()
            return {"error": "could not possible reset password"}, 500
    