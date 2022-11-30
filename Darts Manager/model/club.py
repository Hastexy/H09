class Club:
    def __init__(self, name="", address="", phone_number=""):
        self.name = name
        self.address = address
        self.phone_number = phone_number

    def __str__(self):
        return f"==========\nName: {self.name}\nAddress: {self.address}\nPhone nr: {self.phone_number}\n=========="