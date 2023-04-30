from flask_restful import fields

customer_fields = {
    "id": fields.String,
    "registration": fields.String,
    "name": fields.String,
    "email": fields.String,
    "birth_date": fields.DateTime,
    "address": fields.String,
    "cpf": fields.String,
    "phone_number": fields.String,
    "status": fields.Boolean,
    "joined_date": fields.DateTime,
    "next_payment_date": fields.DateTime,
    "customer_status_payment": fields.String,
    "created_at": fields.DateTime,
    "updated_at": fields.DateTime
}