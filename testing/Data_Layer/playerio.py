from typing import List
import csv
from Models.player import Player


class PlayerIO:
    def __init__(self) -> None:
        self.filename = "files/players.csv"

    def load_all_players_from_file(self) -> List[object]:
        ret_list = []
        with open("players.csv", encoding="utf-8") as data_file:
            reader = csv.DictReader(data_file, delimiter=";")
            for row in reader:
                ret_list.append(Player(*row.values()))
                # row["name"],
                # row["KT"],
                # row["Email"],
                # row["Birthdate"],
                # row["Team"]

        return ret_list

    def create_player(self, player):
        with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["name", "KT", "Email", "Birthdate", "Team"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({"name": player.name, "birth_year": player.birth_year})
