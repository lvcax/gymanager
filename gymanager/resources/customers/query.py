from flask import jsonify
from gymanager.models import Customer

from gymanager.extensions.database import db
from gymanager.resources.customers.checkers import check_email_already_in_use, check_cpf_already_in_use
from gymanager.utils.generators import gen_registration_number


def list_customers():
    customers = Customer.query.all()

    return customers

def get_customer_by_id(customer_id):
    customer = Customer.query.filter_by(id=customer_id).first()

    return customer

def create_customer(data):

    registration = gen_registration_number()

    if check_email_already_in_use(data.email):
        return jsonify({"error": "email already in use"})
    
    cpf_already_in_use = check_cpf_already_in_use(data.cpf)
    if cpf_already_in_use != None:
        return cpf_already_in_use

    customer = Customer(
        registration=registration,
        name=data.name,
        email=data.email,
        birth_date=data.birth_date,
        address=data.address,
        cpf=data.cpf,
        phone_number=data.phone_number,
        joined_date=data.joined_date
    )

    db.session.add(customer)

    try:
        db.session.commit()
        return customer
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "could not possible to create customer"})

def update_customer(customer_id, data):
    customer = Customer.query.filter_by(id=customer_id).first()

    if not customer:
        return jsonify({"error": "customer not found"})
    
    if check_email_already_in_use(data.email):
        return jsonify({"error": "email already in use"})
    
    cpf_already_in_use = check_cpf_already_in_use(data.cpf)
    if cpf_already_in_use != None:
        return cpf_already_in_use
    
    dict(data)
    data_to_be_stored = dict()

    for key, value in data.items():
        if not data[key] == None:
            data_to_be_stored[key] = value

    for key, value in data_to_be_stored.items():
        setattr(customer, key, value)
    
    try:
        db.session.commit()
        return customer
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "could not possible to update customer"})


def delete_customer(customer_id):
    customer = Customer.query.filter_by(id=customer_id).delete()

    if customer:
        try:
            db.session.commit()
            return jsonify({"message": "ok"})
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": "could not possible to delete customer"})
    else:
        return jsonify({"error": "could not possible to delete customer"})

def change_customer_status(customer_id):
    customer = Customer.query.filter_by(id=customer_id).first()
    if not customer:
        return jsonify({"error": "customer not found"})
    
    customer.status = True

    try:
        db.session.commit()
        return customer
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "could not possible to update customer"})
