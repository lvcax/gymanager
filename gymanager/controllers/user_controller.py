from datetime import datetime, timedelta

from flask_restful import marshal
from flask_jwt_extended import create_access_token
from loguru import logger
from werkzeug.security import check_password_hash, generate_password_hash

from gymanager.extensions.database import db
from gymanager.models import User
from gymanager.schemas import user_fields


def register(data: dict) -> dict:
    """Register a new user in database

    Args:
        data (dict): Data to create a nwe instance

    Returns:
        dict: Message to inform the result of database transaction
    """

    user = User.query.filter_by(email=data.get("email")).first()
    if user:
        return {"msg": "email already in use", "status": 400}
    
    password = generate_password_hash(data.get("password"))

    new_user = User()
    new_user.username = data.get("username")
    new_user.email = data.get("email")
    new_user.password = password

    try:
        db.session.add(new_user)
        db.session.commit()

        serialized_data = marshal(new_user, user_fields, "user")
        
        return {"msg": "created", "data": serialized_data}
    except Exception as e:
        logger.error(e)
        db.session.rollback()
        
        return {"msg": "could not possible create user", "status": 500}

def login(user_email: str, password: str) -> dict:
    """Checks credentials and generate access token if
    data is valid

    Args:
        user_email (str): Email used in login attempt
        password (str): Password used in login attempt

    Returns:
        dict: Access token or error message
    """

    user = User.query.filter_by(email=user_email).first()

    if not user:
        return {"msg": "invalid email"}
    if not check_password_hash(user.password, password):
        return {"msg": "invalid password"}
    
    token = create_access_token({"id": user.id}, timedelta(days=1))

    return {"access_token": token}
