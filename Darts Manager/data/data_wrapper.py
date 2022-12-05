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

    def get_all_players(self) -> List[object]:
        return self.player_data.read_all_players()

    def create_player(self, player: object) -> None:
        """Takes in a player object and forwards it to player_data"""
        self.player_data.create_player(player)

    def get_new_player_id(self) -> int:
        return self.player_data.get_new_player_id()

    def update_player_status(self, player_id: str, role: str, team_id: str) -> None:
        """Updates the role and team_id for the player with the given player_id."""
        self.player_data.update_player_status(player_id, role, team_id)

    def get_all_teams(self):
        return self.team_data.read_all_teams()

    def create_team(self, team: object) -> None:
        self.team_data.create_team(team)

    def check_for_clubs(self) -> bool:
        return self.club_data.check_for_clubs()

    def create_club(self, club: object):
        """Takes in a club object and forwards it to club_data"""
        self.club_data.create_club(club)

    def get_all_clubs(self) -> list:
        return self.club_data.get_all_clubs()

    def get_new_club_id(self) -> int:
        return self.club_data.get_new_club_id()

    def get_new_team_id(self) -> int:
        return self.team_data.get_new_team_id()

    def generate_schedule():
        pass

    def get_unplayed_matches():
        pass

    def get_complete_results():
        pass

    def get_leaderboard():
        pass

    def register_result():
        pass

    def edit_result():
        pass

    def create_tournament():
        pass

    def create_a_match():
        pass
    
    def get_new_match_id():
        pass
