from data.player_data import Player_Data
from data.team_data import Team_Data
from data.club_data import Club_Data
from data.league_data import League_Data

from typing import List


class Data_Wrapper:
    def __init__(self):
        self.club_data = Club_Data()
        self.team_data = Team_Data()
        self.player_data = Player_Data()
        self.league_data = League_Data()

    def get_all_players(self) -> List[object]:
        return self.player_data.read_all_players()

    def create_league(self, league: object) -> None:
        self.league_data.create_league(league)

    def create_player(self, player: object) -> None:
        self.player_data.create_player(player)

    def get_new_player_id(self) -> int:
        return self.player_data.get_new_player_id()

    def get_new_league_id(self) -> int:
        return self.league_data.get_new_league_id()

    def update_player_status(self, player_id: str, role: str, team_id: str) -> None:
        self.player_data.update_player_status(player_id, role, team_id)

    def get_all_teams(self, league_id: str = "") -> List[object]:
        if league_id:
            return self.league_data.get_all_teams()
        return self.team_data.read_all_teams()

    def create_team(self, team: object) -> None:
        self.team_data.create_team(team)

    def check_for_clubs(self) -> bool:
        return self.club_data.check_for_clubs()

    def create_club(self, club: object):
        self.club_data.create_club(club)

    def get_all_clubs(self) -> list:
        return self.club_data.get_all_clubs()

    def get_new_club_id(self) -> int:
        return self.club_data.get_new_club_id()

    def get_new_team_id(self) -> int:
        return self.team_data.get_new_team_id()

    def generate_schedule(self, all_teams: List[object], league_ID: str) -> None:
        self.league_data.generate_schedule(all_teams, league_ID)

    def get_unplayed_matches(self):
        pass

    def get_unfinished_matches(self, league_id: str) -> List[object]:
        return self.league_data.get_unfinished_matches(league_id)

    def get_finished_matches(self, league_id: str) -> List[object]:
        return self.league_data.get_finished_matches(league_id)

    def get_all_league_teams(self, league_id: str) -> List[object]:
        return self.league_data.get_all_league_teams(league_id)

    def get_all_leagues(self) -> None:
        return self.league_data.get_all_leagues()

    def get_team_standings(self, league_id: str) -> List[tuple]:
        return self.league_data.get_team_standings(league_id)

    def check_host_name(self, name: str, league_id: str) -> bool:
        return self.league_data.check_host_name(name, league_id)

    def check_captain_name(self, name: str, league_id: str) -> bool:
        return self.league_data.check_captain_name(name, league_id)

    def record_result(self, match: object) -> None:
        self.league_data.record_result(match)

    def get_team_members(self, name: str, league_id: str) -> List[object]:
        return self.league_data.get_team_members(name, league_id)

    def edit_result(self):
        pass

    def create_tournament(self):
        pass

    def create_a_match(self):
        pass

    def get_new_match_id(self) -> int:
        return self.league_data.get_new_match_id()
