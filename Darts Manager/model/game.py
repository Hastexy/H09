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

        # Þetta komment gæti breyst, fer eftir útfærslunni á hvernig við geymum leiki sem eru spilaðir af mörgum spilurum...

        """Initiates an instance of a Game. Each Game object is of a certain type and has two players competing, the home_player and the away_player, both of which are Player objects. Each game can be played by 1-4 players. If one game is played by multiple players, then multiple Game objects must be initiated and the home_score and away_score must be set to 0-0 for all objects except the first one.

        Example:
        --------
        A '301' game was played by four players and the home_team won. Now four Game objects must be created, each of the same type with different player names and the result only registered for the first line and then set to 0-0 for subsequent Game objects.

        Like this:

        Game(301, Greg, George, 1-0, 1-1, 1)
        Game(301, Gary, Markus, 0-0, 0-0, 1)
        Game(301, Henry, James, 0-0, 0-0, 1)
        Game(301, Lucas, Benjamin, 0-0, 0-0, 1)

        This will be displayed as:

        Greg  1-0 301 1-1 George
        Gary  0-0 301 0-0 Markus
        Henry 0-0 301 0-0 James
        Lucas 0-0 301 0-0 Benjamin"""

        self.type = game_type
        self.home_player = home_player
        self.away_player = away_player
        self.home_score = home_score
        self.away_score = away_score
        self.match_ID = match_ID
