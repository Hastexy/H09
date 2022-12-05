import csv
from typing import List
from itertools import combinations
from model.league import League
from model.match import Match
from model.game import Game
from model.team import Team
from model.player import Player


class LeagueData:
    def __init__(self):
        self.file_name = "files/matches.csv"
        self.team_folder = "league_teams"

    def generate_schedule(
        variable, all_teams: List[object]
    ) -> List[tuple]:  # Hrafnkell og Styrmir
        # list((team1, team2))
        # for match in all_teams:
        # record match in the
        pass

    def get_all_teams(league_id: str) -> List[object]:
        all_teams = []
        league_team_file = "files/league_teams/" + league_id + ".csv"
        with open(league_team_file, newline="", encoding="utf-8") as teams_file:
            team_reader = csv.DictReader(teams_file, delimiter=";")
            for team in team_reader:
                t = Team(*team.values())
                member_file = "files/TeamMembers/" + t.id + ".csv"
                with open(member_file, newline="", encoding="utf-8") as member_file:
                    member_reader = csv.DictReader(member_file, delimiter=";")
                    for player in member_reader:
                        p = Player(*player.values())
                        t.players.append(p)
                all_teams.append(t)
        return all_teams

    def get_team_standings(self) -> List[object]:
        pass

    def get_finished_matches(self, league_id: str) -> List[object]:  # Kristinn
        # opna tengingu og sækja allt sem viðkemur þessu tournamenti og filtera og skila lista af objects
        matches = []
        with open(self.file_name, newline="", encoding="utf-8") as match_file:
            reader = csv.DictReader(match_file, delimiter=";")
            for match in reader:
                if match["league_ID"] == league_id:
                    if match["result"]:
                        m = Match(*match.values())
                        matches.append(m)

    def get_unfinished_matches(self, league_id) -> List[object]:  # Kristinn
        matches = []
        with open(self.file_name, newline="", encoding="utf-8") as match_file:
            reader = csv.DictReader(match_file, delimiter=";")
            for match in reader:
                if match["league_ID"] == league_id:
                    if not match["result"]:
                        m = Match(*match.values())
                        matches.append(m)

    def register_teams(self, team_list) -> None:  # KjartanIK

        pass

    def reschedule_match(self, match_id: int) -> object:
        pass
