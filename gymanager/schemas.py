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
    "created_at": fields.DateTime,
    "updated_at": fields.DateTime
}