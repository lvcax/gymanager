import re

all_fields = {
    "student": [
        "full_name", "birth_date", "address", "phone", "email",
    ]
}

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

def validate_fields(data: dict, model: str) -> tuple:
    """Validate fields from request

    Args:
        data (dict): Request data
        model (str): Model to be referenced in validation

    Returns:
        tuple[bool, dict[str]]: A tuple containing a bool value thah
        indicates if validation has been successful or not and a dict
        containing a message to be used in response
    """

    fields = all_fields.get(model)
    missing_fields = list()
    response = dict()
    
    for field in fields:
        if field not in data.keys():
            missing_fields.append(field)
    
    if len(missing_fields) == 0:
        result = validate_phone_number(data.get("phone"))
        if result == False:
            return False, {"msg": "Error: invalid phone number"}
        return True, {"msg": "ok"}
    else:
        if "phone" not in missing_fields:
            result = validate_phone_number(data.get("phone"))
            response["phone"] = "" if result else "Error: invalid phone number"
        for field in missing_fields:
            response[field] = "required field"
    
        return False, response
