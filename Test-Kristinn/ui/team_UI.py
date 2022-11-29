from logic.team_logic import Team_Logic
from logic.player_logic import Player_Logic
from model.player import Player
from model.team import Team

from ui.input_validators import validate_name, NameLengthException


class Team_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        print("Main menu")
        print("\t1. Create a team")  # Create a Team now
        print("\t2. Create a player")  # list all customers
        print("\t3. Show all teams")  # list all customers

    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("\tEnter your command:")
            print()
            command = command.lower()
            if command == "b":
                print("going back")
                return "b"
            elif command == "q":
                print("quitting")
                return "q"
            elif command == "1":
                c = Team()
                while True:
                    c.name = input("Enter the name of the team: ")
                    try:
                        validate_name(c.name)
                        break
                    except NameLengthException:
                        print("name was too long")
                    except:
                        print("some error")

                # for idx in range(1, 5):
                #     c.players = input(f"Enter player {idx} name: ")

                c.club = input("Which club does the team belong to? ")

                self.logic_wrapper.create_team(c)
            elif command == "2":
                c = Player()
                while True:
                    c.name = input("Enter the name of the player: ")
                    try:
                        validate_name(c.name)
                        break
                    except NameLengthException:
                        print("Name was too long")
                    except:
                        print("Unexpected error")
                c.ssn = input("Enter the players ssn: ")
                c.email = input("Enter the player's email address: ")
                c.birth_year = input("Enter the birth year of the customer: ")
                self.logic_wrapper.create_player(c)
            elif command == "3":
                result = self.logic_wrapper.get_all_teams()
                for elem in result:
                    print(
                        f"name: {elem.name}; players: {elem.players}; captain: {elem.captain};"
                    )
            else:
                print("invalid input, try again")
