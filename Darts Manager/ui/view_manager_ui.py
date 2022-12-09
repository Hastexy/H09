from typing import List
from model.team import Team
from model.player import Player
from colorama import init, Fore, Style

init()


STR_NAME = "NAME"
STR_SSN = "SSN"
STR_EMAIL = "EMAIL"
STR_DOB = "DOB"
STR_PHONE = "PHONE"
STR_HOME_PHONE = "HOME PHONE"
STR_ADDRESS = "ADDRESS"
STR_ROLE = "ROLE"

DELIM = "═" * 51
DELIM_MID = f"╠{'═'*39}╬{'═'*34}║"
DELIML = "═" * 39 + "╦═════╦═════"
DELIMR = "═════╦═════╦" + "═" * 39
DELIMLP = "═" * 39 + "╬═════╬═════"
DELIMRP = "═════╬═════╬" + "═" * 39
DELIMLB = "═" * 39 + "╩═════╩═════"
DELIMRB = "═════╩═════╩" + "═" * 39
TOP = f"\n╔{'═'*109}╗"
BOT = f"╚{'═'*109}╝\n"
HOME_TXT = "===Home Team==="
AWAY_TXT = "===Away Team==="


class View_Manager_UI:
    def __init__(self, logic_connection) -> None:
        self.logic_wrapper = logic_connection

    def menu_output(self):
        """Prints out the options available from the view manager screen."""
        print(
            """
╔═══╦═══════════════════════╗
║   ║      League Info      ║
╠═══╬═══════════════════════╣
║ 1 ║ View Teams            ║
║ 2 ║ View Upcoming Matches ║
║ 3 ║ View Finished Matches ║
║ 4 ║ View League Standings ║
║ b ║ Back                  ║
║ q ║ Quit                  ║
╚═══╩═══════════════════════╝"""
        )

    def input_prompt(self):
        """This is the main domain for the view manager."""
        all_leagues = self.logic_wrapper.get_all_leagues()
        league_id = self.select_league_id(all_leagues)

        if league_id == "b":
            return

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
                print(f"\n╔{'═'*120}╗")
                print(f"║{'===Viewing Teams and Players===':^120}║")
                print(f"╚{'═'*120}╝\n")
                all_teams = self.logic_wrapper.get_all_league_teams(league_id)
                for idx, team in enumerate(all_teams, 1):
                    self.display_team_and_players(idx, team)

            elif command == "2":
                print(TOP)
                print(f"║{'===Viewing Upcoming Matches===':^109}║")
                print(BOT)
                try:
                    matches_sorted_by_date = self.logic_wrapper.get_unfinished_matches(
                        league_id
                    )
                except FileNotFoundError:
                    print("Something went wrong in the database, please fix!")
                    return

                for date, matches in matches_sorted_by_date.items():
                    self.show_date(date)
                    for match in matches:
                        self.show_upcoming_matches(match)

            elif command == "3":
                print(TOP)
                print(f"║{'===Viewing Matches with Registered Results===':^109}║")
                print(BOT)
                matches_sorted_by_date = self.logic_wrapper.get_finished_matches(
                    league_id
                )
                for date, matches in matches_sorted_by_date.items():
                    self.show_date(date)

                    for match in matches:
                        self.create_match_table(match)

            elif command == "4":

                self.create_league_standings(league_id)

    def display_available_leagues(self, leagues: List[object]) -> None:
        """displays all available leagues."""
        header = f"║ {'List of all registered Leagues':^39} ║"
        separator = "═" * (len(header) - 2)

        print(f"\n╔{separator}╗")
        print(header)
        print(f"╚{separator}╝")

        print(f"╔{'═'*41}╗")
        print(f"║ {'NAME':<38}{'ID':>2}║")
        print(f"╠{'═'*41}╣")
        for league in leagues:
            print(f"║ {league.name.title():<38}{league.id:>2}║")
        print(f"╚{'═'*41}╝")

    def select_league_id(self, all_leagues: List[object]) -> None:
        """Allows the user to choose a league by its id."""
        while True:
            self.display_available_leagues(all_leagues)
            print(
                f"""{Fore.YELLOW}
╔══════════════════════╗
║ Input "b" to go back ║
╚══════════════════════╝\n{Fore.WHITE}"""
            )
            league_id = input("Which league do you want to view (League ID)?: ")
            if league_id == "b":
                return "b"
            for league in all_leagues:
                if league_id == str(league.id):
                    return league_id

            print("Please select a valid league ID from the list!")

    def create_match_table(self, match) -> str:
        """Formats the information of the match into a table."""
        print(f"╔{DELIM}╦═════╦{DELIM}╗")
        print(f"║{match.home_team.title():^51}║  V  ║{match.away_team.title():^51}║")
        print(f"╠{DELIML}╬═════╬{DELIMR}╣")
        print(f"║{HOME_TXT:^39}║Leg 1║Leg 2║GAMES║Leg 2║Leg 1║{AWAY_TXT:^39}║")
        print(f"╠{DELIMLP}╬═════╬{DELIMRP}╣")
        for count, game in enumerate(match.games):
            self.parse_leg_score(game)
            home_leg1, home_leg2 = game.home_score.split("-")
            away_leg1, away_leg2 = game.away_score.split("-")
            print(
                f"║{game.home_player.title():<39}║{home_leg1:^5}║{home_leg2:^5}║{game.type:^5}║{away_leg2:^5}║{away_leg1:^5}║{game.away_player.title():>39}║"
            )

            if count != 11:
                print(f"╠{DELIMLP}╬═════╬{DELIMRP}╣")
            else:
                print(f"╠{DELIMLB}╬═════╬{DELIMRB}╣")
        home_score, away_score = match.result.split("-")
        print(f"║{home_score:^51}║SCORE║{away_score:^51}║")
        print(f"╚{DELIM}╩═════╩{DELIM}╝")

    def show_upcoming_matches(self, match) -> str:
        """Show all matches that have no results."""
        print(f"╔{DELIM}╦═════╦{DELIM}╗")
        print(f"║{match.home_team.title():^51}║  V  ║{match.away_team.title():^51}║")
        print(f"╚{DELIM}╩═════╩{DELIM}╝")

    def show_date(self, date) -> str:
        """Prints the dare of a match."""
        print(f"╔{'═'*10}╦{'═'*98}╗")
        print(f"║{'Date':^10}║{date:<98}║")
        print(f"╚{'═'*10}╩{'═'*98}╝")

    def display_team_and_players(self, id, team):
        """Displays all teams and all players."""
        print(f"\n╔{'═'*4}╦{'═'*15}╦{'═'*99}╗")
        print(f"║{f'{id}.':^4}║{'TEAM NAME':^15}║ {team.name.title():<98}║")
        print(f"╚{'═'*4}╩{'═'*15}╩{'═'*99}╝")

        print(f"\n╔{'═'*39}╦{'═'*14}╦{'═'*39}╦{'═'*14}╦{'═'*10}╗")
        print(
            f"║{STR_NAME:^39}║{STR_SSN:^14}║{STR_EMAIL:^39}║{STR_DOB:^14}║{STR_ROLE:^10}║"
        )
        for player in team.players:
            print(f"╠{'═'*39}╬{'═'*14}╬{'═'*39}╬{'═'*14}╬{'═'*10}╣")
            print(
                f"║ {player.name.title():<38}║{player.ssn:^14}║ {player.email:<38}║{player.dob:^14}║{player.role.upper():^10}║"
            )

        print(f"╚{'═'*39}╩{'═'*14}╩{'═'*39}╩{'═'*14}╩{'═'*10}╝")

    def create_league_standings(self, league_id) -> str:
        """Prints out all teams and how many games and how legs they've won."""
        print(f"\n╔{'═'*74}╗")
        print(f"║{'===Viewing League Standings===':^74}║")
        print(f"╠{'═'*39}╦{'═'*34}╗")
        print(f"║{'TEAM':<39}║{'MATCHES WON':^34}║")
        teams_sorted_by_wins = self.logic_wrapper.get_team_standings(league_id)
        for team in teams_sorted_by_wins:
            name, matches = team
            print(DELIM_MID)
            print(f"║{name.title():<39}║{matches:^34}║")
        print(f"╚{'═'*39}╩{'═'*34}╝")

    def parse_leg_score(self, game: object) -> None:
        if game.home_score == "0":
            game.home_score = "0-0"
        elif game.home_score == "1":
            game.home_score = "1-0"
        else:
            game.home_score = "1-1"

        if game.away_score == "0":
            game.away_score = "0-0"
        elif game.away_score == "1":
            game.away_score = "0-1"
        else:
            game.away_score = "1-1"
