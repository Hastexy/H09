from Logic_Layer.logic_wrapper import LogicWrapper


class PlayerUI:
    def get_all_players() -> None:
        all_players = LogicWrapper.get_all_players()
        print(all_players)
