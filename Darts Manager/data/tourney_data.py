import csv
from typing import List
from itertools import combinations


class TourneyData:
    def __init__(self):
        self.file_name = "files/matches.csv"
        self.team_folder = "tourney_teams"

    def generate_shcedule(variable, all_teams: List[object]) -> List[tuple]:
        pass

    def get_all_teams(self) -> List[object]:
        tourney_file = self.team_folder + self.id + ".csv"
        with open(tourney_file, newline="", encoding="utf-8") as teams_file:
            reader = csv.DictReader(teams_file, delimiter=";")
            pass

    def get_standings(self) -> List[object]:
        pass

    def get_finished_matches(self) -> List[object]:
        pass

    def get_unfinished_matches(self) -> List[object]:
        pass
