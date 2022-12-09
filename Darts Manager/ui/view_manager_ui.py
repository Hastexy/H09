from typing import List
from model.team import Team
from model.player import Player

STR_NAME = "NAME"
STR_SSN = "SSN"
STR_EMAIL = "EMAIL"
STR_DOB = "DOB"
STR_PHONE = "PHONE"
STR_HOME_PHONE = "HOME PHONE"
STR_ADDRESS = "ADDRESS"
STR_ROLE = "ROLE"

DELIM = "═" * 51
DELIM_MID = f"╠{'═'*39}╬{'═'*34}╬{'═'*34}╣"
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
                print(TOP)
                print(f"║{'===Viewing Teams and Players===':^109}║")
                print(BOT)
                all_teams = self.logic_wrapper.get_all_league_teams(league_id)
                for idx, team in enumerate(all_teams, 1):
                    self.display_team_and_players(idx, team)

            elif command == "2":
                print(TOP)
                print(f"║{'===Viewing Upcoming Matches===':^109}║")
                print(BOT)
                matches_sorted_by_date = self.logic_wrapper.get_unfinished_matches(
                    league_id
                )
                for date, matches in matches_sorted_by_date.items():
                    self.show_date(date)
                    #print("Games:")
                    for match in matches:
                        # home, away = match
                        # print(f"\t{home} VS {away}")
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
                    #test_delim = "x" * 39
                    #print(header)
                    #print("-" * len(header))
                    for match in matches:
                        self.create_match_table(match)
                      
                        # print(
                        #     f"Game:   {match.home_team.title()} VS {match.away_team.title()}\n"
                        # )
                        # for game in match.games:
                        #     self.parse_leg_score(game)
                        #     print(
                        #         f"{game.home_player.title():<25}{game.home_score:<4}{game.type:^4}{game.away_score}{game.away_player.title():>25}"
                        #     )
                        
            elif command == "4":
                
                #print("\n==Viewing League Standings==\n")
                self.create_league_standings(league_id)

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

    def select_league_id(self, all_leagues: List[object]) -> None:
        while True:
            self.display_available_leagues(all_leagues)
            print("Press 'b' to go back")
            league_id = input("Which league do you want to view (League ID)?: ")
            for league in all_leagues:
                if league_id == str(league.id) or league_id == "b":
                    return league_id

            print("Please select a valid league ID from the list!")

    def create_match_table(self, match) -> str:
        
        print(f"╔{DELIM}╦═════╦{DELIM}╗")
        print(f"║{match.home_team.title():^51}║  V  ║{match.away_team.title():^51}║")
        print(f"╠{DELIML}╬═════╬{DELIMR}╣")
        print(f"║{HOME_TXT:^39}║Leg 1║Leg 2║GAMES║Leg 2║Leg 1║{AWAY_TXT:^39}║")
        print(f"╠{DELIMLP}╬═════╬{DELIMRP}╣")
        for count, game in enumerate(match.games):
            self.parse_leg_score(game)
            home_leg1, home_leg2 = game.home_score.split("-")
            away_leg1, away_leg2 = game.away_score.split("-")
            print(f"║{game.home_player.title():<39}║{home_leg1:^5}║{home_leg2:^5}║{game.type:^5}║{away_leg2:^5}║{away_leg1:^5}║{game.away_player.title():>39}║")

            if count != 11:
                print(f"╠{DELIMLP}╬═════╬{DELIMRP}╣")
            else:
                print(f"╠{DELIMLB}╬═════╬{DELIMRB}╣")
        home_score, away_score = match.result.split("-")
        print(f"║{home_score:^51}║SCORE║{away_score:^51}║")             
        print(f"╚{DELIM}╩═════╩{DELIM}╝")
        
    def show_upcoming_matches(self, match) -> str:
        print(f"╔{DELIM}╦═════╦{DELIM}╗")
        print(f"║{match.home_team.title():^51}║  V  ║{match.away_team.title():^51}║")
        print(f"╚{DELIM}╩═════╩{DELIM}╝")

    def show_date(self, date) -> str:
        print(f"╔{'═'*10}╦{'═'*98}╗")
        print(f"║{'Date':^10}║{date:<98}║")
        print(f"╚{'═'*10}╩{'═'*98}╝")

    def display_team_and_players(self, id, team):
        print(f"╔{'═'*4}╦{'═'*15}╦{'═'*88}╗")
        print(f"║{f'{id}.':^4}║{'TEAM NAME':^15}║ {team.name.title():<87}║")
        print(f"╠{'═'*4}╩{'═'*15}╩{'═'*18}╬{'═'*69}╣")
        print(f"║ {STR_NAME:<38}║xxxxxxxxxxxxxxxxx║")
        #print(f"\n{STR_NAME:<35}{STR_PHONE:<12}{STR_SSN:<15}{STR_ADDRESS:<20}{STR_ROLE:<10}")
        for player in team.players:
            print()
            print(f"║{player.name.title():<35}{player.phone:<12}{player.ssn:<15}{player.address.title():<20}{player.role.title():<10}")
                
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
            game.away_score = "1-0"
        else:
            game.away_score = "1-1"

    def create_league_standings(self, league_id) -> str:
        print(TOP)
        print(f"║{'===Viewing League Standings===':^109}║")
        print(f"╠{'═'*39}╦{'═'*34}╦{'═'*34}╣")
        print(f"║{'TEAM':<39}║{'MATCHES WON':^34}║{'LEGS WON':^34}║")
        teams_sorted_by_wins = self.logic_wrapper.get_team_standings(league_id)
        for team in teams_sorted_by_wins:
            name, matches, legs = team
            #print("-" * 53)
            print(DELIM_MID)
            print(f"║{name.title():<39}║{matches:^34}║{legs:^34}║")
        print(f"╚{'═'*39}╩{'═'*34}╩{'═'*34}╝")

    def show_player_info(self, player) -> str:
        pass