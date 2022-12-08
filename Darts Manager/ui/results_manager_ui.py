from typing import List

from model.game import Game


class Results_Manager_UI:
    def __init__(self, logic_connection) -> None:
        self.logic_wrapper = logic_connection

    def menu_output(self):
        print(
            """
╔═══╦════════════════════════╗
║   ║     Match Manager      ║
╠═══╬════════════════════════╣
║ 1 ║ Register Match Results ║
║ 2 ║ Change Match Results   ║
║ b ║ Back                   ║
║ q ║ Quit                   ║
╚═══╩════════════════════════╝"""
        )

    def input_prompt(self):
        all_leagues = self.logic_wrapper.get_all_leagues()
        league_id = self.select_league_id(all_leagues)

        if league_id == "b":
            return
        while True:
            name = input("What is your name (full name)?: ").strip().lower()
            if name == "b":
                return
            elif self.logic_wrapper.check_host_name(name, league_id):
                # þarf að sækja allar kláraðar viðureignir í league-inu:
                all_finished_matches = self.logic_wrapper.get_finished_matches(
                    league_id
                )

                while True:
                    print("1. Change Match Result")
                    print("2. Change Match Date")
                    print("b. Back")

                    command = input("Enter your choice: ").strip().lower()
                    if command == "b":
                        return
                    elif command == "1":
                        self.display_finished_matches(all_finished_matches)
                        self.change_match_results(all_finished_matches, league_id)
                    elif command == "2":
                        self.display_finished_matches(all_finished_matches)
                        self.change_match_date(all_finished_matches, league_id)
                    else:
                        print("Invalid input!")

            elif self.logic_wrapper.check_captain_name(name, league_id):
                print("Komin tenging í captain :)")
            else:
                print("Couldn't find that name, try again!")

        # skoða host nafnið hjá þessu tiltekna league
        # fara í gegnum öll liðin sem taka þátt í keppninni og liðsmenn þeirra
        # while True:
        #     self.menu_output()
        #     command = input("\nEnter your option: ")
        #     command = command.lower()
        #     if command == "q":
        #         print("\nGoodbye for now!")
        #         return "q"
        #     elif command == "b":
        #         print("\nGoing back!")
        #         return "b"
        #     elif command == "1":
        #         print("==Register match result stuff==")
        #     elif command == "2":
        #         print("==Change match result stuff==")

    def select_league_id(self, all_leagues: List[object]) -> None:
        while True:
            self.display_available_leagues(all_leagues)
            print("Press 'b' to go back")
            league_id = input(
                "Which league do you want to register results for (League ID)?: "
            )
            for league in all_leagues:
                if league_id == str(league.id) or league_id == "b":
                    return league_id

            print("Please select a valid league ID from the list!")

    def display_available_leagues(self, leagues: List[object]) -> None:
        header = "* Here is a list of all registered leagues: *"
        separator = "*" * len(header)

        print(f"\n{separator}")
        print(header)
        print(f"{separator}\n")

        print(f"{'NAME':<35}{'ID'}")
        print("-" * 38)
        for league in leagues:
            print(f"{league.name.title():<35}{league.id}")
        print("-" * 38)

    def display_finished_matches(self, all_matches: dict) -> None:
        pass
        header = "* Here is a list of all finished matches: *"
        separator = "*" * len(header)

        print(f"\n{separator}")
        print(header)
        print(f"{separator}\n")

        for date, matches in all_matches.items():
            header = f"#### Date: {date}"
            print(header)
            print("-" * len(header))
            for match in matches:
                print(
                    f"Game:\t{match.home_team.title()} VS {match.away_team.title():<15}ID: {match.id}\n"
                )

    def change_match_date(self, all_matches: dict) -> None:
        match_id = input("Select a match to change (match ID): ")

    def change_match_results(self, all_matches: dict, league_id: str) -> None:
        while True:
            print("Press 'b' to go back")
            match_id = input("Select a match to change (match ID): ")
            if match_id == "b":
                return
            for matches in all_matches.values():
                for match in matches:
                    if str(match.id) == match_id:
                        match.games.clear()
                        self.update_match_result(match, league_id)
                        self.logic_wrapper.record_result(match)
                        return
            print("Please select one of the matches from the list!")

    def update_match_result(self, match: object, league_id: str) -> None:
        # 501 1v1 game
        print("\nFirst there are FOUR 501 games 1v1")
        print(
            "Select a player from each team and assign a score to them for each game!\n"
        )

        home_team_players = self.logic_wrapper.get_team_members(
            match.home_team, league_id
        )
        away_team_players = self.logic_wrapper.get_team_members(
            match.away_team, league_id
        )

        for i in range(1, 5):
            home_player, away_player = self.get_competitors(
                home_team_players, away_team_players, i
            )
            home_score, away_score = self.get_game_scores()
            g = Game("501", home_player, away_player, home_score, away_score)
            match.games.append(g)

        # 301 game
        print("\nNow there is a 301 game 2v2\n")
        home_team_players = self.logic_wrapper.get_team_members(
            match.home_team, league_id
        )
        away_team_players = self.logic_wrapper.get_team_members(
            match.away_team, league_id
        )
        home_player1, home_player2 = self.get_301_players(home_team_players)
        away_player1, away_player2 = self.get_301_players(away_team_players)
        home_score, away_score = self.get_game_scores()

        g = Game("301", home_player1, away_player1, home_score, away_score)
        match.games.append(g)

        g = Game("301", home_player2, away_player2, 0, 0)
        match.games.append(g)

        # Cricket game
        home_player1, home_player2 = home_team_players
        away_player1, away_player2 = away_team_players
        print("\nNow there is a Cricket game 2v2")
        print("Enter the result for the cricket game:\n")
        home_score, away_score = self.get_game_scores()

        g = Game("C", home_player1, away_player1, home_score, away_score)
        match.games.append(g)
        g = Game("C", home_player2, away_player2, 0, 0)
        match.games.append(g)

        # 501 4v4 game
        print("\nNow for the 4v4 501 game")
        print("How did that game go?\n")
        home_team_players = self.logic_wrapper.get_team_members(
            match.home_team, league_id
        )
        away_team_players = self.logic_wrapper.get_team_members(
            match.away_team, league_id
        )
        all_players = list(zip(home_team_players, away_team_players))
        home_score, away_score = self.get_game_scores()
        home_player = all_players[0][0]
        away_player = all_players[0][1]
        g = Game("501", home_player, away_player, home_score, away_score)
        match.games.append(g)

        for players in all_players[1:]:
            home_player, away_player = players
            g = Game("501", home_player, away_player, 0, 0)
            match.games.append(g)

    def display_players(self, players: List[object]) -> None:
        header = "* Available Players: *"
        separator = "*" * len(header)

        print(f"\n{separator}")
        print(header)
        print(f"{separator}\n")

        print(f"{'NAME':<35}{'ID'}")
        print("-" * 38)
        for player in players:
            print(f"{player.name.title():<35}{player.id}")
        print("-" * 38)

    def get_game_scores(self) -> int:
        while True:
            try:
                home_score = int(input("Home Player Score: "))
                if 0 <= home_score <= 2:
                    break
                print("Please enter a score between 0 and 2!")
            except ValueError:
                print("Please enter an integer between 0 and 2!")

        # Gæti þurft að villutékka að það má ekki setja inn 2 fyrir bæði liðin...
        while True:
            try:
                away_score = int(input("Away Player Score: "))
                if 0 <= away_score <= 2:
                    break
                print("Please enter a score between 0 and 2!")
            except ValueError:
                print("Please enter an integer between 0 and 2!")
        return home_score, away_score

    def get_competitors(
        self, home_team_players, away_team_players, game_number
    ) -> object:
        while True:
            home_player = ""
            self.display_players(home_team_players)
            home_player_id = input(
                f"Who competed for the home team in game {game_number} (Player ID)?: "
            )
            for player in home_team_players:
                if home_player_id == player.id:
                    home_team_players.remove(player)
                    home_player = player

            if home_player:
                break
            print("Please insert a valid Player ID from the list!")

        while True:
            away_player = ""
            self.display_players(away_team_players)
            away_player_id = input(
                f"Who competed for the away team  in game {game_number} (Player ID)?:"
            )
            for player in away_team_players:
                if away_player_id == player.id:
                    away_team_players.remove(player)
                    away_player = player

            if away_player:
                break
            print("Please insert a valid Player ID from the list!")
        return home_player, away_player

    def get_301_players(self, available_players: List[object]) -> object:
        print("Select TWO players from the list who competed in the 301 game:")
        both_players = []
        for i in range(1, 3):
            while True:
                a_player = ""
                self.display_players(available_players)
                a_player_id = input(f"Select player {i} (Player ID)?: ")
                for player in available_players:
                    if a_player_id == player.id:
                        available_players.remove(player)
                        a_player = player
                        both_players.append(player)
                if a_player:
                    break
                print("Please insert a valid Player ID from the list!")
        return both_players
