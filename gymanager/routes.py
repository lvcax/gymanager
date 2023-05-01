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

from gymanager.resources.users.resources import RegisterUser, LoginUser, ForgetPassword


def init_app(app):
    api = Api(app, prefix="/api")

    api.add_resource(LoginUser, "/users/auth/login")
    api.add_resource(RegisterUser, "/users/register")
    api.add_resource(ForgetPassword, "/users/forget-password")
    api.add_resource(ListCustomers, "/customers")
    api.add_resource(CreateCustomer, "/customers/create")
    api.add_resource(GetCustomerById, "/customers/<id>")
    api.add_resource(UpdateCustomer, "/customers/update/<id>")
    api.add_resource(DeleteCustomer, "/customers/delete/<id>")
    api.add_resource(ChangeCustomerStatus, "/customers/change-status/<id>")
