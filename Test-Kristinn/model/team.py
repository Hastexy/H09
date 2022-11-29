class Team:
    def __init__(self, name="", club=""):
        self.name = name
        self.club = club
        self.players = ""
        self.captain = ""

    def __str__(self):
        return f"name: {self.name}; club: {self.club}; players: {self.players}; captain: {self.captain}"
