CANCEL = """
╔═══════════════════════════════════════════╗
║ Input "b" at any point to cancel creation ║
╚═══════════════════════════════════════════╝"""
CANCEL2 = """
╔════════════════════╗
║ Creation Cancelled ║
╚════════════════════╝"""

ERR_LENGTH = """
╔═════════════════════════════════════════════════════╗
║ The input must be between 3 and 49 characters long! ║
╚═════════════════════════════════════════════════════╝"""

ERR_UNKNOWN = """
╔═══════════════════════════════════╗
║ Unknown Error Occurred, try again ║
╚═══════════════════════════════════╝"""

ERR_DIGIT = """
╔══════════════════════════════════════════╗
║ Phone number must only consist of digits ║
╚══════════════════════════════════════════╝"""

ERR_PHONE = """
╔════════════════════════════════════╗
║ Phone number must be 7 digits long ║
╚════════════════════════════════════╝"""

class NameLengthException(Exception):
    pass


class InvalidNumberLengthException(Exception):
    pass


class InvalidNumberCharacterException(Exception):
    pass


class NoAsperandSymbolException(Exception):
    pass


class InvalidNameError(Exception):
    pass


def validate_club_length(name):
    if len(name) <= 2 or len(name) >= 50:
        raise NameLengthException()


def validate_team_name(name):
    if len(name) <= 2 or len(name) >= 50:
        raise NameLengthException()


def validate_player_name(name):
    if len(name) <= 2 or len(name) >= 50:
        raise NameLengthException()
    elif not name.replace(" ", "").isalpha():
        raise InvalidNameError()


def validate_number(number):
    if len(number) != 7:
        raise InvalidNumberLengthException()
    if not number.isdigit():
        raise InvalidNumberCharacterException()


def validate_ssn(ssn):
    if len(ssn) != 10:
        raise InvalidNumberLengthException()
    if not ssn.isdigit():
        raise InvalidNumberCharacterException()


def validate_email(email):
    if "@" not in email:
        raise NoAsperandSymbolException


def validate_dob(dob):
    if len(dob) != 10:
        raise NameLengthException
    if dob[2] != "." or dob[5] != ".":
        raise InvalidNumberCharacterException


# class AlreadyRegisteredExeption(Exception)
#     pass

# def validate_results(score):
#     if score in results:
#         raise AlreadyRegisteredExeption()
