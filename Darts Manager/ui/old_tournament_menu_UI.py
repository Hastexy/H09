#from logic.player_logic import Player_Logic
#from model.player import Player
#from ui.player_UI import Player_UI
#from ui.team_UI import Team_UI
from logic.logic_wrapper import Logic_Wrapper

class TournamentMenu_UI:
    def __init__(self):
        self.logic_wrapper = Logic_Wrapper()

    def menu_output(self):
        print("Tournament manager")
        print("\t1. Create Tournament") # Create player
        print("\t2. Create a club")
        print("\t3. create a team/player")
        print("\tr. to return")

    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("\tEnter your command:")
            print()
            command = command.lower()
            if command == "r":
                print("returning")
                break
            elif command == "1":
                pass

            elif command == "2":
                pass

            elif command == "3":
                #menu = Team_UI(self.logic_wrapper)
                #back_method = menu.input_prompt()
                #if back_method == "q":
                    #return "q"
                pass
            else:
                print("invalid input, try again")
            