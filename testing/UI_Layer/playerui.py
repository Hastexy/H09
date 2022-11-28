from Logic_Layer.logic_layer import LogicLayerMain


class PlayerUI:
    def get_player_by_ID() -> None:
        player_ID = input("Enter the player's ID: ")
        player = LogicLayerMain.get_player_by_ID(player_ID)
        if player:
            print(player)
        else:
            print("No player with that ID exists.")


player1 = PlayerUI.get_player_by_ID()
