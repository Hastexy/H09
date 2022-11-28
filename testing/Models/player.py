class Player:
    def __init__(self, name, ssn, email, date_of_birth) -> None:
        self.name = name
        self.ssn = ssn
        self.email = email
        self.date_of_birth = date_of_birth

    def __str__(self) -> str:
        return f"Name: {self.name} Social security number: {self.ssn} Email: {self.email} Date of birth: {self.date_of_birth}"
