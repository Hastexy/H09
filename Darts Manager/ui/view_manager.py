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
╔═══╦══════════════════════════════════════╗
║   ║             View Manager             ║
╠═══╬══════════════════════════════════════╣
║ 1 ║ View Teams                           ║
║ 2 ║ View Upcoming Matches                ║
║ 3 ║ View Finished Matches                ║
║ 4 ║ View Team Standings                  ║
║ b ║ Back                                 ║
║ q ║ Quit                                 ║
╚═══╩══════════════════════════════════════╝"""
        )
        # print("\n---View Manager---")
        # print("1. view team")
        # print("2. view upcoming matches")
        # print("3. view matches with registered results")
        # print("4. view League Scores")
        # print("b. back")
        # print("q. quit")

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
                print("==Viewing Teams and Players==")
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
                print("==Viewing Upcoming Matches==")
            elif command == "3":
                print("==Viewing Matches with registered results==")
            elif command == "4":
                print("==Viewing League Standings==")

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
