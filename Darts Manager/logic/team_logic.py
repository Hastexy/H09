from data.team_data import Team_Data
from model.team import Team


class Team_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_team(self, team):
        """Takes in a team object and forwards it to the data layer"""

        self.data_wrapper.create_team(team)

    def get_all_teams(self):
        return self.data_wrapper.get_all_teams()