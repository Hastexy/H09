from model.team import Team
from model.player import Player

STR_NAME = "NAME"
STR_SSN = "SSN"
STR_EMAIL = "EMAIL"
STR_DOB = "DOB"
STR_PHONE = "PHONE"
STR_HOME_PHONE = "HOME PHONE"
STR_ADDRESS = "ADDRESS"


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
║ 3 ║ View Matches With Registered Results ║
║ 4 ║ View League Scores                   ║
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
                # print("\nYou are viewing the teams and their players")
                all_teams = self.logic_wrapper.get_all_teams()
                for idx, team in enumerate(all_teams, 1):
                    print(f"\n{idx}. TEAM NAME: {team.name}")
                    print(
                        f"\n{STR_NAME:<50}{STR_SSN:<12}{STR_EMAIL:<30}{STR_DOB:<12}{STR_PHONE:<10}{STR_HOME_PHONE:<15}{STR_ADDRESS:<30}\n"
                    )
                    print(team.captain)
                    for player in team.players:
                        print(
                            f"{player.name:<50}{player.ssn:<12}{player.email:<30}{player.dob:<12}{player.phone:<10}{player.home_phone:<15}{player.address:<30}"
                        )
                # for team in all_teams:
                #     print(f"\n1. TEAM NAME: {team.name}")
                #     print()
                #     print(
                #         f"{str_name:<25}{str_ssn:<12}{str_email:<20}{str_dob:<12}{str_phone:<10}{str_home_phone:<15}{str_address:<30}\n"
                #     )
                #     for player in team.players:
                #         print(
                #             f"{player.name:<25}{player.ssn:<12}{player.email:<20}{player.dob:<12}{player.phone:<10}{player.home_phone:<15}{player.address:<30}"
                #         )
            elif command == "2":
                print("==Print Upcoming Matches==")
            elif command == "3":
                print("==Print Matches with registered results==")
            elif command == "4":
                print("==Print League Scores==")
