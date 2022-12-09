from typing import List
from operator import itemgetter


class League_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_league(self, league: object) -> None:
        """sends information about a new league to the data layer to be created/stored."""
        self.data_wrapper.create_league(league)

    def get_new_league_id(self) -> int:
        """Retrives a number 1 higher than the highest id league id from the data layer."""
        return self.data_wrapper.get_new_league_id()

    def get_new_match_id(self) -> int:
        """Makes a request to the data wrapper to fetch a new unique match id number. Returns the match id number as an integer."""
        return self.data_wrapper.get_new_match_id()

    def generate_schedule(self, all_teams: list, rounds: int, league_ID: str) -> None:
        """Makes a request to the datawrapper to generate a schedule for a specific league."""
        self.data_wrapper.generate_schedule(all_teams, rounds, league_ID)

    def get_unfinished_matches(self, league_id: str) -> dict:
        """Makes a request to the datawrapper to fetch all unfinished matches in a specific league. If a match has an empty 'result' column in the database, it is considered unfinished."""
        matches_sorted_by_date = {}
        all_matches = self.data_wrapper.get_unfinished_matches(league_id)
        for match in all_matches:

            if match.date not in matches_sorted_by_date:
                matches_sorted_by_date[match.date] = []

            matches_sorted_by_date[match.date].append(match)
        return matches_sorted_by_date

    def get_finished_matches(self, league_id: str) -> dict:
        """Makes a request to the datawrapper to fetch all unfinished matches in a specific league. If a match has a non-empty 'result' column in the database, it is considered finished."""
        matches_sorted_by_date = {}
        all_matches = self.data_wrapper.get_finished_matches(league_id)
        for match in all_matches:

            if match.date not in matches_sorted_by_date:
                matches_sorted_by_date[match.date] = []

            matches_sorted_by_date[match.date].append(match)
        return matches_sorted_by_date

    def get_all_leagues(self) -> None:
        """Retrives all the leagues from data layer."""
        return self.data_wrapper.get_all_leagues()

    def get_all_league_teams(self, league_id: str) -> List[object]:
        """Makes a request to the datawrapper to fetch all teams participating in a specific league."""
        return self.data_wrapper.get_all_league_teams(league_id)

    def get_team_standings(self, league_id: str) -> List[tuple]:
        """Get team standings from a specific league"""
        all_teams = self.data_wrapper.get_team_standings(league_id)
        return sorted(all_teams, key=itemgetter(1, 2, 0), reverse=True)

    def check_host_name(self, name: str, league_id: str) -> bool:
        """Check if host name already exists."""
        return self.data_wrapper.check_host_name(name, league_id)

    def check_captain_name(self, name: str, league_id: str) -> bool:
        """Checks if the name given belongs to the captain."""
        return self.data_wrapper.check_captain_name(name, league_id)

    def record_result(self, match: object) -> None:
        home_score_total = 0
        away_score_total = 0
        for game in match.games:
            if game.home_score == 2:
                home_score_total += 1
            elif game.away_score == 2:
                away_score_total += 1
        result_string = "-".join([str(home_score_total), str(away_score_total)])
        match.result = result_string
        self.data_wrapper.record_result(match)

    def get_team_members(self, name: str, league_id: str) -> List[object]:
        return self.data_wrapper.get_team_members(name, league_id)

    def reschedule_match(self, match: object) -> None:
        self.data_wrapper.reschedule_match(match)

    def get_team(self, team_id: str) -> object:
        return self.data_wrapper.get_team(team_id)
