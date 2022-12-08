from typing import List
from operator import itemgetter


class League_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_league(self, league: object) -> None:
        self.data_wrapper.create_league(league)

    def get_new_league_id(self) -> int:
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

            matches_sorted_by_date[match.date].append(
                (match.home_team, match.away_team)
            )
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
        return self.data_wrapper.get_all_leagues()

    def get_all_league_teams(self, league_id: str) -> List[object]:
        """Makes a request to the datawrapper to fetch all teams participating in a specific league."""
        return self.data_wrapper.get_all_league_teams(league_id)

    def get_team_standings(self, league_id: str) -> List[tuple]:
        all_teams = self.data_wrapper.get_team_standings(league_id)
        return sorted(all_teams, key=itemgetter(1, 2, 0), reverse=True)
