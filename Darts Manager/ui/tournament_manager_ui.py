from model.club import Club
from model.team import Team
from model.player import Player
from model.tourney import Tourney
from ui.input_validators import *


class Tournament_Manager_UI:
    def __init__(self, data_connection) -> None:
        self.logic_wrapper = data_connection
        self.clubs = ["test", "Dart Vader"]

    def menu_output(self):
        print("\n---Tournament Manager---")
        print("1. create club")
        print("2. create team")
        print("3. create player")
        print("4. create tourney")
        print("b. back")
        print("q. quit")

    def input_promt(self):
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
                c = Club()
                c.id = self.logic_wrapper.get_new_club_id()

                while True:
                    c.name = input("\nEnter the name of your club: ")
                    try:
                        validate_club_name(c.name)
                        break
                    except NameLengthException:
                        print("\n##The name must be between 3 or 49 characters long!##")
                    except:
                        print("\n##Unknown Error Occured, try again##")
                while True:
                    c.address = input("\nEnter the address of your club: ")
                    break
                while True:
                    c.phone_number = input("\nEnter the club phone number: ")
                    try:
                        validate_number(c.phone_number)
                        break
                    except InvalidNumberLengthException:
                        print("\n##Phone number must be 7 digits long##")
                    except InvalidNumberCharacterException:
                        print("\n##Phone number must only consist of digits##")
                    except:
                        print("\n##Unknown Error Occured, try again##")
                self.logic_wrapper.create_club(c)
                print("\n==Club Created==")
            elif command == "2":
                # fyrst skoða hvort clubs séu til
                if not self.logic_wrapper.check_for_clubs():
                    print(
                        "No clubs exist in the database. A team must belong to a club so it is recommended you first create club/s and then create a team."
                    )
                    break
                t = Team()
                # t.id = self.logic_wrapper.get_new_team_id()

                # biðja um almennar upplýsingar um liðið
                print("\n##### Every team must belong to a club. #####")
                while True:
                    header = "* Here is a list of names for every registered club in the system:"
                    separator = "*" * len(header)

                    print(f"\n{separator}")
                    print(header)
                    print(f"{separator}\n")

                    all_clubs_names = self.logic_wrapper.get_all_club_names()
                    for name in all_clubs_names:
                        print(f" - {name.capitalize()}")

                    header = "*Press 'b' to go back to the menu screen.*"
                    separator = "*" * len(header)

                    print(f"\n{separator}")
                    print(header)
                    print(f"{separator}")

                    club_name = input(
                        "\nWhich club does the new team belong to (full name)?: "
                    ).lower()
                    if club_name == "b":
                        break
                    elif self.logic_wrapper.club_exists(t.club):
                        break
                    print("This club does not exist, please try another one.")

                header = "*Remeber, every team MUST have at least four players, one of whom is the team captain.*"
                separator = "*" * len(header)

                print(f"\n{separator}")
                print(header)
                print(f"{separator}")
                while True:
                    t.name = input("\nEnter the name of the new team: ")
                    try:
                        validate_team_name(t.name)
                        break
                    except NameLengthException:
                        print("\n##The name must be between 3 or 49 characters long!##")
                    except:
                        print("\n##Unknown Error Occured, try again##")

                # biðja um team_captain
                # - add existing player
                # - create new player
                # breyta role á gefnum player í player.role = "captain"

                while True:
                    team_captain = input("Who is the team captain?:")

                    break

                while True:
                    # Players
                    player_list = []
                    player_input = ""
                    while True:
                        player_input = input("Enter a player name: ")
                        if player_input == "q":
                            break
                        else:
                            player_list.append(player_input)
                    t.players = player_list
                    break

                # print("\n==Player Created==")
                # self.logic_wrapper.create_player(p)

                # fylla liðið af players (liðsmenn >= 4)
                # - add existing player
                # - create new player

                # breyta status fyrir hvern og einn player í listanum:
                #   - player.team = team_ID
                #   - player.role = captain/player

                # búa til nýja skrá sem heitir: teamID.csv og skrifa persónupplýsngar spilarana þar inn

                # print("\n==Team Created==")
            elif command == "3":
                p = Player()
                p.id = self.logic_wrapper.get_new_player_id()

                while True:
                    p.name = input("\nEnter the name of the player: ")
                    try:
                        validate_player_name(p.name)
                        break
                    except NameLengthException:
                        print("\n##Name is too long##")
                    except:
                        print("\n##Unknown Error Occured, try again##")
                while True:
                    p.ssn = input("\nEnter the social security number of the player: ")
                    try:
                        validate_ssn(p.ssn)
                        break
                    except InvalidNumberLengthException:
                        print("\n##SSN number bust be 10 digits long##")
                    except InvalidNumberCharacterException:
                        print("\n##SSN must only consist of digits##")
                    except:
                        print("\n##Unknown Error Occured, try again##")
                while True:
                    p.email = input("\nEnter the email of the player: ")
                    try:
                        validate_email(p.email)
                        break
                    except NoAsperandSymbolException:
                        print("\n##There needs to be an @ in the email##")
                    except:
                        print("\n##Unknown Error Occured, try again##")
                while True:
                    p.dob = input(
                        "\nEnter the date of birth of the player in this format(dd.mm.yyyy): "
                    )
                    try:
                        validate_dob(p.dob)
                        break
                    except NameLengthException:
                        print("\n##The format is only 10 letters, try again##")
                    except InvalidNumberCharacterException:
                        print("\n##There must be a dot between day, month and year##")

                p.phone = input("\n(Optional)Enter the GSM-Phone of the player: ")
                p.home_phone = input("\n(Optional)Enter the Home-Phone of the player: ")
                p.address = input("\n(Optional)Enter the Address of the player: ")
                # print("\n==Player Created==")
                self.logic_wrapper.create_player(p)
            elif command == "4":
                # print("\n==Tourney Created==")
                pass
            else:
                print("\nInvalid input, try again")
