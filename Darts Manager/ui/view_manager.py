from typing import List
from model.team import Team
from model.player import Player

STR_NAME = "NAME"
STR_SSN = "SSN"
STR_EMAIL = "EMAIL"
STR_DOB = "DOB"
STR_PHONE = "PHONE"
STR_HOME_PHONE = "HOME PHONE"
STR_ADDRESS = "ADDRESS"
STR_ROLE = "ROLE"


class View_Manager_UI:
    def __init__(self, logic_connection) -> None:
        self.logic_wrapper = logic_connection

    def menu_output(self):
        print(
            """
╔═══╦═══════════════════════╗
║   ║      League Info      ║
╠═══╬═══════════════════════╣
║ 1 ║ View Teams            ║
║ 2 ║ View Upcoming Matches ║
║ 3 ║ View Finished Matches ║
║ 4 ║ View League Standings ║
║ b ║ Back                  ║
║ q ║ Quit                  ║
╚═══╩═══════════════════════╝"""
        )

    def input_prompt(self):
        all_leagues = self.logic_wrapper.get_all_leagues()
        league_id = self.select_league_id(all_leagues)

        if league_id == "b":
            return

        while True:
            self.menu_output()
            command = input("\nEnter your option: ")
            command = command.lower()
            if command == "q":
                print("\nGoodbye for now!")
                return "q"
            elif command == "b":
                print("\nGoing back!")
                return "b"
            elif command == "1":
                print("==Viewing Teams and Players==\n")
                all_teams = self.logic_wrapper.get_all_league_teams(league_id)
                for idx, team in enumerate(all_teams, 1):
                    print(f"\n{idx}. TEAM NAME: {team.name}")
                    print(
                        f"\n{STR_NAME:<35}{STR_PHONE:<12}{STR_SSN:<15}{STR_ADDRESS:<20}{STR_ROLE:<10}"
                    )
                    for player in team.players:
                        print(
                            f"{player.name.title():<35}{player.phone:<12}{player.ssn:<15}{player.address.title():<20}{player.role.title():<10}"
                        )

            elif command == "2":
                print("==Viewing Upcoming Matches==\n")
                matches_sorted_by_date = self.logic_wrapper.get_unfinished_matches(
                    league_id
                )
                for date, matches in matches_sorted_by_date.items():
                    header = f"#### Date: {date}"
                    print(header)
                    print("-" * len(header))
                    print("Games:")
                    for match in matches:
                        home, away = match
                        print(f"\t{home} VS {away}")

            elif command == "3":
                print("==Viewing Matches with registered results==\n")
                matches_sorted_by_date = self.logic_wrapper.get_finished_matches(
                    league_id
                )
                for date, matches in matches_sorted_by_date.items():
                    header = f"#### Date: {date}"
                    print(header)
                    print("-" * len(header))
                    for match in matches:
                        print(
                            f"Game:   {match.home_team.title()} VS {match.away_team.title()}\n"
                        )
                        for game in match.games:
                            self.parse_leg_score(game)
                            print(
                                f"{game.home_player.title():<25}{game.home_score:<4}{game.type:^4}{game.away_score}{game.away_player.title():>25}"
                            )
            elif command == "4":
                print("==Viewing League Standings==\n")
                print(f"{'TEAM':<25}{'MATCHES WON':<20}{'LEGS WON'}")
                teams_sorted_by_wins = self.logic_wrapper.get_team_standings(league_id)
                for team in teams_sorted_by_wins:
                    name, matches, legs = team
                    print("-" * 53)
                    print(f"{name:<25}{matches:<20}{legs}")
                print("-" * 53)

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

    def select_league_id(self, all_leagues: List[object]) -> None:
        while True:
            self.display_available_leagues(all_leagues)
            print("Press 'b' to go back")
            league_id = input("Which league do you want to view (League ID)?: ")
            for league in all_leagues:
                if league_id == str(league.id) or league_id == "b":
                    return league_id

            print("Please select a valid league ID from the list!")

    def parse_leg_score(self, game: object) -> None:
        if game.home_score == "0":
            game.home_score = "0-0"
        elif game.home_score == "1":
            game.home_score = "1-0"
        else:
            game.home_score = "1-1"

        if game.away_score == "0":
            game.away_score = "0-0"
        elif game.away_score == "1":
            game.away_score = "1-0"
        else:
            game.away_score = "1-1"
