import csv
from Models.player import Player


class PlayerIO:
    def load_player_from_file(self, ID: str) -> object:
        with open("players.csv", encoding="utf-8") as data_file:
            reader = csv.DictReader(data_file, delimiter=";")

            for person in reader:
                if person["SocialSecurityNumber"] == ID:
                    return Player(*person.values())
