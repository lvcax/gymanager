from flask_restful import Resource, reqparse, marshal_with, marshal

from gymanager.models import Customer
from gymanager.resources.customers import query
from gymanager.resources.customers.checkers import check_email_already_in_use, check_cpf
from gymanager.schemas import customer_fields
from gymanager.utils.generators import gen_registration_number


class ListCustomers(Resource):
    @marshal_with(fields=customer_fields, envelope="customers")
    def get(self):
        customers = query.list_customers()
        return customers, 200


class GetCustomerById(Resource):
    def get(self, id):
        customer = query.get_customer_by_id(id)

        if not customer:
            return {"error": "customer not found"}, 404

        return marshal(customer, customer_fields, "customer"), 200


class CreateCustomer(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        
        parser.add_argument("name", type=str, required=True, help="field required")
        parser.add_argument("birth_date", type=str, required=True, help="field required")
        parser.add_argument("address", type=str, required=True, help="field required")
        parser.add_argument("email", type=str, required=True, help="field required")
        parser.add_argument("cpf", type=str, required=True, help="field required")
        parser.add_argument("phone_number", type=str, required=True, help="field required")
        parser.add_argument("joined_date", type=str, required=True, help="fields required")

        data = parser.parse_args()

        if check_email_already_in_use(data.email):
            return {"error": "email already in use"}, 404

        verify_cpf = check_cpf(data.cpf)
        if verify_cpf != None:
            return verify_cpf, 404
        
        data["registration"] = gen_registration_number()

        response = query.create_customer(data)

        if type(response) == "dict":
            return response, 500
        
        return marshal(response, customer_fields, "customer"), 201


class UpdateCustomer(Resource):
    def patch(self, id):
        customer = Customer.query.filter_by(id=id).first()

        if not customer:
            return {"error": "customer not found"}, 404
        
        parser = reqparse.RequestParser()
        
        parser.add_argument("name", type=str)
        parser.add_argument("birth_date", type=str)
        parser.add_argument("address", type=str)
        parser.add_argument("email", type=str)
        parser.add_argument("cpf", type=str)
        parser.add_argument("phone_number", type=str)
        parser.add_argument("joined_date", type=str)
        parser.add_argument("status", type=bool)

        data = parser.parse_args()

        if check_email_already_in_use(data.email):
            return {"error": "email already in use"}, 400
    
        cpf_already_in_use = check_cpf(data.cpf)
        if cpf_already_in_use != None:
            return cpf_already_in_use, 400
        
        response = query.update_customer(customer, data)
        updated_customer, status = response

        if status != 200:
            return updated_customer, status

        return marshal(updated_customer, customer_fields, "customer"), 200


class DeleteCustomer(Resource):
    def delete(self, id):
        response = query.delete_customer(id)

        data, status = response

        return data, status


class ChangeCustomerStatus(Resource):
    def patch(self, id):
        response = query.change_customer_status(id)

        data, status = response

        return data, status
