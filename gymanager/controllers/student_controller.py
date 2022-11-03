from loguru import logger

from gymanager.models import Student
from gymanager.extensions.db import db

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
        student.birth_date = data.get("birth_date")
        student.address = data.get("address")
        student.phone = data.get("phone")
        student.email = data.get("email")

        db.session.add(data)
        db.commit()

        return {"ok": "created", "data": data}
    except Exception as e:
        logger.error(e)
        return {"error": "could not possible create register"}

def retrieve(id: str):
    query = db.select(Student).filter_by(id=id)
    student = db.session.execute(query)

    return student

def update(data: dict, id: str):
    ...

def delete(id: str):
    ...

def list():
    query = db.select(Student).order_by(Student.full_name)
    students = db.session.execute(query)

    return students

def deactivate(id: str):
    ...
