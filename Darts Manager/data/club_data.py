import csv
from typing import List
from model.club import Club


class Club_Data:
    def __init__(self):
        self.file_name = "files/clubs.csv"

    def read_all_clubs(self) -> List[object]:  # Þurfum við þetta fall????
        """Fetches all registered clubs in the database and returns a list of Club objects"""
        ret_list = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Club(*row.values()))
        return ret_list

    def check_for_clubs(self) -> bool:
        """Checks if any club is registered in the database"""
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            text = csvfile.read()

        return text[1] is not None

    def create_club(self, club: object) -> None:
        """Takes a Club object and registers a new club in the database based on its attributes."""
        with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "name", "address", "phone_number"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")

            writer.writerow(
                {
                    "id": club.id,
                    "name": club.name,
                    "address": club.address,
                    "phone_number": club.phone_number,
                }
            )

    def get_new_club_id(self) -> int:
        """Generates a unique club id."""
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            for id, _ in enumerate(csvfile):
                pass
            new_id = id + 1
        return new_id

    def get_all_clubs(self) -> List[object]:
        """Fetches all registered clubs in the database and returns a list of Club objects"""
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            clubs_list = [Club(*club.values()) for club in reader]
        return clubs_list
