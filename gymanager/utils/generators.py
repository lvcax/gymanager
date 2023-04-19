import random

from gymanager.utils.checkers import check_registration


def gen_registration_number() -> str:
    while True:
        number = str(random.randint(0, 99999))

        if len(number) == 4:
            number = f"0{number}"
        elif len(number) == 3:
            number = f"00{number}"
        elif len(number) == 2:
            number = f"000{number}"
        elif len(number) == 1:
            number = f"0000{number}"
    
        if not check_registration(number):
            return number
