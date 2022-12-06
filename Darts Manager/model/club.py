class Club:
    def __init__(self, id="", name="", address="", phone_number=""):
        """Inititates an instance of a club. Each club has an id number which is used by Team objects to link themselves to a specific club. Each club also has general contact information."""
        self.id = id
        self.name = name
        self.address = address
        self.phone_number = phone_number

    def __str__(self):
        return f"==========\nName: {self.name}\nAddress: {self.address}\nPhone nr: {self.phone_number}\n=========="
