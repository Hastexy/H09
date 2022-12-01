from data.club_data import Club_Data
from model.club import Club


class Club_Logic:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_club(self, club):
        """Takes in a club object and forwards it to the data layer"""
        self.data_wrapper.create_club(club)

    def get_new_club_id(self) -> int:
        return self.data_wrapper.get_new_club_id()

    def check_for_clubs(self) -> bool:
        return self.data_wrapper.check_for_clubs()

    def get_all_club_names(self) -> list:
        names_list = self.data_wrapper.get_all_club_names()
        return sorted(names_list)

    def club_exists(self, club_name: str) -> bool:
        return self.data_wrapper.club_exists(club_name)
