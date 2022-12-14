from ui.tournament_manager_ui import Tournament_Manager_UI
from ui.results_manager_ui import Results_Manager_UI
from ui.view_manager_ui import View_Manager_UI
from logic.logic_wrapper import Logic_Wrapper


class MainMenu_UI:
    def __init__(self):
        self.logic_wrapper = Logic_Wrapper()

    def menu_output(self):
        """Displays all inputs available from the main menu screen."""
        print(
            """
╔═══╦═══════════════╗
║   ║   Main Menu   ║
╠═══╬═══════════════╣
║ 1 ║ Create Menu   ║
║ 2 ║ Match Manager ║
║ 3 ║ League Info   ║
║ q ║ Quit          ║
╚═══╩═══════════════╝"""
        )

    def input_prompt(self):
        """This is the main domain for the main menu."""
        while True:
            self.menu_output()
            command = input("\nEnter your command: ")
            command = command.lower()
            if command == "q":
                print("\nGoodbye")
                break
            elif command == "1":
                verify_user = (
                    input("\nAre you a tournament host? (y/n): ").strip().lower()
                )
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
            elif command == "3":
                menu = View_Manager_UI(self.logic_wrapper)
                back_method = menu.input_prompt()
                if back_method == "q":
                    return "q"
            else:
                print("\ninvalid input, try again")
