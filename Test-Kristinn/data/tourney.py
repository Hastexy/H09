import os
import csv
from model.tourney import Tourney


class Tourney_Data:
    def __init__(self):
        print(os.getcwd())
        self.file_name = "Test-Kristinn/files/Tourneys.csv"

    def read_all_tourneys(self):
        ret_list = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Tourney(*row.values()))
        return ret_list

    def create_tourney(self, tourney):
        with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = [
                "no. of teams",
                "start date",
                "end date",
                "club names",
                "team names",
                "players",
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow(
                {
                    "no. of teams": tourney.no_of_teams,
                    "start date": tourney.start_date,
                    "end date": tourney.end_date,
                    "club names": tourney.club_name,
                    "team names": tourney.team_name,
                    "players": tourney.players,
                }
            )
