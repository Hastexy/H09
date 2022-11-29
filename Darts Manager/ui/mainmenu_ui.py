#from logic.player_logic import Player_Logic
#from model.player import Player
#from ui.player_UI import Player_UI
#from ui.team_ui import Team_UI
#from ui.tournament_menu_UI import TournamentMenu_UI
from ui.tm_verification_ui import Tournament_Manager_Verification_UI
from logic.logic_wrapper import Logic_Wrapper

class MainMenu_UI:
    def __init__(self):
        self.logic_wrapper = Logic_Wrapper()

    def menu_output(self):
        print("\n---Main Menu---")
        print("1. Tournament manager") # Create player
        print("2. Results manager")
        print("3. View manager")
        print("q. to exit")

    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("\nEnter your command:")
            command = command.lower()
            if command == "q":
                print("\nGoodbye")
                break
            elif command == "1":
                #print("\n===TOURNAMENT MANAGER===")
                menu = Tournament_Manager_Verification_UI()
                back_method = menu.input_prompt()
                if back_method == "q":
                    return "q"
                #menu = TournamentMenu_UI()
                #back_method = menu.input_prompt()
                #if back_method == "q":
                    #return "q"
            elif command == "2":
                print("\n===RESULTS MANAGER===")    #Implement RM Menu
                #menu = Team_UI(self.logic_wrapper)
                #back_method = menu.input_prompt()
                #if back_method == "q":
                    #return "q"
            elif command == "3":
                print("\n===VIEW MANAGER===")       #Implement VM Menu
            else:
                print("\ninvalid input, try again")
            