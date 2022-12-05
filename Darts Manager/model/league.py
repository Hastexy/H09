class League:
    def __init__(
        self,
        id="x",
        name="",
        host="",
        phone="",
        start_date="",
        end_date="",
        teams="",
        # team_amount="",
        # rounds="",
    ) -> None:
        self.id = id
        self.name = name
        self.host = host
        self.phone = phone
        self.start_date = start_date
        self.end_date = end_date
        # self.team_amount = team_amount
        # self.round = rounds
        self.teams = []
        self.matches = []

    def __str__(self) -> str:
        return f"==========\nName: {self.name}\nHost: {self.host}\nPhone nr: {self.phone}\nSD: {self.start_date}\nED: {self.end_date}\nAmount of teams: {self.team_amount}\nRounds: {self.round}\n=========="
