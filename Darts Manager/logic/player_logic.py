from data.player_data import Player_Data
from model.player import Player

class Player_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_player(self, player: object) -> None:
        """Takes in a player object and forwards it to the data layer"""
        self.data_wrapper.create_player(player)

    def get_new_player_id(self) -> int:
        return self.data_wrapper.get_new_player_id()

    def get_all_players(self):
        return self.data_wrapper.get_all_players()