class Match:  # viðureign
    def __init__(
        self, id="", date="", home_team="", away_team="", result="", league_id=""
    ) -> None:
        self.id = id
        self.date = date
        self.home_team = home_team
        self.away_team = away_team
        self.result = result
        self.league_id = league_id
        self.games = []
