from typing import List
from logic.player_logic import Player_Logic
from logic.team_logic import Team_Logic
from data.data_wrapper import Data_Wrapper
from logic.club_logic import Club_Logic
from logic.league_logic import League_Logic


class Logic_Wrapper:
    def __init__(self):
        self.data_wrapper = Data_Wrapper()
        self.player_logic = Player_Logic(self.data_wrapper)
        self.team_logic = Team_Logic(self.data_wrapper)
        self.club_logic = Club_Logic(self.data_wrapper)
        self.league_logic = League_Logic(self.data_wrapper)

    def create_player(self, player: object) -> None:
        self.player_logic.create_player(player)

    def create_team(self, team: object) -> None:
        self.team_logic.create_team(team)

    def create_club(self, club: object) -> None:
        self.club_logic.create_club(club)

    def create_league(self, league: object) -> None:
        self.league_logic.create_league(league)

    def get_new_club_id(self) -> int:
        return self.club_logic.get_new_club_id()

    def get_new_team_id(self) -> int:
        return self.team_logic.get_new_team_id()

    def get_new_player_id(self) -> int:
        return self.player_logic.get_new_player_id()

    def get_new_league_id(self) -> int:
        return self.league_logic.get_new_league_id()

    def get_new_match_id(self) -> int:
        return self.league_logic.get_new_match_id()

    def get_all_clubs(self) -> List[object]:
        return self.club_logic.get_all_clubs()

    def get_all_teams(self) -> List[object]:
        return self.team_logic.get_all_teams()

    def get_all_players(self) -> List[object]:
        return self.player_logic.get_all_players()

    def get_unfinished_matches(self, league_id: str) -> List[object]:
        return self.league_logic.get_unfinished_matches(league_id)

    def get_finished_matces(self, league_id: str) -> List[object]:
        return self.league_logic.get_finished_matches(league_id)

    def check_for_clubs(self) -> bool:
        return self.club_logic.check_for_clubs()

    def update_player_status(self, player_id: str, role: str, team_id: str) -> None:
        self.player_logic.update_player_status(player_id, role, team_id)

    def generate_schedule(self, all_teams: List[object], league_ID: str) -> None:
        self.league_logic.generate_schedule(all_teams, league_ID)

    def get_all_league_teams(self, league_id: str) -> List[object]:
        return self.league_logic.get_all_league_teams(league_id)

    def get_all_leagues(self) -> None:
        return self.league_logic.get_all_leagues()
