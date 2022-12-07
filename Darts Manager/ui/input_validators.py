CANCEL = """
╔═══════════════════════════════════════════╗
║ Input "b" at any point to cancel creation ║
╚═══════════════════════════════════════════╝"""
CANCEL2 = """
╔════════════════════╗
║ Creation Cancelled ║
╚════════════════════╝"""

SKIP = """
╔════════════════════════════════════════════════╗
║ Press the enter button to skip optional inputs ║
╚════════════════════════════════════════════════╝"""

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

ERR_SSN = """
╔═══════════════════════════════════════════════╗
║ Social Security Number must be 10 digits long ║
╚═══════════════════════════════════════════════╝"""

ERR_DOB_FORMAT = """
╔══════════════════════════════════════════════════════════════╗
║ The date of birth must be 10 digits long in the format below ║
║ xx/xx/xxxx                                                   ║
╚══════════════════════════════════════════════════════════════╝"""


class NameLengthException(Exception):
    pass


class InvalidNumberLengthException(Exception):
    pass


class InvalidNumberCharacterException(Exception):
    pass


class NoAsperandSymbolException(Exception):
    pass


class TooManyAsperandSymbolException(Exception):
    pass


class InvalidNameError(Exception):
    pass


class NotDigitsError(Exception):
    pass


class RoundLengthError(Exception):
    pass


def validate_rounds(rounds: str) -> None:
    if not rounds.isdigit():
        raise NotDigitsError
    if int(rounds) < 1:
        raise RoundLengthError


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
    if email.count("@") >= 2:
        raise TooManyAsperandSymbolException


def validate_dob(dob):
    if len(dob) != 10:
        raise NameLengthException
    if dob[2] != "/" or dob[5] != "/":
        raise InvalidNumberCharacterException


def validate_league_name(league_name) -> None:
    """Má ég lesa úr gagnagrunninum hérna??"""
    pass


# class AlreadyRegisteredExeption(Exception)
#     pass

# def validate_results(score):
#     if score in results:
#         raise AlreadyRegisteredExeption()
