from itertools import combinations
import math
import random
from typing import List
from model.club import Club
from model.team import Team
from model.player import Player
from model.league import League
from ui.input_validators import *
from datetime import datetime, time, date, timedelta
from colorama import init, Fore, Style, Back

init()
# Colorama options
# Fore = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
# Style = [DIM, NORMAL, BRIGHT]


class Tournament_Manager_UI:
    def __init__(self, data_connection) -> None:

        self.logic_wrapper = data_connection
        self.clubs = ["test", "Dart Vader"]

    def menu_output(self):

        print(
            """
╔═══╦═══════════════╗
║   ║  Create Menu  ║
╠═══╬═══════════════╣
║ 1 ║ Create Club   ║
║ 2 ║ Create Team   ║
║ 3 ║ Create Player ║
║ 4 ║ Create League ║
║ b ║ Back          ║
║ q ║ Quit          ║
╚═══╩═══════════════╝"""
        )

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
                print(CANCEL)
                self.create_team()
            elif command == "3":
                print(CANCEL)
                self.create_player()
            elif command == "4":
                print(CANCEL)
                self.create_league()
            else:
                print("\nInvalid input, try again")

    def display_available_players(self) -> list:
        """Displays all players who are both registered in the database and do not belong to a team."""
        header = f"║ {'List of all available players':^63} ║"
        separator = "═" * (len(header) - 2)

        print(f"\n╔{separator}╗")
        print(header)
        print(f"╠{separator}╣")

        # print(f"╔{'═'*65}╗")
        print(f"║{'NAME':<38}{'SocialSecurityNumber':<25}{'ID':>2}║")
        print(f"╠{'═'*65}╣")
        all_players = self.logic_wrapper.get_all_players()
        for player in all_players:
            print(f"║{player.name.title():<38}{player.ssn:<25}{player.id:>2}║")
        print(f"╚{'═'*65}╝")

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
            f"""{Fore.GREEN}
╔══════════════╗
║ CLUB CREATED ║
╚══════════════╝{Fore.WHITE}"""
        )

    def create_team(self) -> None:
        if not self.logic_wrapper.check_for_clubs():

            print(
                "No clubs exist in the database. A team must belong to a club so you must first create one, and then you can create a team."
            )
            return
        t = Team()
        t.id = self.logic_wrapper.get_new_team_id()

        all_clubs = self.display_all_clubs()
        club_assigned = False
        while True:

            club_ID = input(
                "\nWhich club does the new team belong to? (club ID): "
            ).lower()

            if club_ID == "b":
                print(CANCEL2)
                return

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
            if t.name == "b":
                return

            try:
                validate_team_name(t.name)
                break
            except NameLengthException:
                print("\n##The name must be between 3 or 39 characters long!##")
            except:
                print("\n##Unknown Error Occured, try again##")

        # header = f"║ Every team must have at least 4 players, one of whom is the team captain ║"
        header = f"║ {'Every team must have 4 players minimum':<63} ║"
        separator = "═" * (len(header) - 2)

        print(f"\n╔{separator}╗")
        print(header)
        print(f"║ {'Start by picking the team captain':<63} ║")
        print(f"╚{separator}╝")

        # print("---Let's start by picking the team captain---")

        captain_assigned = False
        all_players = self.display_available_players()

        while True:
            player_ID = input("\nYour choice (Player ID): ")

            if player_ID == "b":
                print(CANCEL2)
                return

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

        print("---Now we need to add the rest of the players (at least THREE more)---")
        print("Press 'q' to stop adding players to the team.")

        while True:
            self.display_available_players()
            player_ID = input("\nYour choice (Player ID): ")

            if player_ID == "q":
                break

            if player_ID == "b":
                return

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

        self.logic_wrapper.create_team(t)
        print(
            f"""{Fore.GREEN}
╔══════════════╗
║ TEAM CREATED ║
╚══════════════╝{Fore.WHITE}"""
        )

    def create_league(self) -> None:
        l = League()
        l.id = self.logic_wrapper.get_new_league_id()
        while True:
            l.name = input("\nEnter the name of your league: ")

            if l.name == "b":
                return

            try:
                validate_league_name(l.name)
                break
            except:
                print(
                    f"""{Fore.RED}
╔══════════════════════════════════════════════════════════════════════╗
║ Name taken! Another league already has this name, choose another one ║
╚══════════════════════════════════════════════════════════════════════╝{Fore.WHITE}"""
                )

        while True:
            l.host = input("\nEnter the host name of your league: ").strip().lower()

            if l.host == "b":
                return

            try:
                validate_player_name(l.host)
                break
            except NameLengthException:
                print(ERR_LENGTH)
            except InvalidNameError:
                print(ERR_DIGIT)
            except:
                print(ERR_UNKNOWN)

        while True:
            l.phone = input("\nHost's phonenumber: ")

            if l.phone == "b":
                return
            try:
                validate_number(l.phone)
                break
            except InvalidNumberLengthException:
                print(ERR_PHONE)
            except InvalidNumberCharacterException:
                print(ERR_DIGIT)

        # Get a list of all the teams participating!!
        # print("\nRegister Teams In The League (At Least TWO Teams):")
        print(
            f"""{Fore.YELLOW}
╔═════════════════════════════════════════╗
║ Register at least TWO teams in a league ║
╚═════════════════════════════════════════╝{Fore.WHITE}"""
        )
        all_teams = self.logic_wrapper.get_all_teams()
        while True:
            self.display_available_teams(all_teams)
            print(
                f"""{Fore.YELLOW}
╔═════════════════════════════════════════╗
║   Press "q" to stop registering teams   ║
╚═════════════════════════════════════════╝{Fore.WHITE}"""
            )
            next_team_id = input("\nRegister Next Team (Team ID): ")

            if next_team_id == "b":
                return

            if next_team_id == "q" and len(l.teams) >= 2:
                break
            else:
                # print("\nYou must register at least TWO teams in a league")
                print(
                    f"""{Fore.YELLOW}
╔═════════════════════════════════════════╗
║ Register at least TWO teams in a league ║
╚═════════════════════════════════════════╝{Fore.WHITE}"""
                )

            for team in all_teams:
                if next_team_id == team.id:
                    all_teams.remove(team)
                    l.teams.append(team)
                    print(
                        f"""{Fore.GREEN}
╔═════════════════════╗
║   Team Registered   ║
╚═════════════════════╝{Fore.WHITE}"""
                    )
                    break
            else:
                print(
                    f"""{Fore.YELLOW}
╔═════════════════════════════════════════╗
║   Please select a team from the list!   ║
╚═════════════════════════════════════════╝{Fore.WHITE}"""
                )

        if len(l.teams) % 2 == 1:
            l.rounds = len(l.teams)
        else:
            l.rounds = len(l.teams) - 1

        while True:
            start_date = input(
                "\nPlease enter the starting date of the league in this format (dd/mm/yyyy hh:mm): "
            )
            try:
                start_date = datetime.strptime(start_date, "%d/%m/%Y %H:%M")
                break
            except ValueError:
                print("\nPlease enter the date like the format shows!")

        # l.round_dates.append(start_date.strftime("%d/%m/%Y %H:%M"))

        interval = int(input("\nHow many days between rounds?: "))
        tdelta = timedelta(days=interval)

        matches_per_round = math.floor(len(l.teams) / 2)
        # búa til nýja orðabók, lyklar: date, value: lista af x matches, x = floor(len(l.teams) / 2)
        next_date = start_date
        all_matches = list(combinations(l.teams, 2))
        all_dates = []

        for _ in range(l.rounds):
            correct_formatted_date = next_date.strftime("%d/%m/%Y %H:%M")
            all_dates.append(correct_formatted_date)
            l.matches[correct_formatted_date] = []

            for _ in range(matches_per_round):
                next_team = random.choice(all_matches)
                l.matches[correct_formatted_date].append(next_team)
                all_matches.remove(next_team)

            next_date += tdelta

            # l.round_dates.append(next_date.strftime("%d/%m/%Y %H:%M"))

        if len(all_dates) > 1:
            l.start_date = all_dates[0]
            l.end_date = all_dates[-1]
        else:
            l.start_date = l.end_date = all_dates[0]

        self.logic_wrapper.create_league(l)
        print(
            f"""{Fore.GREEN}
╔════════════════╗
║ LEAGUE CREATED ║
╚════════════════╝{Fore.WHITE}"""
        )

    def create_player(self) -> None:
        p = Player()
        p.id = self.logic_wrapper.get_new_player_id()

        while True:
            p.name = input("\nEnter the name of the player: ")
            if p.name == "b":
                print(CANCEL2)
                return "b"
            else:
                try:
                    validate_player_name(p.name)
                    break
                except NameLengthException:
                    print(ERR_LENGTH)
                except InvalidNameError:
                    print(ERR_DIGIT)
                except:
                    print(ERR_UNKNOWN)
        while True:
            p.ssn = input("\nEnter the social security number of the player: ")
            if p.ssn == "b":
                print(CANCEL2)
                return "b"
            else:
                try:
                    validate_ssn(p.ssn)
                    break
                except InvalidNumberLengthException:
                    print(ERR_SSN)
                except InvalidNumberCharacterException:
                    print(ERR_DIGIT)
                except:
                    print(ERR_UNKNOWN)
        while True:
            p.email = input("\nEnter the email of the player: ")
            if p.email == "b":
                print(CANCEL2)
                return "b"
            else:
                try:
                    validate_email(p.email)
                    break
                except NoAsperandSymbolException:
                    print(ERR_NO_ASP)
                except TooManyAsperandSymbolException:
                    print(ERR_MANY_ASP)
                except NothingBeforeAsperandException:
                    print(ERR_BEFORE_ASP)
                except NothingAfterAsperandException:
                    print(ERR_AFTER_ASP)
                except NoDotBeforeAsperandException:
                    print(ERR_DOT_ASP)
                except NoDotAtStartException:
                    print(ERR_DOT_START)
                except ConsecutiveDotsException:
                    print(ERR_CONSECUTIVE_DOT)
                except MissingDomainNameException:
                    print(ERR_DOMAIN_MISSING)
                except:
                    print(ERR_UNKNOWN)
        while True:
            p.dob = input(
                "\nEnter the date of birth for the player in this format dd/mm/yyyy: "
            )
            try:
                validate_dob(p.dob)
                break
            except NameLengthException:
                print(ERR_DOB_FORMAT)
            except InvalidNumberCharacterException:
                print(ERR_DOB_FORMAT)
            except:
                print(ERR_UNKNOWN)
        print(SKIP)
        while True:
            p.phone = input("\n(OPTIONAL)Enter the players phone number: ")
            if p.phone == "b":
                print(CANCEL2)
                return "b"
            elif p.phone == "":
                break
            else:
                try:
                    validate_number(p.phone)
                    break
                except InvalidNumberLengthException:
                    print(ERR_PHONE)
                except InvalidNumberCharacterException:
                    print(ERR_DIGIT)
                except:
                    print(ERR_UNKNOWN)
        while True:
            p.home_phone = input("\n(OPTIONAL)Enter the players home-phone number: ")
            if p.home_phone == "b":
                print(CANCEL2)
                return "b"
            elif p.home_phone == "":
                break
            else:
                try:
                    validate_number(p.home_phone)
                    break
                except InvalidNumberLengthException:
                    print(ERR_PHONE)
                except InvalidNumberCharacterException:
                    print(ERR_DIGIT)
                except:
                    print(ERR_UNKNOWN)

        while True:
            p.address = input("\n(Optional)Enter the Address of the player: ")
            if p.address == "b":
                print(CANCEL2)
                return "b"
            elif p.address == "":
                break
            else:
                try:
                    validate_club_length(p.address)
                    break
                except NameLengthException:
                    print(ERR_LENGTH)
                except:
                    print(ERR_UNKNOWN)
        print(
            f"""{Fore.GREEN}
╔════════════════╗
║ PLAYER CREATED ║
╚════════════════╝{Fore.WHITE}"""
        )
        self.logic_wrapper.create_player(p)

    def display_available_teams(self, teams: List[object]) -> None:

        header = f"║ {'Here is a list of all available teams':^39} ║"
        separator = "═" * (len(header) - 2)

        print(f"\n╔{separator}╗")
        print(header)
        print(f"╠{separator}╣")

        # print(f"╔{'═'*41}╗")
        print(f"║ {'NAME':<38}{'ID':>2}║")
        print(f"╠{'═'*41}╣")
        for team in teams:
            print(f"║ {team.name.title():<38}{team.id:>2}║")
        print(f"╚{'═'*41}╝")
