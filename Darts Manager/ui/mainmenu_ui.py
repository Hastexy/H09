# from ui.player_UI import Player_UI
# from ui.team_ui import Team_UI
from ui.tournament_manager_ui import Tournament_Manager_UI
from ui.results_manager_ui import Results_Manager_UI
from ui.view_manager import View_Manager_UI
from logic.logic_wrapper import Logic_Wrapper


class MainMenu_UI:
    def __init__(self):
        self.logic_wrapper = Logic_Wrapper()

    def menu_output(self):
        print("""
╔═══╦═══════════════╗
║   ║   Main Menu   ║
╠═══╬═══════════════╣
║ 1 ║ Create Menu   ║
║ 2 ║ Match Manager ║
║ 3 ║ League Info   ║
║ q ║ Quit          ║
╚═══╩═══════════════╝""")


    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("\nEnter your command:")
            command = command.lower()
            if command == "q":
                print("\nGoodbye")
                break
            elif command == "1":
                # print("\n===TOURNAMENT MANAGER====")
                verify_user = input("\nAre you a tournament host? (y/n): ")
                if verify_user == "y":
                    menu = Tournament_Manager_UI(self.logic_wrapper)
                    back_method = menu.input_promt()
                    if back_method == "q":
                        return "q"
                elif verify_user == "n":
                    print("\nReturning you to main menu")
                else:
                    print("\nInvalid input, try again")
            elif command == "2":
                menu = Results_Manager_UI(self.logic_wrapper)
                back_method = menu.input_prompt()
                if back_method == "q":
                    return "q"
                #print("\n===RESULTS MANAGER===")   Implement RM Menu Later
            elif command == "3":
                # print("\n===VIEW MANAGER===")
                menu = View_Manager_UI(self.logic_wrapper)
                back_method = menu.input_prompt()
                if back_method == "q":
                    return "q"
            else:
                print("\ninvalid input, try again")
