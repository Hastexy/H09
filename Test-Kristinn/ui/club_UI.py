from logic.team_logic import Team_Logic
from model.team import Team
from ui.input_validators import *

class Team_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def menu_output(self):
        print("Club menu")
        print("1. Create a club") # Create a Team now
        print("2. edit a club") # list all customers
        print("3. View Manager") # to go back

    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("Enter your command:")
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
                    c.name = input("Enter the name of the club: ")
                    try:
                        validate_name(c.name)
                        break
                    except NameLengthException:
                        print("name was too long")
                    except:
                        print("some error")
                c.address = input("Enter the club address: ")
                c.phone_number = input("Enter the club phone number: ")
                
                self.logic_wrapper.create_club(c)
            elif command == "2":
                result = self.logic_wrapper.get_all_clubs()
                for elem in result:
                    print(f"name: {elem.name}; address: {elem.address}; phone number: {elem.phone_number};")
            else:
                print("invalid input, try again")
        