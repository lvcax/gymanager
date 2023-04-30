from gymanager.models import Customer
from gymanager.extensions.database import db


def list_customers(page):
    customers = Customer.query.paginate(page=page, per_page=5)

    return customers

def get_customer_by_id(customer_id):
    customer = Customer.query.filter_by(id=customer_id).first()

    return customer

def create_customer(data):
    customer = Customer(
        registration=data.registration,
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
        return {"error": "could not possible to create customer"}

def update_customer(customer, data):
    dict(data)
    data_to_be_update = dict()

    for key, value in data.items():
        if not data[key] == None:
            data_to_be_update[key] = value

    for key, value in data_to_be_update.items():
        setattr(customer, key, value)
    
    try:
        db.session.commit()
        return customer, 200
    except Exception as e:
        db.session.rollback()
        return {"error": "could not possible to update customer"}, 500

def delete_customer(customer_id):
    customer = Customer.query.filter_by(id=customer_id).delete()

    if not customer:
        return {"error": "customer not found"}, 404
    
    try:
        db.session.commit()
        return {"message": "ok"}, 201
    except Exception as e:
        db.session.rollback()
        return {"error": "could not possible to delete customer"}, 500

def change_customer_status(customer_id):
    customer = Customer.query.filter_by(id=customer_id).first()
    
    if not customer:
        return {"error": "customer not found"}, 404
    
    customer.status = True

    try:
        db.session.commit()
        return customer, 200
    except Exception as e:
        db.session.rollback()
        return {"error": "could not possible to update customer"}, 500
