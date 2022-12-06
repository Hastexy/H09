class Game:  # tegund af leik / umferð í einhverri viðureign
    def __init__(
        self,
        game_type="",
        home_player="",
        away_player="",
        home_score="",
        away_score="",
        match_ID="",
    ) -> None:
        self.type = game_type
        self.home_player = home_player
        self.away_player = away_player
        self.home_score = home_score
        self.away_score = away_score
        self.match_ID = match_ID
