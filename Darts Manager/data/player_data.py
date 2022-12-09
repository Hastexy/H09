import csv
from model.player import Player
from typing import List
import fileinput


class Player_Data:
    def __init__(self):
        self.file_name = "files/players.csv"

    def read_all_players(self) -> List[object]:
        '''returns a list of players.'''
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            ret_list = [
                Player(*player.values()) for player in reader if not player["team_ID"]
            ]
        return ret_list

    def create_player(self, player: object):
        '''Creates a new player and stores it in players.csv.'''
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
                "team_ID",
                "role",
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
                    "team_ID": player.team,
                    "role": player.role,
                }
            )

    def get_new_player_id(self) -> int:
        '''Generates a new id for the new player.'''
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            for id, _ in enumerate(csvfile):
                pass
            new_id = id + 1
        return new_id

    def update_player_status(self, player_id, role, team_id) -> None:
        """Updates both role and team id for one player. This function isn't very efficient because it overwrites
        the file contents and then rewrites the ENTIRE data back into the file again with minor changes."""
        with fileinput.input(
            files=(self.file_name), inplace=True, mode="r"
        ) as player_file:

            reader = csv.DictReader(player_file, delimiter=";")
            print(";".join(reader.fieldnames))  # print back the headers
            for player in reader:
                if player["ID"] == player_id:
                    player["team_ID"] = team_id
                    player["role"] = role
                print(";".join([*player.values()]))
