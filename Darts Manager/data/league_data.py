import csv
from typing import List
from itertools import combinations
from model.league import League
from model.match import Match
from model.game import Game
import itertools


class LeagueData:
    def __init__(self):
        self.file_name = "files/matches.csv"
        self.team_folder = "tourney_teams"

    def get_new_match_id(self) -> int:
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            for id, _ in enumerate(csvfile):
                pass
            new_id = id + 1
        return new_id

    def generate_schedule(self, all_teams: List[object], tournament_ID):  # Hrafnkell og Styrmir
        #match_ID;???date;Xhome_team;Xaway_team;Xresult;Xtournament_ID;
        
        id_list = []
        
        for teams in all_teams:
            t_id = teams.id
            id_list.append(t_id)
            
        matches = set(combinations(id_list,2))
        
        with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = [
                "match_ID",
                "date",
                "home_team",
                "away_team",
                "result",
                "tournament_ID",
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")

            for match in matches:
                new_id = self.get_new_match_id()
                writer.writerow(
                    {
                    "match_ID":new_id,
                    "date": "xx/xx/xxxx",
                    "home_team": match[0],
                    "away_team": match[1],
                    "result": "0-0", #Enter results in this format (2-1)
                    "tournament_ID": tournament_ID,
                    }
                )
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
    

