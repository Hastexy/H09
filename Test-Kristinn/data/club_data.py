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
                ret_list.append(Club(*row))
        return ret_list

    def create_club(self, club):
        with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["name", "address", "phone_number"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow(
                {
                    "name": club.name,
                    "address": club.address,
                    "phone number": club.phone_number,
                }
            )
