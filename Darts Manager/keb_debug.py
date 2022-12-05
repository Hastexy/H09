from data.league_data import LeagueData

my_teams = LeagueData.get_all_teams("1")
print(my_teams)
for team in my_teams:
    print(team.players)
