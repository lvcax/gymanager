from uuid import uuid4

from gymanager.extensions.database import db

from sqlalchemy.dialects.postgresql import UUID


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    email = db.Column(db.String(84), nullable=False, unique=True, index=True)
    password = db.Column(db.String(255), nullable=False)

    def __str__(self) -> str:
        return self.email