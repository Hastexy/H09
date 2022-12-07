from model.club import Club
from model.team import Team
from model.player import Player
from model.league import League
from ui.input_validators import *


class Tournament_Manager_UI:
    def __init__(self, data_connection) -> None:
        self.logic_wrapper = data_connection
        self.clubs = ["test", "Dart Vader"]

    def menu_output(self):
        print(
            """
╔═══╦════════════════════╗
║   ║ Tournament Manager ║
╠═══╬════════════════════╣
║ 1 ║ Create Club        ║
║ 2 ║ Create Team        ║
║ 3 ║ Create Player      ║
║ 4 ║ Create League      ║
║ b ║ Back               ║
║ q ║ Quit               ║
╚═══╩════════════════════╝"""
        )
        # print("\n---Tournament Manager---")
        # print("1. create club")
        # print("2. create team")
        # print("3. create player")
        # print("4. create tourney")
        # print("b. back")
        # print("q. quit")

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
                print(CANCEL)
                self.create_club()
            elif command == "2":
                print(self.logic_wrapper.check_for_clubs())
                if not self.logic_wrapper.check_for_clubs():
                    print(
                        "No clubs exist in the database. A team must belong to a club so you must first create one, and then you can create a team."
                    )
                    return "b"
                t = Team()
                t.id = self.logic_wrapper.get_new_team_id()

                all_clubs = self.display_all_clubs()
                club_assigned = False
                while True:

                    club_ID = input(
                        "\nWhich club does the new team belong to? (club ID): "
                    ).lower()

                    for club in all_clubs:
                        if club_ID == club.id:
                            t.club = club_ID
                            club_assigned = True
                            break

                    if club_assigned:
                        break

                    print("Please choose one of the club ID's from the list.")

                while True:
                    t.name = input("\nEnter the name of the new team: ")
                    try:
                        validate_team_name(t.name)
                        break
                    except NameLengthException:
                        print("\n##The name must be between 3 or 49 characters long!##")
                    except:
                        print("\n##Unknown Error Occured, try again##")

                header = "* Remember, every team must have at least FOUR players, one of whom is the team captain. *"
                separator = "*" * len(header)

                print(f"\n{separator}")
                print(header)
                print(f"{separator}\n")

                print("---Let's start by picking the team captain---")

                captain_assigned = False
                all_players = self.display_available_players()

                while True:
                    player_ID = input("\nYour choice (Player ID): ")

                    for player in all_players:
                        if player_ID == player.id:
                            player.role = "captain"
                            player.team = str(t.id)
                            self.logic_wrapper.update_player_status(
                                player_ID, "captain", str(t.id)
                            )
                            t.players.append(player)
                            captain_assigned = True
                            break

                    if captain_assigned:
                        break

                    print("Invalid player ID!")

                print(
                    "---Now we need to add the rest of the players (at least THREE more)---"
                )
                print("Press 'q' to stop adding players to the team.")

                self.display_available_players()
                player_ID = input("\nYour choice (Player ID): ")
                while player_ID != "q" or len(t.players) < 4:

                    for player in all_players:
                        if player_ID == player.id:
                            player.role = "player"
                            player.team = str(t.id)
                            self.logic_wrapper.update_player_status(
                                player_ID, "player", str(t.id)
                            )
                            t.players.append(player)
                            break
                    else:
                        print("Invalid player ID!")

                    self.display_available_players()
                    player_ID = input("\nYour choice (Player ID): ")

                self.logic_wrapper.create_team(t)
                print("\n==Team Created==")
            elif command == "3":
                p = Player()
                p.id = self.logic_wrapper.get_new_player_id()

                while True:
                    p.name = input("\nEnter the name of the player: ").lower().strip()
                    try:
                        validate_player_name(p.name)
                        break
                    except NameLengthException:
                        print("\n##Name is too long##")
                    except InvalidNameError:
                        print("\n##Name cannot contain digits!##")
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
                # print("\n==League Created==")
                l = League()
                # l.id = self.logic_wrapper.get_id() vantar að geta náð id
                while True:
                    l.name = input("\nEnter the name of your league: ")
                    break
                while True:
                    l.host = input("\nEnter the host name of your league: ")
                    break
                while True:
                    l.phone = input("\nEnter the phone nr. of your league: ")
                    break
                while True:
                    l.start_date = input(
                        "\nEnter the starting date of your league (with this format: xx.xx.xxxx): "
                    )
                    break
                while True:
                    l.end_date = input(
                        "\nEnter the ending date of your league (If it is a one day league enter the same date): "
                    )
                    break
                while True:
                    l.teams = input(
                        "\nEnter the amount of teams competing in your league: "
                    )
                    print("===teams picked===")
                    break
                while True:  # spurning hvort það megi bara vera ein umferð per dag?...
                    l.matches = input("\nEnter the amount of rounds per day: ")
                    break

                print("---Testing---")
                print(l)

                pass
            else:
                print("\nInvalid input, try again")

    def display_available_players(self) -> list:
        """Displays all players who are both registered in the database and do not belong to a team."""
        header = "* Here is a list of all available players: *"
        separator = "*" * len(header)

        print(f"\n{separator}")
        print(header)
        print(f"{separator}\n")

        print(f"{'NAME':<35}{'SocialSecurityNumber':<25}{'ID'}")
        print("-" * 64)
        all_players = self.logic_wrapper.get_all_players()
        for player in all_players:
            print(f"{player.name.title():<35}{player.ssn:<25}{player.id}")
        print("-" * 64)

        return all_players

    def display_all_clubs(self) -> list:
        """Displays all clubs registered in the system."""

        print("\n##### Every team must belong to a club. #####")

        header = "* Here is a list of all the clubs registered in the system: *"
        separator = "*" * len(header)

        print(f"\n{separator}")
        print(header)
        print(f"{separator}\n")

        print(f"{'NAME':<35}{'Address':<25}{'ID'}")
        print("-" * 64)
        all_clubs = self.logic_wrapper.get_all_clubs()
        for club in all_clubs:
            print(f"{club.name.title():<35}{club.address:<25}{club.id}")
        print("-" * 64)

        return all_clubs

    def create_club(self) -> None:
        c = Club()
        c.id = self.logic_wrapper.get_new_club_id()

        while True:
            c.name = input("\nEnter the name of your club: ")
            if c.name == "b":
                print(CANCEL2)
                return "b"
            else:
                try:
                    validate_club_length(c.name)
                    break
                except NameLengthException:
                    print(ERR_LENGTH)
                except:
                    print(ERR_UNKNOWN)

        while True:
            c.address = input("\nEnter the address of your club: ")
            if c.address == "b":
                print(CANCEL2)
                return "b"
            else:
                try:
                    validate_club_length(c.address)
                    break
                except NameLengthException:
                    print(ERR_LENGTH)
                except:
                    print(ERR_UNKNOWN)

        while True:
            c.phone_number = input("\nEnter the club phone number: ")
            if c.phone_number == "b":
                print(CANCEL2)
                return "b"
            else:
                try:
                    validate_number(c.phone_number)
                    break
                except InvalidNumberLengthException:
                    print(ERR_PHONE)
                except InvalidNumberCharacterException:
                    print(ERR_DIGIT)
                except:
                    print(ERR_UNKNOWN)

        self.logic_wrapper.create_club(c)
        print(
            """
╔══════════════╗
║ CLUB CREATED ║
╚══════════════╝"""
        )
