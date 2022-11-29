from data.player_data import Player_Data

data_class = Player_Data()
result = data_class.read_all_players()
for elem in result:
    print(elem)