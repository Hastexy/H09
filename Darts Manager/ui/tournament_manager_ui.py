class Tournament_Manager_UI:
    def __init__(self) -> None:
        pass
    
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