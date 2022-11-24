from flask_restful import fields


student_fields = {
    "id": fields.String,
    "full_name": fields.String,
    "birth_date": fields.DateTime,
    "address": fields.String,
    "phone": fields.String,
    "email": fields.String,
    "is_active": fields.Boolean,
    "created_at": fields.DateTime,
    "updated_at": fields.DateTime
}
