from Data_Layer.playerio import PlayerIO


class PlayerLL:
    def get_player_by_ID(ID: str) -> None:
        return PlayerIO.load_player_from_file(ID)
