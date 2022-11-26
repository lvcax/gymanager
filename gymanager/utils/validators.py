import re

from gymanager.extensions.database import db
from gymanager.models import Student


all_fields = {
    "student": [
        "full_name", "birth_date", "address", "phone", "email",
    ]
}

def check_existing_email(email: str) -> bool:
    """Checks if email address is using in another count

    Args:
        email (str): new email to be save

    Returns:
        bool: "True if email is using, False is not
    """

    query_response = db.session.query(Student.email).all()
    emails = [element[0] for element in query_response]
    
    if email in emails:
        return True
    else:
        return False

def validate_phone_number(phone_number: str) -> bool:
    """Verifies if a phone number is valid

    Args:
        phone_number (str): Phone number value

    Returns:
        bool: True if is valid, else if not
    """

    result = re.match(
        pattern=r"\(\d{2}\)\d{4,5}\-\d{4}",
        string=phone_number
    )

    return True if result else False

def validate_fields(data: dict, model: str) -> dict:
    """Validate fields from request

    Args:
        data (dict): Request data
        model (str): Model to be referenced in validation

    Returns:
        dict: Message validations
    """

    fields = all_fields.get(model)
    missing_fields = list()
    response = dict()
    
    for field in fields:
        if field not in data.keys():
            missing_fields.append(field)
    
    response["msg"] = list()

    if len(missing_fields) == 0:
        result_phone = validate_phone_number(data.get("phone"))
        result_email = check_existing_email(data.get("email"))
        
        if result_phone == False:
            response["msg"].append({"phone": "invalid phone number"})
        if result_email == True:
            response["msg"].append({"email": "email already in use"})
        else:
            response["msg"] = "ok"
    else:
        if "phone" not in missing_fields:
            result_phone = validate_phone_number(data.get("phone"))
            if result_phone == False:
                response["msg"].append({"phone": "invalid phone number"})
        if "email" not in missing_fields:
            result_email = check_existing_email(data.get("email"))
            if result_email == True:
                response["msg"].append({"email": "email already in use"})
        for field in missing_fields:
            response["msg"].append({field: "required"})
    
    return response
