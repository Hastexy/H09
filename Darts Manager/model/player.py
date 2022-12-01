class Player:
    def __init__(self, ID="", name="", ssn="", email="", dob="", phone="", home_phone="", address=""):
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
        result_str = f"==========\nName: {self.name}\nSSN: {self.ssn}\nEmail: {self.email}\nDOB: {self.dob}"
        if self.phone != "":
            result_str += f"\nGSM: {self.phone}"
        if self.home_phone != "":
            result_str += f"\nHome-Phone: {self.home_phone}"
        if self.address != "":
            result_str += f"\nAddress: {self.address}"
        result_str += "\n=========="
        return result_str