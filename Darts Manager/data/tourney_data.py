import csv
from model.te import Team

class Team_Data:
    def __init__(self):
        self.file_name = "files/teams.csv"

    def read_all_teams(self):
        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Team(*row))
        return ret_list

    def create_team(self, team):
        with open(self.file_name, 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ["name", "players", "captain"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({'name': team.name, 'players': team.players, 'captain': team.captain})