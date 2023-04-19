from gymanager.models import Customer

from pycpfcnpj import cpfcnpj


def check_registration(number: str) -> bool:
    customer = Customer.query.filter_by(registration=number).first()

    if customer:
        return True
    return False

def check_email(email: str) -> bool:
    customer = Customer.query.filter_by(email=email).first()

    if customer:
        return True
    return False

def check_cpf(cpf: str) -> bool:
    if not cpfcnpj.validate(cpf):
        return False

    customer = Customer.query.filter_by(cpf=cpf).first()

    if customer:
        return True
    return False
