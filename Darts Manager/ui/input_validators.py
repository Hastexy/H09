from colorama import init, Fore, Style

init()
# Colorama options
# Fore = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
# Style = [DIM, NORMAL, BRIGHT]
CANCEL = f"""{Fore.YELLOW}
╔═══════════════════════════════════════════╗
║ Input "b" at any point to cancel creation ║
╚═══════════════════════════════════════════╝{Fore.WHITE}"""
CANCEL2 = f"""{Fore.YELLOW}
╔════════════════════╗
║ Creation Cancelled ║
╚════════════════════╝{Fore.WHITE}"""

SKIP = f"""{Fore.YELLOW}
╔════════════════════════════════════════════════╗
║ Press the enter button to skip optional inputs ║
╚════════════════════════════════════════════════╝{Fore.WHITE}"""

ERR_LENGTH = f"""{Fore.RED}
╔═════════════════════════════════════════════════════╗
║ The input must be between 3 and 39 characters long! ║
╚═════════════════════════════════════════════════════╝{Fore.WHITE}"""

ERR_UNKNOWN = f"""{Fore.RED}
╔═══════════════════════════════════╗
║ Unknown Error Occurred, try again ║
╚═══════════════════════════════════╝{Fore.WHITE}"""

ERR_DIGIT = f"""{Fore.RED}
╔══════════════════════════════════════════╗
║ Phone number must only consist of digits ║
╚══════════════════════════════════════════╝{Fore.WHITE}"""

ERR_PHONE = f"""{Fore.RED}
╔════════════════════════════════════╗
║ Phone number must be 7 digits long ║
╚════════════════════════════════════╝{Fore.WHITE}"""

ERR_SSN = f"""{Fore.RED}
╔═══════════════════════════════════════════════╗
║ Social Security Number must be 10 digits long ║
╚═══════════════════════════════════════════════╝{Fore.WHITE}"""

ERR_DOB_FORMAT = f"""{Fore.RED}
╔══════════════════════════════════════════════════════════════╗
║ The date of birth must be 10 digits long in the format below ║
║ xx/xx/xxxx                                                   ║
╚══════════════════════════════════════════════════════════════╝{Fore.WHITE}"""

ERR_NO_ASP = f"""{Fore.RED}
╔════════════════════╗
║ Missing "@" symbol ║
╚════════════════════╝{Fore.WHITE}"""

ERR_MANY_ASP = f"""{Fore.RED}
╔══════════════════════════╗
║ More than one "@" symbol ║
╚══════════════════════════╝{Fore.WHITE}"""

ERR_BEFORE_ASP = f"""{Fore.RED}
╔════════════════════════════════════════╗
║ There is nothing before the "@" symbol ║
╚════════════════════════════════════════╝{Fore.WHITE}"""

ERR_AFTER_ASP = f"""{Fore.RED}
╔═══════════════════════════════════════╗
║ There is nothing after the "@" symbol ║
╚═══════════════════════════════════════╝{Fore.WHITE}"""

ERR_DOT_ASP = f"""{Fore.RED}
╔══════════════════════════════════════════════════════╗
║ There shouldn't be a dot before the asperand symbol  ║
╚══════════════════════════════════════════════════════╝{Fore.WHITE}"""

ERR_DOT_START = f"""{Fore.RED}
╔═══════════════════════════════════╗
║ An email doesn't start with a dot ║
╚═══════════════════════════════════╝{Fore.WHITE}"""

ERR_CONSECUTIVE_DOT = f"""{Fore.RED}
╔════════════════════════════════════════════════════════════════╗
║ There are not supposed to be consecutive dots in an email ".." ║
╚════════════════════════════════════════════════════════════════╝{Fore.WHITE}"""

ERR_DOMAIN_MISSING = f"""{Fore.RED}
╔════════════════════════════════════════════════════════════╗
║ You are missing the domain ".com" at the end of your email ║
╚════════════════════════════════════════════════════════════╝{Fore.WHITE}"""


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
