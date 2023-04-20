from flask_restful import Api

from gymanager.resources.auth.login import Login
from gymanager.resources.customers.endpoints import ListCustomers, CreateCustomer, DeleteCustomer, GetCustomerById, ChangeCustomerStatus


def init_app(app):
    api = Api(app, prefix="/api")

    api.add_resource(Login, "/auth/login")
    api.add_resource(ListCustomers, "/customers")
    api.add_resource(CreateCustomer, "/customers/create")
    api.add_resource(DeleteCustomer, "/customers/<id>/delete")
    api.add_resource(GetCustomerById, "/customers/<id>")
    api.add_resource(ChangeCustomerStatus, "/customers/<id>/change-status")
