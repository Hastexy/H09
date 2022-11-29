# import os
import csv
from model.player import Player


class Player_Data:
    def __init__(self):
        # print(os.getcwd())
        self.file_name = "files/players.csv"

    def read_all_players(self):
        ret_list = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Player(*row))
        return ret_list

    def create_player(self, player):
        with open(self.file_name, "a", newline="", encoding="utf-8") as csvfile:
            fieldnames = [
                "name",
                "ssn",
                "email",
                "birth_year",
                "team",
                "phone",
                "home_phone",
                "address",
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow(
                {
                    "name": player.name,
                    "ssn": player.ssn,
                    "email": player.email,
                    "birth_year": player.birth_year,
                    "team": player.team,
                    "phone": player.phone,
                    "home_phone": player.home_phone,
                    "address": player.address,
                }
            )
