from flask_restful import Api

from gymanager.resources.auth.login import Login
from gymanager.resources.customers.resources import (
    ListCustomers,
    CreateCustomer,
    DeleteCustomer,
    GetCustomerById,
    ChangeCustomerStatus,
    UpdateCustomer
)


def init_app(app):
    api = Api(app, prefix="/api")

    api.add_resource(Login, "/auth/login")
    api.add_resource(ListCustomers, "/customers")
    api.add_resource(CreateCustomer, "/customers/create")
    api.add_resource(GetCustomerById, "/customers/<id>")
    api.add_resource(UpdateCustomer, "/customers/update/<id>")
    api.add_resource(DeleteCustomer, "/customers/delete/<id>")
    api.add_resource(ChangeCustomerStatus, "/customers/change-status/<id>")
