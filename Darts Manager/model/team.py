class Team:
    def __init__(self, id="", name="", club="") -> None:
        """Initiates an instance of a team. Each team has a unique ID number which is used by Player objects to link themselves to a specific team. Each team also has general information attributes. When a Team object is created, the 'players' attribute list is filled with Player objects and the 'captain' attribute is assigned to one of those players."""
        self.id = id
        self.name = name
        self.club = club
        self.players = []
        self.captain = ""

    def __str__(self) -> str:
        return f"name: {self.name}; club: {self.club}; players: {self.players}; captain: {self.captain}"

        """
        input name: tset
        input club: test
            (check if team exists continue if it does)
        input captain:
            (check if player exists continue if it does)
            else: error 
        input players:
            (check if player exists continue if it does)
            else: error 
        """
