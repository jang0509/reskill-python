import datetime

now = datetime.datetime.now()
name = input("What is your name: \n")
balance = 0
allowedNames = ["James", "Wilkerson", "Angelo"]
allowedPasswords = ["JamesPassword", "WilkPass", "AngPass"]

if (name in allowedNames):
    password = input("What is your password? \n")

    if (password == allowedPasswords[allowedNames.index(name)]):
        print("Current date and time: ")
        print(now.strftime("%B %d, %Y %I:%M %p"))
        print("\n")
        print("Welcome, %s" % name + "!")
        print("\n")
        print("These are the available options:")
        print("1. Withdrawal")
        print("2. Deposit")
        print("3. Complaint")
        print("\n")

        selectedOption = int(input("Please selected an option: \n"))

        if (selectedOption == 1):
            widthdrawal = int(input("How much would you like to withdraw? \n"))
            print("Take your cash!")
        elif (selectedOption == 2):
            deposit = int(input("How much would you like to deposit? \n"))
            currentBalance = balance + deposit
            print("Current balance is %s" % currentBalance)
        elif (selectedOption == 3):
            complain = input("What issue would you like to report? \n")
            print("Thank you for contacting us!")
        else:
            print("Invalid option selected. Please try again!")

    else:
        print("Incorrect password. Enter password again.")
else:
    print("Name is not found. Please try again.")

