import random

database = {}

def init():
    print("Welcome to Python Credit Union")

    have_account = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if have_account == 1:
        login()
    elif have_account == 2:
        register()
    else:
        print("You have selected invalid option")
        init()

def login():
    print("***Login to your account***")
    
    user_account_number = int(input("Please enter your account number! \n"))
    password = input("Enter your password \n")

    for account_number,user_details in list(database.items()):
        if (account_number == user_account_number and user_details[3] == password):
            bank_operation(user_details)
        else:
            print("Invalid account or password")
            login()

def register():
    print("***Register to create your account***")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("What is your password? \n")
    print()
    print("**********************************")

    account_number = generate_account_number()

    database[account_number] = [first_name, last_name, email, password]

    print("Your bank account has been created.")
    print()
    print("Your account number is: %d" % account_number)
    print("**********************************")

    print()

    login()

def bank_operation(user):
    print("Welcome %s %s " % (user[0], user[1]))

    selected_option = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n"))

    if selected_option == 1:
        deposit_operation()
    elif selected_option == 2:
        withdrawal_operation()
    elif selected_option == 3:
        logout()
    elif selected_option == 4:
        exit()
    else:
        print("Invalid option selected")
        bank_operation(user)

def withdrawal_operation():
    print("***Withdrawal***")
    
    set_current_balance(database, 25000.00)

    balance = get_current_balance(database)

    amount_to_withdraw = float(input("Enter amount to withdraw: \n"))

    if (balance > amount_to_withdraw):
        balance -= amount_to_withdraw
        print("The current balance is: %d" % balance)

def deposit_operation():
    print("***Deposit***")

    set_current_balance(database, 10000.00)

    balance = get_current_balance(database)

    amount_to_deposit = float(input("Enter amount to withdraw: \n"))
    
    balance += amount_to_deposit
    print("The current balance is: %d" % balance)
    
def generate_account_number():
    return random.randrange(1111111111, 9999999999)

def set_current_balance(user_details, balance):
    user_details[4] = balance
    
def get_current_balance(user_details):
    return user_details[4]

def logout():
    login()

####Initialize banking system####
init()