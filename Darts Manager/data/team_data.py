import os
import csv
from model.team import Team
from typing import List
from model.player import Player


class Team_Data:
    def __init__(self):
        print(os.getcwd())
        self.file_name = "files/teams.csv"
        self.member_folder = "files/TeamMembers/"

    def read_all_teams(self) -> List[object]:
        """Opens two files: one containing general info about the team and the other file contains its team members. Creates a Team object with an appropriate name and also fills the team.players attribute with player objects. Appends all Team objects into a list and returns it."""
        ret_list = []
        with open(self.file_name, newline="", encoding="utf-8") as team_info_file:
            team_reader = csv.DictReader(team_info_file, delimiter=";")
            for team in team_reader:
                members_file = self.member_folder + team["ID"] + ".csv"
                with open(members_file, newline="", encoding="utf-8") as players_file:
                    player_reader = csv.DictReader(players_file, delimiter=";")
                    t = Team(*team.values())
                    for player in player_reader:
                        p = Player(*player.values())
                        t.players.append(p)
                ret_list.append(t)
        return ret_list

    def create_team(self, team: object):
        members_file = self.member_folder + str(team.id) + ".csv"

        with open(self.file_name, "a", newline="", encoding="utf-8") as team_file:
            fieldnames = ["ID", "name", "club"]
            writer = csv.DictWriter(team_file, fieldnames=fieldnames, delimiter=";")
            writer.writerow({"ID": team.id, "name": team.name, "club": team.club})

        with open(members_file, "a", newline="", encoding="utf-8") as members_file:
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
            writer = csv.DictWriter(members_file, fieldnames=fieldnames, delimiter=";")
            writer.writeheader()
            for player in team.players:
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

    def get_new_team_id(self) -> int:
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            for id, _ in enumerate(csvfile):
                pass
            new_id = id + 1
        return new_id
