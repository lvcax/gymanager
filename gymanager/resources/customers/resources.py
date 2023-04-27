from flask import request
from flask.json import jsonify
from flask_restful import Resource, reqparse, marshal

from gymanager.models import Customer
from gymanager.resources.customers import query
from gymanager.resources.customers.checkers import check_email_already_in_use, check_cpf
from gymanager.schemas import customer_fields
from gymanager.utils.generators import gen_registration_number


class ListCustomers(Resource):
    def get(self):
        page = request.args.get("page", default=1, type=int)
        customers = query.list_customers(page)

        data = list()

        for item in customers.items:
            data.append({
                "id": item.id,
                "registration": item.registration,
                "name": item.name,
                "email": item.email,
                "birth_date": item.birth_date,
                "address": item.address,
                "cpf": item.cpf,
                "phone_number": item.phone_number,
                "status": item.status,
                "joined_date": item.joined_date,
                "next_payment_date": item.next_payment_date,
                "customer_status_payment": item.customer_status_payment,
                "created_at": item.created_at,
                "updated_at": item.updated_at
            })

        meta = {
            "page": customers.page,
            "pages": customers.pages,
            "total_count": customers.total,
            "prev_page": customers.prev_num,
            "next_page": customers.next_num,
            "has_next": customers.has_next,
            "has_prev": customers.has_prev,
        }

        return jsonify({"customers": data, "meta": meta})



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

        if type(response) == dict:
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
