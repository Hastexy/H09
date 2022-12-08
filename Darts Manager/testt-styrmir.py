email_input = input("Enter an email address: ")
counter = 0
for i in email_input:
    if i == "@":
        counter += 1
if counter != 1:
    print("Too many or no @ symbols present")
x,y = email_input.split("@")
if x == "":
    print("Nothing present before the @ symbol.")
if y == "":
    print("Nothing present after the @ symbol.")
if email_input[0] == ".":
    print("The email address starts with a dot")
if x[-1] == ".":
    print("There is a dot just before the @ symbol")
if ".." in email_input:
    print("Consecutive dots found in email address. Exterminate")
if email_input[-4:] != ".com":
    print(".com not present or not correctly written")
else:
    print("all good")




        