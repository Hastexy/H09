from logic.player_logic import Player_Logic
from model.player import Player
from ui.player_UI import Player_UI
from ui.team_UI import Team_UI
from ui.tournament_menu_UI import TournamentMenu_UI
from logic.logic_wrapper import Logic_Wrapper

class MainMenu_UI:
    def __init__(self):
        self.logic_wrapper = Logic_Wrapper()

    def menu_output(self):
        print("Main Menu")
        print("\t1. Tournament manager") # Create player
        print("\t2. Results manager")
        print("\t3. View manager")
        print("\tq. to exit")

    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("\tEnter your command:")
            print()
            command = command.lower()
            if command == "q":
                print("Goodbye")
                break
            elif command == "1":
                menu = TournamentMenu_UI()
                back_method = menu.input_prompt()
                if back_method == "q":
                    return "q"
            elif command == "2":
                menu = Team_UI(self.logic_wrapper)
                back_method = menu.input_prompt()
                if back_method == "q":
                    return "q"
                pass
            else:
                print("invalid input, try again")
            