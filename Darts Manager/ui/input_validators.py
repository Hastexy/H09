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
║ The input must be between 3 and 39 characters long! ║
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

ERR_NO_ASP = """
╔════════════════════╗
║ Missing "@" symbol ║
╚════════════════════╝"""

ERR_MANY_ASP = """
╔══════════════════════════╗
║ More than one "@" symbol ║
╚══════════════════════════╝"""

ERR_BEFORE_ASP = """
╔════════════════════════════════════════╗
║ There is nothing before the "@" symbol ║
╚════════════════════════════════════════╝"""

ERR_AFTER_ASP = """
╔═══════════════════════════════════════╗
║ There is nothing after the "@" symbol ║
╚═══════════════════════════════════════╝"""

ERR_DOT_ASP = """
╔══════════════════════════════════════════════════════╗
║ There shouldn't be a dot before the asperand symbol  ║
╚══════════════════════════════════════════════════════╝"""

ERR_DOT_START = """
╔═══════════════════════════════════╗
║ An email doesn't start with a dot ║
╚═══════════════════════════════════╝"""

ERR_CONSECUTIVE_DOT = """
╔════════════════════════════════════════════════════════════════╗
║ There are not supposed to be consecutive dots in an email ".." ║
╚════════════════════════════════════════════════════════════════╝"""

ERR_DOMAIN_MISSING = """
╔════════════════════════════════════════════════════════════╗
║ You are missing the domain ".com" at the end of your email ║
╚════════════════════════════════════════════════════════════╝"""


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


class NothingBeforeAsperandException(Exception):
    pass


class NothingAfterAsperandException(Exception):
    pass


class NoDotBeforeAsperandException(Exception):
    pass


class NoDotAtStartException(Exception):
    pass


class ConsecutiveDotsException(Exception):
    pass


class MissingDomainNameException(Exception):
    pass


class InvalidNameError(Exception):
    pass


class NotDigitsError(Exception):
    pass


class RoundLengthError(Exception):
    pass


def validate_rounds(rounds: str) -> None:
    if not rounds.isdigit():
        raise NotDigitsError()
    if int(rounds) < 1:
        raise RoundLengthError()


def validate_club_length(name):
    if len(name) <= 2 or len(name) >= 40:
        raise NameLengthException()


def validate_team_name(name):
    if len(name) <= 2 or len(name) >= 40:
        raise NameLengthException()


def validate_player_name(name):
    if len(name) <= 2 or len(name) >= 40:
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
        raise NoAsperandSymbolException()
    if email.count("@") >= 2:
        raise TooManyAsperandSymbolException()
    if email.count("@") == 1:
        x, y = email.split("@")
        if x == "":
            raise NothingBeforeAsperandException()
        if y == "":
            raise NothingAfterAsperandException()
        if x[-1] == ".":
            raise NoDotBeforeAsperandException()

    if email[0] == ".":
        raise NoDotAtStartException()
    if ".." in email:
        raise ConsecutiveDotsException()

    if email[-4] != ".com":
        raise MissingDomainNameException()


def validate_dob(dob: str):
    if len(dob) != 10:
        raise NameLengthException()
    if dob[2] != "/" or dob[5] != "/":
        raise InvalidNumberCharacterException()


def validate_league_name(league_name) -> None:
    """Má ég lesa úr gagnagrunninum hérna??"""
    pass


# class AlreadyRegisteredExeption(Exception)
#     pass

# def validate_results(score):
#     if score in results:
#         raise AlreadyRegisteredExeption()
