from model.club import Club
from model.team import Team
from model.player import Player
from model.tourney import Tourney
from ui.input_validators import *

class Tournament_Manager_UI:
    def __init__(self, logic_connection) -> None:
        self.logic_wrapper = logic_connection
        
    def menu_output(self):
        print("\n---Tournament Manager---")
        print("1. create club")
        print("2. create team")
        print("3. create player")
        print("4. create tourney")
        print("b. back")
        print("q. quit")
        
    def input_promt(self):
        while True:
            self.menu_output()
            command = input("\nEnter your option: ")
            command = command.lower()
            if command == "q":
                print("\nGoodbye for now!")
                return "q"
            elif command == "b":
                print("\nGoing back!")
                return "b"
            elif command == "1":
                c = Club()
                while True:
                    c.name = input("\nEnter the name of your club: ")
                    try:
                        validate_name(c.name)
                        break
                    except NameLengthException:
                        print("\n##Name is too long##")
                    except NameShortException:
                        print("\n##Name is too short##")
                    except:
                        print("\n##Unknown Error Occured, try again##")
                while True:        
                    c.address = input("\nEnter the address of your club: ")
                    try:
                        validate_name(c.address)
                        break
                    except NameLengthException:
                        print("\n##Address is too long##")
                    except NameShortException:
                        print("\n##Address is too short##")
                    except:
                        print("\n##Unknown Error Occured, try again##")
                while True:    
                    c.phone_number = input("\nEnter the club phone number: ")
                    try:
                        validate_number(c.phone_number)
                        break
                    except InvalidNumberLengthException:
                        print("\n##Phone number must be 7 digits long##")
                    except InvalidNumberCharacterException:
                        print("\n##Phone number must only consist of digits##")
                    except:
                        print("\n##Unknown Error Occured, try again##")
                #self.logic_wrapper.create_club(c)    
                #print("\n==Club Created==")
                print()
                print(c)
            elif command == "2":
                #print("\n==Team Created==")
                pass
            elif command == "3":
                p = Player()
                while True:
                    p.name = input("\nEnter the name of the player: ")
                    try:
                        validate_name(p.name)
                        break
                    except NameLengthException:
                        print("\n##Name is too long##")
                    except NameShortException:
                        print("\n##Name is too short##")
                    except:
                        print("\n##Unknown Error Occured, try again##")
                while True:
                    p.ssn = input("\nEnter the social security number of the player: ")
                    try:
                        validate_ssn(p.ssn)
                        break
                    except InvalidNumberLengthException:
                        print("\n##SSN number bust be 10 digits long##")
                    except InvalidNumberCharacterException:
                        print("\n##SSN must only consist of digits##")
                    except:
                        print("\n##Unknown Error Occured, try again##")
                while True:
                    p.email = input("\nEnter the email of the player: ")
                    try:
                        validate_email(p.email)
                        break
                    except NoAsperandSymbolException:
                        print("\n##There needs to be an @ in the email##")
                    except:
                        print("\n##Unknown Error Occured, try again##")
                while True:
                    p.dob = input("\nEnter the date of birth of the player in this format(dd.mm.yyyy): ")
                    try:
                        validate_dob(p.dob)
                        break
                    except NameLengthException:
                        print("\n##The format is only 10 letters, try again##")
                    except InvalidNumberCharacterException:
                        print("\n##There must be a dot between day, month and year##")
                
                p.phone = input("\n(Optional)Enter the GSM-Phone of the player: ")
                p.home_phone = input("\n(Optional)Enter the Home-Phone of the player: ")
                p.address = input("\n(Optional)Enter the Address of the player: ")
                #print("\n==Player Created==")
                print()
                print(p)
            elif command == "4":
                #print("\n==Tourney Created==")
                pass
            else:
                print("\nInvalid input, try again")