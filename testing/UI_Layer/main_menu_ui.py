from Logic_Layer.player_ll import PlayerLL
from Models.player import Player
from UI_Layer.playerui import PlayerUI

from Logic_Layer.logic_wrapper import Logic_Wrapper


class MainMenu_UI:
    def __init__(self):
        self.logic_wrapper = Logic_Wrapper()

    def menu_output(self):
        print("main menu")
        print(
            "1. Tournament manager"
        )  # Create - Leage/Tournament, Club, Team, Player, matches.
        print("2. Result manager")  # next menu - 1. register, 2. edit
        print(
            "3. View manager"
        )  # Team info, Unplayed matches, Complete results, LeaderBoards.

    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("Enter your command:")
            command = command.lower()
            if command == "q":
                print("Goodbye")
                break
            elif command == "1":
                menu = PlayerUI(self.logic_wrapper)
                back_method = menu.input_prompt()
                if back_method == "q":
                    return "q"
            elif command == "2":
                pass
            else:
                print("invalid input, try again")
