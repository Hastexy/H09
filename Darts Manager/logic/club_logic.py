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

    def get_all_clubs(self):
        return self.data_wrapper.get_all_clubs()
