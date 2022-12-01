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
                "ID",
                "name",
                "ssn",
                "email",
                "dob",
                "phone",
                "home_phone",
                "address",
                "team_ID"
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")

            writer.writerow(
                {
                    "ID": player.id,
                    "name": player.name,
                    "ssn": player.ssn,
                    "email": player.email,
                    "dob": player.dob,
                    "phone": player.phone,
                    "home_phone": player.home_phone,
                    "address": player.address,
                    "team_ID": player.team
                }
            )

    def get_new_player_id(self) -> int:
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            for id, _ in enumerate(csvfile):
                pass
            new_id = id + 1
        return new_id

        # Hérna er hugmynd um að nota rand-int... samt ekki, veit ekki...

        #     # for line in csvfile:
        #     #     pass
        #     # new_id, *_ = line.split(";")
        # return int(new_id) + 1
