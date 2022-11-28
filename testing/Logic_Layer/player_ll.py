from Data_Layer.playerio import PlayerIO


class PlayerLL:
    def get_all_player() -> None:
        return PlayerIO.load_player_from_file()
