class Match:
    def __init__(
        self, id="", date="", home_team="", away_team="", result="", league_id=""
    ) -> None:
        """Initiates an instance of a match. Each match has a unique ID number which Game objects use to link themselves to a specific match. Each match has a date in which it takes place. Two teams, a home_team and an away_team, compete with each other in a match. Both home_team and away_team are Team objects. If the 'result' attribute is an empty string, the match has not been played."""
        self.id = id
        self.date = date
        self.home_team = home_team
        self.away_team = away_team
        self.result = result
        self.league_id = league_id
        self.games = []
