from typing import List

class League_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection
        
    def get_new_match_id(self)-> int: 
        return self.data_wrapper.get_new_match_id()
    
    def generate_schedule(self, all_teams: List[object], league_ID: str) -> None:
        self.data_wrapper.generate_schedule(all_teams, league_ID)
    
    def register_teams(self, tourney):
        self.data_wrapper.register_teams(tourney)