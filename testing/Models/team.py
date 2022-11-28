class Team:
    def __init__(self, name, players) -> None:
        self.name = name
        self.players = players

    def __str__(self) -> str:
        return f"{self.name}, {self.players}"
