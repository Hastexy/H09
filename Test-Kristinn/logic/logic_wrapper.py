from logic.player_logic import Player_Logic
from logic.team_logic import Team_Logic
from data.data_wrapper import Data_Wrapper

class Logic_Wrapper:
    def __init__(self):
        self.data_wrapper = Data_Wrapper()
        self.player_logic = Player_Logic(self.data_wrapper)
        self.team_logic = Team_Logic(self.data_wrapper)

    def create_player(self, player):
        """Takes in a player object and forwards it to the data layer"""
        return self.player_logic.create_player(player)

    def get_all_players(self):
        return self.player_logic.get_all_players()
    
    def create_team(self, team):
        """Takes in a team object and forwards it to the data layer"""
        return self.team_logic.create_team(team)

    def get_all_teams(self):
        return self.team_logic.get_all_teams()