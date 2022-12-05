import csv
from typing import List
from itertools import combinations
from model.league import League
from model.match import Match
from model.game import Game


class LeagueData:
    def __init__(self):
        self.file_name = "files/matches.csv"
        self.team_folder = "tourney_teams"

    def generate_schedule(
        variable, all_teams: List[object]
    ) -> List[tuple]:  # Hrafnkell og Styrmir
        # list((team1, team2))
        # for match in all_teams:
        # record match in the
        pass

    def get_all_teams(self) -> List[object]:
        tourney_file = self.team_folder + self.id + ".csv"
        with open(tourney_file, newline="", encoding="utf-8") as teams_file:
            reader = csv.DictReader(teams_file, delimiter=";")
            pass

    def get_team_standings(self) -> List[object]:
        pass

    def get_finished_matches(self) -> List[object]:  # Kristinn
        pass

    def get_unfinished_matches(self) -> List[object]:  # Kristinn
        pass

    def register_teams(self, team_list) -> None:  # KjartanIK

        pass

    def reschedule_match(self, match_id: int) -> object:
        pass
