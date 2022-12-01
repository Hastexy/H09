from model.player import Player

testing_dict = {"Dart Vader": [Player("1","óskar","1234567890","oskar@gmail.com","14.04.1982","6963583","56704044","DisneyLand")]}

for key, value in testing_dict.items():
    print(f"1. TEAM NAME: {key}")
    print()
    print("name ssn email dob phone home_phone address")
    for test in value:
        print(test)
        
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