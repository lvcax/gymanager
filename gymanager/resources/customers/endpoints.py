from flask import jsonify, abort, request
from flask_restful import Resource, reqparse, marshal_with, marshal

from gymanager.schemas import customer_fields
from gymanager.resources.customers import query


class ListCustomers(Resource):
    @marshal_with(fields=customer_fields, envelope="customers")
    def get(self):
        customers = query.list_customers()
        return customers

class GetCustomerById(Resource):
    def get(self, id):
        customer = query.get_customer_by_id(id)

        if not customer:
            return jsonify({"error": "customer not found"})

        return marshal(customer, customer_fields, "customer")

class CreateCustomer(Resource):
    @marshal_with(fields=customer_fields, envelope="customer")
    def post(self):
        parser = reqparse.RequestParser()
        
        parser.add_argument("name", type=str, required=True, help="field required")
        parser.add_argument("birth_date", type=str, required=True, help="field required")
        parser.add_argument("address", type=str, required=True, help="field required")
        parser.add_argument("email", type=str, required=True, help="field required")
        parser.add_argument("cpf", type=str, required=True, help="field required")
        parser.add_argument("phone_number", type=str, required=True, help="field required")

        data = parser.parse_args()
        customer = query.create_customer(data)

        return customer

class DeleteCustomer(Resource):
    def delete(self, id):
        response = query.delete_customer(id)

        return response
