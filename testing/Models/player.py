class Player:
    def __init__(self, name, ssn, email, date_of_birth) -> None:
        self.name = name
        self.ssn = ssn
        self.email = email
        self.date_of_birth = date_of_birth

    def __str__(self) -> str:
        return f"Name: {self.name} Social security number: {self.ssn} Email: {self.email} Date of birth: {self.date_of_birth}"


"""Main filinn"""
# from ui.mainmenu_ui import MainMenu_UI

# mainmenu = MainMenu_UI()
# mainmenu.input_prompt()

"""Debug filinn"""
# from data.customer_data import Customer_Data

# data_class = Customer_Data()
# result = data_class.read_all_customers()
# for elem in result:
#     print(elem)
