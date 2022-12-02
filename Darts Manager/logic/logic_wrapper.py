from typing import List
from logic.player_logic import Player_Logic
from logic.team_logic import Team_Logic
from data.data_wrapper import Data_Wrapper
from logic.club_logic import Club_Logic


class Logic_Wrapper:
    def __init__(self):
        self.data_wrapper = Data_Wrapper()
        self.player_logic = Player_Logic(self.data_wrapper)
        self.team_logic = Team_Logic(self.data_wrapper)
        self.club_logic = Club_Logic(self.data_wrapper)

    def create_player(self, player: object) -> None:
        """Takes in a player object and forwards it to the data layer"""
        self.player_logic.create_player(player)

    def get_new_player_id(self) -> int:
        return self.player_logic.get_new_player_id()

    def get_all_players(self) -> List[object]:
        return self.player_logic.get_all_players()

    def create_team(self, team: object) -> None:
        """Takes in a team object and forwards it to the data layer"""
        self.team_logic.create_team(team)

    def check_for_clubs(self) -> bool:
        return self.club_logic.check_for_clubs()

    def create_club(self, club: object) -> None:
        """Takes in a club object and forwards it to the data layer"""
        self.data_wrapper.create_club(club)

    def get_new_club_id(self) -> int:
        return self.club_logic.get_new_club_id()

    def get_new_team_id(self) -> int:
        return self.team_logic.get_new_team_id()

    def get_all_teams(self) -> List[dict]:
        # return self.team_logic.get_all_teams()
        return self.team_logic.get_all_teams()

    def get_all_clubs(self) -> list:
        return self.club_logic.get_all_clubs()

    def update_player_status(self, player_id: str, role: str, team_id: str) -> None:
        """Updates the role and team_id for the player with the given player_id."""
        self.player_logic.update_player_status(player_id, role, team_id)
