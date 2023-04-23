from flask import jsonify

from gymanager.models import Customer

from pycpfcnpj import cpfcnpj


def check_registration(number: str) -> bool:
    customer = Customer.query.filter_by(registration=number).first()

    if customer:
        return True
    return False

def check_email_already_in_use(email: str) -> bool:
    email_already_use = Customer.query.filter_by(email=email).first()
    
    if email_already_use:
        return True
    return False

def check_cpf_already_in_use(cpf: str) -> bool:
    if not cpfcnpj.validate(cpf):
        return jsonify({"error": "invalid cpf"})

    cpf_already_use = Customer.query.filter_by(cpf=cpf).first()
    if cpf_already_use:
        return jsonify({"error": "cpf already in use"})
    
    return None
