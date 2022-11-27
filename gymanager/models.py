import uuid

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from gymanager.extensions.database import db


class Student(db.Model):
    __tablename__ = "student"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    full_name = db.Column(db.String(50), nullable=False)
    birth_date = db.Column(db.DateTime(timezone=True), nullable=False)
    address = db.Column(db.String(80), nullable=False)
    number_address = db.Column(db.String(5), nullable=False)
    phone = db.Column(db.String(14), nullable=False)
    email = db.Column(db.String(30), nullable=False, unique=True)
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    def __repr__(self) -> str:
        return self.full_name

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(30), unique=True, index=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    def __repr__(self) -> str:
        return self.username
