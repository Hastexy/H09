from logic.player_logic import Player_Logic
from model.player import Player
from ui.input_validators import *

class Player_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        print("Main menu")
        print("\t1. Create a player") # Create a player now
        print("\t2. Results Manager") # list all customers
        print("\t2. View Manager") # to go back

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
                c = Player()
                while True:
                    c.name = input("Enter the name of the player: ")
                    try:
                        validate_name(c.name)
                        break
                    except NameLengthException:
                        print("name was too long")
                    except:
                        print("some error")
                c.ssn = input("Enter the players ssn: ")
                c.email = input("Enter the player´s email address: ")
                c.birth_year = input("Enter the birth year of the customer: ")
                self.logic_wrapper.create_player(c)
            elif command == "2":
                result = self.logic_wrapper.get_all_players()
                for elem in result:
                    print(f"name: {elem.name}, ssn: {elem.ssn}, email: {elem.email}, birth year: {elem.birth_year}")
            else:
                print("invalid input, try again")
        