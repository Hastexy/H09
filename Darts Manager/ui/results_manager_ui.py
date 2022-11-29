class Results_Manager_UI: #Change Class name
    def __init__(self) -> None:
        pass    #Only import logic wrapper and put it in the __init__ if this menu creates something else leave empty
    
    def menu_output(self):  #Change text in this function
        print("\n---Results Manager---")    
        print("1. Option 1")
        print("2. Option 2")
        print("b. Back")
        print("q. Quit")
        
    def input_prompt(self): #Change text in this function
        while True:
            self.menu_output()
            command = input("\nEnter your option: ")
            command = command.lower()
            if command == "q":
                return "q"
            elif command == "b":
                return "b"
            elif command == "1":
                print("\nOption 1 Selected")
            elif command == "2":
                print("\nOption 2 Selected")
            else:
                print("\nInvalid input, try again")