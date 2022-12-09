import csv
import fileinput
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
        self.match_folder = "files/league_matches/"
        self.team_folder = "files/league_teams/"
        self.game_folder = "files/match_games/"

    def create_league(self, league: object) -> None:
        """Registers a new league in the database. Also generates a schedule for the league and stores the matches in the database."""
        with open(self.league_file, "a", newline="", encoding="utf-8") as league_file:
            field_names = [
                "ID",
                "name",
                "host_name",
                "host_phonenumber",
                "start_date",
                "end_date",
                "rounds",
            ]
            writer = csv.DictWriter(league_file, delimiter=";", fieldnames=field_names)
            writer.writerow(
                {
                    "ID": league.id,
                    "name": league.name,
                    "host_name": league.host,
                    "host_phonenumber": league.phone,
                    "start_date": league.start_date,
                    "end_date": league.end_date,
                    "rounds": league.rounds,
                }
            )
        self.register_teams(league)
        self.generate_schedule(league)
        # Þetta er það eina sem er eftir af create dæminu!!.

    def generate_schedule(self, league: object) -> None:
        """Creates a schedule for a league. It makes sure that all the teams compete with each other only once."""

        all_matches = list(combinations(league.teams, 2))
        matchfile = self.match_folder + str(league.id) + ".csv"
        with open(matchfile, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = [
                "match_ID",
                "date",
                "home_team",
                "away_team",
                "result",
                "league_ID",
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
            next_id = int(self.get_new_match_id())
            for match in all_matches:  # a match is a tuple containing two Team objects
                m = Match()
                m.id = next_id
                next_id += 1
                m.date = ""  # vantar að sækja úr league.round_dates
                m.home_team, m.away_team = match
                writer.writerow(
                    {
                        "match_ID": m.id,
                        "date": m.date,
                        "home_team": m.home_team.name,
                        "away_team": m.away_team.name,
                        "result": m.result,
                        "league_ID": league.id,
                    }
                )

    def get_all_league_teams(self, league_id: str) -> List[object]:
        """Receives a league_id number and fetches all the teams participating in that specific league. Returns a list of Team objects."""
        all_teams = []
        league_team_file = "files/league_teams/" + league_id + ".csv"
        with open(league_team_file, newline="", encoding="utf-8") as teams_file:
            team_reader = csv.DictReader(teams_file, delimiter=";")
            for team in team_reader:
                t = Team(team["ID"], team["name"])
                memberfile = "files/TeamMembers/" + t.id + ".csv"
                with open(memberfile, newline="", encoding="utf-8") as member_file:
                    member_reader = csv.DictReader(member_file, delimiter=";")
                    for player in member_reader:
                        p = Player(*player.values())
                        t.players.append(p)
                all_teams.append(t)
        return all_teams

    def get_team_standings(self, league_id: str) -> List[tuple]:
        """Returns points a  has scored."""
        team_list = []
        teamfile = self.team_folder + str(league_id) + ".csv"
        with open(teamfile, newline="", encoding="utf-8") as team_file:
            reader = csv.DictReader(team_file, delimiter=";")
            for team in reader:
                team_list.append((team["name"], team["match_wins"], team["legs_wins"]))
        return team_list

    def get_finished_matches(self, league_id: str) -> List[object]:
        """Receives a league_id number and fetches all the matches that have been completed in that league. Returns a list of Match objects."""
        matches = []
        matchfile = self.match_folder + str(league_id) + ".csv"
        with open(matchfile, newline="", encoding="utf-8") as match_file:
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
                        gamefile = self.game_folder + m.id + ".csv"
                        with open(gamefile, newline="", encoding="utf-8") as game_file:
                            game_reader = csv.DictReader(game_file, delimiter=";")
                            for game in game_reader:
                                g = Game(*game.values())
                                m.games.append(g)
                        matches.append(m)
        return matches

    def get_unfinished_matches(self, league_id) -> List[object]:  # Kristinn
        """Receives a league_id number and fetches all the matches that have yet to be  in that league. Returns a list of Match objects."""
        matches = []
        matchfile = self.match_folder + str(league_id) + ".csv"
        with open(matchfile, newline="", encoding="utf-8") as match_file:
            reader = csv.DictReader(match_file, delimiter=";")
            for match in reader:
                if match["league_ID"] == league_id:
                    if not match["result"]:
                        m = Match(
                            match["match_ID"],
                            match["date"],
                            match["home_team"],
                            match["away_team"],
                            match["result"],
                            match["league_ID"],
                        )
                        gamefile = self.game_folder + m.id + ".csv"

                        with open(gamefile, newline="", encoding="utf-8") as game_file:
                            game_reader = csv.DictReader(game_file, delimiter=";")
                            for game in game_reader:
                                g = Game(*game.values())
                                m.games.append(g)
                        matches.append(m)
        return matches

    def register_teams(self, league: object) -> None:
        """Registers all the teams participating in league in the database."""

        teams_file = self.team_folder + str(league.id) + ".csv"

        with open(teams_file, "a", newline="", encoding="utf-8") as teams_file:
            fieldnames = ["ID", "name", "clubID", "match_wins", "legs_wins"]
            writer = csv.DictWriter(teams_file, fieldnames=fieldnames, delimiter=";")
            writer.writeheader()
            for team in league.teams:
                writer.writerow(
                    {
                        "ID": team.id,
                        "name": team.name,
                        "clubID": team.club,
                        "match_wins": "0",
                        "legs_wins": "0",
                    }
                )

    def reschedule_match(self, match: object) -> None:
        """Changes the date of a match"""
        matchfile = self.match_folder + str(match.league_id) + ".csv"
        with fileinput.input(files=matchfile, inplace=True, mode="r") as match_file:

            reader = csv.DictReader(match_file, delimiter=";")
            print(";".join(reader.fieldnames))
            for a_match in reader:
                if a_match["match_ID"] == match.id:
                    a_match["date"] = match.date
                print(";".join([*a_match.values()]))

    def get_new_league_id(self) -> int:
        """Generates a new id for a league."""
        with open(self.league_file, newline="", encoding="utf-8") as csvfile:
            for id, _ in enumerate(csvfile):
                pass
            new_id = id + 1
        return new_id

    def get_new_match_id(self) -> int:
        """Generates a unique match id."""
        with open(self.match_file, newline="", encoding="utf-8") as csvfile:
            for id, _ in enumerate(csvfile):
                pass
            new_id = id + 1
        return new_id

    def get_all_leagues(self) -> list:
        """Returns a list of all league names."""
        with open(self.league_file, newline="", encoding="utf-8") as league_file:
            reader = csv.DictReader(league_file, delimiter=";")
            all_leagues = [League(*league.values()) for league in reader]
        return all_leagues

    def check_host_name(self, name: str, league_id: str) -> bool:
        """Checks if hostname already exists."""
        with open(self.league_file, newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file, delimiter=";")
            for league in reader:
                if league["ID"] == str(league_id):
                    if league["host_name"] == name:
                        return True
        return False

    def check_captain_name(self, name: str, league_id: str) -> bool:
        """Checks if the given player is a captain in a team participating in a specific league."""
        teamfile = self.team_folder + league_id + ".csv"
        with open(teamfile, newline="", encoding="utf-8") as team_file:
            team_reader = csv.DictReader(team_file, delimiter=";")
            for team in team_reader:
                memberfile = "files/TeamMembers/" + team["ID"] + ".csv"
                with open(memberfile, newline="", encoding="utf-8") as member_file:
                    member_reader = csv.DictReader(member_file, delimiter=";")
                    for player in member_reader:
                        if player["name"] == name and player["role"] == "captain":
                            return Player(*player.values())
        return False

    def record_result(self, match: object) -> None:
        matchfile = self.match_folder + str(match.league_id) + ".csv"
        with fileinput.input(files=matchfile, inplace=True, mode="r") as match_file:

            reader = csv.DictReader(match_file, delimiter=";")
            print(";".join(reader.fieldnames))
            for a_match in reader:
                if a_match["match_ID"] == match.id:
                    a_match["result"] = match.result
                print(";".join([*a_match.values()]))

        gamefile = self.game_folder + str(match.id) + ".csv"
        with open(gamefile, "w", newline="", encoding="utf-8") as game_file:
            field_names = ["type", "h_player", "a_player", "h_score", "a_score"]
            writer = csv.DictWriter(game_file, fieldnames=field_names, delimiter=";")
            writer.writeheader()
            for game in match.games:
                writer.writerow(
                    {
                        "type": game.type,
                        "h_player": game.home_player.name,
                        "a_player": game.away_player.name,
                        "h_score": game.home_score,
                        "a_score": game.away_score,
                    }
                )

    def get_team_members(self, name: str, league_id: str) -> List[object]:
        teamfile = self.team_folder + league_id + ".csv"
        with open(teamfile, newline="", encoding="utf-8") as team_file:
            teamreader = csv.DictReader(team_file, delimiter=";")
            for team in teamreader:
                if team["name"] == name:
                    memberfile = "files/TeamMembers/" + team["ID"] + ".csv"
                    with open(memberfile, newline="", encoding="utf-8") as member_file:
                        memberreader = csv.DictReader(member_file, delimiter=";")
                        all_team_players = [
                            Player(*member.values()) for member in memberreader
                        ]
                        return all_team_players

    def get_team(self, team_id: str) -> object:
        with open("files/teams.csv", newline="", encoding="utf-8") as team_file:
            reader = csv.DictReader(team_file, delimiter=";")
            for team in reader:
                if team["ID"] == team_id:
                    return Team(*team.values())
