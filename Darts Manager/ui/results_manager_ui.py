from typing import List


class Results_Manager_UI:
    def __init__(self, logic_connection) -> None:
        self.logic_wrapper = logic_connection

    def menu_output(self):
        print(
            """
╔═══╦════════════════════════╗
║   ║    Results Manager     ║
╠═══╬════════════════════════╣
║ 1 ║ Register Match Results ║
║ 2 ║ Change Match Results   ║
║ b ║ Back                   ║
║ q ║ Quit                   ║
╚═══╩════════════════════════╝"""
        )
        # print("\n---Results Manager---")
        # print("1. register match results")
        # print("2. change match results")
        # print("b. back")
        # print("q. quit")

    def input_prompt(self):
        all_leagues = self.logic_wrapper.get_all_leagues()
        league_id = self.select_league_id(all_leagues)

        if league_id == "b":
            return
        while True:
            name = input("What is your name (full name)?: ").strip().lower()
            if name == "b":
                return
            elif self.logic_wrapper.check_host_name(name, league_id):
                print("Komin tenging host :)")
            elif self.logic_wrapper.check_captain_name(name, league_id):
                print("Komin tenging í captain :)")
            else:
                print("Couldn't find that name, try again!")
            break
        # skoða host nafnið hjá þessu tiltekna league
        # fara í gegnum öll liðin sem taka þátt í keppninni og liðsmenn þeirra
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
                print("==Register match result stuff==")
            elif command == "2":
                print("==Change match result stuff==")

    def select_league_id(self, all_leagues: List[object]) -> None:
        while True:
            self.display_available_leagues(all_leagues)
            print("Press 'b' to go back")
            league_id = input(
                "Which league do you want to register results for (League ID)?: "
            )
            for league in all_leagues:
                if league_id == str(league.id) or league_id == "b":
                    return league_id

            print("Please select a valid league ID from the list!")

    def display_available_leagues(self, leagues: List[object]) -> None:
        header = "* Here is a list of all registered leagues: *"
        separator = "*" * len(header)

        print(f"\n{separator}")
        print(header)
        print(f"{separator}\n")

        print(f"{'NAME':<35}{'ID'}")
        print("-" * 38)
        for league in leagues:
            print(f"{league.name.title():<35}{league.id}")
        print("-" * 38)
