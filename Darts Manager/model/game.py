class Game:  # tegund af leik / umferð í einhverri viðureign
    def __init__(
        self,
        game_type="",
        home_player="",
        away_player="",
        home_score="",
        away_score="",
    ) -> None:

        # Þetta komment gæti breyst, fer eftir útfærslunni á hvernig við geymum leiki sem eru spilaðir af mörgum spilurum...

        """Initiates an instance of a Game. Each Game object is of a certain type and has two players competing, the home_player and the away_player. The Game object also keeps the score for the game."""

        self.type = game_type
        self.home_player = home_player
        self.away_player = away_player
        self.home_score = home_score
        self.away_score = away_score
