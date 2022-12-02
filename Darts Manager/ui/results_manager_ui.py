class Results_Manager_UI:
    def __init__(self, logic_connection) -> None:
        self.logic_wrapper = logic_connection
        
    def menu_output(self):
        print("""
╔═══╦════════════════════════╗
║   ║    Results Manager     ║
╠═══╬════════════════════════╣
║ 1 ║ Register Match Results ║
║ 2 ║ Change Match Results   ║
║ b ║ Back                   ║
║ q ║ Quit                   ║
╚═══╩════════════════════════╝""")
        # print("\n---Results Manager---")
        # print("1. register match results")
        # print("2. change match results")
        # print("b. back")
        # print("q. quit")

    def input_prompt(self):

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
                print("==Register match result stuff==")
            elif command == "2":
                print("==Change match result stuff==")

