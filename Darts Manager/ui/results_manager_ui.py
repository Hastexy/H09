from typing import List


class Results_Manager_UI:
    def __init__(self, logic_connection) -> None:
        self.logic_wrapper = logic_connection

    def menu_output(self):
        print(
            """
╔═══╦════════════════════════╗
║   ║     Match Manager      ║
╠═══╬════════════════════════╣
║ 1 ║ Register Match Results ║
║ 2 ║ Change Match Results   ║
║ b ║ Back                   ║
║ q ║ Quit                   ║
╚═══╩════════════════════════╝"""
        )

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
                # þarf að sækja allar kláraðar viðureignir í league-inu:
                all_finished_matches = self.logic_wrapper.get_finished_matches(
                    league_id
                )

                while True:
                    print("1. Change Match Result")
                    print("2. Change Match Date")
                    print("b. Back")

                    command = input("Enter your choice: ").strip().lower()
                    if command == "b":
                        return
                    elif command == "1":
                        self.display_finished_matches(all_finished_matches)
                        self.change_match_results(all_finished_matches)
                    elif command == "2":
                        self.display_finished_matches(all_finished_matches)
                        self.change_match_date(all_finished_matches, league_id)
                    else:
                        print("Invalid input!")

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

    def display_finished_matches(self, all_matches: dict) -> None:
        pass
        header = "* Here is a list of all finished matches: *"
        separator = "*" * len(header)

        print(f"\n{separator}")
        print(header)
        print(f"{separator}\n")

        for date, matches in all_matches.items():
            header = f"#### Date: {date}"
            print(header)
            print("-" * len(header))
            for match in matches:
                print(
                    f"Game:\t{match.home_team.title()} VS {match.away_team.title():<15}ID: {match.id}\n"
                )

    def change_match_date(self, all_matches: dict) -> None:
        match_id = input("Select a match to change (match ID): ")

    def change_match_results(self, all_matches: dict) -> None:
        while True:
            print("Press 'b' to go back")
            match_id = input("Select a match to change (match ID): ")
            if match_id == "b":
                return
            for matches in all_matches.values():
                for match in matches:
                    if str(match.id) == match_id:

                        self.logic_wrapper.update_match_results(match)
                        return
            print("Please select one of the matches from the list!")
