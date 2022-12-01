from model.player import Player

testing_dict = {"Dart Vader": [Player("1","óskar","1234567890","oskar@gmail.com","14.04.1982","6963583","4567892","DisneyLand"),
                            Player("2","styrmir","0987654321","styrmir@gmail.com","10.09.2000","5012345","9685742","Discord"),
                            Player("3","kjartan","1020304050","kjartan@gmail.com","11.11.2016","9876541","3574692","RU")]}

str_name = "NAME"
str_ssn = "SSN"
str_email = "EMAIL"
str_dob = "DOB"
str_phone = "PHONE"
str_home_phone = "HOME_PHONE"
str_address = "ADDRESS"


for key, value in testing_dict.items():
    print(f"\n1. TEAM NAME: {key}")
    print()
    print(f"{str_name:<25}{str_ssn:<12}{str_email:<20}{str_dob:<12}{str_phone:<10}{str_home_phone:<15}{str_address:<30}")
    for test in value:
        print(f"{test.name:<25}{test.ssn:<12}{test.email:<20}{test.dob:<12}{test.phone:<10}{test.home_phone:<15}{test.address:<30}")
        
    #print(f"{key} : {test}")
    








"""name ssn email dob phone home_phone address"""
    
"Name: óskarSSN: 1234567890Email: oskar@gmail.comDOB: 14.04.1982GSM: 6963583Home-Phone: 56704044Address: DisneyLand"
"Name: óskarSSN: 1234567890Email: oskar@gmail.comDOB: 14.04.1982GSM: 6963583Address: DisneyLand"
    
"""
1. TEAM NAME: The Brahms

NAME                           SSN     EMAIL      DOB                            ROLE
Sporgonizza Fabio              6422410            neighborlystreet 280           Captain
Gwendoline Lucider             8637421 1512713385 knowledgestreet 33             Player
Zarathustra Ford               8621632 0811933925 swingstreet 135                Player
Winston Birdshill              7389448 1408783929 mittenstreet 32                Player

"""