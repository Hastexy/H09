import os
import csv
from model.team import Team


class Team_Data:
    def __init__(self):
        print(os.getcwd())
        self.file_name = "files/teams.csv"
        self.member_folder = "files/TeamMembers/"

    def read_all_teams(self):
        ret_list = []
        with open(self.file_name, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Team(*row))
        return ret_list

    def create_team(self, team):
        new_file = self.member_folder + team.id

        with open(self.file_name, "a", newline="", encoding="utf-8") as team_file:
            fieldnames = ["ID", "name", "club"]
            writer = csv.DictWriter(team_file, fieldnames=fieldnames)

            writer.writerow(
                {
                    "ID": team.id,
                    "name": team.name,
                    "club": team.club,
                }
            )
        with open(new_file, "a", newline="", encoding="utf-8") as members_file:
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
            ]
            writer = csv.DictWriter(members_file, fieldnames=fieldnames, delimiter=";")
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
                    }
                )
