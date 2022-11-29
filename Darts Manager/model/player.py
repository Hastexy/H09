class Player:
    def __init__(self, name="", ssn="", email="", birth_year="2000"):
        self.name = name
        self.ssn = ssn
        self.email = email
        self.birth_year = birth_year

    def __str__(self):
        return f"name: {self.name}, ssn: {self.ssn}, email: {self.email}, birth year: {self.birth_year}"