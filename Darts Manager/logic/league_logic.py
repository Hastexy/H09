from typing import List


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

    def register_teams(self, tourney) -> None:  # breyta parameters og virkni!!!
        """Makes a request to the datawrapper to register a list of teams in a specific league."""
        self.data_wrapper.register_teams(tourney)

    def get_unfinished_matches(self, league_id: str) -> List[object]:
        """Makes a request to the datawrapper to fetch all unfinished matches in a specific league. If a match has an empty 'result' column in the database, it is considered unfinished."""
        return self.data_wrapper.get_unfinished_matches(league_id)

    def get_finished_matches(self, league_id: str) -> List[object]:
        """Makes a request to the datawrapper to fetch all unfinished matches in a specific league. If a match has a non-empty 'result' column in the database, it is considered finished."""
        return self.data_wrapper.get_finished_matches(league_id)

    def get_all_league_teams(self, league_id: str) -> List[object]:
        """Makes a request to the datawrapper to fetch all teams participating in a specific league."""
        return self.data_wrapper.get_all_league_teams(league_id)
