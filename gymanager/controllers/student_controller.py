from datetime import datetime

from flask_restful import marshal
from loguru import logger

from gymanager.extensions.database import db
from gymanager.models import Student
from gymanager.schemas import student_fields


def create(data: dict) -> dict:
    """Register a new Student instance on database

    Args:
        data (dict): Student data

    Returns:
        dict: A success message if commit works fine
    """

    try:
        student = Student()
        student.full_name = data.get("full_name")
        student.birth_date = datetime.strptime(data.get("birth_date"), "%d/%m/%Y")
        student.address = data.get("address")
        student.number_address = data.get("number_address")
        student.phone = data.get("phone")
        student.email = data.get("email")
    
        db.session.add(student)
        db.session.commit()

        serialized_data = marshal(student, student_fields, "student")
        return {"msg": "created", "data": serialized_data}
    except Exception as e:
        logger.error(e)
        db.session.rollback()
        return {"msg": "could not possible create register"}

def retrieve(id: str) -> dict:
    """Retrieve a giver instance from database
    by Id.

    Args:
        id (str): Student id

    Returns:
        dict: Dict containing a message and data if query works
    """

    try:
        student = Student.query.filter_by(id=id).first()
        serialized_data = marshal(student, student_fields, "student")
        return {"msg": "ok", "data": serialized_data}
    except Exception as e:
        logger.error(e)
        return {"msg": "object does not exist"}

def update(data: dict, id: str) -> dict:
    """Update a given instance by id.

    Args:
        data (dict): Data to be update
        id (str): Student id to be updated

    Returns:
        dict: Dict containing a message and data if query works
    """
    try:
        student = Student.query.filter_by(id=id).first()

        student.full_name = data["full_name"] if "full_name" in data.keys() else student.full_name
        student.birth_date = data["birth_date"] if "birth_date" in data.keys() else student.birth_date
        student.address = data["address"] if "address" in data.keys() else student.address
        student.number_address = data["number_address"] if "number_address" in data.keys() else student.number_address
        student.phone = data["phone"] if "phone" in data.keys() else student.phone
        student.email = data["email"] if "email" in data.keys() else student.email
        student.update_at = datetime.now()

        db.session.add(student)
        db.session.commit()

        serialized_data = marshal(student, student_fields, "student")
        return {"msg": "ok", "data": serialized_data}
    except Exception as e:
        logger.error(e)
        db.session.rollback()
        return {"msg": "could not possible update register"}

def delete(id: str) -> dict:
    """Delete student by id.

    Args:
        id (str): Student id

    Returns:
        dict: Dict containing a message and data if query works
    """
    
    try:
        Student.query.filter(Student.id==id).delete()
        db.session.commit()

        return {"msg": "deleted"}
    except Exception as e:
        logger.error(e)
        db.session.rollback()
        return {"msg": "could not possible delete register"}

def get_all() -> dict:
    """List all students in database

    Returns:
        Object: Query response
    """
    try:
        students = Student.query.all()
        serialized_data = marshal(students, student_fields, "students")
        return {"msg": "ok", "data": serialized_data}
    except Exception as e:
        logger.error(e)
        return {"msg": "could not possible retrieve data"}

def deactivate(id: str):
    ...
