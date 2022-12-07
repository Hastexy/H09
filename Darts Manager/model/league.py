class League:
    def __init__(
        self,
        id="",
        name="",
        host="",
        phone="",
        start_date="",
        end_date="",
        rounds="",
    ) -> None:
        """Initiates an instance of a league. Each league has a unique ID number which Match objects use to link themselves to a specific league. Each league has a name and a host. The host must have a name and a phonenumber."""
        self.id = id
        self.name = name
        self.host = host
        self.phone = phone
        self.start_date = start_date
        self.end_date = end_date
        self.rounds = rounds
        self.teams = []
        self.round_dates = []

    def __str__(self) -> str:
        return f"==========\nName: {self.name}\nHost: {self.host}\nPhone nr: {self.phone}\nSD: {self.start_date}\nED: {self.end_date}\nAmount of teams: {self.teams}\nRounds: {self.rounds}\n=========="
