class Player:
    def __init__(
        self,
        ID="",
        name="",
        ssn="",
        email="",
        dob="",
        phone="",
        home_phone="",
        address="",
        team="",
        role="",
    ):
        self.id = ID
        self.name = name
        self.ssn = ssn
        self.email = email
        self.dob = dob
        self.phone = phone
        self.home_phone = home_phone
        self.address = address
        self.team = ""
        self.role = ""

    def __str__(self):
        result_str = f"{self.name} {self.ssn}{self.email}{self.dob}"
        if self.phone != "":
            result_str += f"{self.phone}"
        if self.home_phone != "":
            result_str += f"{self.home_phone}"
        if self.address != "":
            result_str += f"{self.address}"
        return result_str
