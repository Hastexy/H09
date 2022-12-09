class Player_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_player(self, player: object) -> None:
        """Takes in a player object and forwards it to the data layer"""
        self.data_wrapper.create_player(player)

    def get_new_player_id(self) -> int:
        """Makes a request to the datawrapper to fetch a new unique player id number. Returns the id number as an integer."""
        return self.data_wrapper.get_new_player_id()

    def get_all_players(self):
        """Makes a request to the datawrapper to fetch a list of all the players registered in the database. Sorts the player list alphabetically and returns it."""
        all_players = self.data_wrapper.get_all_players()
        return sorted(all_players, key=lambda p: p.name)

    def update_player_status(self, player_id: str, role: str, team_id: str) -> None:
        """Makes a request to the datawrapper to update the role and team_id for the player with the given player_id."""
        self.data_wrapper.update_player_status(player_id, role, team_id)
