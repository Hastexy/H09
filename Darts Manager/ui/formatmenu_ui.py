class TestMenu:
    def __init__(self) -> None:
        pass    #Only import logic wrapper and put it in the __init__ if this menu creates something else leave empty
    
    def menu_output(self):
        print("\n---Menu name/ Question---")
        print("1. Option 1")
        print("2. Option 2")
        print("3. Option 3")
        print("b. Back")
        print("q. Quit")
        
    def input_prompt(self):
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
            elif command == "3":
                print("\nOption 3 Selected")
            else:
                print("\nInvalid input, try again")