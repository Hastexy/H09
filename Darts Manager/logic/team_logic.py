class Team_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_team(self, team: object) -> None:
        """Takes in a team object and forwards it to the data layer"""
        self.data_wrapper.create_team(team)

    def get_all_teams(self):
        """Makes a request to the datawrapper to fetch all teams registered in the database. Returns a list of Team objects."""
        return self.data_wrapper.get_all_teams()

    def get_new_team_id(self) -> int:
        """Makes a request to the data wrapper to fetch a new unique team id number. Returns the team id number as an integer."""
        return self.data_wrapper.get_new_team_id()
