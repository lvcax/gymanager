from datetime import datetime, timedelta
from uuid import uuid4

from gymanager.extensions.database import db

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.sql import func


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    email = db.Column(db.String(84), nullable=False, unique=True, index=True)
    password = db.Column(db.String(255), nullable=False)

    def __str__(self) -> str:
        return self.email

class Customer(db.Model):
    __tablename__ = "customers"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    registration = db.Column(db.String(6), nullable=False, unique=True, index=True)
    name = db.Column(db.String(130), nullable=False, unique=True)
    email = db.Column(db.String(84), nullable=False, unique=True, index=True)
    birth_date = db.Column(db.DateTime(), nullable=False)
    address = db.Column(db.String(150), nullable=False)
    cpf = db.Column(db.String(15), nullable=False)
    phone_number = db.Column(db.String(11), nullable=False)
    status = db.Column(db.Boolean, default=True, nullable=False)
    joined_date = db.Column(db.DateTime(), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())

    def __str__(self) -> str:
        return self.name

    @hybrid_property
    def next_payment_date(self):
        next_payment = self.joined_date + timedelta(days=30)

        if next_payment.weekday == 6:
            next_payment += timedelta(days=1)
        elif next_payment.weekday == 5:
            next_payment += timedelta(days=2)
        
        return next_payment
    
    @hybrid_property
    def customer_status_payment(self):
        DIFF_DAYS = self.next_payment_date - datetime.now()
        
        if DIFF_DAYS.days >= 7 and DIFF_DAYS.days < 1:
            return "close to pay"
        elif DIFF_DAYS.days == 1:
            return "pay tomorrow"
        elif DIFF_DAYS.days == 0:
            return "pay today"
        elif DIFF_DAYS.days > 0 and self.status == False:
            return "overdue"
        else:
            return "ok"
