import csv
from typing import List
from itertools import combinations
from model.league import League
from model.match import Match
from model.game import Game
from model.team import Team
from model.player import Player


class League_Data:
    def __init__(self):
        self.league_file = "files/leagues.csv"
        self.match_file = "files/matches.csv"
        self.team_folder = "league_teams"

    def get_new_match_id(self) -> int:
        """Generates a unique match id."""
        with open(self.match_file, newline="", encoding="utf-8") as csvfile:
            for id, _ in enumerate(csvfile):
                pass
            new_id = id + 1
        return new_id

    def generate_schedule(self, all_teams: List[object], league_ID: str) -> None:
        """Creates a schedule for a league. It makes sure that all the teams compete with each other only once."""

        id_list = []

        for teams in all_teams:
            t_id = teams.id
            id_list.append(t_id)

        matches = set(combinations(id_list, 2))

        with open(self.match_file, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = [
                "match_ID",
                "date",
                "home_team",
                "away_team",
                "result",
                "league_ID",
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")

            for match in matches:
                new_id = self.get_new_match_id()
                writer.writerow(
                    {
                        "match_ID": new_id,
                        "date": "xx/xx/xxxx",
                        "home_team": match[0],
                        "away_team": match[1],
                        "result": "0-0",  # Enter results in this format (2-1)
                        "league_ID": league_ID,
                    }
                )

    def get_all_league_teams(self, league_id: str) -> List[object]:
        """Receives a league_id number and fetches all the teams participating in that specific league. Returns a list of Team objects."""
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

    def get_finished_matches(self, league_id: str) -> List[object]:
        """Receives a league_id number and fetches all the matches that have been completed in that league. Returns a list of Match objects."""
        matches = []
        with open(self.match_file, newline="", encoding="utf-8") as match_file:
            reader = csv.DictReader(match_file, delimiter=";")
            for match in reader:
                if match["league_ID"] == league_id:
                    if match["result"]:
                        m = Match(
                            match["match_ID"],
                            match["date"],
                            match["home_team"],
                            match["away_team"],
                            match["result"],
                            match["league_ID"],
                        )
                        with open(
                            "files/games.csv", newline="", encoding="utf-8"
                        ) as game_file:
                            game_reader = csv.DictReader(game_file, delimiter=";")
                            for game in game_reader:
                                if game["match_ID"] == m.id:
                                    g = Game(*game.values())
                                    m.games.append(g)
                        matches.append(m)
        return matches

    def get_unfinished_matches(self, league_id) -> List[object]:  # Kristinn
        """Receives a league_id number and fetches all the matches that have yet to be  in that league. Returns a list of Match objects."""
        matches = []
        with open(self.match_file, newline="", encoding="utf-8") as match_file:
            reader = csv.DictReader(match_file, delimiter=";")
            for match in reader:
                if match["league_ID"] == league_id:
                    if not match["result"]:
                        m = Match(
                            match["id"],
                            match["date"],
                            match["home_team"],
                            match["away_team"],
                            match["result"],
                            match["league_ID"],
                        )
                        with open(
                            "files/games.csv", newline="", encoding="utf-8"
                        ) as game_file:
                            game_reader = csv.DictReader(game_file, delimiter=";")
                            for game in game_reader:
                                if game["match_ID"] == m.id:
                                    g = Game(*game.values())
                                    m.games.append(g)
                        matches.append(m)
        return matches

    def register_teams(self, teams: List[object], league_id: str) -> None:  # KjartanIK
        """Takes a Team object and registers a new Team in the database based on its attributes."""

        teams_file = self.team_folder + league_id.id + ".csv"

        with open(self.match_file, "a", newline="", encoding="utf-8") as teams_file:
            fieldnames = ["ID", "name", "host_name", "host_phonenumber"]
            writer = csv.DictWriter(teams_file, fieldnames=fieldnames, delimiter=";")
            writer.writerow(
                {
                    "ID": league_id.id,
                    "name": league_id.name,
                    "host_name": league_id.host_name,
                    "host_phonenumber": league_id.host_phonenumber,
                }
            )

        with open(teams_file, "a", newline="", encoding="utf-8") as teams_file:
            fieldnames = ["ID", "name", "host_name", "host_phonenumber"]
            writer = csv.DictWriter(teams_file, fieldnames=fieldnames, delimiter=";")
            writer.writeheader()
            for team in league_id.teams:
                writer.writerow({"ID": team.id, "clubID": team.clubID})

    def reschedule_match(self, match_id: int) -> object:
        pass

    def get_new_league_id(self) -> int:
        with open(self.league_file, newline="", encoding="utf-8") as csvfile:
            for id, _ in enumerate(csvfile):
                pass
            new_id = id + 1
        return new_id
