from model.team import Team
from model.player import Player

str_name = "NAME"
str_ssn = "SSN"
str_email = "EMAIL"
str_dob = "DOB"
str_phone = "PHONE"
str_home_phone = "HOME_PHONE"
str_address = "ADDRESS"


class View_Manager_UI:
    def __init__(self, logic_connection) -> None:
        self.logic_wrapper = logic_connection
        self.testing = {
            "Dart Vader": [
                Player(
                    "1",
                    "óskar",
                    "1234567890",
                    "oskar@gmail.com",
                    "14.04.1982",
                    "6963583",
                    "4567892",
                    "DisneyLand",
                ),
                Player(
                    "2",
                    "styrmir",
                    "0987654321",
                    "styrmir@gmail.com",
                    "10.09.2000",
                    "5012345",
                    "9685742",
                    "Discord",
                ),
                Player(
                    "3",
                    "kjartan",
                    "1020304050",
                    "kjartan@gmail.com",
                    "11.11.2016",
                    "9876541",
                    "3574692",
                    "RU",
                ),
            ]
        }

    def menu_output(self):
        print("\n---View Manager---")
        print("1. view team")
        print("b. back")
        print("q. quit")

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
                for key, value in all_teams.items():
                    print(f"\n1. TEAM NAME: {key}")
                    print()
                    print(
                        f"{str_name:<25}{str_ssn:<12}{str_email:<20}{str_dob:<12}{str_phone:<10}{str_home_phone:<15}{str_address:<30}\n"
                    )
                    for test in value:
                        print(
                            f"{test.name:<25}{test.ssn:<12}{test.email:<20}{test.dob:<12}{test.phone:<10}{test.home_phone:<15}{test.address:<30}"
                        )

    # Menu fyrir view manager, með option a view teams.
    # Þegar teams eru viewed þarf ég að prenta rétta formattið
