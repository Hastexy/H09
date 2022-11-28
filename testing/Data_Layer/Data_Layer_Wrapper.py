from Data_Layer.playerio import PlayerIO


class Data_Layer_Wrapper:
    def __init__(self):
        self.playerio = PlayerIO()

    def get_all_players(self):
        return self.playerio.load_all_players_from_file()

    def create_player(self, player):
        return self.play.create_player(player)
