class Team:
    def __init__(self, name=""):
        self.name = name
        self.players = ""
        self.captain = ""

    def __str__(self):
        return f"name: {self.name}; players: {self.players}; captain: {self.captain}"