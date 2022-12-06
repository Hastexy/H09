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
        """Initiates an instance of a player. Each player has a unique id number associated with them. Each player has basic personal information. If a player is a part of a team, the 'team' attribute is set to that team's ID number and the 'role' attribute can  either be a 'player' or a 'captain', depending on that player's status within the team."""
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
