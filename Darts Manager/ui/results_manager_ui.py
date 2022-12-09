from datetime import datetime
from typing import List
from colorama import init, Fore, Style
from model.game import Game

BACK = f"""{Fore.YELLOW}
╔══════════════════════╗
║ Input "b" to go back ║
╚══════════════════════╝\n{Fore.WHITE}"""


class Results_Manager_UI:
    def __init__(self, logic_connection) -> None:
        self.logic_wrapper = logic_connection

    def menu_output(self):
        """Prints out all available inputs from the result manager screen."""
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
        """This is the main domain for the result manager."""
        all_leagues = self.logic_wrapper.get_all_leagues()
        league_id = self.select_league_id(all_leagues)

        if league_id == "b":
            return
        while True:
            name = input("\nEnter your registered name: ").strip().lower()
            if name == "b":
                return "b"
            elif self.logic_wrapper.check_host_name(name, league_id):
                print(f"Hello {name}, you are here to make some changes")
                all_finished_matches = self.logic_wrapper.get_finished_matches(
                    league_id
                )

                all_unfinished_matches = self.logic_wrapper.get_unfinished_matches(
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
                        header = "* Here is a list of all finished matches: *"
                        self.display_matches(all_finished_matches, header)
                        self.change_match_result(all_finished_matches, league_id)
                    elif command == "2":
                        header = "* Here is a list of all upcoming matches: *"
                        self.display_matches(all_unfinished_matches, header)
                        self.change_match_date(all_unfinished_matches)
                    else:
                        print("Invalid input!")

            elif self.logic_wrapper.check_captain_name(name, league_id):
                print(f"\n{Fore.YELLOW}╔{'═'*78}╗")
                print(
                    f"║ {f'Hello {name}, you are here to update a match result':^77}║"
                )
                the_captain = self.logic_wrapper.check_captain_name(name, league_id)
                all_unfinished_matches = self.logic_wrapper.get_unfinished_matches(
                    league_id
                )
                the_team_of_the_captain = self.logic_wrapper.get_team(the_captain.team)
                filtered_unfinished_matches = {}
                for date, matches in all_unfinished_matches.items():
                    for match in matches:
                        if match.home_team == the_team_of_the_captain.name:
                            filtered_unfinished_matches[date] = matches
                if not filtered_unfinished_matches:
                    print(f"║ {'You have no matches to record results for':^76} ║")
                    print(f"╚{'═' * 78}╝{Fore.WHITE}")
                    return
                header = f"║ {'Here is a list of all your unfinished matches':^76} ║"
                self.display_matches(filtered_unfinished_matches, header)
                self.change_match_result(filtered_unfinished_matches, league_id)
                print("#### Going Back To Main Menu")
                return
            else:
                print(
                    f"""{Fore.RED}
╔═════════════════════════════════════╗
║ Couldn't find that name, try again! ║
╚═════════════════════════════════════╝{Fore.WHITE}"""
                )

    def select_league_id(self, all_leagues: List[object]) -> None:
        """Allows the user to select a league by its id."""
        while True:
            self.display_available_leagues(all_leagues)
            print(BACK)
            league_id = input("Enter the ID of the League you want to work on: ")
            if league_id == "b":
                return "b"
            for league in all_leagues:
                if league_id == str(league.id):
                    return league_id

            print(
                f"""{Fore.RED}
╔═════════════════════════════════════════╗
║ Select a valid league ID from the list! ║
╚═════════════════════════════════════════╝{Fore.WHITE}"""
            )

    def display_available_leagues(self, leagues: List[object]) -> None:
        """Displays all registerd leagues."""
        header = f"║ {'List of all registered leagues':^39} ║"
        separator = "═" * (len(header) - 2)

        print(f"\n╔{separator}╗")
        print(header)
        print(f"╠{separator}╣")

        print(f"║ {'NAME':<38}{'ID':>2}║")
        print(f"╠{'═'*41}╣")
        for league in leagues:
            print(f"║ {league.name.title():<38}{league.id:>2}║")
        print(f"╚{'═'*41}╝")

    def display_matches(self, all_matches: dict, header: str) -> None:
        separator = "═" * (len(header) - 2)

        print(header)
        print(f"╚{separator}╝{Fore.WHITE}")

        for date, matches in all_matches.items():

            print(f"╔{'═'*10}╦{'═'*67}╗")
            print(f"║{'Date':^10}║{date:<67}║")
            print(f"╠{'═'*6}╦{'═'*3}╩{'═'*24}╦{'═'*5}╦{'═'*28}╦{'═'*7}╣")
            for match in matches:
                print(
                    f"║ Game ║ {match.home_team.title():>26} ║  V  ║ {match.away_team.title():<26} ║ ID: {match.id} ║"
                )

            print(f"╚{'═'*6}╩{'═'*28}╩{'═'*5}╩{'═'*28}╩{'═' * 7}╝")

    def change_match_date(self, all_matches: dict) -> None:
        while True:
            print(BACK)
            match_id = input("Select a match to change the date of (match ID): ")
            if match_id == "b":
                return
            for matches in all_matches.values():
                for match in matches:
                    if str(match.id) == match_id:
                        self.update_match_date(match)
                        self.logic_wrapper.reschedule_match(match)
                        print("\n#### Date Changed Successfully\n")
                        return
            print("Please select one of the matches from the list!")

    def change_match_result(self, all_matches: dict, league_id: str) -> None:
        while True:
            print(BACK)
            match_id = input("Select a match to change (match ID): ")
            if match_id == "b":
                return
            for matches in all_matches.values():
                for match in matches:
                    if str(match.id) == match_id:
                        match.games.clear()
                        self.update_match_result(match, league_id)
                        self.logic_wrapper.record_result(match)
                        print("\n#### Result Recorded Successfully\n")
                        return
            print("Please select one of the matches from the list!")

    def update_match_date(self, match: object) -> None:
        while True:
            new_date = input(
                "Please enter the new date of the match in this format (dd/mm/yyyy hh:mm): "
            )
            try:
                new_date = datetime.strptime(new_date, "%d/%m/%Y %H:%M")
                match.date = str(new_date.strftime("%d/%m/%Y %H:%M"))
                return
            except ValueError:
                print("Please enter the date like the format shows!")

    def update_match_result(self, match: object, league_id: str) -> None:
        print(f"\n╔{'═'*67}╗")
        print(f"║{'First there are FOUR 501 games 1v1':^67}║")
        print(f"║{'Select a player from each team and then assign the scores':^67}║")
        print(f"╚{'═'*67}╝")

        home_team_players = self.logic_wrapper.get_team_members(
            match.home_team, league_id
        )
        away_team_players = self.logic_wrapper.get_team_members(
            match.away_team, league_id
        )
        # 501 Games
        for i in range(1, 5):
            home_player, away_player = self.get_competitors(
                home_team_players, away_team_players, i
            )
            home_score, away_score = self.get_game_scores()
            g = Game("501", home_player, away_player, home_score, away_score)
            match.games.append(g)

        # 301 game
        print(f"\n╔{'═'*67}╗")
        print(f"║{'Now there is a 301 game 2v2':^67}║")

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
        print(f"\n╔{'═'*67}╗")
        print(f"║{'Now there is a Cricket game 2v2':^67}║")
        print(f"║{'Enter the result for the cricket game':^67}║")
        print(f"╚{'═'*67}╝")

        home_score, away_score = self.get_game_scores()

        g = Game("C", home_player1, away_player1, home_score, away_score)
        match.games.append(g)
        g = Game("C", home_player2, away_player2, 0, 0)
        match.games.append(g)

        # 501 4v4 game
        print(f"\n╔{'═'*67}╗")
        print(f"║{'Now for the 4v4 501 game':^67}║")
        print(f"║{'Enter the result for the last 501 game':^67}║")
        print(f"╚{'═'*67}╝")
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
        """Get the game scores for a game in a given match."""
        while True:
            try:
                home_score = int(input("Home Player Score: "))
                if 0 <= home_score <= 2:
                    break
                print("Please enter a score between 0 and 2!")
            except ValueError:
                print("Please enter an integer between 0 and 2!")

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
        """"""
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
        print(
            f"║{'Select TWO players from the list who competed in the 301 game':^67}║"
        )
        print(f"╚{'═'*67}╝")
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
