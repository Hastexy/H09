class Team_Captain_Verification_UI:
    def __init__(self) -> None:
        pass

    def menu_output(self):
        print("\nAre you a Tournament Manager? (y/n)")
        print("q. to exit")
        
    def input_prompt(self):
        while True:
            self.menu_output()
            command = input("\nEnter your option: ")
            command = command.lower()
            if command == "q":
                print("\nGoodbye")
                return "q"
            elif command == "y":
                print("==You are TC===")    #Implement TC Menu
            elif command == "n":
                return "n"
            else:
                print("\nInvalid input, try again")
    
    