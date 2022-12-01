import csv
from model.club import Club


class Club_Data:
    def __init__(self):
        self.file_name = "files/clubs.csv"

    def read_all_clubs(self):
        ret_list = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Club(*row.values()))
        return ret_list

    def check_for_clubs(self) -> bool:
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            text = csvfile.read()

        return text[1] is not None

    def create_club(self, club):
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
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            for id, _ in enumerate(csvfile):
                pass
            new_id = id + 1
        return new_id

    def club_exists(self, club_name: str) -> bool:
        """Searches the csv file for a given club name. If the club exists the function returns True, else it returns False"""
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for club in reader:
                if club["name"] == club_name:
                    return True
        return False

    def get_all_club_names(self) -> list:
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            names_list = [club["name"] for club in reader]
        return names_list
