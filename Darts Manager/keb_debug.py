from data.league_data import League_Data

my_tourney = League_Data()

my_teams = my_tourney.get_all_league_teams("1")
print(my_teams)
for team in my_teams:
    print(team.players)

my_matches = my_tourney.get_finished_matches("1")
for match in my_matches:
    print(match.date)
    for game in match.games:
        print(game.type)
