class Club:
    def __init__(self, name, address, phonenumber) -> None:
        self.name = name
        self.address = address
        self.phonenumber = phonenumber

    def __str__(self) -> str:
        return f"Club name: {self.name} Address: {self.address} Phonenumber: {self.phonenumber}"
